from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("🧪 Gemini Health Check")

# ✅ CORRECT LangChain-compatible model name
llm = ChatGoogleGenerativeAI(
    model="models/gemini-pro",
    temperature=0
)

st.markdown("This checks whether Gemini is reachable from Streamlit Cloud.")

if st.button("Test Gemini"):
    try:
        response = llm.invoke("Say exactly: Gemini is working")
        st.success(response.content)
    except Exception as e:
        st.error("Gemini call failed")
        st.exception(e)
