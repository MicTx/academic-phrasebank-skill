# Organize public source content and repository documentation - 验收清单

## 假设与范围对齐

- [x] 无阻塞性待确认项。
- [x] 范围内/范围外与实现一致：只清理非核心 source content，保留学术例句。
- [x] 本轮发现的可执行问题已回写并完成。

## 简洁性

- [x] 没有未请求的扩展或配置化。
- [x] 当前方案只增加精确 marker 清洗和必要回归测试。

## 变更边界

- [x] 改动可追溯到三个任务。
- [x] 没有无关重构或历史 archive 改动。

## 功能完整性

- [x] builder 可过滤营销页记录并清洗 raw 快照。
- [x] 普通学术 `grammar book` 例句保留。
- [x] README 保留参考网站来源。

## 测试与验证

- [x] quick validator、项目 validator、7 个单测、organize `--check` 通过。
- [x] release archive、白名单、checksum 和安装 smoke 通过。

## 文档同步

- [x] README、source coverage、manifest、DEVELOPMENT 和本 spec 已同步。
- [x] 公开提交使用中性内容整理描述。

## 部署验证（如适用）

- [x] 用户 release 构建成功。
- [x] 公开包不含 raw/data/tools/tests/evals/Agent/DEVELOPMENT。

## 边界回归

- [x] 越界负样本：普通 book 例句未被 marker 清洗误删。
- [x] 顺序交换负样本：网络重建失败时旧生成物不被半写入覆盖。
- [x] 旁路负样本：validator 直接扫描 raw markers，不能绕过清洗规则。

## 验收证据

- 裁决性检查：`python3 tools/validate_skill_package.py` @ 2026-10-02。
- 证据锚点：HEAD `b7046a1` @ 2026-10-02T21:25:00+08:00
- 脚本验证：validator、organize `--check`、git diff check 通过。
- 差异边界：营销 marker 已从 raw/coverage/manifest 移除；普通 grammar book 保留。
- 行为成效：用户 release 不包含 source raw、tools、tests、evals 或开发文档。
- 构建：`academic-phrasebank-skill-b7046a1` archive 和 SHA256SUMS 通过。
- 测试：`python3 -m unittest discover -s tests -v`，7 个测试通过。
- 手工验证：README 来源 URL 和 raw marker 扫描通过。

---

**验收结果**：通过
