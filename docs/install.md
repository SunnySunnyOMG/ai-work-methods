# Installation

This is an Agent Skills package for compatible AI agents. The package contains seven sibling skill directories. Keep their names and relative layout intact; installing only `ai-work` breaks its routes.

## CLI

Run the command for your host from the target project. These commands install the pinned v0.1.1 release:

```sh
# Codex
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent codex --copy --yes

# Claude Code
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent claude-code --copy --yes
```

Use `SunnySunnyOMG/ai-work-methods` as the source to follow the default branch, or choose an already published tag. Use `--global` for user scope. Use `--list` to inspect available skills without installing. The [CLI documentation](https://github.com/vercel-labs/skills) defines source formats and options. Version 1.7.0 is the documented installer pin; Node.js 22.20.0+ and npm are installer prerequisites. Check the install output for all seven names.

## Codex built-in installer

If your Codex environment provides `$skill-installer`, give it this explicit prompt:

```text
$skill-installer Install all seven skills from SunnySunnyOMG/ai-work-methods at tag v0.1.1:
skills/ai-work
skills/ai-work-workflow
skills/ai-work-intelligence
skills/ai-work-orchestration
skills/ai-work-delivery
skills/ai-work-knowledge
skills/ai-work-distill
Keep their references and scripts intact, and report the installation destination.
```

This is an alternative installer request, not a guarantee that every host bundles the installer. Follow its conflict handling if a same-name skill already exists.

## Manual installation without Node

Download the tagged source archive or clone the repository at a published tag such as `v0.1.1`. Copy the **seven directories inside `skills/`**, including their references and scripts. Keep the sibling layout intact and inspect existing same-name directories before replacing anything.

| Host | Project directory | Manual user directory | Explicit entry |
| --- | --- | --- | --- |
| Codex CLI / IDE | `.agents/skills/` | `~/.agents/skills/` | `$ai-work` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `/ai-work` |

The pinned skills CLI uses `CODEX_HOME/skills` (default `~/.codex/skills/`) for Codex global installs; the manual directory above follows current OpenAI discovery guidance. Record the actual installer destination, especially when mixing installation methods. Claude Code global CLI installs use `CLAUDE_CONFIG_DIR/skills` when configured, otherwise `~/.claude/skills/`. See the [pinned installer implementation](https://github.com/vercel-labs/skills/blob/v1.7.0/src/agents.ts).

[Codex documentation](https://learn.chatgpt.com/docs/build-skills) describes local discovery and `$` invocation. [Claude Code documentation](https://code.claude.com/docs/en/skills) describes its directories, `/skill-name` invocation, and default user/model access. This package does not disable model invocation, so Claude Code may select it when relevant; this is permission to select, not a guarantee that a task will trigger it. Codex presentation metadata in `agents/openai.yaml` is optional for other hosts.

Start with an explicit invocation to distinguish discovery problems from implicit matching. Check that all seven directories exist and that your host settings permit skills. Codex detects local changes; if they do not appear, restart it. These Claude instructions target **Claude Code**, not Claude Desktop/Cowork or direct Anthropic API requests, which have their own integration paths. Other Agent Skills hosts have their own locations and invocation syntax; behavior across all hosts has not been validated.

## Updating and removing

Copied installations do not update automatically. Before upgrading, record the current version and actual destination, and back up any local edits outside those seven directories. Compare your edits with the new release before reinstalling; do not assume the installer merges them. Then install a selected published tag using the same scope, agent, and all-seven selection, and check all seven names. A copied installation is independent of the source checkout. Use your installer's removal command or remove only the seven package directories from the recorded destination. Avoid duplicate same-name installations at multiple scopes.

The installation commands above write to the chosen skill location. The optional Python helpers remain read-only. No user-wide installation is required to use or validate the repository itself.
