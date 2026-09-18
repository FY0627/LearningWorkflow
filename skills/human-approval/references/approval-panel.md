# Plan Review Panel

Load when a plan is ready for a human decision.

## Presentation

Use the operator's language. Name the revision and link the full plan. Present its summary
without silently altering the plan.

| Review item | Required content |
|---|---|
| Work and scope | Actions, affected components, boundaries |
| Result and acceptance | Intended outcome and how it will be checked |
| Material effects | Consequences and decision-relevant limitations |
| Recovery readiness | Verified recovery and coverage, or pending prerequisites |

Then offer two main choices: A, approve this revision; B, request adjustments.
Waiting is the default. An explicit cancellation is accepted without a permanent third option.

## Rules

- Meet the 30-second reading target for a tired operator. Aim for one screen and at most
  150 Chinese characters or 100 English words of explanation, excluding paths and links.
  This concerns reading, not execution time.
- Never omit scope, acceptance, material effects, or unmet prerequisites to shorten the panel.
  Split independent decisions upstream; explicitly flag a longer panel if disclosure needs it.
- Approval requires the displayed identifier, without a second acknowledgment or comprehension
  test. Concrete revision feedback does not need an identifier.
- A Git repository is not a verified checkpoint. Distinguish existing and proposed recovery.
  Approval of preparation does not prove preparation succeeded.
- An irreversible external effect remains visible even when file changes have a checkpoint.
- Show recovery readiness, coverage, and limitations; do not generate or display recovery commands.
- Replace material changes with a clearly identified new panel. Do not repeat unchanged panels.

## Paired designed examples — not execution evidence

The work stays constant; only recovery readiness changes. Paths and revisions are illustrative.

```text
待审核：登录提示优化 v2 — [完整计划](implementation_plan.md)

| 审核事项 | 计划 |
|---|---|
| 工作与范围 | 修改登录失败提示及测试，不改变验证逻辑 |
| 结果与验收 | 显示明确错误提示；验证错误与成功登录流程 |
| 主要影响 | 用户看到新文案，无数据迁移 |
| 恢复准备 | 检查点 R01 已验证，覆盖涉及文件的当前内容 |

| 选项 | 含义 |
|---|---|
| A. 批准 | 按 v2 范围执行 |
| B. 调整 | 说明需要修改的内容 |
```

```text
待审核：登录提示优化 v2 — [完整计划](implementation_plan.md)

| 审核事项 | 计划 |
|---|---|
| 工作与范围 | 修改登录失败提示及测试，不改变验证逻辑 |
| 结果与验收 | 显示明确错误提示；验证错误与成功登录流程 |
| 主要影响 | 用户看到新文案，无数据迁移 |
| 恢复准备 | 待建立覆盖涉及文件当前内容的检查点；验证成功后才能修改 |

| 选项 | 含义 |
|---|---|
| A. 批准 | 按 v2 范围执行 |
| B. 调整 | 说明需要修改的内容 |
```

Both require approval. The second permits disclosed preparation but blocks edits until its
prerequisite succeeds. No example establishes that recovery actually exists.

## Acceptance criteria

- The operator can identify scope, outcome, effects, and readiness from the panel.
- Approval identifies a revision; adjustment returns to planning without starting edits.
- Questions and silence do not authorize implementation.
- Tests of the former per-operation gate do not validate this plan-review contract.
