# AI 工作方法

[English](README.md) · [七条原则](docs/methods.md) · [来源](docs/sources.md)

帮助使用 AI 工作的人完成几个关键判断：哪些部分适合自动化、需要什么上下文、怎样分工、如何验收、失败后从哪里继续，以及经验怎样影响下次行动。

一个统一入口，六个短主干 Skill，细节按条件渐进加载。简单任务直接完成，复杂任务按当前瓶颈选择方法。Skill 正文为中文，发现描述为英文。

## 快速安装

在目标项目目录执行，需要 Node.js **22.20.0+** 和 npm：

```sh
npx --yes skills@1.7.0 add SunnySunnyOMG/ai-work-methods --skill '*' --agent codex --copy --yes
```

建议七个一起安装，入口通过相对链接读取兄弟模块。这个命令使用默认分支；固定首版可把源替换为 `https://github.com/SunnySunnyOMG/ai-work-methods/tree/v0.1.0`。用户级安装加 `--global`；Claude Code 使用 `--agent claude-code`。选项依据 [skills CLI](https://github.com/vercel-labs/skills)。[其他安装方式](docs/install.md)包含 Codex 内置安装器和无需 Node 的手动复制。

安装后，在 Codex CLI 或 IDE 中输入：

```text
$ai-work 把这两份材料整理成供团队决策的报告，保留来源，核对冲突，并交付文件。
```

新技能未出现时重启宿主，参见 [Codex 文档](https://learn.chatgpt.com/docs/build-skills)。其他宿主的调用语法可能不同。加载 Skill 不需要额外接入模型 API，Agent 需要自己的可用运行环境；只有可选脚本需要 Python 3.9+。

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
