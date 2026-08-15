---
name: security-audit
description: >-
  在代码准备提交或流向 CI 流水线前，进行代码安全扫描、敏感信息泄露防范和硬编码密钥检查时触发此 Skill。
---

# 代码安全审计 (Security Audit)

本 Skill 对应 `docs/workflow.md` 中的 **4. 门禁与结项归档层 -> 代码安全审计 (security-audit)** 节点。

## 目标 (Goal)
扫描代码中的高危安全隐患（XSS, SQL 注入, 越权漏洞及 API Key 硬编码）。
