# LangChain + Chroma RAG プロトタイプ調査レポート（2025-05-20）

## 1. 調査目的

- Windows 環境で **LangChain + Chroma** を用いた RAG QA プロトタイプを構築する。
- Markdown 資料をベクトル化・インデックス化し、`python main.py` で CLI 質問応答を確認する。

---

## 2. 本日の作業ログと知見

| 時刻帯 | 作業内容 / 発生事象                                            | 対応・解決策                                            |
| ------ | -------------------------------------------------------------- | ------------------------------------------------------- |
| 午前   | `langchain-community` 未インストールで `ModuleNotFoundError`   | `pip install -U langchain-community` で解決             |
| 午前   | `DirectoryLoader`,`TextLoader`,`Chroma` の **deprecated** 警告 | インポートを `langchain_community.*` へ変更             |
| 午前   | `UnicodeDecodeError: cp932`（.md を読み込めず）                | `TextLoader(…, encoding="utf-8")` を追加                |
| 午前   | `KeyError: 'output'`                                           | 返却キーを `ans["answer"]` へ修正                       |
| 午後   | `persist()` なしの新 API で `AttributeError`                   | `vectordb.persist()` 行を削除し、自動永続化に移行       |
| 午後   | 回答の取りこぼし（k 値不足・チャンク粗い）                     | `chunk_size=500`,`chunk_overlap=50`,`k=8` に調整        |
| 午後   | ドキュメント不足で回答欠落                                     | `guide.md` と `faq.md` に不足情報を追記し再インデックス |
| 夕方   | 全 10 問のサンプル質問で回答を検証                             | すべて正答を取得し、プロトタイプ完成を確認              |

---

## 3. 修正ポイントの概要

1. **依存ライブラリ**

   ```powershell
   pip install -U langchain langchain-community langchain-openai langchain-chroma
   ```

2. **main.py 主要修正**

   - インポートを `langchain_community` / `langchain_chroma` へ変更
   - `TextLoader` に `encoding="utf-8"` を渡す
   - `ans["answer"]` を出力
   - `Chroma.from_documents(..., persist_directory=...)` のあとに `.persist()` を呼ばない
   - `RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)`
   - `retriever = vectordb.as_retriever(search_kwargs={"k": 8})`

3. **ドキュメント補強**

   - `guide.md` に「終了方法」「Python 3.10 以上」を追加
   - `faq.md` に「パラメータ調整」「出典コード例」「VC++ Build Tools」「Streamlit UI」「Chroma サーバーモード」を追加

4. **インデックス更新フロー**

   ```powershell
   Remove-Item -Recurse -Force vector_store
   python main.py   # docs/ を再スキャンして自動生成
   ```

---

## 4. 最終動作確認

- `python main.py` 起動後、以下の質問で正答を取得

  - ディレクトリ構成
  - CLI 終了コマンド
  - インデックス更新手順
  - ローカル埋め込みモデル利用方法
  - 調整すべきパラメータ
  - 出典ドキュメント表示コード例
  - Python 最低バージョン
  - Chroma サーバーモード永続化手順
  - VC++ Build Tools が必要な場面
  - Web UI 追加の簡易手段（Streamlit）

---

## 5. 今後の改善アイデア

| 分類 | 具体案                                                        |
| ---- | ------------------------------------------------------------- |
| UI   | Streamlit 版 UI／FastAPI + React で SPA 化                    |
| 精度 | OpenAI `text-embedding-3-small` や bge-reranker の導入        |
| 運用 | Chroma Server 常駐＋ FastAPI バックエンドを Docker Compose 化 |
| 監視 | LangSmith でチェーン可視化・デバッグ                          |
| CI   | pytest による E2E テストと GitHub Actions 連携                |
