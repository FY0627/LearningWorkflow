---
name: subagents-dispatch
description: >-
  当任务涉及大批量代码修改、模块间相互独立或需要并行研发（如后端 API 与前端 UI 拆分）时触发此 Skill。
---

# 子 Agent 任务调度 (Subagents Dispatch)

本 Skill 对应 `Frank_Agentic_Workflow.md` 中的 **3. 代码实施层 -> 子 Agent 任务总览 (subagentsOverview)** 节点。

## 目标 (Goal)
将复杂任务解耦拆分，使用 `invoke_subagent` 分发给不同的子 Agent 独立并发执行。
