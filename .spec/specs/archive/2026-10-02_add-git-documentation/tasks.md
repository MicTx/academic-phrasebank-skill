# Add mature open source documentation and GitHub templates - 任务拆解

## 阶段一：公开叙事

- [x] 重写读者入口和版本记录
  - id: task-reader-docs
  - boundary: 只改 `README.md`、`CHANGELOG.md`、`SUPPORT.md` 和本 spec；删除内部过程叙述，不改产品行为
  - verify: README 包含安装、用法、来源、许可证和文档导航；CHANGELOG 使用公开版本格式

## 阶段二：协作资料

- [x] 完善贡献、安全、行为准则和开发指南
  - id: task-maintainer-docs
  - depends-on: task-reader-docs
  - boundary: 只改 `CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`SECURITY.md`、`DEVELOPMENT.md`
  - verify: 每份文档包含稳定入口；不含当前会话、工作树或内部验收状态描述

- [x] 增加 GitHub 原生协作模板
  - id: task-github-templates
  - depends-on: task-reader-docs
  - boundary: 只新增 `.github/ISSUE_TEMPLATE/*` 和 `.github/pull_request_template.md`
  - verify: 模板文件存在、字段完整、配置关闭无模板 issue，并通过项目 validator

## 阶段三：验收与交付

- [x] 扩展文档门禁并运行全量验证
  - id: task-doc-acceptance
  - depends-on: task-maintainer-docs, task-github-templates
  - boundary: 只改 `tools/validate_skill_package.py`、checklist、spec archive 和 release 产物
  - verify: quick validator、项目 validator、7 个单测、git diff check、release 白名单和 checksum 全部通过

---

**当前进度**：由脚本计算，无需手动维护
