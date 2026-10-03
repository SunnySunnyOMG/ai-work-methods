# AI Work Methods

[中文](README.zh-CN.md) · [Seven principles](docs/methods.md) · [Sources](docs/sources.md)

An Agent Skills package for Codex, Claude Code, and other compatible AI agents. Small skills for turning AI assistance into usable work: choose what to automate, provide the right context, divide independent tasks, verify results, recover safely, and reuse experience.

One entry skill routes to six focused skills. Each has a short core and loads references only when relevant. Simple requests proceed directly; complex tasks get the method they need. The skill bodies are currently Chinese, with English discovery descriptions; an English translation is not included.

## Quick install

Run the command for your agent in the target project. Both commands require Node.js **22.20.0+** and npm:

```sh
# Codex
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent codex --copy --yes

# Claude Code
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent claude-code --copy --yes
```

Install all seven together: the entry uses relative links to sibling skills. These commands copy the pinned v0.1.1 release into the project. To follow the current default branch instead, use `SunnySunnyOMG/ai-work-methods` as the source. Add `--global` for user-wide installation. Copied skills do not update automatically; back up local edits before installing another version. Options come from the [skills CLI](https://github.com/vercel-labs/skills).

[Installation, updates, and troubleshooting](docs/install.md) include manual copying without Node. Loading these files requires no extra provider API integration; the agent needs its own working runtime. Python 3.9+ is needed only for the optional helpers. The Claude instructions target **Claude Code**; Claude Desktop/Cowork and direct API use have different installation and integration paths.

## Use

Invoke the installed entry with a real task. In Codex CLI or IDE:

```text
$ai-work Compare these two proposals and produce a decision memo.
Use the attached sources, flag contradictions, and deliver the memo as a file.
```

In Claude Code:

```text
/ai-work Compare these two proposals and produce a decision memo.
Use the attached sources, flag contradictions, and deliver the memo as a file.
```

Or invoke a focused skill directly. Both hosts can select relevant skills from their discovery descriptions; actual implicit selection depends on the host and task. Claude Code allows both user and model invocation by default. If the skills do not appear, check the installation scope and host settings; see [Codex](https://learn.chatgpt.com/docs/build-skills) and [Claude Code](https://code.claude.com/docs/en/skills) documentation. Other compatible hosts have their own locations and invocation syntax.

For another AI agent, use its supported skill mechanism. If it can read local files, ask it to read `skills/ai-work/SKILL.md` and give it the task, for example: “Reconcile these meeting notes with the original sources, flag changed claims, and deliver a corrected brief.” If it cannot read files, supply the entry and relevant module text in the conversation. This provides context; it does not guarantee automatic discovery or grant tool access.

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
