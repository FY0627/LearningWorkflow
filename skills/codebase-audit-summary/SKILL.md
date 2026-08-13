---
name: codebase-audit-summary
description: >-
  在对现有代码库进行重构、添加新功能、排查复杂样式冲突或评估组件依赖时触发此 Skill。
  源码调研完成之后，整理输出结构化的代码库审计摘要凭据。
---

# 代码库审计摘要 (codebase-audit-summary)

本 Skill 对应 `docs/workflow.md` 中的 **2. 证据收集与规划层 -> 代码库审计摘要 (codebase-audit-summary)** 节点。

## 目标 (Goal)
快速梳理项目现有的组件树结构、全局样式 Token 定义、依赖库版本及全局状态分布，避免无意义的重复轮子和样式污染。

## 审计维度 (Audit Dimensions)

1. **项目技术栈识别**：
   - 确定框架（React, Vue, Vite, Next.js, HTML/JS）。
   - 确定样式解决方案（Vanilla CSS, TailwindCSS, CSS Modules, Styled Components）。
2. **组件与路由结构分析**：
   - 梳理主页面布局与公共 UI 组件（Button, Modal, Card, Navbar）。
3. **全局样式与 Token 定位**：
   - 查找 `index.css`, `globals.css` 或 `theme` 配置文件，确认 CSS 变量定义情况。
4. **潜在风险点记录**：
   - 是否存在写死的大段行内样式 (style="...")。
   - 是否存在旧样式与新样式的 CSS 选择器命名冲突。

## 输出摘要模板 (Output Format)

```markdown
### 代码库审计摘要 (Codebase Audit Summary)
- **技术栈**：[例如 Vite + React + Vanilla CSS]
- **公共组件位置**：`src/components/`
- **样式 Token 文件**：[例如 `src/index.css`]
- **重构/新增功能注意事项**：
  1. [注意事项 1]
  2. [注意事项 2]
```
