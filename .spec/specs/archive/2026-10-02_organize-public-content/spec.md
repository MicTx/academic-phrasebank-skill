# Organize public source content and repository documentation - 项目范围

## 1. 问题定义

- **项目目标**：清理上游页面中的非核心销售/推广内容，保持学术参考材料，并在 README 中清楚记录参考网站来源。
- **目标用户**：使用公开技能包的用户和维护源码的贡献者。
- **核心价值**：公开包只保留学术编辑能力与来源说明，不暴露上游页面的营销入口。

## 2. 假设与待确认

### 2.1 已确认事实

- 非核心内容出现在上游 HTML raw 快照的侧栏、`source-coverage.md` 的 excluded 列表和 `manifest.json` 的 excluded 列表。
- 学术正文中出现的普通 `book` 用法属于语言参考内容，不应按营销内容删除。
- README 已有 Manchester Academic Phrasebank 来源说明，应继续保留并明确参考网站地址。

### 2.2 关键假设

- 本轮删除范围仅是上游销售/推广区块和对应营销页记录。
- builder 与 raw snapshot 清洗使用同一组明确 marker；网络重建失败时保留旧数据并允许用已保存 raw 快照完成确定性清洗。

### 2.3 待确认问题

- 无。

### 2.4 可选解释与取舍

- commit 和公开 Git 记录使用中性的 public content cleanup 表述，不把具体删改对象写入提交标题或正文。
- 不删除普通学术语言中的 `book` 例句，不改变参考内容的学术功能。

## 3. 功能范围

### 3.1 核心功能（MVP）

- [x] builder 过滤营销页面记录，并清洗 raw 快照中的销售/推广区块。
- [x] manifest/source coverage 不再列出营销页。
- [x] README 保留并明确 Manchester Academic Phrasebank 参考网站来源。
- [x] validator、测试和 release 继续通过。

### 3.2 扩展功能

- 无。

### 3.3 不在范围内

- 不删除普通学术参考中的 `book` 语言例句。
- 不改变 Phrasebank 学术短语组、skill 路由和安装名称。
- 不修改历史 `.spec` 归档内容。

## 4. 最小实现路径

- 增加 suppressed marketing slug 与 raw marker 清洗规则。
- 对现有 raw 快照执行同一规则，更新 coverage/manifest。
- 补充回归测试，运行 validators、release 和公开包白名单检查。

## 5. 技术决策

- 技术栈：Python 标准库、Markdown、Git；适用外：无。
- 本轮允许改动：builder、validator、generated raw/manifest/coverage、README、tests 和本 spec。
- 本轮不应触碰：运行时 skill 路由、历史 archive、remote 配置和 GitHub 仓库。
- Git integration branch：`spec/2026-10-02_organize-public-content`

### 5.4 编排策略

- route: local
- 改动边界清晰，主会话直接执行、验收和归档。

## 6. 成功标准与验证方式

- raw/reference/manifest/source coverage 不含营销 markers；普通 academic `grammar book` 例句保留。
- README 包含官方参考网站链接。
- quick validator、项目 validator、7 个单测、organize `--check` 和用户 release 构建通过。

## 7. 风险与约束

- 上游网络可能超时；builder 必须保持旧产物，快照清洗仍需可重复。
- 删除范围必须由 marker 精确控制，不能用宽泛 `book` 匹配误伤学术内容。
