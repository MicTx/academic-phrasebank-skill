# Rename skill and package to academic-phrasebank-skill - 验收清单

## 假设与范围对齐

- [x] 无阻塞性待确认项；GitHub 仓库地址缺失属于本轮明确范围外。
- [x] 范围内/范围外与实现一致；历史 archive 保留旧名称，运行时与用户包统一新名称。
- [x] 本轮发现的可执行问题已回写并完成。

## 简洁性

- [x] 没有未请求的扩展；未创建 GitHub 仓库或 remote。
- [x] 当前方案保持最小可行：rename、兼容清理、验证。

## 变更边界

- [x] 改动可追溯到三个 rename 任务。
- [x] 没有无关重构。

## 功能完整性

- [x] 新 skill 名称在目录、frontmatter、metadata、脚本和用户文档中一致。
- [x] 旧安装目录清理兼容已处理。
- [x] 历史 spec archive 未被改写。

## 测试与验证

- [x] quick validator、项目 validator、6 个单测、py_compile 和 git diff check 通过。
- [x] 新旧安装目录 smoke 和公开归档白名单检查通过。

## 文档同步

- [x] README、DEVELOPMENT、NOTICE、CONTRIBUTING、Agent 和 release 文档已同步新名称。
- [x] spec 三文件已同步。

## 部署验证（如适用）

- [x] 临时 Codex/Claude 目录安装通过。
- [x] `academic-phrasebank-skill-bc9807a-dirty` tar/zip、manifest 和 checksum 生成并验证通过。

## 边界回归

- [x] 越界负样本：归档不含旧运行时目录名和开发目录。
- [x] 顺序交换负样本：rename 不改变参考语料和用户功能链路。
- [x] 旁路负样本：release builder 仍强制跑 validators、tests 和 install smoke。

## 验收证据

- 裁决性检查：`python3 tools/build_release.py` @ 2026-10-02。
- 证据锚点：HEAD `bc9807a` @ 2026-10-02T20:45:00+08:00
- 脚本验证：quick validator、项目 validator、py_compile、git diff --check 全部通过。
- 差异边界：新运行时名为 `academic-phrasebank-skill`；旧名只存在于 installer legacy cleanup 和历史 archive。
- 行为成效：安装生成新目录并清理 `academic-phrasebank-assistant` 与 `sci-academic-writing`。
- 构建：新名 tar/zip checksum 和公开文件白名单通过。
- 测试：`python3 -m unittest discover -s tests -v`，6 个测试通过。
- 手工验证：临时安装目录与归档路径检查通过。

---

**验收结果**：通过
