# Installation

The package contains seven sibling skill directories. Keep their names and relative layout intact; installing only `ai-work` breaks its routes.

## CLI

The quick command in the README installs the current default branch into the selected project. For the first tagged release:

```sh
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.0 --skill '*' --agent codex --copy --yes
```

Use `--global` for user scope. Replace `codex` with `claude-code` for that host. Use `--list` to inspect available skills without installing. The [CLI documentation](https://github.com/vercel-labs/skills) defines source formats and options. Version 1.7.0 is the documented installer pin; Node.js 22.20.0+ and npm are installer prerequisites. Check the install output for all seven names.

## Codex built-in installer

If your Codex environment provides `$skill-installer`, give it this explicit prompt:

```text
$skill-installer Install all seven skills from SunnySunnyOMG/ai-work-methods at tag v0.1.0:
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

Download the tagged source archive or clone the repository at `v0.1.0`. Copy the **seven directories inside `skills/`**, including their references and scripts, to `.agents/skills/` in your project. For user-wide Codex discovery, use `~/.agents/skills/`. Inspect existing same-name directories before replacing anything. These locations and explicit `$` invocation are documented by [OpenAI](https://learn.chatgpt.com/docs/build-skills); other runtimes have their own directories and invocation syntax.

Codex detects local skill changes; if the package does not appear, restart Codex. Start with an explicit invocation to distinguish discovery problems from implicit matching. Hosts supporting Agent Skills may read the package, but behavior across all such hosts has not been validated.

## Updating and removing

To update deliberately, install a selected newer tag using the same scope, agent, and all-seven selection. A copied installation is independent of the source checkout. Use your installer's removal command or remove only the seven package directories from the recorded destination. Avoid duplicate same-name installations at multiple scopes.

The installation commands above write to the chosen skill location. The optional Python helpers remain read-only. No user-wide installation is required to use or validate the repository itself.
