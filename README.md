# 🤖 Ask Buddy – QNA Bot

Ask Buddy is a conversational AI chatbot built using **LangChain**, **Groq**, and **Streamlit**.  
It supports **multi-turn conversational memory**, allowing users to ask follow-up questions with proper context.

---

## 🚀 Features

- Conversational Q&A chatbot
- Maintains session-based conversation history
- Handles contextual follow-up questions
- Clean and interactive Streamlit chat interface
- Secure API key handling using environment variables

---

## 🧠 Conversational Memory

Large Language Models (LLMs) are **stateless by default**.  
In this project, conversation history is manually stored and sent with every user query, enabling the assistant to understand context across multiple turns.

**Example:**
```text
User: Describe a tiger  
User: How many legs does it have?
