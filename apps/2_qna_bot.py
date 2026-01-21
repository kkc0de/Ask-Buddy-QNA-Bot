from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini (stable)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

st.title("🤖 Ask Buddy QNA Bot")
st.markdown("My QNA Bot with LangChain and Google Gemini")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
query = st.chat_input("Ask me anything ?")

if query:
    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(query)

    # ---- BUILD GEMINI-SAFE PROMPT ----
    conversation = "You are Ask Buddy, a helpful, concise AI assistant.\n\n"

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"
        elif msg["role"] == "ai":
            conversation += f"Assistant: {msg['content']}\n"

    # Append current query ONLY ONCE
    conversation += f"User: {query}\nAssistant:"

    # Invoke Gemini with plain text (stable)
    response = llm.invoke(conversation)

    # Show AI response
    with st.chat_message("ai"):
        st.markdown(response.content)

    # Save messages AFTER response
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )
    st.session_state.messages.append(
        {"role": "ai", "content": response.content}
    )
