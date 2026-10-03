# AI 工作方法

[English](README.md) · [七条原则](docs/methods.md) · [来源](docs/sources.md)

适用于 Codex、Claude Code 及其他兼容 AI Agent 的 Agent Skills 方法包，帮助使用 AI 工作的人完成几个关键判断：哪些部分适合自动化、需要什么上下文、怎样分工、如何验收、失败后从哪里继续，以及经验怎样影响下次行动。

一个统一入口，六个短主干 Skill，细节按条件渐进加载。简单任务直接完成，复杂任务按当前瓶颈选择方法。Skill 正文为中文，发现描述为英文。

## 快速安装

在目标项目目录选择对应命令，需要 Node.js **22.20.0+** 和 npm：

```sh
# Codex
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent codex --copy --yes

# Claude Code
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --agent claude-code --copy --yes
```

七个一起安装，入口通过相对链接读取兄弟模块。上述命令复制固定版本 v0.1.1 到项目。若要跟随默认分支，可将源替换为 `SunnySunnyOMG/ai-work-methods`。用户级安装加 `--global`。复制安装不会自动更新；升级前备份本地修改。选项依据 [skills CLI](https://github.com/vercel-labs/skills)。[安装与更新说明](docs/install.md)包含无需 Node 的手动复制和 Codex 内置安装器。

在 Codex CLI 或 IDE 中输入：

```text
$ai-work 把这两份材料整理成供团队决策的报告，保留来源，核对冲突，并交付文件。
```

在 Claude Code 中输入：

```text
/ai-work 把这两份材料整理成供团队决策的报告，保留来源，核对冲突，并交付文件。
```

也可以直接调用专题 Skill。两个宿主均可依据发现描述选择相关技能，实际隐式选择取决于宿主与任务；Claude Code 默认允许用户与模型调用。新技能未出现时检查安装范围和宿主设置，参见 [Codex](https://learn.chatgpt.com/docs/build-skills) 与 [Claude Code](https://code.claude.com/docs/en/skills) 文档。其他兼容宿主有自己的目录和调用方式。

加载 Skill 无需额外接入模型 API，Agent 仍需要自己的可用运行环境；可选脚本需要 Python 3.9+。这里的 Claude 安装与调用说明针对 **Claude Code**；Claude Desktop/Cowork 和直接 API 使用采用各自的接入方式。

其他 AI Agent 可使用自己的技能机制。环境能读本地文件时，可要求它读取 `skills/ai-work/SKILL.md` 并给出任务，例如：“把会议笔记与原始来源对照，标出发生变化的主张，交付修正后的简报。”不能读文件时，把入口及相关模块正文放入对话上下文。这只提供方法上下文，不保证自动发现，也不赋予工具权限。

| Skill | 主要判断 |
| --- | --- |
| [ai-work](skills/ai-work/SKILL.md) | 当前瓶颈需要哪一种方法 |
| [ai-work-workflow](skills/ai-work-workflow/SKILL.md) | 如何围绕实际用途安排上下文、工具与重复流程 |
| [ai-work-intelligence](skills/ai-work-intelligence/SKILL.md) | 哪些环节用 AI、程序或人判断 |
| [ai-work-orchestration](skills/ai-work-orchestration/SKILL.md) | 如何分工、选择模型、安排依赖与并行 |
| [ai-work-delivery](skills/ai-work-delivery/SKILL.md) | 如何交付并证明结果达到哪一层 |
| [ai-work-knowledge](skills/ai-work-knowledge/SKILL.md) | 如何保留来源、处理纠正与下游影响 |
| [ai-work-distill](skills/ai-work-distill/SKILL.md) | 哪些经验值得固化，怎样优先改善现有流程 |

两个只读脚本检查依赖和同名写入冲突，以及本地来源 hash 和声明的派生关系；不执行任务，不判断语义真假。

方法结合实践案例与 13 份一手外部来源。[验证范围](docs/validation.md)明确记录构造场景与本地文件任务，尚未证明普遍提速、原生自动发现或真实外部系统可靠性。私人聊天不进入公开包。欢迎提交带条件、结果与反例的小案例，见 [贡献说明](CONTRIBUTING.md)。采用 [MIT](LICENSE) 许可。
