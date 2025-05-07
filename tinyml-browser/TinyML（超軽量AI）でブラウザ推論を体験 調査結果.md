# TinyML（超軽量 AI）でブラウザ推論を体験 調査結果

## 1. 調査日

2025 年 5 月 2 日（金）

## 2. 調査目的

TensorFlow.js を利用し、軽量な画像分類モデル（MobileNet）を Web ブラウザ上で動作させることで、サーバレスな AI 推論の可能性と開発体験を検証する。

## 3. 実施環境

- OS: Windows 11
- ブラウザ: Google Chrome
- Node.js: v20.x
- Web サーバ: http-server（npx 経由で使用）
- ライブラリ: TensorFlow.js（CDN）
- ネットワーク: プロキシあり（影響なし）

## 4. 実施手順

### 4.1. 開発セットアップ

```bash
mkdir tinyml-browser
cd tinyml-browser
npm init -y
npm install @tensorflow/tfjs
```

### 4.2. HTML 構成（index.html）

```html
<video id="video" width="224" height="224" autoplay></video>
<p id="result">分類中...</p>
```

### 4.3. 推論コード（main.js）

```js
const model = await tf.loadGraphModel(
  "https://storage.googleapis.com/tfjs-models/savedmodel/mobilenet_v2_1.0_224/model.json"
);
```

- カメラ映像を取得
- MobileNet モデルで 2 秒ごとに分類
- 結果をクラス ID として画面に表示

### 4.4. ローカル実行

```bash
npx http-server .
```

ブラウザで `http://127.0.0.1:8080` にアクセス

---

## 5. 結果

- カメラ映像がリアルタイムで表示された
- 推論結果（例：クラス ID: 795）が定期的に更新された
- 初期は CORS エラーが発生したが、モデル URL の修正により解消
- キャッシュの影響で古い JS が実行されていたが、強制リロードで解決

---

## 6. 所感

- TensorFlow\.js により、ブラウザだけで AI 推論が成立することを実感
- 通信せずリアルタイム処理できるため、エッジ用途への応用が期待できる
- モデル読み込みの CORS やキャッシュ問題に対して注意が必要
- カメラ連携やモデル応答速度も十分なレベル

---

## 7. 今後の検討事項

| 検討内容                                       | 優先度 |
| :--------------------------------------------- | :----- |
| ImageNet のクラス ID にラベル名を表示する機能  | 中     |
| ONNX.js など他の軽量推論ライブラリとの比較検証 | 高     |
| 手書き分類（MNIST）や音声認識への応用          | 高     |
| 推論結果の音声出力（Text-to-Speech）           | 中     |
| モデルサイズの圧縮や量子化モデルの導入         | 中     |
