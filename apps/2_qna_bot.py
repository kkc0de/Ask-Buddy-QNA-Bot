from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash-lite')

st.title('🤖 Ask Buddy QNA Bot')
st.markdown('My QNA Bot with LangChain and Google Gemini')

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are Ask Buddy, a helpful, concise AI assistant."
        }
    ]

if st.button("🧹 Clear Chat"):
    st.session_state.messages = st.session_state.messages[:1]
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
query = st.chat_input("Ask me anything ?")

if query:
    # Add user message to history
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    # 🔥 SEND FULL HISTORY, NOT JUST QUERY
    response = llm.invoke(st.session_state.messages)

    with st.chat_message("ai"):
        st.markdown(response.content)

    # Add AI response to history
    st.session_state.messages.append(
        {"role": "ai", "content": response.content}
    )
