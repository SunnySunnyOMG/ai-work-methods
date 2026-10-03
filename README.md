# AI Work Methods

[中文](README.zh-CN.md) · [Seven principles](docs/methods.md) · [Sources](docs/sources.md)

A portable [Agent Skills](https://agentskills.io/specification) package for compatible AI agents. Small skills for turning AI assistance into usable work: choose what to automate, provide the right context, divide independent tasks, verify results, recover safely, and reuse experience.

One entry skill routes to six focused skills. Each has a short core and loads references only when relevant. Simple requests proceed directly; complex tasks get the method they need. The skill bodies are currently Chinese, with English discovery descriptions; an English translation is not included.

## Install

Run in the project where you want the skills. The installer detects the environment or offers agent selection and shows the destinations; the package itself does not require a particular provider:

```sh
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --copy
```

Requires Node.js **22.20.0+** and npm for this installer only. In an ordinary interactive terminal, select your agents and scope when prompted. When run inside an agent, the installer may detect that host and proceed non-interactively. Review the resulting destinations; add `--agent` to choose explicit targets and `--global` for user scope. `npx --yes` accepts downloading the installer; a trailing installer `--yes` would additionally accept its choices. Install all seven sibling skills together. Copies do not update automatically.

No Node or unsupported installer target? Download the release and copy the **seven folders inside `skills/`** into your agent's documented skills directory, preserving their names, references, scripts, and sibling layout. Agent Skills defines a portable format, not one universal installation directory. [Installation guide](docs/install.md) covers target selection, manual installation, updates, and optional host-specific commands. The [skills CLI](https://github.com/vercel-labs/skills/tree/v1.7.0#supported-agents) supports many host destinations; destination support is not proof of runtime behavior in every host.

## Use

Give your agent a real task and ask it to use **ai-work**, for example:

```text
Use ai-work to compare these two proposals and deliver a decision memo.
Use the attached sources and flag contradictions.
```

Use the host's own skill invocation or discovery mechanism. If it can read files, it can read `skills/ai-work/SKILL.md` and load only the relevant sibling modules and references. If it cannot load skills or local files, supply the entry and the needed module/reference text in context; this is manual method use, not installed automatic discovery.

Optional invocation examples: `$ai-work` in Codex, `/ai-work` in Claude Code. Other hosts use their own syntax and settings. Relevant implicit selection is allowed by the package, but actual selection depends on the host and task. `agents/openai.yaml` is optional host metadata; the core instructions do not depend on it.

No extra provider API integration is required by the package. Your agent needs its own runtime and access to the task materials; Python 3.9+ is needed only for the optional helpers. Desktop/web apps and direct APIs may use upload or integration mechanisms rather than a filesystem skills directory; follow their own instructions.

| Skill | Use it to… |
| --- | --- |
| [ai-work](skills/ai-work/SKILL.md) | Choose the method for the current bottleneck |
| [ai-work-workflow](skills/ai-work-workflow/SKILL.md) | Build a repeatable workflow around actual users, context, and tools |
| [ai-work-intelligence](skills/ai-work-intelligence/SKILL.md) | Separate uncertain judgment from stable program steps |
| [ai-work-orchestration](skills/ai-work-orchestration/SKILL.md) | Assign responsibility, models, dependencies, and parallel tasks |
| [ai-work-delivery](skills/ai-work-delivery/SKILL.md) | Deliver an artifact and verify the layer actually achieved |
| [ai-work-knowledge](skills/ai-work-knowledge/SKILL.md) | Track sources and repair conclusions affected by corrections |
| [ai-work-distill](skills/ai-work-distill/SKILL.md) | Turn reusable experience into a skill or improve an existing workflow |

Two optional, read-only helpers check [task dependencies and named write conflicts](skills/ai-work-orchestration/scripts/check_plan.py) and [local source hashes and declared downstream dependencies](skills/ai-work-knowledge/scripts/check_sources.py). They neither execute tasks nor establish truth. Each owning skill links the relevant input format.

## Scope and evidence

The methods combine personal AI-work research with 13 primary external sources. They are conditional guidance, not universal performance claims. [Validation](docs/validation.md) covers constructed regression scenarios, local artifact tasks, and structural checks; it does not establish speedups, native auto-discovery, or live external-system reliability. Raw private conversations are excluded.

Contribute a small case showing a condition, action, outcome, and counterexample. See [CONTRIBUTING.md](CONTRIBUTING.md). Released under the [MIT license](LICENSE).
