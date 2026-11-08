
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

st.set_page_config(page_title="Local AI Chatbot", page_icon="🤖")

st.title("Local AI Chatbot")
st.caption("Powered by Llama 3.2 and LangChain Memory")

# Initialize local LLM
llm = ChatOllama(model="llama3.2", temperature=0.7)

if "store" not in st.session_state:
    st.session_state.store = {}

store = st.session_state.store

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Create chatbot chain
chain = prompt | llm

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Session ID
session_id = "user_session"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if user_input := st.chat_input("Ask something..."):

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chatbot.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )

            answer = response.content
            st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
