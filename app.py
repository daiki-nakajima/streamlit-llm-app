import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
)

EXPERT_PROMPTS = {
    "ITコンサルタント": (
        "あなたはIT業界に精通したコンサルタントです。"
        "クライアントの状況に寄り添い、ロジカルシンキングに基づいて助言と提案をしてください。"
    ),
    "スポーツ栄養士": (
        "あなたはトップアスリートを支えるスポーツ栄養士です。"
        "科学的根拠と具体的な食事例を交えて助言してください。"
    ),
}

def ask_expert(question: str, expert_key: str) -> str:
    system_msg = SystemMessage(content=EXPERT_PROMPTS[expert_key])
    human_msg  = HumanMessage(content=question)
    return llm([system_msg, human_msg]).content

st.title("Lesson21: Streamlitを活用したWebアプリ開発")

st.markdown(
"""
## 概要
このアプリは、Streamlit + LangChain + OpenAI を用いて  
選択した専門家になりきったAIからアドバイスを得るWEBアプリです。  
質問を入力して送信すると、AI がリアルタイムで回答を生成します。
"""
)

st.markdown(
"""
## 操作手順
1. ラジオボタンで相談したい専門家AIを選択してください。  
2. テキストボックスに質問を入力してください。  
3. 送信ボタンを押すと、選択した専門家AIによる回答が表示されます。
"""
)

expert_choice = st.radio("専門家の種類を選択してください:", list(EXPERT_PROMPTS.keys()))
user_input    = st.text_input("質問を入力してください:")

if st.button("送信") and user_input.strip():
    with st.spinner("回答を生成中…"):
        answer = ask_expert(user_input, expert_choice)
    st.markdown("## 回答")
    st.write(answer)
