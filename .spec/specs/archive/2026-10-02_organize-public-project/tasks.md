# Organize open-source project structure and documentation - 任务拆解

## 阶段一：结构事实与边界

- [x] 完成结构事实审计和目录 disposition
  - id: task-structure-audit
  - boundary: 只读取结构审计、Git inventory 和 live reference graph；不移动或删除目录
  - verify: `python3 scripts/organize_project_structure.py --root .`；对 `.spec`、`data`、`tests`、`tools` 和 skill 目录分别记录 keep 理由

## 阶段二：文档修正

- [x] 修正内部文档路径和开源贡献指南路径
  - id: task-doc-paths
  - depends-on: task-structure-audit
  - boundary: 只改 `Agent.md`、`CONTRIBUTING.md` 和本 spec 文档
  - verify: 结构审计 finding class 中的 dangling doc paths 清零，Markdown 路径均从仓库根目录可达

- [x] 同步公开/开发 release 边界说明
  - id: task-release-boundary
  - depends-on: task-doc-paths
  - boundary: 只补文档事实，不改变 `build_release.py` 的既有过滤行为
  - verify: 用户 release 归档检查继续证明不包含 Agent、DEVELOPMENT、tests、evals、data、tools

## 阶段三：验收与交付

- [x] 运行项目全量验证并完成组织记录
  - id: task-organize-acceptance
  - depends-on: task-release-boundary
  - boundary: 只更新 checklist、spec archive 和必要验收证据
  - verify: organize `--check`、quick validator、项目 validator、6 个单测、`git diff --check` 和 release 构建全部通过

---

**当前进度**：由脚本计算，无需手动维护
