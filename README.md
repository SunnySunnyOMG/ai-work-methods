# AI Work Methods

[中文](README.zh-CN.md) · [Seven principles](docs/methods.md) · [Sources](docs/sources.md)

Small skills for turning AI assistance into usable work: choose what to automate, provide the right context, divide independent tasks, verify results, recover safely, and reuse experience.

One entry skill routes to six focused skills. Each has a short core and loads references only when relevant. Simple requests proceed directly; complex tasks get the method they need. The skill bodies are currently Chinese, with English discovery descriptions; an English translation is not included.

## Quick install

Run in the project where you want the skills available. Requires Node.js **22.20.0+** and npm for this installer:

```sh
npx --yes skills@1.7.0 add SunnySunnyOMG/ai-work-methods --skill '*' --agent codex --copy --yes
```

Install all seven together: the entry uses relative links to sibling skills. The command targets Codex, copies files, and uses the repository's current default branch. For a reproducible release, replace the source with `https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.0`. Add `--global` for user-wide installation; use `--agent claude-code` to target Claude Code. These options come from the [skills CLI](https://github.com/vercel-labs/skills).

[Other installation methods, updates, and troubleshooting](docs/install.md) include a Codex installer prompt and manual copying without Node. Loading these files requires no provider API integration; the agent still needs its own working runtime. Python 3.9+ is needed only for the optional helpers.

## Use

In Codex CLI or IDE, invoke the installed entry with a real task:

```text
$ai-work Compare these two proposals and produce a decision memo.
Use the attached sources, flag contradictions, and deliver the memo as a file.
```

Or invoke a focused skill directly. Other hosts may use different invocation syntax. If the new skills do not appear, restart the host; see [Codex discovery documentation](https://learn.chatgpt.com/docs/build-skills).

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
