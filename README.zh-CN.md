# AI 工作方法

[English](README.md) · [七条原则](docs/methods.md) · [来源](docs/sources.md)

遵循 [Agent Skills 开放规范](https://agentskills.io/specification) 的通用方法包，帮助使用 AI 工作的人完成几个关键判断：哪些部分适合自动化、需要什么上下文、怎样分工、如何验收、失败后从哪里继续，以及经验怎样影响下次行动。

一个统一入口，六个短主干 Skill，细节按条件渐进加载。简单任务直接完成，复杂任务按当前瓶颈选择方法。Skill 正文为中文，发现描述为英文。

## 安装

在目标项目目录运行，让安装工具检测环境或提供 Agent 选择，并展示安装位置；方法包本身不要求特定供应商：

```sh
npx --yes skills@1.7.0 add https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.1 --skill '*' --copy
```

这个安装工具需要 Node.js **22.20.0+** 和 npm。普通交互终端按提示选择 Agent 和范围；在 Agent 内运行时，安装工具可能自动识别当前宿主并直接安装。核对输出的目标位置；指定目标用 `--agent`，用户级范围用 `--global`。开头的 `npx --yes` 只接受下载安装工具；末尾另加安装器的 `--yes` 才是接受其安装选项。七个兄弟 Skill 一起安装；复制件不会自动更新。

没有 Node，或安装工具没有列出你的 Agent？下载版本源码，将 **`skills/` 内的七个文件夹**放入该 Agent 文档指定的技能目录，保留名称、references、scripts 和兄弟布局。Agent Skills 统一的是文件格式，不是所有宿主的安装路径。[安装说明](docs/install.md)提供通用手动流程、更新方式和可选宿主命令；[skills CLI](https://github.com/vercel-labs/skills/tree/v1.7.0#supported-agents) 可处理多种宿主目录，但目录安装支持不等于所有宿主行为都已验证。

## 使用

给 Agent 真实任务，并让它使用 **ai-work**，例如：

```text
使用 ai-work，把这两份材料整理成供团队决策的报告，保留来源，核对冲突，并交付文件。
```

使用宿主自己的 Skill 调用或发现机制。能读本地文件时，读取 `skills/ai-work/SKILL.md`，再按需要加载兄弟模块与 references。不能加载 Skill 或文件时，将入口及所需模块/reference 内容放入上下文；这是手动使用方法，不等于已安装并能自动发现。

可选调用例子：Codex 使用 `$ai-work`，Claude Code 使用 `/ai-work`；其他 Agent 使用自己的语法与设置。包允许按相关性隐式选择，实际是否触发由宿主和任务决定。`agents/openai.yaml` 仅是可选宿主元数据，核心方法不依赖它。

方法包无需额外接入供应商 API。Agent 需要自己的运行环境与材料访问能力；只有可选脚本需要 Python 3.9+。桌面端、网页端和直接 API 可能采用上传或专门接入方式，而非本地技能目录，按各自说明处理。

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
