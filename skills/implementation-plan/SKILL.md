---
name: implementation-plan
description: >-
  在真正编写代码前，需要生成分步骤、带文件清单和验证方案的架构实施计划时触发此 Skill。
---

# 实施计划生成 (Implementation Plan)

本 Skill 对应 `docs/workflow.md` 中的 **2. 证据收集与规划层 -> 生成实施计划 (implementation-plan)** 节点。

## 目标 (Goal)
生成标准 `implementation_plan.md` 产物，包含需求概要、待修改/新建的文件列表、组件关系及自动化/手动验证计划。

## 规则限制 (Boundary)
- **只生成实施计划 Markdown 文档，严禁修改任何源代码**。
- 引导用户进行评审并获取授权 (Human Approval Gate)。
