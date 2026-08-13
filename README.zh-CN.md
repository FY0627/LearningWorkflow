# LearningWorkflow

一套 26 节点的 Agentic 软件工程工作流，以可移植的 agent skill 形式打包，
并配有一个在 CI 中强制执行质量标准的校验器。

English: [README.md](README.md)

## 当前状态

**版本 0.1.0。框架已完成，内容尚未完成。**

全部 24 个 skill 均处于 `draft` 层级。draft 的含义是：节点已命名、目标已陈述，
**但它还不会实质性改变模型行为**。这一点写在这里，而不是留给使用者自己发现。
仓库本身也强制了这件事：skill 无法在不通过对应检查的情况下声称更高层级，
层级计数在 `skill-pack.json` 中可见。

| 层级 | 数量 |
|---|:--:|
| `stable` | 0 |
| `beta` | 0 |
| `draft` | 24 |

## 它解决什么问题

大多数所谓的 agent "工作流"就是一张图。而图是简单的那一半。真正会崩的是图说不出来的部分：

- **漂移。** 图说一套，skill manifest 说另一套，磁盘目录说第三套。没人发现，因为没有任何东西在检查。
- **空心 skill。** 一个只有标题和一句话的 skill 文件，在文件列表里看起来像个 skill，运行时什么都不做。
- **不可证伪的质量。** 没有评分卡、没有测试用例、没有门禁的"高标准"，是一句主张，不是一个属性。
- **溯源腐烂。** 复刻自他人的部分被说成原创，或原创部分完全没有标注，几个月后没人分得清哪是哪。

本仓库把这四件事全部当作**有机械解法的工程问题**来处理。

## 工作机制

**三份真相，互相校验。** [`docs/workflow.md`](docs/workflow.md) 中的 Mermaid 图、
`skill-pack.json` 的 `skills[]` 数组、`skills/` 下的目录，三者必须是完全相同的集合。
每个承载 skill 的节点标签都以括号内的 slug 结尾；校验器把它们解析出来，
并在所有方向上断言集合相等。改了节点却没改 skill，CI 直接红。

**成熟度分级 + 单向棘轮。** 每个 skill 在 manifest 中声明 `draft`、`beta` 或 `stable`，
层级越高检查越严。`maturity_floor` 记录各层级的数量，校验器断言实际计数**永不低于**该地板。
于是 CI 今天在 24 个 draft 的状态下就是绿的，而**质量一旦倒退立刻变红**。

**溯源逐节点记录。** 本工作流的一部分复刻自一个只能以打码截图形式获得的来源。
[`docs/workflow-fidelity.zh-CN.md`](docs/workflow-fidelity.zh-CN.md) 为每个节点标注
`replicated`（复刻）、`inferred`（推断）或 `original`（原创），列出各自依据，
并单独列出哪些设计决策是我的而非来源的。**14 个复刻，11 个推断，1 个原创。**

**隐私是扫描出来的，不是承诺出来的。** 绝对用户路径、家目录路径、邮箱地址、
形似凭据的 token，命中即构建失败。

## 工作流本身

四层：入口与分流、证据与规划、编织式并行实施、门禁与结项。其中两条性质值得单独点名：

**人工授权是硬门禁。** `implementation-plan` 无法绕过 `human-approval` 直达
`implementation`。人负责设定目标、把关架构、承担风险；Agent 矩阵负责执行与自我纠错。

**CI 通过是分叉，不是串联。** `production-deployment-gate` 与 `security-audit` 是兄弟节点 ——
串起来就等于在审计一个已经上线的东西。

完整图与设计理由：[`docs/workflow.zh-CN.md`](docs/workflow.zh-CN.md)。

## 目录结构

```
LearningWorkflow/
├── skills/<name>/SKILL.md        24 个 skill，与工作流节点一一对应
├── docs/
│   ├── workflow.md               26 节点图与设计理由
│   ├── workflow-fidelity.md      逐节点溯源
│   ├── skill-authoring-standard.md   层级定义与各层强制项
│   ├── compatibility.md          跨 agent 可移植性契约
│   ├── trigger-tuning.md         如何写出能正确触发的 description
│   ├── release-checklist.md      发布前门禁清单
│   └── skill-template/SKILL.md   撰写模板（不是可安装 skill）
├── examples/
│   ├── dry-runs.md               prompt 与期望行为，含对抗性用例
│   └── usage-benchmark.md        7 项评分卡，每项 0-2 分，及格线 11/14
├── scripts/
│   ├── validate-pack.py          门禁本体；仅用标准库；有错即 exit 1
│   └── install.ps1               多目标安装脚本
├── skill-pack.json               manifest：层级、棘轮、隐私策略
└── AGENTS.md                     agent 编辑本仓库时的规则
```

## 安装

```powershell
# 干跑，只看会发生什么，不写任何文件
./scripts/install.ps1 -Target all -WhatIf

# 为单个 agent 安装
./scripts/install.ps1 -Target claude

# 覆盖已有安装
./scripts/install.ps1 -Target claude -Force
```

可选目标：`claude`（`$HOME/.claude/skills`）、`codex`（`$HOME/.codex/skills`）、
`gemini`（`$HOME/.gemini/config/skills`）、或 `all`。
**不加 `-Force` 时，脚本拒绝覆盖已存在的 skill**（抛错，而非静默跳过）。

## 校验

```bash
python scripts/validate-pack.py .
```

仅用标准库，零依赖，有错即退出码 1。该命令在每次 push 时于 CI 运行
（[`.github/workflows/validate.yml`](.github/workflows/validate.yml)），
环境为 `windows-latest` + Python 3.12，同时附带安装脚本的语法解析检查与干跑。

## 参与本仓库

先读 [`AGENTS.md`](AGENTS.md)。其中最要紧的几条：frontmatter 严格两个键、
`SKILL.md` 不超过 220 行、层级提升与 `maturity_floor` 抬升必须在同一个 commit 里、
以及**不是复刻的东西不许说成复刻**。

## 诚信声明

本仓库**没有发布任何 benchmark 结果，因为一次都还没跑过**。
[`examples/usage-benchmark.md`](examples/usage-benchmark.md) 定义了评分卡与证据标签，
其结果表是空的，并将一直保持为空，直到一次真实运行产生一个真实数字。
[`examples/dry-runs.md`](examples/dry-runs.md) 中的全部用例都标注为 `designed-dry-run` ——
手工撰写，从未执行。

## 许可证

MIT，见 [LICENSE](LICENSE)。
