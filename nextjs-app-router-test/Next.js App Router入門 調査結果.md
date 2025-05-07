# Next.js App Router 入門 調査結果

## 1. 調査日

2025 年 4 月 28 日（月）

## 2. 調査テーマ

Next.js 13 以降の新しい App Router 構成を使った基本操作体験

## 3. 実施環境

- OS: Windows 11
- ランタイム: bun v1.2.10
- Next.js: 15.3.1
- Node.js: 20.x
- プロキシ環境: あり

## 4. 実施内容

### 4.1. プロジェクト作成

- 作業ディレクトリを作成
- 以下コマンドでプロジェクト初期化
  ```bash
  bun create next-app@latest .
  ```
- 質問への回答内容
  - TypeScript: Yes
  - ESLint: Yes
  - Tailwind CSS: No
  - src/ディレクトリ: No
  - App Router: Yes
  - Turbopack: No

### 4.2. 依存パッケージインストール

- 初回`bun install`でエラー発生（Integrity check failed）
- `bun install --no-cache`に切り替えて再試行
- 正常完了

### 4.3. 開発サーバ起動

- `bun dev`でローカルサーバ起動
- `http://localhost:3000` にアクセスし、Next.js 初期画面を確認

### 4.4. /posts ページ作成

- `app/posts/page.tsx` ファイルを新規作成
- 以下機能を実装
  - メモ入力フォーム
  - Add ボタンでリストにメモ追加
  - Delete ボタンでリストからメモ削除

### 4.5. 動作確認

- ブラウザで `http://localhost:3000/posts` にアクセス
- メモ追加、メモ削除が正常に動作することを確認

## 5. 結論

- bun を使った Next.js App Router プロジェクト作成は成功した
- App Router 構成における基本的なページ追加、状態管理、簡単な動作実装ができた
- bun 環境ではキャッシュ不整合によるインストールエラーが起きやすく、`--no-cache`オプションを付けた再実行が有効であると確認できた

## 6. 今後の課題

- ページ間遷移（リンク機能）の実装体験
- LocalStorage 保存などフロントエンドの状態永続化技術体験
- SSR（Server Side Rendering）や API Route などの拡張学習
