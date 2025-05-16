# Tailwind CSS 導入調査レポート

**日付：2025 年 5 月 16 日**

---

## 調査目的

Vite + React プロジェクトに Tailwind CSS を導入し、ログイン UI を構築するために、Windows + nvm 環境で Tailwind CLI を正常に動作させることを目的とした。

---

## 実施環境

- OS：Windows 10（64bit）
- Node.js：

  - v22.14.0（Store 版、後に削除）
  - v20.12.2（nvm 経由で切り替え）

- npm：10.5.0
- nvm：使用
- プロジェクトツール：Vite + React + Tailwind CSS
- パス：`D:\tech_survey\vite-react-tailwind-login`

---

## 問題点と対応経緯

### 1. `tailwindcss` CLI がインストールされない

- `npm install -D tailwindcss postcss autoprefixer` を何度実行しても、`.bin/tailwindcss` が生成されず
- `npx tailwindcss init -p` 実行時に `could not determine executable` エラーが発生

#### 原因：

- `tailwindcss` パッケージが壊れた CSS 用の別物（CLI なし）だった可能性が高い
- `npm install` が意図しないパッケージを解決していた

---

### 2. Node.js のバージョンと `nvm` の競合

- `nvm use` を実行しても、`node -v` が `v22` のまま
- 実は Microsoft Store 版 Node.js が環境変数上で優先されていた

#### 対応：

- Store 版 Node.js をアンインストールし、nvm での `v20.12.2` に統一
- `where node` で確認し、`C:\Program Files\nodejs` を無効化

---

### 3. 正しい Tailwind CLI のインストール方法

以下の方法で、CLI 付きの安定バージョンを明示的に指定：

```bash
npm install -D tailwindcss@3.4.1 postcss autoprefixer
```

- `.bin/tailwindcss` が生成されたことを確認
- `npx tailwindcss init -p` 成功

---

## 成果

- Tailwind CSS CLI を正しくインストール・初期化完了
- `tailwind.config.js` と `postcss.config.js` が自動生成された
- ログイン UI の画面実装も成功し、レスポンシブ対応の動作を確認済み

---

## 今後の課題

- Tailwind のバージョンを上げる際は `cli.js` の有無を確認する必要がある
- Windows + nvm 環境では、Store 版 Node.js の干渉に注意
- 公式 CLI の `exports` 対応が進むまでは、安定バージョンの指定を推奨

---

## 備考

- 今後、Supabase との認証連携やバリデーション実装、React Router を含めた SPA 化も検討可能
