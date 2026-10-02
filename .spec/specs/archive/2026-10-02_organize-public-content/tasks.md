# Organize public source content and repository documentation - 任务拆解

## 阶段一：边界审计

- [x] 定义学术正文与非核心 source content 的边界
  - id: task-content-boundary
  - boundary: 只更新本 spec；不改变 skill 路由或历史 archive
  - verify: spec 明确 marker 规则、普通 book 例句保留和不在范围内内容

## 阶段二：内容清洗

- [x] 清洗 builder、raw snapshot、manifest 和 source coverage
  - id: task-content-cleanup
  - depends-on: task-content-boundary
  - boundary: 只改 `tools/build_phrasebank_refs.py`、`tools/validate_skill_package.py`、generated raw/manifest/coverage 和测试
  - verify: raw/coverage/manifest 无营销 markers；`grammar book` fixture 保留；validator 和 7 个单测通过

- [x] 同步 README 参考网站来源说明
  - id: task-source-doc
  - depends-on: task-content-boundary
  - boundary: 只改 README 和本 spec 记录；保留官方 Manchester Academic Phrasebank URL
  - verify: README 来源段包含官方参考网站地址，Markdown 路径有效

## 阶段三：验收与交付

- [x] 运行结构、测试、release 和 spec 验收
  - id: task-content-acceptance
  - depends-on: task-content-cleanup, task-source-doc
  - boundary: 只更新 checklist、spec archive 和 release 产物
  - verify: organize `--check`、两个 validator、7 个单测、git diff check、release 白名单和 checksum 全部通过

---

**当前进度**：由脚本计算，无需手动维护
