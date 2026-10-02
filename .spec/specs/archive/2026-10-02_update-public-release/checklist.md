# Prepare public release documentation and user package - 验收清单

## 假设与范围对齐

- [x] 无阻塞性待确认项；GitHub remote URL 尚未提供，但已明确本轮只操作现有 `origin`，不阻塞当前 package。
- [x] 范围内/范围外与实现一致：用户包只含公开运行材料，开发材料留在源码仓库。
- [x] 本轮发现的可执行问题已回写任务包并完成，未甩给用户。

## 简洁性

- [x] 没有未请求的扩展、抽象或配置化；GitHub remote 和 CI/CD 明确留到后续。
- [x] 当前方案保持最小可行：一个 package 覆盖同一条公开发布链。

## 变更边界

- [x] 每项改动都能追溯到 `tasks.md` 中的稳定任务 ID。
- [x] 没有无关重构或顺手清理。

## 功能完整性

- [x] MVP 功能全部实现：skill 规范化、语料修复、公开文档、用户 release。
- [x] 边界条件已处理：inline HTML、hidden break、staging rollback、ZIP/TAR 0755、开发文件过滤。
- [x] 错误处理符合预期：validator、安装 smoke 和失败回滚均有证据。

## 测试与验证

- [x] 核心逻辑有测试：6 个 builder/staging 单测通过。
- [x] 关键路径已验证：live rebuild、用户归档、checksum、重复构建、安装 smoke 和旧新 skill benchmark 已完成。

## 文档同步

- [x] 受影响文档已更新：README、LICENSE、NOTICE、CHANGELOG、贡献/行为/安全/开发文档和 Agent 内部说明。
- [x] `spec.md` / `tasks.md` / `checklist.md` 已同步。

## 部署验证（如适用）

- [x] 本地安装 smoke 正常；目标目录覆盖前的失败保护测试通过。
- [x] 构建成功：用户 tar/zip release、manifest 和 SHA256SUMS 均生成并校验通过。

## 边界回归

- [x] 越界负样本：用户归档检查证明 `Agent.md`、`DEVELOPMENT.md`、tests、evals、data、tools 未混入交付。
- [x] 顺序交换负样本：任务依赖只影响执行顺序，当前验收由最终脚本/归档事实裁决；无可交换运行时步骤混入产品行为。
- [x] 旁路负样本：release builder 强制运行 quick validator、项目 validator、单测和安装 smoke；未运行验证不会写入通过状态。

## 验收证据

- 裁决性检查：`python3 tools/build_release.py` @ 2026-10-02；连续第二次构建哈希一致。
- 证据锚点：HEAD `d7e1eea` @ 2026-10-02T19:25:00+08:00
- 外部对标：spec package 当前 6/6 任务完成，之后由 `check_spec_package.py` 决定是否可 archive。
- 脚本验证：quick validator、项目 validator、py_compile、`git diff --check` 全部通过。
- 旧新对比：3 个用例 × 3 次运行；新版正式断言通过率 88.9%，旧版 69.4%。
- 差异边界：用户包 28 个文件；不含 Agent、DEVELOPMENT、tests、evals、data、tools。
- 行为成效：Phrasebank 参考文件不再生成 `B e ing` 或裸 `break`；install.sh 权限为 0755。
- 构建：tar、zip、manifest、SHA256SUMS 连续两次哈希一致；归档 integrity 通过。
- 测试：`python3 -m unittest discover -s tests -v`，6 个测试通过。
- 手工验证：tar/zip 解包、公开文件白名单和安装失败保留旧目标检查通过。

---

**验收结果**：通过
