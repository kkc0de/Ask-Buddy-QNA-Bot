from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

st.title("🤖 Ask Buddy – QNA Bot")
st.markdown("Conversational AI chatbot using LangChain + Groq")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
query = st.chat_input("Ask me anything")

if query:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    # Build conversation prompt (stable)
    conversation = "You are Ask Buddy, a helpful, concise AI assistant.\n\n"

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"
        else:
            conversation += f"Assistant: {msg['content']}\n"

    conversation += "Assistant:"

    # Invoke Groq
    response = llm.invoke(conversation)

    with st.chat_message("assistant"):
        st.markdown(response.content)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )
