# Organize open-source project structure and documentation - 验收清单

## 假设与范围对齐

- [x] 无阻塞性待确认项；目录迁移判定均为 keep。
- [x] 范围内/范围外与实现一致：只修正文档路径和组织说明，不移动 live 目录。
- [x] 本轮发现的可执行问题已回写并完成。

## 简洁性

- [x] 没有未请求的扩展、抽象或配置化。
- [x] 当前方案保持最小可行：审计、路径修正、验证。

## 变更边界

- [x] 改动可追溯到结构审计和文档任务。
- [x] 没有无关重构或顺手清理。

## 功能完整性

- [x] `academic-phrasebank-skill`、`data`、`tests`、`tools` 的职责说明清晰。
- [x] `.spec`、`data/raw` 等无 live reference 候选均有 keep 理由。
- [x] 文档路径不再指向不存在的相对路径。

## 测试与验证

- [x] 结构审计和 `--check` 已运行。
- [x] quick validator、项目 validator、6 个单测和 release 构建均通过。

## 文档同步

- [x] `Agent.md`、`CONTRIBUTING.md` 和本 spec 文档已同步。
- [x] 用户 README、开发文档、skill 路径和 source coverage 保持一致。

## 部署验证（如适用）

- [x] 本地运行与安装 smoke 通过。
- [x] 用户 release 归档白名单和 checksum 通过。

## 边界回归

- [x] 越界负样本：未移动 `.spec`、`data`、`tests`、`tools` 或 skill references。
- [x] 顺序交换负样本：结构审计只影响文档修正，未改变 builder/release 执行顺序。
- [x] 旁路负样本：组织审计没有绕过 validator、tests 或 release 检查。

## 验收证据

- 裁决性检查：`python3 scripts/organize_project_structure.py --root . --check` @ 2026-10-02。
- 证据锚点：HEAD `7725f00` @ 2026-10-02T21:10:00+08:00
- 脚本验证：quick validator、项目 validator、py_compile、git diff check 通过。
- 差异边界：仅修正文档路径与组织说明；目录 disposition 全部 keep。
- 行为成效：结构审计不再报告 dangling doc paths；用户包仍排除开发材料。
- 构建：`academic-phrasebank-skill-7725f00` release archive、manifest 和 checksum 通过。
- 测试：`python3 -m unittest discover -s tests -v`，6 个测试通过。
- 手工验证：`Agent.md` 和 `CONTRIBUTING.md` 路径从仓库根目录可达。

---

**验收结果**：通过
