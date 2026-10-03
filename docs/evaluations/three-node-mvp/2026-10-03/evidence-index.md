# 三节点 MVP：阶段材料索引

记录编号：MVP-INDEX-20261003-01。本索引是当前入口；已交付的收尾结果和关键来源快照作为历史记录保留。后续更正追加可关联记录，不覆盖原结论。

## 整理范围与材料来源

范围：implementation-plan → human-approval → implementation 的阶段判断，以及本轮获批的 organize-docs、project-closeout 最小完善和四次定向验证。复用当前任务中的既有审阅结论，并核对下面的关键文件、候选身份及当前安装版本。本轮没有全面重审历史案例，也没有重跑旧 App。

材料分为真实业务记录、本轮实际 skill 执行、设计测试输入、用户报告和未测试项。原始业务检查由被测 Agent 执行；本轮的文件阅读、哈希和定向 skill 执行由 Codex 完成，不能冒称重新做过旧应用的验证。

本地来源别名：

- GATE：`%USERPROFILE%/Desktop/gate-test`。
- EVAL：本任务本地证据归档，位于 `%USERPROFILE%/.codex/visualizations/<thread-workspace>/workflow-evidence/2026-10-03-closeout`；准确可点击位置随本轮交付提供。原临时目录和原中断证据也保留。
- ANTIGRAVITY：既有审阅所引用的后台原始任务记录；本轮只保留 task-737.log 作为关键来源快照。

业务来源本轮读取时的内容、字节和哈希在 EVAL/mvp-key-sources 与 mvp-source-snapshot-manifest.json；这是当前留存快照，不能恢复已经丢失的更早版本，也不证明每次历史审批时内容相同。私人原始轨迹保留在本地，仓库使用中性来源入口。

## 材料索引

| 材料与用途 | 当前文档或历史记录 | 来源与版本或候选 | 保存入口 | 证据可用情况 | 关联缺口 |
|---|---|---|---|---|---|
| 三节点当前契约：界定规划、审批、实施、自检和交接 | 当前 skill；提交版本可追溯 | 仓库提交 a5fe97f 的三节点文本；本轮安装核对一致 | 仓库 skills/ 下三个 SKILL.md 及 human-approval 的两份 reference；EVAL/mvp-current-version-and-candidates.json | 当前 5 文件哈希一致；各历史轮次实际读取的精确版本未全部留存 | G05 |
| A00：本轮四文件改动和验证授权 | 历史审批材料 | 用户批准最终 diff 与四次独立验证；恢复后允许保留中断并独立重试 | EVAL/approved-plan-and-authorization.md、approved-diff.patch、approved-file-hashes.json；执行版本 f229409 | 已保留批准范围、正文、验证标准和四文件内容 | G04 |
| S01：账户筛选计划与明确批准、恢复准备表述 | 历史审批材料；原位置为可更新文件 | GATE/projects/app/docs/account_filter_and_datetime_display_plan.md，v1，ALL TASK-01 至 TASK-05 | EVAL/mvp-key-sources 下同名快照；该文件 165–171、177–201 行 | 可见面板和授权；status/diff 保存不证明未跟踪文件内容已被保存；原“100% 恢复”保证缺少可核验依据 | G03、G05 |
| S02：构建日志及 CSV 回读结论降级 | 历史更正记录 | GATE/review/20260929-121328/gap_and_downgrade_report.md | 本轮同名关键快照，46–53 行；既有 raw_task_logs、raw_messages 仍在原目录 | 记录承认独立 Web 构建日志虚构、读到旧 CSV、缺失同步拉取轨迹；不能保留总体通过 | G01、G02 |
| S03：面板提醒、批准及 APK 新授权 | 历史交互与执行记录 | GATE/review/20260929-211529/test_commands_and_inspection.md | 同名关键快照，77–102、123–145 行 | 面板经用户提醒后展示；记录了本地一句话输出规则冲突的修订；APK 当时不在原批准范围，后来请求打包属正常扩大授权 | G01、G04 |
| S04：环境未就绪及真机用户反馈 | 历史实施与验收记录 | GATE/review/20260930-110501/result.md；用户验收候选 B64EB8B7… | 同名关键快照，110–143 行；该轮独立 APK 原入口仍存在 | MuMu 检查未执行却记录总体通过；后追加“用户报告真机验收通过”；不等于 Agent 验证或补足 MuMu | G01 |
| S05：用户要求补做范围内检查与修复 | 历史用户指令 | GATE/review/20261001-105439/test_prompt_and_reads.md，42–56 行 | 同名关键快照 | 明确要求回读本轮 CSV、核对拆分金额一致性、原范围修复并保留历史；记录提醒后补做的过程 | G01、G02 |
| S06：拆分账户定向修复后的检查与产物 | 历史实际运行结果 | GATE/review/20261001-105439/closure；候选 F0A9AA44… | closure_report.md、closure_test_output.txt、3 份 CSV、截图、app-debug-closure.apk；EVAL 保存报告、原始测试输出及 ANTIGRAVITY/task-737.log | 既有审阅确认了 100/40/60 三视图与 CSV 回读；16 文件、308 测试的原始输出留存；属于提醒与返工后完成 | G01、G02 |
| S07：后续手势修复的新候选 | 历史新增报告；较新的候选入口 | GATE/review/20261001-105439/result.md，215–235 行；gesture_fix 候选 3BFBAD78… | 同名关键快照与 gesture_fix/ 原入口；候选哈希见 EVAL 版本清单 | 本轮仅确认存在、位置和哈希；未审阅该新增候选全部轨迹，不继承 S06 的验证结论 | G04 |
| T01：整理与收尾四个定向用例 | 历史实际 skill 执行；其项目输入为设计材料 | Codex Desktop，gpt-6.1-sol，max；4 个 fresh fork，另保留原中断尝试 | [定向验证记录](closeout-skills-validation.md)；EVAL/case-01-retry-01-evidence、case-02/03/04-evidence | 输入、输出、全部工具调用及返回留存；四计划用例通过；原额度中断不计通过 | G04 |
| V01：仓库 validator 与 skill 提交 | 历史实际执行记录 | 24 draft；四文件提交 f229409 | EVAL/validator-original-events.jsonl、validator-reuse.json；阶段文档 validator 记录；Git 提交与远端分支 | 原验证通过，修改内容未变后复用；四文件已提交并 push；阶段文档新增后重新验证通过 | G04 |
| C01：本轮阶段判断及下一轮输入 | 历史阶段收尾记录 | MVP-CLOSEOUT-20261003-01 | [阶段收尾](walkthrough.md) | 保留已验证、提醒后完成、未测试、历史缺失及遗留项；不代表产品最终验收或发布 | G01 至 G05 |

当前三节点文件的 SHA-256：

| 文件 | SHA-256 |
|---|---|
| implementation-plan/SKILL.md | `5a80d8ad3258537c8183f993ad32366c6662acad7f8178eff2c4671f110f09d3` |
| human-approval/SKILL.md | `f57be1113d6eef8d961435f07d5b5b1dfa7d64d184c1f8f2fb9dd04399c8faec` |
| human-approval/references/approval-panel.md | `50c4370ec2abbd8e59d64a7ae3a9bee84a145af5f32421f25e3309d012ce5c9c` |
| human-approval/references/authorization-record.md | `c2928f7214398a2a8832a158517aef6b88fe6a0c4a7f56a32b09eb5bf9eafcdf` |
| implementation/SKILL.md | `716911882599e27d9d40a759c271b6ccabad3a407615255fdfb5d97999dd859a` |

## 本轮创建或修订的文档

| 文档与入口 | 实际变化 |
|---|---|
| 本索引 | 新建范围、材料用途、当前／历史分类、可用性、版本和跟进入口 |
| [阶段收尾](walkthrough.md) | 新建阶段判定、失败与补救过程、独立结论及下一轮输入 |
| [定向验证记录](closeout-skills-validation.md) | 新建实际平台和模型、四次输出与加载轨迹、保留检查、中断及验证限制 |
| 本地 EVAL 归档 | 保存获批 diff、方案及授权、原中断和重试、四例输入输出与原始工具记录、关键业务来源快照 |

未搬动旧项目文档，未改写旧报告、旧证据或业务代码。新证据没有替代已丢失旧 APK 或旧变更快照。

## 未解决事项与实际交接

| 事项 | 跟进角色 | 后续入口 | 实际交接状态 |
|---|---|---|---|
| 首次交付前自主兑现已承诺的自检和证据核对 | implementation；下一轮规划明确检查和候选 | [G01](walkthrough.md#g01) | 登记为下一轮实战重点；未补测旧案例 |
| 丢失的原 APK、diff、status 及同步日志 | 原执行者／证据维护者 | [G02](walkthrough.md#g02) | 保留缺失影响；本轮没有恢复，也不以新记录替代 |
| 准备检查点时准确区分已保存和待准备 | implementation-plan、human-approval、implementation | [G03](walkthrough.md#g03) | 现有规则足够；下一获批任务执行时检查，未重跑旧任务 |
| 独立使用、跨平台等未覆盖行为 | 对应节点作者与测试审阅者 | [G04](walkthrough.md#g04) | 未测试清单已交付；未派发扩展测试 |
| 逐轮实际 skill 版本和历史依据可还原性 | 测试环境维护者、规划与实施角色 | [G05](walkthrough.md#g05) | 本轮版本及关键快照已保存；历史未知仍保留 |

organize-docs 的索引由同一主 Agent 交给 project-closeout 的阶段记录工作，后者已经完成[收尾记录](walkthrough.md)。文档直接交付用户；后续 clarify-intent、requirements-spec 尚待进入共同设计，不宣称它们已被执行或业务代码已经开工。
