---
type: concept
hubs: [ai-engineering]
sources: 1
updated: 2026-11-23
---
# Model Personality

**Summary:** Each model family has a recognizable character, and users feel it in ChatGPT, Claude and Gemini alike. These built-in biases in how a model answers survive prompting: you can change what it does, but not quite how it does it. Gemini follows a style request such as "be brutal" or "criticize me" closely, yet still does it in a very Gemini way, and OpenAI and Anthropic models differ just as clearly. This "personality" is shallow next to a human's. One builder calls it "custom intelligence", tuned to whatever it was shaped for, which is also why it is jagged. Real personalization will likely come from fine-tuning rather than ever-longer prompt files.

## Key ideas
- Users feel a different character in each chat model (ChatGPT, Claude, Gemini). Its biases in how it answers are "there": prompts shift them somewhat, but you still feel them ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]], [[people/uri-nachum]]).
- Building a home robot on an OpenAI model (GPT-4, he thinks), Nachum couldn't get it out of its built-in biases, such as a strong tendency to be nice in one particular way. He didn't want to build "mountains of markdown" just to make it respond differently ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]], [[people/uri-nachum]]).
- Gemini gives very high control over its style: tell it to be brutal or to criticize you and it always tries. But the way it does so stays very Gemini, whatever the instructions. The same holds for every model, and OpenAI's differ clearly from Anthropic's ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]], [[people/uri-nachum]]).
- Shallow next to a person: watching his two daughters grow and learn, Nachum sees a huge gap in depth between them and even a very smart model like Claude. It isn't child or human intelligence, just a different kind: "not alien intelligence, custom intelligence", tuned to what's needed, which is why it's jagged ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]], [[people/uri-nachum]]).
- Personalization through fine-tuning: since prompts can't override a model's character, Nachum expects personalized models to come from fine-tuning, because a fine-tuned layer feels completely different from another vendor's ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]], [[people/uri-nachum]]).
- In the opposite direction, a persona can hurt task agents: see [[concepts/agent-architectures]] for Roy Mann's agent that carried its whole persona into a bug-fixing loop ([[episodes/startup-for-startup--362-agent-architecture-fit]], [[people/roy-mann]]).

## Disagreements & open questions
- Can prompts set an agent's personality? Nachum says the model's own character always shows through ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]], [[people/uri-nachum]]); a host asks whether personalized models are then hard to build, or whether light adjustments per user are enough. Nachum's answer is fine-tuning.

## Takeaways
- [ ] If an agent needs a specific voice, try it on several model families before adding more prompt rules ([[episodes/explainable--170-uri-nachum-agents-that-work-for-you]])

## Related
[[concepts/agent-architectures]] · [[concepts/llm-post-training]] · [[concepts/llm-safety]] · [[concepts/model-selection]] · [[concepts/robotics-foundation-models]]
