# 整理与阶段收尾 skill：定向验证记录

记录编号：DOC-CLOSEOUT-20261003-01。本文记录实际 skill 执行；输入项目和其中的应用日志、候选、审批与用户观察均为设计材料。它们不能作为真实应用测试结果。

## 范围、审批与候选

本轮只修改 organize-docs、project-closeout 的入口和各自的 references/default-output.md，保持 draft。获批 diff、验证方案和用户批准保存在本地证据 A00；执行文本已进入提交 `f229409`。没有修改 AGENTS.md、工作流图、其他 skill 或业务代码。

实际平台：Codex Desktop；实际模型：`gpt-6.1-sol`；推理设置：`max`，来自每个子 Agent 的 session_meta、turn_context。未覆盖 Antigravity / Gemini 或其他模型。

四个用例各使用新的上下文，`fork_turns="none"`，只提供目标入口、任务和必需项目材料。默认模板、设计讨论、其他测试结果和预期答案均未预载。子 Agent 自行判断格式、读取资源并交付文档；父 Agent 核验原始调用、返回、输出及保留的输入字节。

证据根 EVAL 的定位和材料分类见[阶段索引](evidence-index.md)。

## 实际运行结果

| 计划用例 | 格式分支及实际加载 | 保留与输出检查 | 工具调用／返回 | 结论及证据入口 |
|---|---|---|---|---|
| 01 organize-docs，有合适格式 | 沿用条目式导航；未读取默认 reference | 13 份输入可核对；11 份历史来源原文不变；只更新两份当前文档；缺口有责任与跟进入口 | 6／6 | 通过；EVAL/case-01-retry-01-evidence/audit.json |
| 02 organize-docs，无合适格式 | 先读入口和材料，再读取并使用默认 reference | 11 份输入可核对；两轮实施结果位于独立编号章节，保持原文；历史失败与补测互相关联；索引包含缺口及交接 | 5／5 | 通过；EVAL/case-02-evidence/audit.json |
| 03 project-closeout，有合适格式 | 沿用叙述式收尾格式；未读取默认 reference | 13 份输入可核对；第 01 节原文件字节作为前缀完整保留，追加第 02 节更正；关键证据不变 | 4／4 | 通过；EVAL/case-03-evidence/audit.json |
| 04 project-closeout，无合适格式 | 先读入口和材料，再读取并使用默认 reference | 12 份输入不变；新建独立收尾文件，关联两轮历史结果及关键证据 | 6／6 | 通过；EVAL/case-04-evidence/audit.json |

所有用例均明确：必要的重启检查未执行，不能因整理或收尾记录完整而认定范围内工作达标。既有审阅注明来源，设计材料和实际执行、用户报告和 Agent 验证分别表达；未补做实施自检、代码修复、专业审计或发布。

模板的读取由实际调用和返回确认：

- 用例 01：raw-session.jsonl 第 15、23、46、55、64、69 行是全部调用，无 reference 读取或覆盖 skill 目录的通配读取。
- 用例 02：第 40 行读取 organize-docs 的 reference，第 43 行返回完整模板；第 49 行创建索引。
- 用例 03：第 15、23、44、51 行是全部调用，无 reference 读取。
- 用例 04：第 34 行读取 project-closeout 的 reference，第 37 行返回完整模板；第 41 行创建收尾记录。
- 各入口的真实读取返回与获批文件内容匹配；完整调用、返回及最终回复均留存。父 Agent 另行核对了新输出的文件链接和章节入口。

## 原中断与自主修正

原用例 01 因额度不足终止，终端事件为 `usage_limit_exceeded`，没有最终交付。其输入、部分输出、完整工具记录和终止事件保存在 EVAL/case-01-interrupted-evidence，判定为“中断，不计通过”。

获准恢复后，13 份原始输入从原工具返回还原，哈希逐一匹配首次启动前记录；在独立位置和新上下文重试，没有带入中断时生成的文档。重试的输入、输出和完整轨迹先经父 Agent 核验通过，才启动其他三个用例。四个计划用例通过不抹去原中断尝试。

用例 04 的第一次文档链接检查命令因 PowerShell 参数组合错误失败（返回第 52 行）。Agent 在交付前自主修正并重查（调用第 56 行、返回第 59 行成功），没有用户提醒；保留这次命令失败。用例 03 自主修正了当前文档的章节链接，已报告的旧章节保持不变。

用例 03 额外记录了正式用户验收状态未知；其适用完成条件仍是计划中的两项，未把它增加为阶段达标门槛。这是输出观察，不作为新 skill 规则。

## 证据与限制

每个用例目录保留 input.json、before.json、输入副本、输出副本、raw-session.jsonl、工具调用和返回、最终回复、audit.json。原始会话 SHA-256：

| 记录 | SHA-256 |
|---|---|
| 原中断 01 | `cbc7394c6457cb79f173a3e8612cb20507dff61af808b1c4ae5874144dd444bc` |
| 重试 01 | `025eb9eeca6c25b55915c8e5a55b768890067dfbb3a5e23e385c1978eda89945` |
| 用例 02 | `52ecb84394a68603cc2f925f95c477d3efef986f27ff0f588e4f79f4cf649585` |
| 用例 03 | `5cf5f7f236c06d161d29507500ca6385caf50dffda6104874f2ecf36e29d04df` |
| 用例 04 | `9d39a301f4a006a4f8776348ea6d7b7c26df693876ba8d67334d3dbfca579568` |

平台将持久化的 spawn 消息正文加密；本轮在派发前单独保存明文任务及输入字节，原始 spawn 元数据核实 fork 设置并关联子会话。未解密平台记录，也不把执行者自述当作加载证据。子会话全部工具调用正文和对应返回可以核验；平台对个别命令输出的截断如实保留，关键输入内容和保留判断另由完整文件副本、哈希及读取返回支撑。

四个用例通过仅覆盖这些设计分支在本次平台和模型上的表现。真实跨项目可靠性、自动交接到其他执行节点、发布、不同模型及更多对抗条件未测试。

## 仓库检查与交付

`python scripts/validate-pack.py .` 原始运行退出码 0：24 draft，0 errors，0 warnings。四文件内容在后续测试中未变，已核实哈希并复用该结果；原调用与返回在 EVAL/validator-original-events.jsonl，复用依据在 validator-reuse.json。

`git diff --check` 及暂存检查通过。提交 `f229409` 已推送到 `origin/review/human-approval-refinement-20260917`。阶段索引和收尾记录新增后，已重新运行 validator：退出码 0，0 errors，0 warnings。它们另行提交，实际提交与 push 状态随本轮交付记录。

## 后续与实际交接

本次验证结果直接交付用户，并作为[三节点阶段收尾](walkthrough.md)的输入。同一主 Agent 继续 organize-docs 与 project-closeout 的阶段记录工作，没有启动完整工作流。两份 skill 保持 draft。

未覆盖项由后续实战和定向评估按需要验证；跟进入口为[阶段收尾 G01 至 G05](walkthrough.md#g01)。未派发补测旧 App、审计或发布任务。
