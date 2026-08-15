---
name: sandbox-test
description: >-
  在本地代码改动完成后，运行单元测试、测试套件或在隔离环境验证代码逻辑时触发此 Skill。
---

# 本地沙盒测试验证 (Sandbox Test)

本 Skill 对应 `docs/workflow.md` 中的 **3. 代码实施层 -> 本地沙盒测试验证 (Local Sandbox Testing)** 节点。

## 目标 (Goal)
运行测试命令（如 `npm test`, `pytest`），捕获任何断言失败并确保 100% 通过。
