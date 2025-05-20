# LangChain + Chroma RAG プロトタイプ 使い方ガイド

## 1. プロジェクト概要

Markdown 資料をベクトル化し、CLI で質問回答（RAG）できる最小構成です。

```

rag-langchain-chroma/
├─ docs/          # ← 資料置き場（ここに本ファイルを保存）
│  ├─ guide.md
│  └─ faq.md
├─ main.py        # 実行スクリプト
└─ .env           # OPENAI\_API\_KEY など

```

## 2. 前提

- Windows 10 以降 / PowerShell
- Python 3.10 以上（仮想環境推奨）
- OpenAI API キー（無料枠でも可）

## 3. セットアップ手順（簡易版）

````powershell
# 仮想環境作成
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt   # または手動でライブラリをインストール

## 4. CLI の起動と操作

```powershell
python main.py
````

- `❓>` プロンプトが出たら質問を入力
- `exit` / `quit` で終了

## 5. Markdown 資料の追加方法

1. `docs/` に `.md` ファイルを置く
2. **最初の 1 回だけ**: `vector_store/` フォルダーを削除して再実行

   - 削除しない場合、古いインデックスが再利用されます

## 6. 拡張アイデア

- HuggingFaceEmbeddings でローカル埋め込み
- メモリ機能を足してチャット継続
- Chroma Server モードで永続化
- LangSmith でチェイン可視化

## 7. CLI の終了方法

- 入力欄に **`exit`** または **`quit`** と打つ

## 8. 必要な Python バージョン

- **Python 3.10 以上**（3.12 でも動作確認済み）
