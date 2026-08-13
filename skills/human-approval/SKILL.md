---
name: human-approval
description: >-
  在关键规划、架构重构或可能产生破坏性变更的代码实施前，引导用户进行人工评审与授权时触发此 Skill。
---

# 人工评审与授权 (Human Approval Gate)

本 Skill 对应 `Frank_Agentic_Workflow.md` 中的 **2. 证据收集与规划层 -> 人工评审与授权 (APPROVAL)** 节点。

## 目标 (Goal)
清晰提示变更风险与重要影响，暂停自动化流转，确保用户明确同意后方可进入代码修改。

## 检查要点
- 是否有破坏性变更 (Breaking Change)？
- 实施计划是否已获得用户 Proceed 许可？
