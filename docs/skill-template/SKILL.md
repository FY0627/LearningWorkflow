---
name: skill-name-here
description: >-
  清晰简短地用第三人称描述该 Skill 的功能及触发时机。
  例如：“当用户需要对项目需求进行澄清、补全意图或定义范围时使用此 Skill。”
---

# Skill 名称 (如: Clarify Intent)

## 目的与触发场景
简要说明该流程节点在 `Frank_Agentic_Workflow.md` 中的位置与目标。

## 输入产物 (Inputs Required)
- 用户原始需求 / 想法 / 缺陷报告
- 相关代码上下文（如有）

## 执行步骤 (Execution Steps)
1. **初步分析**：分析用户需求的完整度与潜在风险。
2. **提问与澄清**：引导用户确认以下核心要素：
   - 核心功能点 (Functional Requirements)
   - 非功能性需求 (Performance/Security/UI)
   - 边界条件与限制 (Constraints)
3. **成果输出**：格式化整理澄清结果。

## 规范输出模板 (Output Template)
```markdown
### 需求澄清汇总
- **原始意图**：...
- **确认范围**：...
- **遗留/需用户决策点**：...
```

## 校验与质量关卡 (Verification Checklist)
- [ ] 所有模糊点均已得到明确答复
- [ ] 影响范围已在代码库中初步确认
