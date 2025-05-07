# Cloudflare Workers によるエッジ API 構築体験 調査結果

## 1. 調査日

2025 年 5 月 1 日（木）

## 2. 調査目的

Cloudflare Workers を用いて、世界中で高速に応答可能なサーバレス API を構築・公開し、開発・デプロイの流れを体験する。

## 3. 実施環境

- OS: Windows 11
- Node.js: 20.x
- wrangler: 4.13.2
- Cloudflare アカウント: 無料プラン
- プロキシ環境: 有り（環境変数により自動検出）
- ブラウザ: Google Chrome

## 4. 手順

### 4.1. wrangler インストールと認証

```bash
npm install -g wrangler
wrangler login
```

ブラウザにて Cloudflare アカウント連携を許可し、CLI からの認証に成功。

### 4.2. プロジェクト作成

```bash
wrangler init hello-worker
```

対話形式で以下を選択：

- テンプレート: Hello World example
- 種類: Worker only
- 言語: TypeScript
- Git 管理: No
- 初期デプロイ: No

### 4.3. `src/index.ts` の編集

```ts
export default {
	async fetch(request: Request): Promise<Response> {
		return new Response('Hello from Cloudflare Worker!', {
			headers: { 'content-type': 'text/plain' },
		});
	},
};
```

### 4.4. ローカル確認

```bash
wrangler dev
```

ブラウザで http://localhost:8787 にアクセスし、レスポンス確認
→ "Hello from Cloudflare Worker!" を表示

### 4.5. 本番デプロイとサブドメイン登録

```bash
wrangler deploy
```

初回デプロイ時に `houmatsu-worker.workers.dev` を登録
デプロイ先 URL：

```
https://hello-worker.houmatsu-worker.workers.dev
```

DNS 伝播待機後、アクセス成功。

## 5. 結果と確認内容

| 項目              | 状態                         |
| :---------------- | :--------------------------- |
| Wrangler 導入     | 成功                         |
| Cloudflare 認証   | 成功                         |
| ローカル開発      | 成功（即時応答確認）         |
| 本番デプロイ      | 成功（サブドメイン登録あり） |
| 公開 URL アクセス | 成功（DNS 反映まで約 10 分） |

## 6. 所感と課題

- 初期構築からグローバル公開まで 30 分程度で完了
- サーバ不要でエッジ展開できる開発体験は非常にスムーズ
- DNS 伝播による待機が初回のみ発生する点は留意すべき
- wrangler v4 以降では `publish` ではなく `deploy` が必要
- `wrangler open` コマンドは v4 で廃止されている点に注意

## 7. 今後の検討事項

- Cloudflare Workers KV や Durable Objects を使ったステート管理の追加
- REST API エンドポイント化や JSON レスポンス対応
- CI/CD との連携（GitHub Actions での自動デプロイ）
- 独自ドメインとの紐付けによる API 提供の実用化
