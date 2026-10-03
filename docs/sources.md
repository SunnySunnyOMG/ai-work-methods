# Sources and interpretation

Reviewed on 2026-10-03. The research read relevant primary-source sections; it did not reproduce their internal benchmarks. Official documentation describes mechanisms and recommendations, engineering articles describe their authors' experience, and standards define representations. None establish this package's performance.

| Source | What it informed | Limit |
| --- | --- | --- |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Begin with simple composable patterns; distinguish preset workflows and dynamic agents. | Architecture guidance, not a universal choice of framework or autonomy. |
| [Anthropic: Writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents) | Design tools around valuable tasks and relevant outputs; evaluate actual use. | More tools alone do not imply improved work. |
| [Anthropic: Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Select sufficient high-signal context and obtain details as needed. | Minimum useful context does not mean the shortest prompt. |
| [Anthropic: Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Progressive disclosure, code for deterministic operations, iteration from use. | Packaging is not an effectiveness evaluation. |
| [Anthropic: Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Independent breadth exploration, clear assignments, coordination and resource costs. | Internal research results do not predict everyday or programming speedups. |
| [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Inspect environment outcomes, mix graders, calibrate against reference judgments. | A trace or a passing subset does not prove complete delivery. |
| [OpenAI: Practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) | Establish quality before optimizing model cost; begin with simpler agent arrangements. | No fixed model ranking or pricing recommendation is imported. |
| [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Include ordinary, boundary, and adversarial cases; calibrate judges. | Method guidance is used without a dependency on its evaluation platform. |
| [LangGraph: Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | State persistence and checkpoints support recovery. | Requires actual persistence configuration; this package does not require LangGraph. |
| [LangGraph: Functional API documentation](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/functional-api.mdx) | Isolate side effects, account for replay, use idempotency or reconcile destination state. | An unfinished task can rerun; external exactly-once effects are not guaranteed. This source is a mutable main-branch document. |
| [W3C: PROV Overview](https://www.w3.org/TR/prov-overview/) | Represent sources, activities, responsibility, derivation, and versions. | Provenance does not decide truth or automatically repair conclusions. |
| [Agent Skills: Specification](https://agentskills.io/specification) | Focused metadata, small core, direct links and on-demand resources. | Format validity does not prove discovery or useful execution. |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Clear trigger descriptions, explicit invocation, references and scripts. | Runtime discovery differs by host; correct packaging still needs behavioral tests. |

The research also examined a private, time-bounded set of AI-work records. A broad navigation pass covered 9,349 unique input texts, followed by selected task-window reviews. Deduplication did not transfer authorization, actor identity, or outcome evidence between sources. Some cloud-hosted chat bodies, unreadable source paths, and injected-memory tails remained outside full semantic coverage. This was not an exhaustive read of every conversation.

Correction propagation and allowing zero new skills chiefly arise from the local cases. The external sources support useful structures and checks, but do not directly prove those policies' general benefit. Future counterexamples may narrow, merge, or withdraw a rule. Raw conversations, private identifiers, and original evidence locators are excluded from this repository.
