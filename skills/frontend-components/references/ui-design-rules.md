# 高端前端 UI 设计规范与美学禁区 (UI Design System Rules)

## 一、 美学原则 (Aesthetic Principles)

1. **实用驱动设计 (Function-Driven Design)**：首要目标是帮助用户高效达成目的，信息层级清晰，无多余装饰。
2. **现代字体系 (Modern Typography)**：使用 Google Modern Fonts（如 Inter, Plus Jakarta Sans, Outfits），注重 `letter-spacing`, `line-height` 细节。
3. **流体响应式 (Fluid Responsiveness)**：按钮、输入框、容器尺寸必须随屏幕和父容器自适应，不写死固定的宽/高。

## 二、 🚫 严禁使用的俗套设计 (Forbidden Cliché Tropes)

- ✕ **禁止滥用 Dashboard 格式**：非数据监控类应用不要强行套用仪表盘布局。
- ✕ **禁止深色背景配合浅紫色文字 (No Purple on Dark)**。
- ✕ **禁止使用彩色边框线发光 (No Colored Border Accents/Glowing outlines)**。
- ✕ **禁止堆砌无关图标的 Bento Box (No Icon-Stuffed Bento Boxes)**。
- ✕ **禁止标题上方加带脉冲圆点的 Pill 标签 (No Headline Biscuit Pills)**。
- ✕ **禁止大标题使用 CSS Gradient 渐变文字填充 (No Gradient Text Fill)**。
- ✕ **禁止网格背景线或粒子网格遮罩 (No Grid Backgrounds / Mesh Overlays)**。
- ✕ **禁止卡片多层嵌套超过 3 层 (No Over-Nested Cards)**。

## 三、 推荐色彩与 CSS 变量规范

```css
:root {
  --color-bg-primary: hsl(220, 15%, 98%);
  --color-bg-surface: hsl(0, 0%, 100%);
  --color-text-main: hsl(220, 20%, 10%);
  --color-text-muted: hsl(220, 10%, 45%);
  --color-accent: hsl(220, 90%, 56%);
  
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  
  --shadow-subtle: 0 2px 8px rgba(0, 0, 0, 0.04);
  --shadow-hover: 0 8px 24px rgba(0, 0, 0, 0.08);
}
```
