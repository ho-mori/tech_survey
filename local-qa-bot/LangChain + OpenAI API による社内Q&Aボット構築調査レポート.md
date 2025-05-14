# LangChain + OpenAI API による社内Q&Aボット構築調査レポート

## 調査日

2025年5月14日（水）

## 調査目的

社内で管理されているMarkdown形式の文書を対象に、LangChainとOpenAI APIを用いて自然言語による社内Q&Aボットを構築し、社員が手軽に文書から情報を取得できる環境を整備する。

## 使用技術

- 言語：Python 3.10
- ライブラリ：
  - langchain==0.1.x
  - langchain-community
  - langchain-openai
  - faiss-cpu
  - tiktoken
  - python-dotenv
- API：OpenAI API（gpt-3.5-turbo）
- ベクトルDB：FAISS
- OS：Windows 11
- 実行環境：仮想環境（venv）

## フォルダ構成

```

local-qa-bot/
├── docs/                         # 社内Markdown文書（複数対応）
├── data/faiss\_index/            # FAISSインデックス保存先
├── .env                          # OpenAI APIキー
├── main.py                       # 実行スクリプト
├── requirements.txt              # ライブラリ定義
└── README.md                     # 説明書

````

## 実施内容

### ステップ1：フォルダと仮想環境の構築

```bash
mkdir local-qa-bot
cd local-qa-bot
python -m venv .venv
.venv\Scripts\activate
````

### ステップ2：ライブラリインストール

```bash
pip install langchain-community langchain-openai faiss-cpu tiktoken python-dotenv
```

### ステップ3：Markdown文書を配置

`docs/` フォルダに以下3ファイルを配置：

* intro.md
* policy.md
* manuals/user\_guide.md

### ステップ4：main.pyの構築

* `DirectoryLoader` で Markdown 複数読み込み
* `OpenAIEmbeddings` によるベクトル化
* `FAISS` による類似検索ベースのRetriever構築
* `ChatOpenAI` + `RetrievalQA` によるQ\&A実装
* `.invoke()` による質問応答を実施

### ステップ5：動作確認

以下の質問に対し、正確な回答を返すことを確認：

* 「社内システムの種類は？」
* 「パスワードはどれくらいで変更する？」
* 「有給の申請方法を教えて」

## 出力例（実行結果）

```
質問: 社内システムの種類は？
回答: 主な社内システムは以下の通りです：
- 勤怠管理システム
- 経費精算システム
- 顧客管理（CRM）システム
- 社内ポータルサイト

質問: パスワードはどれくらいで変更する？
回答: パスワードは原則として90日以内に定期的に変更することが推奨されています。

質問: 有給の申請方法を教えて
回答: 有給の申請方法は以下の通りです：

1. メニューから「申請」→「有給申請」を選択します。
2. 申請する日付と理由を入力します。
3. 申請する上司を選択し、「申請」ボタンを押して申請を提出します。
```

## 課題と改善点

* 毎回インデックスを再構築しているため、FAISSインデックスの保存と再利用を導入予定。
* Web UI対応（Streamlit/Flask）で非エンジニアでも使いやすくする。
* 出典文書の表示や信頼スコアなどの機能追加の検討。

## 結論

LangChain + OpenAI API + FAISS により、社内Markdown文書に基づいたQ\&Aボットが構築可能であることを確認した。ローカル環境で簡易に構築できるため、社内ナレッジ検索や教育支援用途に有効と考えられる。