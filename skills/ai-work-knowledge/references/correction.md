# 纠正传播和只读一致性检查

触发：材料撤回、观察变更或要追踪本地派生依赖。

记录撤回/纠正原因和受影响来源；列出依赖主张与产物，逐条判断旧论点是否仍被独立材料支持。需要降级/撤回的标明状态并修下游；其他内容保留。波及范围未知时显式留未决，不整库删除，也不只改一条笔记就收口。

可选：从本Skill目录执行 `python3 scripts/check_sources.py manifest.json --changed source-id`。manifest使用相对路径：`{"sources":[{"id":"s","path":"source.txt","sha256":"64位小写hash"}],"claims":[{"id":"c","source_ids":["s"],"depends_on":[]}]}`。文件默认从manifest所在目录读取，`--root`可指定授权根目录；拒绝根外路径，不打印内容。

脚本检查本地文件hash与显式依赖；changed_sources/affected_claims列出需复核项。退出0只说明所给结构与hash一致，退出2是输入或一致性错误。`--changed`支持显式标注来源撤回，即使hash未变。脚本不修改任何文件，也不判断文件真假、引用是否支持主张、遗漏依赖或语义是否受影响。

先回原材料，再更新主张、相关报告和使用方。保留修改前证据与新判据，禁止把派生摘要当新的独立来源。
