# Rename skill and package to academic-phrasebank-skill - 任务拆解

## 阶段一：名称迁移

- [x] 统一本地运行时名称与目录
  - id: task-runtime-rename
  - boundary: 只改 skill 目录、frontmatter、metadata、脚本常量、当前文档和测试路径；保留历史 spec archive 原文
  - verify: `rg` 当前文件无旧运行时名，quick validator 和项目 validator 通过

- [x] 保留旧安装目录清理兼容
  - id: task-installer-compat
  - depends-on: task-runtime-rename
  - boundary: 只改 `install.sh`、installer validator 和安装测试
  - verify: 临时 Codex/Claude 目录安装后存在新目录，两个旧目录均被清理

## 阶段二：构建与 release

- [x] 同步 builder、release 和用户文档
  - id: task-release-rename
  - depends-on: task-runtime-rename
  - boundary: 只改 `tools/build_phrasebank_refs.py`、`tools/build_release.py`、`README.md`、`DEVELOPMENT.md`、`NOTICE.md`、`CONTRIBUTING.md`、`Agent.md` 和 `.gitignore`
  - verify: release builder 生成 `academic-phrasebank-skill-<commit>`，归档包含新 skill 路径且不含旧运行时名或开发目录

## 阶段三：验收与交付

- [x] 完成全量验证并准备私有开发仓库提交
  - id: task-rename-acceptance
  - depends-on: task-installer-compat, task-release-rename
  - boundary: 只更新本 spec 记录和 release 产物，不创建 GitHub remote 或修改历史 archive
  - verify: 6 个单测、两个 validator、py_compile、git diff --check、安装 smoke、归档 checksum 和公开文件白名单全部通过

---

**当前进度**：由脚本计算，无需手动维护
