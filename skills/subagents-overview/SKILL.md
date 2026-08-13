---
name: subagents-overview
description: >-
  当任务涉及大批量代码修改、模块间相互独立或需要并行研发（如后端 API 与前端 UI 拆分）时触发此 Skill。
  用于产出子 Agent 任务总览与分工边界。
---

# 子 Agent 任务总览 (subagents-overview)

本 Skill 对应 `docs/workflow.md` 中的 **3. 代码实施与并行处理层 -> 子 Agent 任务总览 (subagents-overview)** 节点。

## 目标 (Goal)
将复杂任务解耦拆分，分发给不同的子 Agent 独立并发执行，并明确各子任务之间的接口契约与合并顺序。
