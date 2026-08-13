---
name: visual-e2e-verify
description: >-
  当前端页面或组件开发完成，需要进行视觉效果验证、响应式适配检查、交互流程测试或集成验收时触发此 Skill。
---

# 视觉与端到端验证 (Visual & E2E Verification)

本 Skill 对应 `Frank_Agentic_Workflow.md` 流程图中的 **3. 代码实施层 -> 视觉与端到端集成验证 (Visual & E2E Verification)** 节点。

## 目标 (Goal)
确保交付的前端 UI 页面无样式错位、无文字溢出、无响应式断裂，且微交互符合预期。

## 验证步骤 (Verification Steps)

1. **构建/开发服务检查**：
   - 检查本地 Dev Server 或预览环境是否可正常编译。
2. **视觉自检维度**：
   - **布局完整性**：容器边界、Padding/Margin 是否匀称。
   - **文字与对齐**：长文本是否溢出、多语言或变长文本缩放效果。
   - **响应式排查**：在不同尺寸（手机 375px、平板 768px、桌面 1440px）下无横向滚动条出现。
   - **交互反馈**：按钮点击、Hover 悬停、Focus 焦点的 Style 切换是否平滑。
3. **缺陷归类与处理**：
   - 若发现严重样式错误或渲染失败，**回退至 `frontend-components` Skill 重新修复**。

## 验证结论产物模板 (Output Checklist)

```markdown
### 👁️ 前端视觉与 E2E 验证结果
- [x] 桌面端 (1440px) 布局渲染正常
- [x] 移动端 (375px) 自适应布局无溢出
- [x] Hover / Active 交互微动画正常
- [x] 无浏览器控制台 Console Error/Warning
```
