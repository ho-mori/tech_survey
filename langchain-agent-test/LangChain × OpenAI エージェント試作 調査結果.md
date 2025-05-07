# LangChain × OpenAI エージェント試作 調査結果

## 1. 調査日

2025 年 4 月 30 日（水）

## 2. 調査テーマ

LangChain と OpenAI API を使用して、自己紹介および質問応答が可能なエージェントを試作する。

## 3. 実施環境

- OS: Windows 11
- Python: 3.10
- 仮想環境: venv
- LangChain: 最新版（v0.1.0 以降）
- OpenAI: gpt-3.5-turbo
- プロキシ環境: あり

## 4. 実施手順

### 4.1. プロジェクト作成と環境構築

```bash
mkdir langchain-agent-test
cd langchain-agent-test
python -m venv venv
.\venv\Scripts\activate
pip install langchain openai langchain-community
```

### 4.2. API キーの準備

- `.env`ファイルまたはスクリプト内で OpenAI API キーを設定。

### 4.3. Python スクリプト作成（agent_test.py）

- 使用ライブラリ: `ChatOpenAI`, `initialize_agent`, `Tool`
- 自己紹介用の Tool を実装し、LangChain のエージェントに組み込み
- 質問受付ループを構築

```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool

def simple_self_intro(_input: str) -> str:
    return "私は技術開発部所属のAIエージェントです。あなたの質問に答えます。"

tools = [
    Tool(
        name="SelfIntroduction",
        func=simple_self_intro,
        description="自己紹介を行います。"
    )
]

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

while True:
    user_input = input("質問をどうぞ (exitで終了)：")
    if user_input.lower() == "exit":
        break
    result = agent.run(user_input)
    print(result)
```

### 4.4. 実行と動作確認

- コマンドラインで起動

```bash
python agent_test.py
```

- 入力例と応答：

```
質問をどうぞ (exitで終了)：あなたは誰？
→ 私は技術開発部所属のAIエージェントで、質問に答えたり、サポートを提供したりするためにここにいます。

質問をどうぞ (exitで終了)：次世代技術の注目点は？
→ 次世代技術の注目点は、AI、IoT、ブロックチェーン、バーチャルリアリティなどがあります。
```

## 5. 成果と評価

| 項目                           | 結果                       |
| :----------------------------- | :------------------------- |
| LangChain + OpenAI 連携        | 成功                       |
| 自己紹介ツール呼び出し         | 成功                       |
| 自然言語質問への応答           | 成功                       |
| エージェントの推論ステップ表示 | 成功（verbose 出力で確認） |

## 6. 発生した警告と今後の対応

| 警告内容                                    | 対応方針                                       |
| :------------------------------------------ | :--------------------------------------------- |
| `from langchain.chat_models` が非推奨       | `langchain_community.chat_models` への移行検討 |
| `ChatOpenAI` クラスの将来的移動             | `langchain-openai`パッケージでの使用に切替可能 |
| `agent.run()`の非推奨化                     | `.invoke()` への置き換え推奨                   |
| LangChain Agent から LangGraph への移行推奨 | LangGraph の学習・検証を次回以降検討           |

## 7. 結論

- LangChain と OpenAI を使用したエージェントの試作は成功した。
- 自己紹介ツールと汎用質問応答を組み合わせた、簡易的な REACT 型エージェントを動作確認できた。
- LangChain のバージョン変更による警告が多く、今後は LangGraph およびモジュール分割に対応した構成への移行が求められる。
