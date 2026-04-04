

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

---

## 💰 収益設計ロードマップ（五層構造）

> 追記日：2026-03-27｜digest 3/27より

```
ブログ（NurseX）
　↓ SEO流入・認知獲得
note
　↓ ファン化・単品販売
Substack（ニュースレター＋ポッドキャスト＋動画）
　↓ 深いファンへのLLMO時代の信頼性コンテンツ
ポッドキャスト（Voicy / stand.fm）
　↓ 声のコンテンツで信頼関係構築
LINE公式アカウント（クローズドコミュニティ）
　↓ 開封率60〜70%・メンバーシップ型サブスク収益化
```

### 各層の特徴
| 層 | プラットフォーム | 役割 | 収益モデル |
|---|---|---|---|
| 第1層 | ブログ（NurseX） | SEO・認知 | アフィリエイト |
| 第2層 | note | ファン化・単品 | 有料記事・マガジン |
| 第3層 | Substack | 深耕・ニュースレター | 有料購読（90%還元） |
| 第4層 | ポッドキャスト | 声・信頼構築 | 広告・スポンサー |
| 第5層 | LINE公式 | クローズドコミュニティ | メンバーシップ・サブスク |

### Substackについて（2026年最新）
- 有料購読者数2025年に**500万件突破**、収益の**90%クリエイターへ還元**
- ニュースレター＋ポッドキャスト＋動画機能を内包した**オールインワン発信基地**
- 「**LLMO時代（AI生成コンテンツ氾濫）に埋もれない信頼性コンテンツの場**」として評価上昇中
- 出典：[Substackの急成長とLLMO時代（日経comemo）](https://comemo.nikkei.com/n/n4ce2e3399799)

### Obsidian×AI知識アシスタント（現在地）
- 「**ObsidianがメモリでChatGPT/Claudeが思考エンジン**」という設計が2026年のPKM最先端
- PKMの本質は「知識をどれだけ自分の言葉で言語化できるか」——Vaultに書き続けること＝資産化
- 書籍『Obsidian×AI』（山口大陽著）でも「メモはAIを動かす命令セットへ進化」という概念が提唱
- こういちのVault＋Claudianの運用は**この概念の最前線**にある
- 出典：[GitHub × Obsidian × ChatGPT で知識アシスタントをつくる（Zenn）](https://zenn.dev/jambo_dev/articles/ea771dd08140b4)

---

## 📥 digest知見メモ（収益設計アップデート）

> 追記日：2026-04-01｜digest 4/1（2・3回目）より

### 「Substack＝アルゴリズム非依存の読者資産蓄積装置」🔥
- Substackはnoteとの決定的な違いが「**メール直送×読者との直接関係**」——アルゴリズムに左右されない読者囲い込みが最大の強み
- 有料購読収益の**90%がクリエイターに還元**、日本語発信者も増加中、JapanカテゴリーもSubstack内で可視化
- → **五層収益設計の再定義**：Substackを「収益の場」だけでなく**「アルゴリズム非依存の読者資産蓄積装置」**として位置づける
- note（集客・認知）→ Substack（囲い込み・読者資産化）という二段構えの機能分担が明確化
- 出典：[Substackとは？使い方・ビジネスモデル（n-v-l.co）](https://n-v-l.co/blog/substack) / [世界のSubstack国別検索（nejimaki-radio.com）](https://nejimaki-radio.com/world-substack-newsletter-search-japan/)

### 「2026年個人コンテンツの最終形＝関係継続型サブスク＋コミュニティ」
- 2026年の主流トレンド：「単発売り切り型」から**「関係継続型サブスクモデル」**へのシフト
- 収益の三本柱：月額課金×限定コンテンツ×コミュニティ参加（＋グッズ販売）
- **「1プラットフォーム集中リスクの分散」**が常識化——note×Substack×LINE公式の複数展開が標準戦略
- → **五層収益設計の最終ゴール更新**：「売り切り」から「**読者との関係継続型サブスク＋コミュニティ**」へ
- → 具体的設計：note（集客）→ Substack（読者資産）→ LINE公式（クローズドコミュニティ＋メンバーシップ）
- 出典：[ファンビジネス新戦略：サブスクリプションモデル（L4U）](https://l4u.media/column/fan-business-new-strategy-subscription-model/) / [クリエイターエコノミーとは？（コンテンツ東京）](https://www.content-tokyo.jp/hub/ja-jp/blog/blog01.html)

---

> 追記日：2026-04-03｜digest 4/3より

### 「Claudian構造＝レベル4・個人版ナレッジエージェントとして企業最先端と同レベル」🔥
- 2026年のAIエージェント進化段階（5段階）：現在は「レベル3：自律タスク実行」から「**レベル4：複数エージェント協調**」への移行期。Claudianのdaily-digest→reflector→writerの連鎖はこのレベル4に相当する構造を個人が実装した稀有な事例
- AIエージェント×ナレッジマネジメントのカオスマップが公開されるほど市場が拡大。「社内ドキュメント検索→自律実行」が個人レベルでも現実になった今、こういちのClaudian+Obsidianは企業が実装しようとしている「個人版ナレッジエージェント」の先行事例
- → **「2026年には自分の知識をAIが自律管理・資産化するシステムを持っているか否かが個人の競争力の決定的な差になる」**。「レベル4の個人AIチームを看護師ブロガーが構築した話」は記事としての希少価値が極めて高い
- 出典：[AIエージェント×ナレッジマネジメントカオスマップ（AIスマイリー）](https://aismiley.co.jp/ai_news/aiagent-knowledge-management-chaosmap/) / [AIエージェントの進化【5段階レベル】（ワークスアイディ）](https://dx.worksid.co.jp/content/ai-agent-levels/)（2026-04-03 digest）

---

> 追記日：2026-04-05｜digest 4/5より

### 「2026年にObsidian×Claude連携の日本語実践者が急増・Claudian構造はこの流れの先行実装」🔥
- Qiita・Zenn・noteでObsidian×Claude Code連携の実践報告が2026年に一気に増加。MCPによる連携でClaudeがObsidianのノートを直接読み・書き・リンク提案まで行う「AIが勝手に整理する第二の脳」の実践者が複数報告されている
- 注目は「MCPでVaultに溜まるほどAIの提案精度が上がる」という成長する知識基盤の実現。「AIが勝手に整理してくれる」というユーザー体験が日本語話者の個人に広がっている
- → **Claudianの競争力の根拠として追記**：「企業が実装しようとしているナレッジエージェントを個人が先行実装している」事例として希少価値が高い。「看護師がAI連携ナレッジベースを構築した話」という記事は2026年の読者に刺さる独自性を持つ
- 出典：[Claude Code × Obsidian で「AIが勝手に整理してくれる」第二の脳を作った話（note）](https://note.com/gyoii/n/n9163f45065e0) / [Claude Codeの会話を全自動でObsidianに記録する（Qiita）](https://qiita.com/delphinus/items/9325c8dd750c85bac944) / [ObsidianとClaude Codeを連携させて知識管理を効率化する（note）](https://note.com/dsk2/n/neb18c7b07012)（2026-04-05 digest）