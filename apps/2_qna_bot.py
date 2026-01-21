from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

st.title("🤖 Ask Buddy QNA Bot")
st.markdown("A conversational AI chatbot built with Google Gemini")

# UI-only chat history (NOT sent to model)
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask me anything")

if query:
    # show user
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # 🔒 SIMPLE, STABLE PROMPT (NO HISTORY)
    prompt = f"You are a helpful AI assistant. Answer clearly.\n\nUser: {query}\nAssistant:"

    response = llm.invoke(prompt)

    st.session_state.messages.append(
        {"role": "ai", "content": response.content}
    )

    with st.chat_message("ai"):
        st.markdown(response.content)
