# LangChain + Chroma RAG よくある質問（FAQ）

## Q1. インデックスを作り直すには？

`vector_store/` フォルダーを削除してから `python main.py` を再実行してください。

## Q2. OpenAI 料金が気になる…

- 小規模ドキュメントなら埋め込みコストは数十円程度
- 完全オフライン運用したい場合は
  ```python
  from langchain.embeddings import HuggingFaceEmbeddings
  embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")
  ```

## 7. CLI の終了方法

- 入力欄に **`exit`** または **`quit`** と打つ

## 8. 必要な Python バージョン

- **Python 3.10 以上**（3.12 でも動作確認済み）

## Q9. Chroma をサーバーモードで永続化する方法は？

```bash
pip install chromadb  # CLI がまだ無ければ
chroma run --path ./vector_store
```


## Q10. 回答が的外れになるときに調整すべきパラメータは？
- **chunk_size / chunk_overlap** : テキスト分割粒度を調整  
- **search_kwargs={"k": N}** : Retriever が返す候補数を増減  
- **system_prompt** : 期待する答え方を詳しく書く

## Q11. 出典ドキュメントを表示するコード例は？
```python
ans = chain.invoke({"input": q})
for doc in ans["context"]:
    print(doc.metadata["source"])

## Q12. Windows で VC++ Build Tools が必要になる場面は？

* Chroma や sentence-transformers など、**C++ バックエンドをビルドするパッケージを pip install するとき**
* 具体的には *error: Microsoft Visual C++ 14.0* のようなビルドエラーが出たケース

## Q13. Web UI を追加する一番手軽な方法は？

* **Streamlit** を使うと、20 行程度でチャット UI が書ける
* 例：`pip install streamlit` → `streamlit run ui.py`