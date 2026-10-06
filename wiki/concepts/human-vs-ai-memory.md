---
type: concept
hubs: [knowledge-management, ai-engineering]
sources: 2
updated: 2026-10-06
---
# Human vs AI Memory

**Summary:** Neuroscience offers both inspiration and warnings for agent memory. Human memory encodes, consolidates (replay during sleep strengthens connections), and retrieves by reassembling experiences from cues, which makes retrieved memories editable and imperfect. It's strong at organizing knowledge into schemas, separating signal from noise, and tagging importance and emotion, and it learns continuously. AI memory today is mostly a static, unlimited vector store fed by generic extraction prompts: precise but without salience, schema, or continuous learning.

## Key ideas
- Definition: taking in information, encoding, storing, and retrieving it in a way that changes behavior ([[episodes/langtalks--60-brain-memory]], [[people/meytar-zemer]]).
- Types: short-term and working memory (e.g. holding an SMS code); long-term memory, split into episodic, semantic, and procedural. H.M., after bilateral medial temporal lobe removal, couldn't form new memories but kept intellect and working memory, and improved at a motor task he didn't remember practicing ([[episodes/langtalks--60-brain-memory]]).
- Encoding: activity across sensory regions converges on the hippocampus, which coordinates with the cortex. Replay (awake but mostly in sleep) strengthens synapses until memories depend on the cortex alone ([[episodes/langtalks--60-brain-memory]]).
- The amygdala tags emotional valence; emotional salience affects what we remember ([[episodes/langtalks--60-brain-memory]]).
- Reconsolidation: retrieving a memory reopens it for editing, so the memories we recall most are the most changeable. 9/11 "flashbulb" memories measured over years drifted ([[episodes/langtalks--60-brain-memory]]).
- H.M. is like an LLM whose training stopped ([[episodes/langtalks--60-brain-memory]]).
- Schemas speed encoding and retrieval but cause errors ("beach, sun…" falsely recalls "towel"). Role prompts ("you're a neuroscientist") may work by activating a schema in the weights ([[episodes/langtalks--60-brain-memory]]).
- AI memory example (Mem0 v1): an LLM with a generic prompt extracts memories from messages into a vector DB (optionally a graph), with metadata filters; background dedupe in which the newest wins conflicts. Hosts question task-agnostic extraction and "newest wins" ([[episodes/langtalks--60-brain-memory]]).
- Academia now lags industry; big papers come from companies, unlike the AlexNet era ([[episodes/langtalks--60-brain-memory]]).
- Friedman doesn't consider human memory the ideal design ("mine is terrible"); expect memory architectures that differ from the brain, with LLMs trained to use them ([[episodes/langtalks--57-memory]]).

## Disagreements & open questions
- Should AI memory imitate human memory at all, given its decay and distortions, or aim for precise but salience-aware storage ([[episodes/langtalks--60-brain-memory]])?

## Takeaways
- [ ] Make memory extraction task-aware (what matters differs for coding vs SQL vs Q&A) ([[episodes/langtalks--60-brain-memory]])
- [ ] Prefer frequency/consistency over recency when resolving conflicting memories ([[episodes/langtalks--60-brain-memory]])

## Related
[[concepts/memory-consolidation]] · [[concepts/knowledge-graphs]] · [[concepts/autonomous-agents-outlook]] · [[concepts/second-brain]] · [[concepts/agent-memory]]
