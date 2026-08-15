---
name: clarify-intent
description: >-
  当用户提出新需求、想法或功能修改请求，但细节不够清晰、边界模糊或缺乏架构要求时触发此 Skill。
  用于引导用户澄清意图，梳理出结构化的需求规约前提。
---

# 澄清意图 (Clarify Intent)

本 Skill 对应 `docs/workflow.md` 流程图中的 **入口分流层 -> 澄清意图 (clarify-intent)** 节点。

## 目标 (Goal)
将用户的模糊需求/原始想法转化为清晰、明确、结构化的需求范围说明，为后续生成 `requirements-spec`（需求规约书）提供凭据。

## 执行步骤 (Steps)

1. **评估需求完整度**：
   - 检查用户输入是否包含：目的 (Why)、功能点 (What)、适用场景 (Who/Where)、限制条件 (Constraints)。
2. **主动提问与排查**：
   - 如果缺乏技术选型或 UI 样式要求，提出 2-3 个关键多选题或针对性问题。
   - 探查代码库，确定受影响的模块或目录。
3. **整理结构化意图**：
   - 归纳核心功能与次要功能。
   - 识别潜在的风险点或破坏性变更 (Breaking Changes)。

## 输出规范 (Output Format)

在对话中生成如下格式的【需求意图澄清摘要】：

```markdown
## 🎯 需求意图澄清摘要 (Clarification Summary)

### 1. 核心目标
- **业务/功能目标**：[简述]
- **目标用户/场景**：[简述]

### 2. 需求边界与范围
- **包含范围 (In Scope)**：
  - [功能点 1]
  - [功能点 2]
- **排除范围 (Out of Scope)**：
  - [暂不处理的细节]

### 3. 待决策/确认事项 (Action Items for User)
> [!IMPORTANT]
> 1. [需要用户确认的决策点 1]
> 2. [需要用户确认的决策点 2]
```

## 交付与后续流转 (Next Steps)
- 澄清完成后，流入下一步节点：**`requirements-spec` (需求规约书)** 或 **`implementation-plan` (实施计划)**。
