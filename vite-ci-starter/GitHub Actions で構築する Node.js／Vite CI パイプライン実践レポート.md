# GitHub Actions で構築する Node.js／Vite CI パイプライン実践レポート（2025-05-19）

## 調査対象

GitHub Actions を用いた Node.js／Vite プロジェクトの CI パイプライン構築
（push 時にテスト → ビルドを自動実行し、結果を README バッジで表示）

---

## 実施内容と経緯

| 時刻帯 | イベント                        | 主なエラー                  | 対応                                                                             |
| ------ | ------------------------------- | --------------------------- | -------------------------------------------------------------------------------- |
| 午前   | `.github/workflows/ci.yml` 作成 | ―                           | checkout → setup-node → `npm ci` → test → build の流れを定義                     |
|        | `npm ci` 実行                   | lock ファイルが無い         | `npm init -y` で `package.json` 生成 → 依存追加 → `package-lock.json` をコミット |
|        | `vitest run` 実行               | テストファイルが無い        | `src/math.test.ts` を追加し最小テストを作成                                      |
|        | `vite build` 実行               | `index.html` が見つからない | Vite テンプレートを導入し、`index.html`・`vite.config.ts` を配置                 |
| 午後   | ローカル検証                    | ―                           | `npm ci` と `npm run build` が成功                                               |
|        | GitHub Actions 実行             | すべて成功                  | `build-and-test` ジョブが 11 s で完了                                            |
|        | README 更新                     | ―                           | ステータスバッジを貼り付け、緑表示を確認                                         |

---

## 得られた成果

1. **CI パイプラインが安定稼働**

   - push ごとにテスト・ビルドが自動実行
   - 成果物 `dist/` をアーティファクトとして保存

2. **README にバッジ追加**

   - 成功時は緑、失敗時は赤で自動更新

3. **最小ユニットテストを導入**

   - Vitest でベースラインを確保

---

## 主な学び

- `npm ci` を使う場合は lock ファイル (`package-lock.json`) が必須
- Vite はプロジェクトルート（または `root` 指定先）に `index.html` が無いとビルド失敗
- テストが 0 件だと Vitest は exit code 1 を返す
- GitHub Actions での失敗は、まずカレントディレクトリとコミット内容を確認する

---

## 今後の拡張案

| 目的             | 具体策                                                    |
| ---------------- | --------------------------------------------------------- |
| 多バージョン検証 | `strategy.matrix.node-version: [18, 20, 21]` を追加       |
| コード品質ゲート | ESLint／Prettier を追加し `npm run lint` を CI に組み込む |
| カバレッジ計測   | `vitest --coverage` と Codecov バッジを導入               |
| 依存更新自動化   | Dependabot または Renovate を有効化                       |
| 自動デプロイ     | Vercel／Netlify／GitHub Pages などへの CD ジョブ追加      |
