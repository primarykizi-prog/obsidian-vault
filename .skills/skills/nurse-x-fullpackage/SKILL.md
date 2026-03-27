---
name: nurse-x-fullpackage
description: >
  ナースXのカンファレンス室（WordPress看護師アフィリエイトブログ）のコンテンツ一式を、キーワード1つから自動生成するスキル。
  ブログHTML・noteエッセイ・なのバナナ画像プロンプト・画像ファイル名・NotebookLMプロンプト・メタ情報をまとめた
  Wordファイル（.docx）として出力する。
  「フルパッケージ作って」「note記事とブログ記事を作りたい」「キーワードからコンテンツを一括生成して」
  などのリクエストが来たら、必ずこのスキルを使うこと。
---

# ナースX フルパッケージ生成スキル v2.3
> 更新：2026-03-25　画像プロンプトをなのバナナ2フォーマットに変更
> 更新：2026-03-26　noteサムネイル（ヘッダー）にタイトルテキスト追加・Midjourneyパラメータ禁止を明記
> 更新：2026-03-27　Step 0追加（ひかるカンパニーblog/note CLAUDE.md方針確認を必須化）・保存先を30_記事製造ライン/フルパッケージ/に固定・【7】ドラマ考察ジャーナリング記事を章として追加

## 概要

ユーザーがキーワードを渡したら、以下のコンテンツを一括生成して .docx ファイルにまとめる。

1. **noteエッセイ**（約1500文字・見出し4か所）
2. **ブログHTML**（WordPress SWELL向け・v2骨格・balloon吹き出し・CTA・テキスト内リンク込み）
3. **なのバナナ画像プロンプト**（ブログ用7枚・note用4枚、すべて Aspect ratio 16:9）
4. **画像ファイル名＆alt属性一覧**
5. **NotebookLMプロンプト**（全体版＋処方箋見出し別）
6. **メタディスクリプション**（79文字以内）＋ **noteハッシュタグ**（5〜7個）
7. **ドラマ考察ジャーナリング記事**（ドラマ×テーマのnote投稿用完成原稿）

### 保存先（固定）

`Obsidian Vault/30_記事製造ライン/フルパッケージ/` に保存する。毎回この場所に出力すること。
ファイル名：`{キーワード}_{日付}_v1.0.docx`

---

## サイト基本設定

**サイト名**：ナースXのカンファレンス室
**URL**：https://nurse-x-sekando.com/
**テーマ**：WordPress SWELL
**ターゲット**：一般人80% / 看護師20%

### 吹き出し3キャラクター（balloonID）— 絶対に間違えない

| ID | キャラ | 役割 |
|---|---|---|
| **1** | **ひかる**（先輩） | 25年経験の看護師・先輩目線・現場の重みある一言 |
| **3** | **ナースX**（筆者） | 解説・教訓抽出・CTA誘導・各セクションの締め役 |
| **4** | **ゆめこ**（後輩） | 読者代弁・共感・「わかる！」反応・本音告白 |

balloonID="2" は存在しない。ゆめこは必ず balloonID="4" を使う。これを間違えると画像が表示されない。

### WordPress balloon HTMLフォーマット（SWELL）

吹き出しは必ず以下の形式で出力する：

  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>ひかるのセリフ（鉤括弧なし）</p>
  <!-- /wp:loos/balloon -->

  <!-- wp:loos/balloon {"balloonID":"3"} -->
  <p>ナースXのセリフ（鉤括弧なし）</p>
  <!-- /wp:loos/balloon -->

  <!-- wp:loos/balloon {"balloonID":"4"} -->
  <p>ゆめこのセリフ（鉤括弧なし）</p>
  <!-- /wp:loos/balloon -->

絶対禁止：吹き出しのセリフに「」を使わない

---

## Step 0：ひかるカンパニーの部署方針を確認する（必須）

キーワードを受け取ったら、**記事制作に入る前に**以下のファイルを必ず読む。

1. `ひかるカンパニー/blog/CLAUDE.md`（ブログ事業部の方針・ターゲット・使ってはいけないキーワード角度）
2. `ひかるカンパニー/note/CLAUDE.md`（note編集部の方針・2軸運営ルール）

読んだ上で、以下をチェックする：
- このキーワードがブログ事業部の「使ってはいけないキーワード角度」に該当しないか
- noteは2軸（ドラマ考察軸 or リアル記事軸）のどちらで書くか
- ターゲット（一般人80%/看護師20%）に合った角度になっているか

⚠️ 方針に合わない場合は、ユーザーに「blog/CLAUDE.mdの方針と合わない可能性があります」と伝えて方向性を相談する。

---

## Step 1：キーワード分析と記事設計

キーワードを受け取ったら、以下を決める。

1. **コアテーマ軸の選択**（必ず1〜2軸を明記してカルテに入れる）
   - 軸① アセスメント思考で人生設計
   - 軸② 2番手の法則で最大価値
   - 軸③ 看護師免許をお守りに自由を手に入れる
   - 軸④ INFJ的生存戦略・燃え尽きない
   - 軸⑤ 自分株式会社・経験を資産化
   - 軸⑥ 夫婦でOS統合・人生再設計

2. **CTA種別**：退職代行 ／ マッチングアプリ ／ その他
3. **検索意図**：何を知りたいユーザーが検索するか
4. **一般人への感情フック**：「看護師」限定にせず「頑張っているすべての人」に届く角度を先に考える
5. **タイトル案3つ**：感情に響く・SEO的に強い・クリックされやすいものを提案

ユーザーにタイトルを選んでもらうか、最適なものを1つ推薦して進める。

---

## Step 2：noteエッセイ生成（約1500文字）

### 文体・トーン

ひかる（先輩看護師）の一人称エッセイ。「説明」ではなく「感情の告白」として書く。

書き出しの鉄則：状況説明から入らない。感情の核心から始める。
- 悪い例：4月のシフト明け、眠い目をこすりながら映画館に飛び込んだ。（状況説明）
- 良い例：「泣けなかった」映画館の帰り道、私は自分の心が死んだのだと思った。（感情の告白）

必ず使うテクニック：
- 「〜はありませんか？」「〜だと思いませんか？」という読者への問いかけ
- 「マジで」「ボロボロ」「腐りながら」など口語・俗語を適所に入れる
- 体言止めと長文を交互に使い、リズムを作る
- 核心となる一文を**太字**で強調する

### 構成（見出し4か所・宣言型）

見出しは宣言型にする。説明的な見出しは避け、短く・強く・感情を持たせる。
- 弱い例：映画で感動できなかった体験について
- 強い例：意味のない日なんて、マジでない。

  ## [導入見出し]  ← 感情的・エンタメと現実の接点（200〜300文字）
  ## [体験談見出し]  ← 具体的・泥臭い体験（300〜400文字）
  ## [考察見出し]  ← 現実と深くつながる洞察・コアテーマ軸を投入（300〜400文字）
  ## [出口見出し]  ← 背中を押す・押しつけない（200〜300文字）

### 末尾の必須要素

  noteでは書ききれなかった、[テーマに関連した具体的なノウハウ]は、ブログの方に詳しく置いておきました。
  [リンク：記事タイトル]
  
  ※本記事は作品を元にした独自の考察です。

noteのルール：
- 棒線（━━━）は使わない
- ハッシュタグ：末尾に5〜7個（#エッセイ #note #スキしてみて + テーマ関連2〜3個）

---

## Step 3：ブログHTML生成（WordPress SWELL・v2骨格）

### v2骨格セクション構成（この順番で組む）

  1. 冒頭フック（太字・問いかけ形式）
  2. 冒頭吹き出し ID3→ID1→アイキャッチ→ID4（感情フック）
  3. カルテ（この記事でわかること）
  4. H2：問診室「作品名が描く〇〇の現実」
  5. H2：診察室①「コアテーマ軸の視点」
  6. H2：診察室②「あなたに必要な次の一手」← ここで初めてCTA伏線
  7. H2：処方箋「気づく・動く・守る」
  8. ポイントブロック（厚労省・信頼性補強）
  9. CTA誘導ブロック
  10. H2：本日のカンファレンス（まとめ）
  11. 関連記事・参照リスト

---

### 3人会話テンプレート（セクション別）

各セクションで誰が・何回・どの順でしゃべるかを必ずこの通りに従う。

---

#### 【冒頭フック】テンプレート（ID3 → ID1 → アイキャッチ → ID4）

  <!-- wp:paragraph -->
  <p><strong>「[作品名]の[印象的なシーン or セリフ]——見ていて、胸がざわついた人はいませんか？」</strong></p>
  <!-- /wp:paragraph -->
  
  <!-- wp:paragraph -->
  <p><strong>[作品の印象的なシーン or セリフを1〜2行で描写。一般人が共感できる言葉で]</strong></p>
  <!-- /wp:paragraph -->
  
  <!-- ナースX：記事全体の案内（少し長め・2〜3文） -->
  <!-- wp:loos/balloon {"balloonID":"3"} -->
  <p>ようこそ、ナースXのカンファレンス室へ。今回は[作品名]の[キャラ名]を回診しながら、[現実テーマ]についてお話しします。</p>
  <!-- /wp:loos/balloon -->
  
  <!-- ひかる：作品と職場経験を重ねた一言 -->
  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>[ひかるの感想 — 作品と職場経験を重ねた先輩目線の一言]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- アイキャッチ画像（ひかるとゆめこの間に必ず入れる） -->
  <!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
  <figure class="wp-block-image size-large"><img src="[eyecatch_url]" alt="[alt属性]" /></figure>
  <!-- /wp:image -->
  
  <!-- ゆめこ：読者代弁・「わかる！」反応（少し長め・2〜3文） -->
  <!-- wp:loos/balloon {"className":"u-mb-ctrl u-mb-10","balloonID":"4"} -->
  <p class="u-mb-ctrl u-mb-10">[ゆめこの共感 — 読者が「わかる！」と思う言葉。テンション高め]</p>
  <!-- /wp:loos/balloon -->

---

#### 【カルテ】テンプレート

  <!-- wp:heading {"level":3,"className":"is-style-section_ttl"} -->
  <h3 class="wp-block-heading is-style-section_ttl">この記事のカルテ</h3>
  <!-- /wp:heading -->
  
  <!-- wp:list {"className":"is-style-num_circle"} -->
  <ul class="wp-block-list is-style-num_circle">
  <!-- wp:list-item --><li>[作品・キャラ紹介など実用情報]</li><!-- /wp:list-item -->
  <!-- wp:list-item --><li>[現実の職場・人間関係テーマへのリンク]</li><!-- /wp:list-item -->
  <!-- wp:list-item --><li>コアテーマ軸「[軸名]」で読み解く視点</li><!-- /wp:list-item -->
  <!-- wp:list-item --><li>[CTA前の問題提起]</li><!-- /wp:list-item -->
  <!-- wp:list-item --><li>[処方箋・行動指針の内容]</li><!-- /wp:list-item -->
  </ul>
  <!-- /wp:list -->

---

#### 【問診室】テンプレート（ID1 → ID4 → 画像 → ID3）

  <!-- wp:heading -->
  <h2 class="wp-block-heading">問診室：[作品名]が描く[テーマ]の現実</h2>
  <!-- /wp:heading -->
  
  <!-- セクション画像 -->
  <!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
  <figure class="wp-block-image size-large"><img src="[img_url]" alt="[alt]" /></figure>
  <!-- /wp:image -->
  
  <!-- 本文（1〜2段落） -->
  <!-- wp:paragraph -->
  <p>[問診室の本文 — ドラマの状況説明、現実職場との共通点を述べる]</p>
  <!-- /wp:paragraph -->
  
  <!-- ひかる：ドラマ解説・現場経験と重ねた一言 -->
  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>[ひかる — ドラマを職場経験と重ねた先輩目線のコメント]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- ゆめこ：読者代弁・共感・驚き -->
  <!-- wp:loos/balloon {"balloonID":"4"} -->
  <p>[ゆめこ — 読者代弁の共感コメント。「そうそう！」などテンション高め]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- 画像 -->
  <!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
  <figure class="wp-block-image size-large"><img src="[img_url]" alt="[alt]" /></figure>
  <!-- /wp:image -->
  
  <!-- ナースX：まとめ・現実との橋渡し（長め・className="u-mb-ctrl u-mb-10"必須） -->
  <!-- wp:loos/balloon {"className":"u-mb-ctrl u-mb-10","balloonID":"3"} -->
  <p class="u-mb-ctrl u-mb-10">[ナースX — ドラマと現実の橋渡し。次のセクションへ誘導]</p>
  <!-- /wp:loos/balloon -->

---

#### 【診察室①】テンプレート（ID1 → ID4 → 画像 → ID3）

  <!-- wp:heading -->
  <h2 class="wp-block-heading">診察室①｜[コアテーマ軸のタイトル]</h2>
  <!-- /wp:heading -->
  
  <!-- セクション画像 -->
  <!-- wp:image {"sizeSlug":"large","linkDestination":"none","className":"u-mb-ctrl u-mb-10"} -->
  <figure class="wp-block-image size-large u-mb-ctrl u-mb-10"><img src="[img_url]" alt="[alt]" /></figure>
  <!-- /wp:image -->
  
  <!-- H3症例（1〜2個） -->
  <!-- wp:heading {"level":3} -->
  <h3 class="wp-block-heading">症例1：[症例タイトル]</h3>
  <!-- /wp:heading -->
  
  <!-- 症例画像 -->
  
  <!-- ひかる：具体的な体験・ドラマ解説 -->
  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>[ひかる — 具体的なドラマの場面解説 or 職場経験談]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- ゆめこ：感情反応・読者代弁 -->
  <!-- wp:loos/balloon {"balloonID":"4"} -->
  <p>[ゆめこ — 感情的な反応・「私も同じです」という共感]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- 画像 -->
  
  <!-- ナースX：教訓・CTA伏線（className="u-mb-ctrl u-mb-10"必須） -->
  <!-- wp:loos/balloon {"className":"u-mb-ctrl u-mb-10","balloonID":"3"} -->
  <p class="u-mb-ctrl u-mb-10">[ナースX — 教訓・現実への架け橋。<a href="[退職ページ]">自然なリンクテキスト（退職視点）</a>を入れる]</p>
  <!-- /wp:loos/balloon -->

---

#### 【診察室②】テンプレート（ID1 → ID4 → 画像 → ID3 → CTA）

  <!-- wp:heading -->
  <h2 class="wp-block-heading">診察室②｜あなたに必要な「次の一手」</h2>
  <!-- /wp:heading -->
  
  <!-- セクション画像 -->
  
  <!-- ひかる：次の一手を示唆・退職リンク付き -->
  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>[ひかる — 次の一手を示唆する言葉。<a href="[退職ページ]">自然なリンクテキスト</a>を含める]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- ゆめこ：本音告白・感情吐露（最も読者に刺さるパート） -->
  <!-- wp:loos/balloon {"balloonID":"4"} -->
  <p>[ゆめこ — 本音を吐露する。「私も〜でした」「怖くて動けなくて」など]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- 画像 -->
  
  <!-- ナースX：行動促進・退職CTAへの橋渡し（className="u-mb-ctrl u-mb-10"必須） -->
  <!-- wp:loos/balloon {"className":"u-mb-ctrl u-mb-10","balloonID":"3"} -->
  <p class="u-mb-ctrl u-mb-10">[ナースX — 行動を促す。「情報を集めるだけでいい」。<a href="[退職ページ]"><strong>自然なリンクテキスト</strong></a>]</p>
  <!-- /wp:loos/balloon -->
  
  [blog_parts id="2673"]

---

#### 【処方箋】テンプレート

  <!-- wp:heading -->
  <h2 class="wp-block-heading">【本日の処方箋】[作品名]から学ぶ3つの行動指針</h2>
  <!-- /wp:heading -->
  
  <!-- 処方箋画像 -->
  
  <!-- H3 -->
  <!-- wp:heading {"level":3} -->
  <h3 class="wp-block-heading">対策：[タイトル]の3つの行動指針</h3>
  <!-- /wp:heading -->
  
  <!-- ① 気づく -->
  <!-- wp:group {"className":"","layout":{"type":"constrained"}} -->
  <div class="wp-block-group"><!-- wp:heading {"level":4} -->
  <h4 class="wp-block-heading">① 気づく — [現状を正確に認識する]</h4>
  <!-- /wp:heading -->
  <!-- wp:group {"className":"is-style-big_icon_memo","layout":{"type":"constrained"}} -->
  <div class="wp-block-group is-style-big_icon_memo"><!-- wp:paragraph -->
  <p><strong>行動</strong>：[具体的な気づきのアクション]<br><strong>結果</strong>：[気づくことで何が変わるか]</p>
  <!-- /wp:paragraph --></div><!-- /wp:group --></div><!-- /wp:group -->
  
  <!-- ② 動く -->
  <!-- wp:group {"className":"","layout":{"type":"constrained"}} -->
  <div class="wp-block-group"><!-- wp:heading {"level":4} -->
  <h4 class="wp-block-heading">② 動く — [最初の一歩を踏み出す]</h4>
  <!-- /wp:heading -->
  <!-- wp:group {"className":"is-style-big_icon_memo","layout":{"type":"constrained"}} -->
  <div class="wp-block-group is-style-big_icon_memo"><!-- wp:paragraph -->
  <p><strong>行動</strong>：[最小限の最初の行動]<br><strong>結果</strong>：[動くことで何が変わるか]</p>
  <!-- /wp:paragraph --></div><!-- /wp:group --></div><!-- /wp:group -->
  
  <!-- ③ 守る（最後にCTAリンクを自然に入れる） -->
  <!-- wp:group {"className":"","layout":{"type":"constrained"}} -->
  <div class="wp-block-group"><!-- wp:heading {"level":4} -->
  <h4 class="wp-block-heading">③ 守る — [自分・大切なものを守る]</h4>
  <!-- /wp:heading -->
  <!-- wp:group {"className":"is-style-big_icon_memo","layout":{"type":"constrained"}} -->
  <div class="wp-block-group is-style-big_icon_memo"><!-- wp:paragraph -->
  <p><strong>行動</strong>：[再発防止・自己防衛のアクション]<br><strong>結果</strong>：[守ることで手に入る未来。<a href="[退職ページ]"><strong>CTAリンク</strong></a>]</p>
  <!-- /wp:paragraph --></div><!-- /wp:group --></div><!-- /wp:group -->
  
  <!-- ワンポイントメモ -->
  <!-- wp:group {"className":"is-style-big_icon_point","layout":{"type":"constrained"}} -->
  <div class="wp-block-group is-style-big_icon_point"><!-- wp:paragraph -->
  <p>💡 ナースXのワンポイント・メモ</p>
  <!-- /wp:paragraph -->
  <!-- wp:paragraph -->
  <p>[厚労省・公的機関データを引用・1〜2文]</p>
  <!-- /wp:paragraph --></div><!-- /wp:group -->
  
  <!-- 参考リンク -->
  <!-- wp:paragraph {"className":"u-mb-ctrl u-mb-10"} -->
  <p class="u-mb-ctrl u-mb-10">参考：<a href="https://www.mhlw.go.jp/...">医療機能評価機構「[タイトル]」</a></p>
  <!-- /wp:paragraph -->
  
  <!-- ひかる：共感・限界サインへの言及 -->
  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>[ひかる — 読者への共感。「今の職場が笑えないなら、それはあなたのせいじゃない」など]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- ゆめこ：本音の疲れ告白（最もリアルな読者代弁） -->
  <!-- wp:loos/balloon {"className":"u-mb-ctrl u-mb-10","balloonID":"4"} -->
  <p class="u-mb-ctrl u-mb-10">[ゆめこ — 限界の本音。「毎日ピリピリしてて、本音が言えなくて」など]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- 画像 -->
  
  <!-- ひかる：CTA誘導の一言（リンク付き） -->
  <!-- wp:loos/balloon {"className":"u-mb-ctrl u-mb-10","balloonID":"1"} -->
  <p class="u-mb-ctrl u-mb-10">[ひかる — CTA前の最後の一押し。<a href="[退職ページ]">環境を変える勇気</a>を持っていいんだよ、のような流れ]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- H3 退職CTAブロック -->
  <!-- wp:heading {"level":3} -->
  <h3 class="wp-block-heading">職場が辛い、でも「辞める」と言い出せないあなたへ</h3>
  <!-- /wp:heading -->
  
  <!-- is-style-big_icon_good ブロック -->
  <!-- wp:group {"className":"is-style-big_icon_good","layout":{"type":"constrained"}} -->
  <div class="wp-block-group is-style-big_icon_good"><!-- wp:paragraph -->
  <p>[退職・転職への背中を押す文章。「毎朝、仕事に行くのが怖い」から始め、<a href="[退職ページ]"><strong>上司に一切会わずに退職できる方法</strong></a>があります、で締める]</p>
  <!-- /wp:paragraph --></div><!-- /wp:group -->
  
  <!-- ひかる：締め（短い一言） -->
  <!-- wp:loos/balloon {"balloonID":"1"} -->
  <p>[ひかる — 短い締めの言葉。「失敗してもカバーし合える、温かい仲間がいる場所で働いてほしいな」など]</p>
  <!-- /wp:loos/balloon -->
  
  [blog_parts id="2673"]

---

#### 【本日のカンファレンス】テンプレート（ID3（長め） → ID4（読者への問いかけ））

  <!-- wp:heading -->
  <h2 class="wp-block-heading">本日のカンファレンス</h2>
  <!-- /wp:heading -->
  
  <!-- セクション画像 -->
  
  <!-- ナースX：総括（長め・3〜4文・CTA誘導リンク付き） -->
  <!-- wp:loos/balloon {"balloonID":"3"} -->
  <p>[ナースX — 記事全体の総括。コアテーマ軸の結論を述べ、<a href="[退職ページ]"><strong>情報を集めることは逃げではなく次のステージへの準備</strong></a>で締める]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- ゆめこ：読者への問いかけ（エンゲージメント促進・直通ポストへ誘導） -->
  <!-- wp:loos/balloon {"balloonID":"4"} -->
  <p>[ゆめこ — 読者への問いかけ。「みなさんの職場に〜みたいな人いますか？」など。下の直通ポストへの誘導]</p>
  <!-- /wp:loos/balloon -->
  
  <!-- shortcodes / 参考資料リスト -->

---

### アフィリエイトCTA

- **退職代行**：[blog_parts id="2673"]（記事内最大3か所）
- 配置の原則：診察室②の直後・処方箋後の2か所が基本
- CTAブロックを連続配置しない。間に必ずブリッジ文を入れる

### テキスト内リンク配置ルール（80:20 = 退職重視）

**⚠️ 絶対ルール：退職リンク×3、転職リンク×1（最大）。転職リンクを増やさないこと。**

省略不可。HTMLに4か所埋め込む。配置は以下の通り固定：

| 配置箇所 | リンク種別 | テンプレート |
|----------|-----------|------------|
| 問診室・ナースX締め | **退職** | `<a href="https://nurse-x-sekando.com/%e3%80%90%e9%99%90%e7%95%8c%e3%83%8a%e3%83%bc%e3%82%b9%e3%81%b8%e3%80%91%e5%b8%ab%e9%95%b7%e3%81%a8%e9%a1%94%e3%82%92%e5%90%88%e3%82%8f%e3%81%9b%e3%81%9a%e3%81%ab%e5%8d%b3%e6%97%a5%e9%80%80%e8%81%b7/" target="_blank" rel="noopener">[退職視点のアンカーテキスト]</a>` |
| 診察室①・ナースX締め | **退職**（転職は使わない） | `<a href="https://nurse-x-sekando.com/%e3%80%90%e9%99%90%e7%95%8c%e3%83%8a%e3%83%bc%e3%82%b9%e3%81%b8%e3%80%91%e5%b8%ab%e9%95%b7%e3%81%a8%e9%a1%94%e3%82%92%e5%90%88%e3%82%8f%e3%81%9b%e3%81%9a%e3%81%ab%e5%8d%b3%e6%97%a5%e9%80%80%e8%81%b7/" target="_blank" rel="noopener">[退職視点のアンカーテキスト]</a>` |
| 診察室②・ひかる or ナースX | **退職** | `<a href="https://nurse-x-sekando.com/%e3%80%90%e9%99%90%e7%95%8c%e3%83%8a%e3%83%bc%e3%82%b9%e3%81%b8%e3%80%91%e5%b8%ab%e9%95%b7%e3%81%a8%e9%a1%94%e3%82%92%e5%90%88%e3%82%8f%e3%81%9b%e3%81%9a%e3%81%ab%e5%8d%b3%e6%97%a5%e9%80%80%e8%81%b7/" target="_blank" rel="noopener">[退職視点のアンカーテキスト]</a>` |
| 処方箋③「守る」 or カンファレンス | **退職** | `<a href="https://nurse-x-sekando.com/%e3%80%90%e9%99%90%e7%95%8c%e3%83%8a%e3%83%bc%e3%82%b9%e3%81%b8%e3%80%91%e5%b8%ab%e9%95%b7%e3%81%a8%e9%a1%94%e3%82%92%e5%90%88%e3%82%8f%e3%81%9b%e3%81%9a%e3%81%ab%e5%8d%b3%e6%97%a5%e9%80%80%e8%81%b7/" target="_blank" rel="noopener">[退職視点のアンカーテキスト]</a>` |

**転職キラーページ（使用は全記事通じて1か所のみ）：**
`<a href="https://nurse-x-sekando.com/%e3%80%90%e9%99%90%e7%95%8c%e3%83%8a%e3%83%bc%e3%82%b9%e3%81%b8%e3%80%91%e3%80%8c%e4%bb%8a%e3%81%99%e3%81%90%e8%bb%a2%e8%81%b7%e3%80%8d%e3%81%98%e3%82%83%e3%81%aa%e3%81%8f%e3%81%a6%e3%81%84%e3%81%84/" target="_blank" rel="noopener">[転職視点のアンカーテキスト]</a>`
→ 使う場合でも診察室①の1か所のみ。省略して退職リンクにしてもよい。

アンカーテキストは「こちら」を使わず、自然な文脈の一部にする。

### 記事末尾の参照セクション（必須）

  <p style="color:#888; font-size:0.83em;">参照：<a href="[作品公式URL]" target="_blank" rel="noopener">『[作品名]』公式サイト</a>（[著者名]／[放送局]）／ <a href="https://kokoro.mhlw.go.jp/nowhow/vol01/" target="_blank" rel="noopener">厚生労働省「こころの耳」</a> 等を参考に、看護師として25年以上の現場経験を持つ筆者が独自に構成・執筆しています。作品の設定を借りた筆者独自の考察と創作を含む記事です。</p>

主な作品の公式URL（不明な場合はWebで検索して確認）：
- アンナチュラル：TBSドラマ公式ページを検索
- コードブルー：https://www.fujitv.co.jp/codeblue/
- ドクターX：https://www.tv-asahi.co.jp/doctor-x/
- 鬼滅の刃：https://kimetsu.com/
- 進撃の巨人：https://shingeki.tv/

### NG事項

- 吹き出しセリフに「」を使わない（絶対禁止）
- blockquote タグは使わない（p タグで代替）
- CTAを連続配置しない
- 「看護師向け」の言葉を前面に出しすぎない（一般人が離脱する）
- **balloonID="2" を絶対に使わない**（ゆめこは必ず="4"）

---

## Step 4：なのバナナ画像プロンプト生成

すべてのプロンプトは **なのバナナ2フォーマット**・Aspect ratio 16:9 で統一する。

⚠️ **Midjourney・Nijijourneyのパラメータ（--niji、--ar、--v等）は絶対に使わない。**

基本フォーマット：
  A cinematic and emotional anime style illustration of [具体的なシーン描写・感情・雰囲気]. Masterpiece, highly detailed, cel-shaded, soft rim lighting, vibrant colors. Aspect ratio 16:9

### ブログ用（7枚）
1. アイキャッチ画像（最もインパクトのあるシーン）
2. 問診室（読者の共感）
3. 診察室①（転換点・気づき）
4. 診察室②（問題の本質・橋渡し）
5. 処方箋（行動・決断）
6. CTA周辺（新しい一歩・選択）
7. まとめ（希望・前向き）

### note用（4枚）— ブログ用とスタイルが異なる

**⚠️ ブログ用とnote用は画像スタイルが完全に別。混同しないこと。**

#### note_01：ヘッダー（サムネイル）— 1枚絵＋タイトルテキスト
- ブログ用と同じ「A cinematic and emotional anime style illustration」の**1枚絵**
- 漫画風パネルにしない。サムネイルらしいシンプルな構図
- 末尾に `Large bold Japanese text "[記事タイトルの短縮版]" displayed prominently in the lower half of the image in white font with subtle shadow outline, easily readable` を追加
- 参考：暗めの背景＋キャラクター＋大きな白文字タイトルが映えるスタイル

#### note_02〜04：本文中画像 — 漫画風4コマパネル＋日本語字幕
- 「A dramatic manga-style 4-panel comic layout」で始める
- 各パネルに Japanese text "〇〇" で日本語の字幕・セリフを指定
- 最終パネルに記事の核心メッセージを大きなテキストで配置
- ダークネイビー基調、マンガインクスタイル、ハイコントラスト

構成：
1. ヘッダー画像（サムネイル）← **1枚絵＋タイトルテキスト**
2. 見出し1〜2のイメージ（体験談）← **漫画風4コマ＋字幕**
3. 見出し3〜4のイメージ（内省・変化）← **漫画風4コマ＋字幕**
4. 末尾画像（余韻・希望）← **漫画風4コマ＋字幕**

---

## Step 5：画像ファイル名＆alt属性

命名規則：キーワード（ハイフン区切り英語）_番号.jpg

| No. | ファイル名 | alt属性（日本語・30文字以内） |
|-----|-----------|---------------------------|
| 01  | ...       | ...                       |

---

## Step 6：NotebookLMプロンプト

デザイン設定（全スライド共通）：

  【全体デザイン設定】
  トーン：ドラマチック・日本漫画・アクション・物語
  背景：白黒の漫画原稿スタイル（スクリーントーン・集中線・効果音を使用）
  文字色：黒（アクセントにのみ赤を使用・多用しない）
  画像スタイル：スクリーントーン・集中線・効果音・コマ割りレイアウト・吹き出し・インク・点描
  タイポグラフィ：アンティーク調（見出しは明朝+ゴシック）
  実写写真・アニメ風カラーイラストは使わない。白黒漫画のコマとして描くこと。

全体版プロンプト：

  テーマ：[キーワード] × [コアテーマ軸]
  対象：頑張っているすべての人（一般人80%・看護師20%）
  スライド数：10〜12枚
  構成：以下の4つの見出しをスライドのタイトルとして使用
  [見出し1〜4]
  【全体デザイン設定】（上記参照）

---

## Step 7：Wordファイル（.docx）に出力

ファイル保存先（固定）：`Obsidian Vault/30_記事製造ライン/フルパッケージ/`
ファイル名：`{キーワード}_{YYYY-MM-DD}_v1.0.docx`

章構成：
  【1】noteエッセイ（見出し4か所付き・約1500文字）
  【2】なのバナナ画像プロンプト（ブログ用7枚）— 1枚絵アニメスタイル・字幕なし
  【2-2】なのバナナ画像プロンプト（note用4枚）— サムネ=1枚絵+テキスト、02〜04=漫画風4コマ+字幕
  【3】画像ファイル名＆alt属性
  【4】NotebookLMプロンプト（全体版）
  【4-2】NotebookLMプロンプト（見出し別）
  【5】ブログHTML下書き
  【6】メタディスクリプション＋noteハッシュタグ
  【7】ドラマ考察ジャーナリング記事（note投稿用完成原稿）

python-docx（python3）を使ってスクリプトを書き、実行する。npmのdocxライブラリはネットワーク制限で使用不可。
出力後は必ず present_files ツールで表示してユーザーが直接開けるようにする。

---

## Step 6.5：AI臭さ除去（noteエッセイ＋ブログHTML両方に適用）

Step 2（noteエッセイ）とStep 3（ブログHTML）で生成した文章に対し、
以下の2ステップを内部で自動実行する。ユーザーに追加操作は求めない。

### ステップA：チェック（リストアップのみ・書き直さない）

生成した記事を読み、以下の観点で「AIが書いたとわかる不自然な表現」を洗い出す。

**チェック対象：**
- 「〜することが重要です」「〜と言えるでしょう」などの締め常套句
- 「まず〜。次に〜。最後に〜。」という単調な列挙パターン
- 「非常に」「とても」「大変」などの曖昧な強調副詞
- 「〜だけでなく〜でもある」というAI特有の接続構文
- 同じ語尾・文末表現の連続（です/ます/でしょう の繰り返し）
- 見出しと本文の内容のズレ
- 根拠が示されていない主張
- 冗長な言い換え・不要なまとめ表現

各項目について「問題のある表現」「なぜ不自然か」「修正案」を内部的にリスト化する。

### ステップB：改善（リストの箇所だけ修正）

ステップAで洗い出した箇所だけを修正する。
それ以外の文章・構成・語順・文体・HTML構造は一切変えない。

**絶対に変えてはいけないもの：**
- 見出しの構成と順番
- ステップAのリストに含まれていない文章
- balloonID・className等のHTML属性
- 吹き出しの登場順（ID3→ID1→ID4等）
- CTA配置・リンクURL
- v2骨格のセクション構成

### トーンスライダー自動適用

**noteエッセイ用（体験談ベース共感型）：**

| スライダー | 設定値 | 意味 |
|---|---|---|
| 感情 ↔ 論理 | -5 | 体験・感情やや重視 |
| カジュアル ↔ フォーマル | -6 | くだけた話し言葉 |
| 謙虚 ↔ 自信 | -4 | 断言より「〜だった」「〜と思う」 |
| 短文 ↔ 長文 | -4 | 改行多め、テンポよく |
| 抑制 ↔ 熱量 | +3 | 少しだけ熱がある |

**ブログHTML用（実用的ハウツー寄り・ただし感情フックあり）：**

| スライダー | 設定値 | 意味 |
|---|---|---|
| 感情 ↔ 論理 | -2 | やや感情寄り（ドラマ×看護の文脈） |
| カジュアル ↔ フォーマル | -3 | 吹き出しは口語、本文はやや丁寧 |
| 謙虚 ↔ 自信 | +2 | 先輩看護師としての確信を持った語り |
| 短文 ↔ 長文 | +1 | 吹き出しは短め、本文はやや丁寧に |
| 抑制 ↔ 熱量 | +2 | 適度な熱量（押しつけない） |

**注意：**
- スライダーは文体の「傾向」であり、全文を均一にしない
- 強調したい箇所では意図的にスライダー値から外れた表現を使う
- 吹き出しキャラごとの口調（ひかる＝先輩、ゆめこ＝テンション高め、ナースX＝解説者）は維持する

---

## 出力前の最終チェックリスト

**AI臭さ除去チェック**
- [ ] ステップA（チェック）→ステップB（改善）をnoteエッセイに実行済みか
- [ ] ステップA（チェック）→ステップB（改善）をブログHTMLに実行済みか
- [ ] noteエッセイにトーンスライダー（共感型）を適用済みか
- [ ] ブログHTMLにトーンスライダー（ハウツー型）を適用済みか
- [ ] 改善後にv2骨格の構成・吹き出し順が崩れていないか

**構成・フォーマットチェック**
- [ ] noteエッセイが「感情の告白」スタイルで始まっている
- [ ] noteエッセイの見出しが宣言型になっている
- [ ] 吹き出しがすべて balloonID="1"、"3"、"4" のみ（"2"は使っていない）
- [ ] 吹き出しセリフに「」が含まれていない
- [ ] 冒頭の吹き出し順が ID3→ID1→アイキャッチ→ID4 になっている
- [ ] 各セクションで「ID1→ID4→画像→ID3」の会話パターンが守られている
- [ ] 問診室・診察室・処方箋のID3吹き出しに className="u-mb-ctrl u-mb-10" が付いている
- [ ] カルテにコアテーマ軸が明記されている
- [ ] v2骨格の順番通り（問診室→診察室①→診察室②→処方箋→CTA）
- [ ] 処方箋が「気づく・動く・守る」の3軸になってい