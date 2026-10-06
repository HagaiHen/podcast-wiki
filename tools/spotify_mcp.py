"""Spotify MCP server: podcast episodes the user has heard from followed shows.

  uv run tools/spotify_mcp.py             # MCP server over stdio
  uv run tools/spotify_mcp.py --auth      # one-time interactive OAuth login
  uv run tools/spotify_mcp.py --list      # print heard episodes as JSON (scheduled job)
  uv run tools/spotify_mcp.py --selftest
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE = "user-library-read user-read-playback-position"
EPISODES_PER_SHOW = 20  # ponytail: older heard episodes are ignored; paginate show_episodes if that matters


def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def client():
    import spotipy
    from spotipy.cache_handler import CacheFileHandler
    from spotipy.oauth2 import SpotifyPKCE

    load_env()
    return spotipy.Spotify(auth_manager=SpotifyPKCE(  # PKCE: no client secret to store
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        redirect_uri="http://127.0.0.1:8888/callback",
        scope=SCOPE,
        cache_handler=CacheFileHandler(cache_path=str(ROOT / ".spotify_cache")),
    ))


def progress(ep):
    rp = ep.get("resume_point") or {}
    if rp.get("fully_played"):
        return 1.0
    duration = ep.get("duration_ms") or 0
    return rp.get("resume_position_ms", 0) / duration if duration else 0.0


def heard_episodes(sp, min_progress=0.5):
    shows, page = [], sp.current_user_saved_shows(limit=50)
    while page:
        shows += [item["show"] for item in page["items"]]
        page = sp.next(page) if page["next"] else None
    out = []
    for show in shows:
        for ep in sp.show_episodes(show["id"], limit=EPISODES_PER_SHOW, market="from_token")["items"]:
            if not ep:  # Spotify returns null for unavailable episodes
                continue
            p = progress(ep)
            if p < min_progress:
                continue
            out.append({
                "id": ep["id"],
                "show_name": show["name"],
                "show_id": show["id"],
                "title": ep["name"],
                "release_date": ep["release_date"],
                "description": ep.get("description", ""),
                "duration_ms": ep.get("duration_ms") or 0,
                "progress": round(p, 2),
                "spotify_url": ep["external_urls"]["spotify"],
                "language": ep.get("language") or (ep.get("languages") or [""])[0],
            })
    return out


def selftest():
    assert progress({"resume_point": {"fully_played": True}, "duration_ms": 0}) == 1.0
    assert progress({"resume_point": {"resume_position_ms": 30_000}, "duration_ms": 60_000}) == 0.5
    assert progress({"resume_point": {"resume_position_ms": 10}, "duration_ms": 0}) == 0.0
    assert progress({"duration_ms": 60_000}) == 0.0
    assert progress({"resume_point": None}) == 0.0

    def ep(id_, pos, dur=100):
        return {"id": id_, "name": f"T{id_}", "release_date": "2026-01-01", "description": "d",
                "duration_ms": dur, "resume_point": {"resume_position_ms": pos},
                "external_urls": {"spotify": f"https://open.spotify.com/episode/{id_}"}, "language": "he"}

    class FakeSpotify:
        def current_user_saved_shows(self, limit):
            return {"items": [{"show": {"id": "s1", "name": "Show"}}], "next": "page2"}

        def next(self, page):
            return {"items": [{"show": {"id": "s2", "name": "Other"}}], "next": None}

        def show_episodes(self, show_id, limit, market):
            return {"items": [None, ep(show_id + "a", 60), ep(show_id + "b", 10)]}

    got = heard_episodes(FakeSpotify(), 0.5)
    assert [e["id"] for e in got] == ["s1a", "s2a"], got
    assert got[0]["show_name"] == "Show" and got[0]["progress"] == 0.6
    assert set(got[0]) == {"id", "show_name", "show_id", "title", "release_date", "description",
                           "duration_ms", "progress", "spotify_url", "language"}
    print("selftest ok")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--selftest":
        selftest()
    elif arg == "--auth":
        print("Logged in as", client().current_user()["display_name"])
    elif arg == "--list":
        print(json.dumps(heard_episodes(client()), ensure_ascii=False, indent=1))
    else:
        from mcp.server.mcpserver import MCPServer

        mcp = MCPServer("spotify")

        @mcp.tool()
        def list_heard_episodes(min_progress: float = 0.5) -> list[dict]:
            """Podcast episodes from the user's followed Spotify shows that are fully played
            or at least `min_progress` (0-1) played. Checks each show's 20 most recent episodes."""
            return heard_episodes(client(), min_progress)

        mcp.run()
