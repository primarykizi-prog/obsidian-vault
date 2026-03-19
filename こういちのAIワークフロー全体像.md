

作成日：2026-03-19

---

## 🧠 全体の仕組み（三種の神器）

```
Googleドキュメント（音声メモ・情報の入口）
　　↓
GitHub Actions（自動で情報を収集・同期）
　　↓
Obsidian Vault（全情報が集まる第二の脳）
　　↓
Claude API（考えて・整理して・動く）
```

---

## 📱 各ツールの役割

|ツール|役割|状況|
|---|---|---|
|**Obsidian**|情報を貯める冷蔵庫|✅ 完成|
|**GitHub**|バージョン管理・変更履歴|✅ 完成（30分自動プッシュ）|
|**GitHub Actions**|自動でAIを動かすタイマー|🔜 次のステップ|
|**Claude API**|AIエンジン|🔜 APIキー取得が必要|
|**Googleドキュメント**|音声メモの入口|🔜 Keepから移行|
|**Cowork**|ObsidianへのPC直接保存|✅ 使用中|
|**claude.ai**|内容整理・戦略立案|✅ 使用中|

---

## 🔄 今のワークフロー（手動）

```
音声入力
　↓
Google Keep（メモ）
　↓
claude.aiに貼る（整理・日報化）
　↓
Coworkでobsidianに保存
```

---

## 🚀 目指すワークフロー（自動）

### STEP 1：音声メモの自動化

```
音声入力
　↓
Googleドキュメント（Keepの代わり）
　↓ ← GitHub Actionsが自動取得
Obsidianに日報として自動保存
```

### STEP 2：Gmailの自動集約

```
noteコメント・重要メール
　↓ ← GitHub Actionsが1時間ごとに取得
Obsidianの「受信トレイ」フォルダに自動保存
```

### STEP 3：ブログ・noteネタの自動収集

```
RSS・ニュース・トレンド情報
　↓ ← GitHub Actionsが毎朝取得
Obsidianの「ネタ帳」フォルダに自動保存
```

---

## 📋 次にやること（TODO）

- [ ] AnthropicのAPIキーを取得する
- [ ] Google KeepをやめてGoogleドキュメントに音声入力に切り替える
- [ ] GitHub ActionsでGoogleドキュメント→Obsidian自動同期を設定
- [ ] GitHub ActionsでGmail→Obsidian自動集約を設定

---

## 💡 重要な理解

**OpenClawは不要（今は）** OpenClawはLINEやDiscordから操作できるようにする「入口の便利化」ツール。 中身はClaude APIと同じ。情報の一元管理が整ってから入れれば十分。

**GitHub Actionsが自律化の核心** これがないとAIは「話しかけた時だけ動く」状態。 これがあると「寝ている間も自動で動く」状態になる。

**claude.aiとCoworkの使い分け**

- claude.ai → 考える・整理する・戦略を立てる
- Cowork → ObsidianにPC経由で直接保存する