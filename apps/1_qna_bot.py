from dotenv import load_dotenv
load_dotenv()

# Project Starts here 
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
llm=ChatGoogleGenerativeAI(model='models/gemini-2.5-flash-lite')

st.title('🤖 Ask Buddy QNA Bot')
st.markdown('My QNA Bot with Langchain and Google Gemini')

if 'messages' not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message['role']
    content=message['content']
    st.chat_message(role).markdown(content)

query=st.chat_input('Ask me anything ?')
if query:
    st.session_state.messages.append({'role':'user','content':query})
    st.chat_message('user:').markdown(query)
    response=llm.invoke(query)
    st.chat_message('ai:').markdown(response.content)
    st.session_state.messages.append({'role':'ai','content':response.content})
  
    # print('AI :',query)
# while True:
#     query=input('user: ')

#     if query.lower() in  ['exit','end','bye']:
#         print('End of conversation 🙋🏻‍♂️')
#         break
#     result=llm.invoke(query)
#     print('ai:',result.content)
