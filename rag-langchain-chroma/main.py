# main.py
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma

# LCEL 版：公式が推奨する最新の組み方
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain  # 正しい import パスに注意 :contentReference[oaicite:2]{index=2}

load_dotenv()

DOCS_DIR = "docs"
VECTOR_DIR = "vector_store"

def build_or_load_vectordb():
    """VectorDB が無ければ作って返す。あればロードして返す。"""
    embeddings = OpenAIEmbeddings()  # HuggingFaceEmbeddings に差し替え可
    if Path(VECTOR_DIR).exists():
        return Chroma(persist_directory=VECTOR_DIR,
                      embedding_function=embeddings)
    # --- インデックスを新規作成 ---
    loader = DirectoryLoader(
        DOCS_DIR,
        glob="**/*.md",
        loader_cls=TextLoader,      # md → 文字列
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
        use_multithreading=True
    )
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                              chunk_overlap=200)
    split_docs = splitter.split_documents(docs)
    vectordb = Chroma.from_documents(split_docs,
                                     embeddings,
                                     persist_directory=VECTOR_DIR)
    return vectordb

def build_rag_chain(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    # ---- ドキュメント結合用プロンプト ----
    system_prompt = (
        "あなたは Markdown 資料の専門家です。"
        "以下の <context></context> 内だけを根拠に日本語で簡潔に答えてください。"
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt),
         ("human", "<context>{context}</context>\n\n質問: {input}")]
    )

    combine_chain = create_stuff_documents_chain(
        llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0),
        prompt=prompt,
    )
    return create_retrieval_chain(retriever, combine_chain)  # RetrievalQA は 0.1.17 で非推奨 :contentReference[oaicite:3]{index=3}

def interactive_cli(chain):
    print("=== RAG QA CLI ===   'exit' で終了")
    while True:
        q = input("❓> ")
        if q.lower() in {"exit", "quit"}:
            break
        ans = chain.invoke({"input": q})
        print("💡", ans["answer"])
        # 出典文書を見たい場合:
        # for doc in ans["context"]:
        #     print("📄", doc.metadata["source"])

if __name__ == "__main__":
    vectordb = build_or_load_vectordb()
    rag_chain = build_rag_chain(vectordb)
    interactive_cli(rag_chain)
