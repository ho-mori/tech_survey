# 技術調査レポート：Vite + React + Tailwind CSS 開発環境構築

## 調査日

2025 年 5 月 7 日（水）

## 調査目的

モダンなフロントエンド開発体験の評価を目的に、Vite + React + Tailwind CSS を組み合わせた開発環境を構築し、初期表示までを確認する。

## 使用技術

- Vite v6.3.5
- React + TypeScript
- Tailwind CSS v4.1.5
- Node.js v20.x（ローカル開発用）

## 実施環境

- OS：Windows 11
- ターミナル：PowerShell / CMD
- エディタ：Visual Studio Code

## 実施手順

1. プロジェクト作成と初期化

   ```bash
   mkdir vite-react-tailwind
   cd vite-react-tailwind
   npm create vite@latest
   # 選択内容：
   # Project name: .
   # Framework: React
   # Variant: TypeScript
   npm install
   ```

2. Tailwind CSS のインストール（v4 仕様に対応）

   ```bash
   npm install -D tailwindcss@latest postcss autoprefixer @tailwindcss/cli @tailwindcss/postcss
   ```

3. 手動で設定ファイル作成

   - `tailwind.config.js`

     ```js
     module.exports = {
       content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
       theme: {
         extend: {},
       },
       plugins: [],
     };
     ```

   - `postcss.config.cjs`（v4 対応のため `.cjs` 拡張子を使用）

     ```js
     module.exports = {
       plugins: {
         "@tailwindcss/postcss": {},
         autoprefixer: {},
       },
     };
     ```

4. `src/index.css` を修正し、Tailwind を読み込む

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

5. `src/App.tsx` を編集して動作確認

   ```tsx
   function App() {
     return (
       <div className="min-h-screen bg-gray-100 flex items-center justify-center">
         <div className="bg-white p-8 rounded shadow">
           <h1 className="text-2xl font-bold text-blue-600">
             Vite + React + Tailwind
           </h1>
           <p className="mt-2 text-gray-700">セットアップ完了です。</p>
         </div>
       </div>
     );
   }
   export default App;
   ```

6. 開発サーバー起動と表示確認

   ```bash
   npm run dev
   ```

   `http://localhost:5173` にて、Tailwind CSS が適用された UI が表示された。

## 成果と考察

### 良かった点

- Vite による開発体験は非常に高速かつ軽量
- Tailwind CSS v4 にも対応でき、ユーティリティベースで即反映が体験できた
- ブラウザ上での表示が即時更新され、開発効率が高いと感じた

### 苦労した点・対応策

- Tailwind v4 において `npx tailwindcss init -p` が使えず、設定ファイルを手動で作成する必要があった
- `postcss.config.js` を `.cjs` に変更しないと `module is not defined` エラーが発生
- Tailwind の PostCSS プラグインも `@tailwindcss/postcss` を明示的に指定する必要があった

## 今後の展望

- コンポーネント設計や Atomic Design との相性を検証
- フォームやバリデーション、状態管理（Recoil, Zustand）との統合を確認
- Storybook や Playwright との連携評価

## 結論

Vite + React + Tailwind CSS の組み合わせは、2025 年時点でもっとも効率的なフロントエンド開発環境の一つである。特に Vite のビルド速度と Tailwind のクラス構成によって、高速な UI 構築が可能となる。一方で Tailwind v4 の変更点により、セットアップには最新版仕様の理解が必要だった。
