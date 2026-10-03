# Validation scope

The first version was checked at several distinct layers. These checks support a bounded release, not a claim that the methods improve all AI work.

| Layer | Checks performed | What remains unproved |
| --- | --- | --- |
| Package structure | Seven skill frontmatters, local reference links, resource presence, short cores, and absence of private source material. | Native automatic discovery and implicit routing in every host. |
| Read-only helpers | Seven behavior tests across dependency ordering, cycles, missing dependencies, shared writes, changed/unreadable sources, out-of-root paths, and unknown source identities. | Semantic independence, truth, complete provenance, or task success. |
| Judgment scenarios | 15 constructed scenarios compared baseline and skill-assisted responses; independent review inspected outputs and evidence. | Blind held-out accuracy, causal performance gains, or statistical generalization. |
| Local artifact tasks | Five controlled file tasks: comparison CSV, corrected report, collaborative plan and final table, improved workflow, and a requested narrow skill. | Live accounts, production external writes, actual multi-agent speedups, or long-term reuse. |

Independent review found two issues in the initial judgment outputs: a missing requested draft and insufficient evidence of revisiting the original source. The instructions were narrowly revised and those cases rerun with the needed artifacts and evidence. Original failures were retained in the private research record. Most baseline answers were already reasonable, so the comparison does not justify a general improvement claim.

Local artifact tasks tested usable outputs from file-based skill loading, with references read on demand. They were controlled exercises with real local files, not live business deployments. Raw traces and private research ledgers are excluded from the public repository.

The core plus six modules contains 14 conditional references and two optional standard-library Python helpers. Installation/discovery checks are a separate release layer; copying files successfully cannot substitute for testing the method on your own task.

For a contribution, provide the initial input, expected action or artifact, actual result, relevant version, and a failure or boundary case. Reproduce against the current package before changing a rule, and report the precise layer checked.

## Follow-up portability review and installation checks

A follow-up review of v0.1.0 ran the structural validator and all 14 tests locally on Python 3.9.6 and 3.14.3. Both passed. Two targeted filesystem cases exposed gaps in the source helper: a symlink loop escaped JSON error handling on Python 3.9, and a FIFO could block while opening a source. Those findings motivate the v0.1.1 changes; passing the original tests alone did not cover them.

The v0.1.1 candidate rejects non-regular source/manifest files, returns JSON for looped or invalid source/manifest/root paths, and preserves downstream review for unreadable sources. New regressions failed on the old helper before the repair; all 19 tests passed locally on Python 3.9.6 and 3.14.3 after it. Tests also preserve ordinary in-root symlinks and reject paths escaping the root. These checks do not certify resistance to arbitrary concurrent filesystem mutation.

Three separate reviewers inspected methods, portability and adversarial boundaries. Four new controlled non-development exercises produced actual files: a venue decision memo and unsent email, a requested narrow editorial skill with correction examples, a two-sentence answer from conflicting event notices, and simulated cross-application recovery. The recovery simulation preserved completed effects and did not retry an unknown effect. Inputs and outputs were created by the same reviewer in each exercise; these are not blind or independent-model benchmarks. Two inferred risks remain unmeasured: broad delivery descriptions may attract trivial requests, and the existing `holdout.jsonl` name does not make those constructed regressions held-out evidence.

Claude Code CLI 2.1.286 was available but not logged in, so no Claude-model review was obtained. This absence is separate from the file installation check below.

For installation, the pinned skills CLI 1.7.0 installed the published **v0.1.0** into a fresh temporary project with `--agent claude-code --copy --yes`. All seven skills appeared in `.claude/skills/`; SHA256 comparisons of all 30 packaged skill files matched the v0.1.0 release commit. No user-wide installation or authenticated Claude model task was performed. This proves a bounded Claude Code project copy, not native discovery, explicit task behavior, implicit selection, or v0.1.1 installation.

The version in an installation command is not itself evidence of successful public installation of that version. Additional host behavior checks should record host version, installation destination, task input, actual loaded modules, and resulting artifact.
