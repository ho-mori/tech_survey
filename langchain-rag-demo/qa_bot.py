import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

load_dotenv()

# TextLoader に encoding を追加
loader = TextLoader("doc.md", encoding="utf-8")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
texts = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(texts, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    retriever=vectorstore.as_retriever()
)

while True:
    query = input("質問を入力してください：")
    if query.lower() in ["exit", "quit"]:
        break
    result = qa.invoke(query)["result"]
    print("回答：", result)
