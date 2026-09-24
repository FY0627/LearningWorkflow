# 工作流溯源与保真度

本文逐节点记录 [`workflow.zh-CN.md`](workflow.zh-CN.md) 中哪些部分复刻自原始工作流、
哪些部分是我自己的设计。

它之所以存在，是因为诚实的答案是"部分复刻，且以下是精确的分界线"。
**未标注的复刻**与**夸大的原创声明**，是同一种失败的两个方向。

英文版本：[`workflow-fidelity.md`](workflow-fidelity.md)。

## 可用证据

原始工作流我只拿到**打码截图** —— 节点框可见，绝大多数标签文字被涂抹。
共两张：全图视图，以及下半部分的放大视图。

我**没有**原始仓库、原始 Mermaid 源码，也**没有**未打码的节点清单。

## 方法

Mermaid `flowchart TD` 由 dagre 布局。两条性质使得即使文字不可读，拓扑仍可部分还原：

1. 子节点必然被放置在比父节点更低的 rank 上。
2. 同一 rank 的节点距根节点的图距离相同，因此**同一水平线上的两个框不可能是父子关系** ——
   它们要么是兄弟，要么无关。

逐 rank 数框因而可以重建图的**形状**，但重建不出**标签**。下文所有 `inferred`（推断）
分类，依据全部来自于此。

## 溯源标签

| 标签 | 含义 | 数量 |
|---|---|:--:|
| `replicated` 复刻 | 截图中标签文字可辨认，我按其明确含义实现 | 14 |
| `inferred` 推断 | 该位置该 rank 确有一个框，但文字被打码。**位置是证据，内容是我的设计** | 11 |
| `original` 原创 | 该位置找不到对应节点，属我的新增 | 1 |

`inferred` 占多数，这是诚实的结果。它的含义是：我知道这里应该有一个节点，
我不知道原作者管它叫什么，对应 skill 里的一切内容都是我写的。

## 节点表

### 第 1 层 —— 入口与分流

| 节点 | 标签 | 溯源 | 依据 |
|---|---|---|---|
| `START` | 需求 / 想法 / 现有项目 | `replicated` | 文字完全可辨认 |
| `DECISION` | 此工作需要什么？ | `replicated` | 文字完全可辨认 |
| `clarify-intent` | 澄清意图 | `replicated` | 首字符 `clar…` 可辨认 |
| `fix-issue` | 修复问题 | `replicated` | 首字符 `fix …` 可辨认 |
| `report-source` | 源码调研 | `replicated` | `reportSou…` 可辨认 |
| `feature-ready` | 功能就绪 | `replicated` | 尾字符 `…eady` 可辨认。rank 位置存疑 —— 见待决问题 1 |

### 第 2 层 —— 证据与规划

| 节点 | 标签 | 溯源 | 依据 |
|---|---|---|---|
| `requirements-spec` | 需求规约书 | `inferred` | 证据层 rank 有框，文字被打码 |
| `root-cause-analysis` | 根因分析报告 | `inferred` | 证据层 rank 有框，文字被打码 |
| `codebase-audit-summary` | 代码库审计摘要 | `inferred` | 证据层 rank 有框，文字被打码 |
| `implementation-plan` | 生成实施计划 | `inferred` | 有框，文字被打码 |
| `human-approval` | 人工评审与授权 | `inferred` | 证据层与 `implementation` 之间共占两个 rank，与"计划 + 审批"数量吻合。**并非原创** |

### 第 3 层 —— 实施与验收

| 节点 | 标签 | 溯源 | 依据 |
|---|---|---|---|
| `implementation` | 代码实施 | `replicated` | 文字完全可辨认 |
| `subagents-overview` | 子 Agent 任务总览 | `replicated` | `subagentsOv…` 可辨认 |
| `sandbox-test` | 本地沙盒测试验证 | `inferred` | 并行段 rank 1 有框，文字被打码 |
| `api-backend-agents` | 后端与 API 子 Agent | `inferred` | rank 2 汇聚点有框，文字被打码。**把这个 skill 指派到那个位置是我的设计决策** —— 见设计决策 3 |
| `frontend-components` | 前端视图组件 | `replicated` | `fronten…` 可辨认 |
| `code-consolidation` | 代码重构与汇总 | `inferred` | rank 3 有框，文字被打码 |
| `visual-e2e-verify` | 视觉验收 | `inferred` | rank 4 有框，文字被打码 |
| `e2e-verify` | 端到端验收 | **`original`** | 原图此处**只有一个节点**。我把它拆成了视觉验收与端到端验收 —— 见设计决策 2 |

### 第 4 层 —— 门禁与结项

| 节点 | 标签 | 溯源 | 依据 |
|---|---|---|---|
| `github-actions-ci` | GitHub Actions CI 流水线 | `replicated` | `…thub-actions-ci` 可辨认 |
| `production-deployment-gate` | 生产环境发布门禁 | `inferred` | `required checks pass` 边正下方确有一个框。**并非原创** |
| `telemetry-global-memory` | 性能遥测与全局记忆沉淀 | `inferred` | 发布门禁下方有框，文字被打码 |
| `security-audit` | 代码安全审计 | `replicated` | 尾字符 `…udit` 可辨认 |
| `agents-md` | 更新规范准则 | `replicated` | 文字完全可辨认 |
| `organize-docs` | 整理归档文档 | `replicated` | 文字完全可辨认 |
| `project-closeout` | 项目结项闭环 | `replicated` | 文字完全可辨认 |

## 设计决策

以下是我有意做出的改动。它们**不是**复刻，也不以复刻的名义主张。

### 1. `security-audit` 是 `production-deployment-gate` 的兄弟节点，不是子节点

原图截图中，发布门禁框与安全审计框位于**同一条水平线**上。依据前述 rank 性质，
二者不可能构成父子关系 —— 它们都是 `github-actions-ci` 的子节点。

此前的复刻版本把它们串成了 `github-actions-ci → 发布门禁 → 安全审计`。
这个顺序等于在审计一个**已经通过发布门禁的软件**。已修正为分叉。

**留给后续阶段的子问题：** 兄弟关系意味着发布门禁并不以审计结果为前置条件。
"以审计结果作为发布门禁的前置"可能比现有两种安排都更强。
我选择保留**有证据支撑的拓扑**，而不是拿我的偏好替换它，并在此标注存疑。

### 2. 单一验收节点被拆成两个

原图在此处只有一个节点，本工作流有 `visual-e2e-verify` 与 `e2e-verify` 两个。

拆分的原因：已有两个 skill 分别承载这两项职责，而"24 个 skill 指向 23 个节点"
是一个必须能被校验器抓住的缺陷。

视觉验收回答"看起来对不对"；端到端验收回答"跑通没跑通"。证据不同，失败模式也不同。

### 3. 并行段是编织结构（2-1-2-1），且汇聚点的 skill 归属是我指派的

原图并行段的 rank 分布为 **2-1-2-1**：两个框、一个框、两个框、一个框。
此前的复刻版本渲染为 **1-2-2-1** —— 两条平行直轨一路到底、仅在末尾汇聚，中途没有同步点。

**编织形状是复刻的。但 rank 2 汇聚点由哪个 skill 占据，是我的决定**：
选择 `api-backend-agents`，理由是两条轨道都必须先有一个稳定的 API 接口面，
之后前端工作与代码整合才能真正各自独立推进。原图该处标签被打码。

### 4. 两条失败回退边，而非一条

原图只有一条标注了文字的失败回退边指向 `implementation`。它的起点在截图中是模糊的 ——
其高度更接近 CI 节点，而非验收节点。

我没有去抠像素，而是按语义定夺：`e2e-verify` 失败与 `github-actions-ci` 失败
是两类失败、两条诊断路径，因此分设两条回退边。**这是设计，不是复刻。**

### 5. 代码证据时效性的回退边

虚线 `implementation-plan → report-source` 和 `implementation → report-source` 是本项目新增的
流程设计，并非声称打码原图中可见这些连线。代码证据缺失或过期时，计划先退回范围内的源码调查；
实施期间若相关计划外代码变化使获批计划的依据失效，也经同一路径补充调查、修订并重新审批。
`feature-ready` 只表示需求结果已经明确，不代表现有代码库的证据仍有效。

## 待决问题

1. **`feature-ready` 的 rank 位置。** 原图中它似乎位于**证据层 rank 的最右侧**，
   由一条长边直接从 `DECISION` 拉过来，而非与其余三个分支并列在分流层 rank。
   两种读法的可达性相同。暂未定论；当前实现将其置于分流层 rank。

2. **被打码的标签将永远保持打码状态。** 在拿到原始资料之前，`inferred` 一栏中
   没有任何一项可以升级为 `replicated`。如果那份资料永远拿不到，它们就**永久保持
   `inferred`**，不会被悄悄提级。

## 规则

`inferred` 或 `original` 的节点，在本仓库、在 README、在作品集、在任何对话中，
都不得被描述为复刻。**诚实的不确定优先于虚假的确定。**
