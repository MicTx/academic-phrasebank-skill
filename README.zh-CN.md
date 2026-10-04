# Academic Phrasebank Skill

`academic-phrasebank-skill` 是面向 Codex 和 Claude Code、以证据为边界的科研英语编辑 skill。

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/MicTx/academic-phrasebank-skill)](https://github.com/MicTx/academic-phrasebank-skill/releases/latest)

它可以起草、翻译、重构、诊断和润色科研手稿，同时保留作者的证据、术语、引用和不确定性。

核心原则很简单：**让语言和证据一样清楚，但不要让语言比证据更强。** 内置 Phrasebank 提供修辞模式，不会为手稿提供事实。

> [!WARNING]
> 这个 skill 改善表达和结构，但不会核验研究结果、创建参考文献，也不会让论点强于已有证据。

## 从这里开始

1. 使用 `./install.sh` 安装 skill。
2. 在 Codex 或 Claude Code 会话中调用 `$academic-phrasebank-skill`。
3. 说明任务、手稿章节、需要保护的内容和交付格式。

```text
$academic-phrasebank-skill
Polish this Results paragraph. Preserve every number, citation, variable,
and uncertainty marker. Do not add interpretation or references.
```

如果还不清楚问题在哪一层，可以先请求诊断：

```text
$academic-phrasebank-skill
Diagnose this Discussion section at manuscript, section, paragraph,
sentence, and phrase levels. Do not rewrite it yet. Keep [REF] unchanged.
```

## 它会保护什么

- 数字、单位、变量、统计符号、样本量和方向。
- 术语、缩写、方法名、引用和 `[REF]` 等占位符。
- 观察、关联、可能机制、含义和建议之间的证据差异。
- 样本、研究设计和证据支持的范围。

这个 skill 不会编造结果、机制、方法、参考文献或统计数据，也不会把 Phrasebank 示例中的 `X`、`Smith` 或 `Jones` 变成用户研究的事实。

## 选择合适的指南

- [中文介绍](academic-phrasebank-skill/docs/introduction.md) 说明 skill 的用途和边界。
- [教程](academic-phrasebank-skill/docs/tutorial.md) 通过一个受约束的 Results 修改示例说明使用方法。
- [Skill 契约](academic-phrasebank-skill/SKILL.md) 是模型执行任务时遵循的契约。
- [参考索引](academic-phrasebank-skill/references/index.md) 将任务路由到最小的参考文件集合。
- [修订框架](academic-phrasebank-skill/references/revision-framework.md) 定义多层次修订流程。

## 安装

可以从源码仓库或发布归档运行安装器：

```bash
./install.sh
```

默认会同时安装到 Codex 和 Claude Code。可以使用独立目录进行 smoke test：

```bash
CODEX_SKILLS_DIR=/tmp/academic-phrasebank-codex \
CLAUDE_SKILLS_DIR=/tmp/academic-phrasebank-claude \
./install.sh
```

可安装的 skill 名称是 `academic-phrasebank-skill`。

## 参考来源

参考页来自曼彻斯特大学公开发布的 [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/)。[来源覆盖说明](academic-phrasebank-skill/references/source-coverage.md)记录抓取页面、排除项、数量和来源 URL。

参考页是修辞模式库，不是科学事实来源。应根据用户的论点改写模式，不能把示例当作证据。重新分发或修改上游材料前，请阅读 [NOTICE.md](NOTICE.md)。

## 帮助与贡献

- [支持](SUPPORT.md) 说明使用问题或 bug 报告应包含哪些信息。
- [安全策略](SECURITY.md) 说明如何私下报告漏洞。
- 贡献者可以在源码仓库中阅读 `CONTRIBUTING.md` 了解内容规则和 pull request 检查，阅读 `DEVELOPMENT.md` 了解参考重建、校验和发布构建。
- [变更日志](CHANGELOG.md) 记录公开变更。

## 许可证

原始项目代码、安装器和项目文档采用 Apache License 2.0。Phrasebank 派生材料仍属于上游材料；归属与来源信息见 [NOTICE.md](NOTICE.md)。
