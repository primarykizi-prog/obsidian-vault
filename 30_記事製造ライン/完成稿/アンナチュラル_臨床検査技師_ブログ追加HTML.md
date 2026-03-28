---
title: アンナチュラル臨床検査技師｜ブログHTML追加パーツ
status: 追加用
date: 2026-03-28
説明: ブログ→noteの逆導線。「本日のカンファレンス」セクションのゆめこ吹き出しの後に挿入する
---

## 挿入場所

「本日のカンファレンス」セクション → ゆめこの吹き出し（「いなくなって初めて気づかれる人…」）の **直後**、参照セクションの **直前** に以下のHTMLブロックを挿入する。

## 追加するHTMLブロック

```html
<!-- ========== note誘導 ========== -->

<!-- wp:group {"className":"is-style-big_icon_memo","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-big_icon_memo"><!-- wp:paragraph -->
<p>この記事のエッセイ版をnoteで公開しています。ブログでは「臨床検査技師の仕事」を解説しましたが、noteでは看護師26年の筆者が東海林の姿に重ねた<strong>個人的な想い</strong>を書いています。</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>▶ <a href="https://note.com/hikaru_kango26" target="_blank" rel="noopener">誰にも気づかれない仕事が、誰かの命を繋いでいる｜ひかる</a><br><small>※公開後に記事個別URLに差し替え</small></p>
<!-- /wp:paragraph --></div><!-- /wp:group -->
```

## 設計意図

- ブログは「解説・情報」、noteは「個人の想い・エッセイ」という役割分担を明示
- 読者が「この人の考えをもっと読みたい」と思ったタイミングでnoteに流す
- CTA（退職代行）の後に置くことで、収益導線を邪魔しない
- SWELLの「メモ」装飾ボックスで控えめに表示

## 導線の全体像（循環構造）

```
note記事（中盤）→ ブログ記事（詳しい解説）
                         ↓
ブログ記事（まとめ後）→ note（エッセイ版）
                         ↓
X投稿 → note記事（紹介）→ ブログ → ...
```
