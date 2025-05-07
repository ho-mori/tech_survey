# LangChain + ChatGPT API による Q&A ボット構築

## 調査日

2025 年 5 月 6 日（火）

## 調査目的

手元の社内ドキュメント（Markdown 形式）を読み込み、ChatGPT と LangChain を使って自然言語で質問できる検索拡張型 Q&A ボット（RAG）を構築する。

## 使用技術

- Python 3.10
- LangChain v0.1.x
- OpenAI API（gpt-3.5-turbo）
- FAISS（ベクトル検索エンジン）
- TextLoader（langchain_community）
- `.env` による API キー管理

## 実施環境

- OS：Windows 11
- エディタ：VS Code
- 仮想環境：venv
- モデル：gpt-3.5-turbo（ChatOpenAI）

## 実施手順

1. プロジェクト作成と仮想環境構築

   ```bash
   mkdir langchain-rag-demo
   cd langchain-rag-demo
   python -m venv .venv
   ```

2. 必要パッケージのインストール

   ```bash
   pip install langchain langchain-openai langchain-community faiss-cpu python-dotenv
   ```

3. `.env` ファイルに OpenAI API キーを記述

   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

4. Markdown ファイル `doc.md` を作成

   ```md
   ## 勤怠申請

   - 勤怠は毎月 25 日締め。
   ```

5. Python スクリプト `qa_bot.py` を作成し、以下を実装

   - 文書を読み込み
   - 分割してベクトル化
   - ベクトル検索で取得し、ChatGPT と連携して回答を生成

6. 実行コマンド

   ```bash
   python qa_bot.py
   ```

7. 実行結果

   ```
   質問を入力してください：勤怠の締日は？
   回答： 勤怠の締め日は毎月25日です。
   ```

## 成果と考察

### 良かった点

- 自前の Markdown 文書から正確に情報を検索・回答できた
- LangChain を使って、短時間で RAG 構成の Q\&A ボットを実現できた
- OpenAI の埋め込み＋ FAISS で検索精度が高かった

### 改善点・注意点

- `run()` は非推奨となっており、将来的には `invoke()` への置き換えが必要
- ドキュメントのエンコーディングによっては `UnicodeDecodeError` が発生するため、`encoding="utf-8"` の明示が必要だった
- 複数ファイル対応や PDF 対応は現時点では未実装（今後の拡張候補）

## 今後の展望

- DirectoryLoader を使った複数ファイル対応
- PDF や HTML など、他形式の社内資料対応
- Gradio / Streamlit による Web UI 化
- 精度・応答速度の観点で gpt-4 やローカル LLM への切り替え評価

## 結論

LangChain + OpenAI API を用いることで、数十行のコードで社内文書に特化した Q\&A ボットを構築可能であることを確認した。今回の構成は社内ナレッジの検索体験改善に有効であり、他形式対応や UI 化によってさらに実用性を高められる見込みである。
