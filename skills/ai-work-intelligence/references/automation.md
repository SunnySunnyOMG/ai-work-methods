# 探索、固化与例外

触发：重复操作已有可重复路径，准备替换自主探索。

先用AI或现有工具跑通真实任务，记录输入、动作、输出判据和失败样本。稳定部分脚本化，保留契约验证、目标端检查与例外入口。脚本值应区分“0”与“未知/解析失败”，避免默认值掩盖缺失。

网页节点变了：保存授权可读的当前页面/错误样本，标结果未知；让模型观察或定位变化，再修规则并重跑新旧样本，核查真实输出。不能凭模型生成“合理价格”。处理不稳定来源时可继续人工/模型路径，不必急于固化。

重复CSV求和已有有效契约时直接运行程序，异常schema/差值/缺失才进入判断。LLM兜底是有条件的恢复，不是每次成功执行后的额外批准层。重试必须有停止条件，重复相同故障转为诊断或未决报告。

依据：[workflows与agents](https://www.anthropic.com/engineering/building-effective-agents)、[Skills与确定代码](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)。
