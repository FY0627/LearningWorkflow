---
name: fix-issue
description: >-
  当用户提出具体的 Bug、程序报错、功能异常或逻辑缺陷修补请求时触发此 Skill。
---

# 修复问题 (Fix Issue)

本 Skill 对应 `docs/workflow.md` 中的 **1. 入口与分流层 -> 修复问题 (fix-issue)** 节点。

## 目标 (Goal)
重现问题现象，收集完整的错误日志/凭据 (Evidence)，并输出供后续分析的诊断结论。

## 执行步骤 (Execution Steps)
1. **收集日志凭据**：读取未截断的崩溃日志、Terminal 报错或控制台输出。
2. **定位相关文件**：确定引发异常的代码模块与行号。
3. **交付产物**：流转至 `root-cause-analysis` 或 `implementation-plan` 节点。
