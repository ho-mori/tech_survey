import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# 環境変数読み込み
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Markdown文書読み込み（サブディレクトリ含む）
loader = DirectoryLoader(
    "docs",
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
documents = loader.load()

# 文書をチャンクに分割
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Embedding + FAISSでベクトル化
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("data/faiss_index")

# Retriever + ChatGPT でQA処理
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(temperature=0.2)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 質問ループ
while True:
    query = input("質問を入力してください（終了するには 'exit'）: ")
    if query.lower() == 'exit':
        break
    result = qa.invoke(query)
    print("回答:", result['result'])  # ← 結果部分だけを表示
