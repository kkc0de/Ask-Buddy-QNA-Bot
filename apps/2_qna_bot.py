from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
    temperature=0.3)

st.title('🤖 Ask Buddy QNA Bot')
st.markdown('My QNA Bot with LangChain and Google Gemini')

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

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
    # Add user message to history
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.markdown(query)

    conversation = (
        "You are Ask Buddy, a helpful, concise AI assistant.\n\n"
    )

    # 🔥 SEND FULL HISTORY, NOT JUST QUERY
    
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n"
        elif msg["role"] == "ai":
            conversation += f"Assistant: {msg['content']}\n"

    conversation += "Assistant:"

    # Invoke Gemini with plain text (STABLE)
    response = llm.invoke(conversation)

    #Show AI respose
    with st.chat_message("ai"):
        st.markdown(response.content)

    # Add AI response to history
    st.session_state.messages.append(
        {"role": "ai", "content": response.content}
    )
