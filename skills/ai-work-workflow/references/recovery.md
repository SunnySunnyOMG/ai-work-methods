# 状态核对与副作用恢复

触发：中断、超时、日志与目标状态冲突，或任务会写入/发送/通知。

每个副作用尽量有操作身份、目标状态、回执/证据和重试条件；支持幂等键则同一意图复用同一键。多个影响分别记状态，别仅存一项“任务完成”。恢复先核对哪些已发生，再补缺口。

邮件发送超时且无回执：查发送记录、目标状态或幂等身份。已发送则不再发送；确认未发送且既有授权允许才重试该步；无法确认则保持unknown并报告具体未决，不能盲重发。不要为已获授权的同一行动再问泛泛permission。

排队不等于消费，进程存活不等于有效工作；日志空可能是观察故障。查任务ID/消费者/目标读回，分别修观察与执行。只能确认某层就报告该层。

checkpoint恢复可能重跑未完成步骤，外部系统未必exactly-once。只对可重试故障有限次数恢复，同故障反复出现改为诊断；不能用重试掩盖坏输出。

依据：[持久化/checkpoint](https://docs.langchain.com/oss/python/langgraph/persistence)、[replay与幂等](https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/functional-api.mdx)。不要求采用该框架。
