# Install in your agent

The package uses the [Agent Skills open format](https://agentskills.io/specification). Install the same seven sibling folders in any compatible host; there is no provider API dependency or vendor-specific method implementation. The host determines discovery, destination, invocation and tool permissions.

## 1. Let an installer handle the destination

From the target project, run:

```sh
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --copy
```

Requires Node.js 22.20.0+ and npm for the installer only. An ordinary interactive terminal offers agent/scope choices and an installation summary. Inside an agent environment, the installer may detect the host and proceed non-interactively. Review the actual destination paths and install all seven skills; use explicit `--agent` targets when detection is not what you want. The first `--yes` belongs to npx, allowing it to obtain the installer; a trailing installer `--yes` additionally accepts its choices. Some targets share a `.agents/skills/` directory; that path is not a guarantee that every agent reads it.

The [pinned installer documentation](https://github.com/vercel-labs/skills/tree/v1.7.0#supported-agents) lists available targets, including OpenCode, Cursor, Gemini CLI, GitHub Copilot, Claude Code and Codex. An installer target means it can place files in a known location; it does not mean this package's native discovery or behavior has been tested in every target.

For non-interactive installation, use `--agent` to explicitly select one or more targets and a trailing `--yes` to accept the installer choices. For example:

```sh
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent opencode cursor --copy --yes
```

Replace the target names with those you use. Add `--global` for user scope; otherwise use project scope. Use `--list` to inspect the seven available skills without installing. Do not use `--all` unless you actually want the installer's all-agent behavior.

The commands pin v0.1.1. Use another published tag to choose another version. Using `SunnySunnyOMG/ai-work-methods` as the source copies the default branch at installation time; it does not enable automatic updates.

## 2. Manual installation without Node or a listed target

1. Download the [v0.1.1 source archive](https://github.com/SunnySunnyOMG/ai-work-methods/archive/refs/tags/v0.1.1.zip) or clone that tag.
2. Find your host's documented skills directory or import mechanism. Agent Skills defines the format, not a universal project/user path. Record the chosen destination and check same-name conflicts before writing.
3. Copy the **seven directories inside `skills/`** into that directory. Preserve names, resources and sibling layout:

```text
<your-host-skills-directory>/
  ai-work/SKILL.md
  ai-work-workflow/SKILL.md
  ai-work-intelligence/SKILL.md
  ai-work-orchestration/SKILL.md
  ai-work-delivery/SKILL.md
  ai-work-knowledge/SKILL.md
  ai-work-distill/SKILL.md
```

Keep each folder's `references/`, `scripts/` and optional `agents/` files. Installing only the entry breaks its sibling routes. The package needs access to these sibling files; a host that imports skills into isolated containers may require an adapter and is not established as compatible merely by accepting an upload.

If the host has no skills discovery but can read files, keep the downloaded `skills/` tree intact and ask it to read `skills/ai-work/SKILL.md`, then give it your task. If it cannot read files, provide the entry and needed module/reference text in its context. This supplies the methods, not automatic installation, discovery or tool access. Web apps and APIs may have their own upload/integration mechanisms; a local copy does not automatically configure them.

## 3. Check the installed package

- Confirm all seven folders and their resources are present.
- Use the host's own invocation syntax or ask it to load the entry. Give it a small real task and inspect the actual output before relying on implicit selection.
- Check that required references can be read relative to the installed skill, rather than resolving paths from an unrelated working directory.
- If discovery fails, check the destination, scope, settings and the host's reload procedure. Optional Python helpers require Python 3.9+; reading the methods does not require Python.

Implicit selection is permitted by this package, but the host decides when to use it. `agents/openai.yaml` is optional host metadata; the core does not depend on that file. The package does not disable Claude Code model invocation or prescribe a model/provider.

## Optional host examples

These illustrate host conventions rather than define the portable format:

| Host | Explicit entry | Project/manual-user examples |
| --- | --- | --- |
| Codex | `$ai-work` | `.agents/skills/`, `~/.agents/skills/` |
| Claude Code | `/ai-work` | `.claude/skills/`, `~/.claude/skills/` |
| Other compatible hosts | Their own skill invocation or file-loading mechanism | Their documented directory/import mechanism |

See [Codex documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills). The pinned CLI's user destination for Codex defaults to `~/.codex/skills/`, while manual discovery documentation also supports `~/.agents/skills/`. Configured `CODEX_HOME` or `CLAUDE_CONFIG_DIR` can affect CLI destinations; inspect the summary and [pinned destination implementation](https://github.com/vercel-labs/skills/blob/v1.7.0/src/agents.ts), and avoid duplicate same-name copies across scopes.

If your host includes a skill installer, ask it to install **all seven** `skills/ai-work*` folders from this repository at the chosen tag, preserve resources and sibling layout, and report the actual destination. No particular built-in installer is required.

## Updating and removing

Copied installations do not update automatically. Before upgrading, record the current version and actual destination, and back up local edits outside those seven directories. Compare your edits with the new release; do not assume an installer merges them. Install a chosen published tag using the same scope and all-seven selection, and recheck the installed package. Symlinking copies across host directories can share a local source but does not itself fetch future releases.

Use your installer's removal command or remove only the seven package folders from the recorded destination. Installing or removing in a project is separate from user-wide scope. The optional helpers remain read-only; installation writes the chosen destination.
