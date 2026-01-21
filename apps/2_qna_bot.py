from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("Gemini Health Check")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0
)

if st.button("Test Gemini"):
    try:
        response = llm.invoke("Say exactly: Gemini is working")
        st.success(response.content)
    except Exception as e:
        st.error("Gemini call failed")
        st.exception(e)
