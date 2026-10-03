# Seven principles

These are conditional methods for AI-assisted work. They apply to research, writing, coordination, operations, and development; their examples are proposed applications, not proof across every profession. The entry selects a current bottleneck rather than imposing seven mandatory steps.

| Principle | Minimum useful action | Boundary or counterexample | Main skill |
| --- | --- | --- | --- |
| 1. Give AI a finishable goal and working conditions | Identify the recipient, usable result, necessary context and tools; check the result from the recipient's side. | More context or tools can add noise. Ask only about unknown choices that change the next action. Preserve existing valid work during changes. | workflow; entry |
| 2. Let AI handle uncertainty and programs handle stable parts | Explore, test ordinary and contrary cases, then automate stable steps with an exception path. | Repeatable execution can repeat a semantic error. A fixed workflow may still contain model calls; start with the simplest sufficient approach. | intelligence |
| 3. Assign responsibility and dependencies before parallelizing | Specify scope, inputs, outputs, ownership, and acceptance; parallelize independent work. | Shared resources or unsettled conclusions require coordination. Validate cheaper models against a quality baseline and include integration costs. | orchestration |
| 4. Build a verification layer and check the verifier | Match acceptance to evidence, test good and deliberately bad controls, inspect actual artifacts. | Agreement between agents is not independent evidence. Adjust checks to error cost; send people unresolved judgment with useful evidence. | delivery |
| 5. Bind progress and recovery to confirmed facts | Distinguish queued, produced, saved, sent, received, and usable; inspect existing effects before continuing. | A timeout may conceal a successful write. Check the destination and recover each effect separately; a checkpoint is not external exactly-once delivery. | delivery; workflow |
| 6. Keep knowledge traceable and propagate corrections | Track source, time, scope, and uncertainty; recheck affected conclusions when a source changes. | A citation can exist without supporting the claim. Declared dependency graphs do not establish semantic completeness. | knowledge |
| 7. Make experience change the next action | Extract a condition, action, and effectiveness check; improve an existing workflow first. | A one-off parameter or repeated commonplace needs no new skill. An explicit request to create a skill should still produce usable source. | distill |

For example, a browser workflow can begin with AI exploration and later use a script for known steps. A report correction should update claims that depend on the corrected source while preserving unrelated valid material. A multi-source comparison can gather independent evidence in parallel, then resolve conflicting interpretations centrally.

The package includes short cores, directly linked conditional references, and two deterministic structural helpers. Splitting files does not prove better behavior. Professional task skills and tools remain supplied by your own environment; these methods do not grant permission to operate external accounts.

[External sources](sources.md) informed the limits above. [Validation](validation.md) records what was actually checked.
