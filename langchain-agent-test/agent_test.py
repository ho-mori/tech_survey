import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.schema import SystemMessage
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# OpenAI APIキー設定
openai_api_key = os.getenv("OPENAI_API_KEY") or "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# LLMモデル定義
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.2,
    openai_api_key=openai_api_key,
)

# シンプルな自己紹介ツールを作る
def simple_self_intro(_input: str) -> str:
    return "私は技術開発部所属のAIエージェントです。あなたの質問に答えます。"

# ツール定義
tools = [
    Tool(
        name="SelfIntroduction",
        func=simple_self_intro,
        description="自己紹介を行います。何者かを尋ねる質問に使ってください。",
    ),
]

# エージェント初期化
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# 質問を試す
while True:
    user_input = input("質問をどうぞ (exitで終了)：")
    if user_input.lower() == "exit":
        break
    result = agent.run(user_input)
    print(result)
