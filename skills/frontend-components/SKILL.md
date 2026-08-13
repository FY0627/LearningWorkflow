---
name: frontend-components
description: >-
  当需要编写、修改或重构前端 UI 组件、页面布局、CSS 样式或交互逻辑时触发此 Skill。
  用于指导高质量 UI 实现、确保遵循 Design System 规范与防御性设计原则。
---

# 前端视图组件开发 (Frontend Components)

本 Skill 对应 `Frank_Agentic_Workflow.md` 中的 **3. 代码实施层 -> 前端视图组件 (frontend-components)** 节点。

## 目标 (Goal)
交付符合高端视觉美学 (Premium Aesthetic)、具备流体响应式 (Fluid Responsive) 且代码干净无臃肿的前端组件。

## 核心设计规范 (Design System Rules)

详细的设计禁区与美学要求见：
[ui-design-rules.md](./references/ui-design-rules.md)

关键要点：
1. **语义化 HTML5**：正确使用 `<header>`, `<main>`, `<nav>`, `<article>`, `<button>` 等语义化标签。
2. **设计系统 Token 优先**：统一在 CSS 根节点声明变量（Hsl 颜色、字号、间距、圆角与 Shadow）。
3. **交互与微动画**：所有按钮、卡片添加流畅的 `:hover`, `:active`, `transition` 效果。

## 执行步骤 (Execution Steps)

1. **检查与设计 Token 定义**：查看现有 `index.css` 或样式文件是否有统一的色彩与字号 Token。
2. **编写组件结构**：按 Functional-Driven 理念构建结构，不堆砌无意义的装饰性节点。
3. **样式与响应式注入**：确保组件在移动端 (Mobile)、平板 (Tablet) 和桌面端 (Desktop) 自适应流体缩放。
4. **自检与禁区排查**：对照 [ui-design-rules.md](./references/ui-design-rules.md) 检查是否有俗套设计（如强加网格背景、紫光深色调等）。

## 成果验证 (Verification)
- 检查 HTML 唯一 ID 标记是否完整。
- 确认组件无硬编码 static pixel 冲突。
