# Local LLM Chatbot with LangChain Memory

## Project Overview

Local LLM Chatbot is a simple AI-powered chatbot built using Python, Streamlit, Ollama, and LangChain. It allows users to interact with an AI assistant while maintaining conversation history using LangChain memory.

The application uses a local Llama 3.2 model through Ollama when running on a local computer and Groq when deployed on Streamlit Cloud.

DEMO LINK

https://local-llm-chatbot-mtkbjrp4bjwdugmakapnbe.streamlit.app/

SCREENSHORTS

<img width="1385" height="842" alt="{0700B0E2-76C5-427F-938C-2E29321A13B6}" src="https://github.com/user-attachments/assets/51880f51-ea51-4279-b329-d07ce6081bfe" />
<img width="1013" height="808" alt="{B62CA6EC-E66C-430A-8E3F-0C4F3F808CEA}" src="https://github.com/user-attachments/assets/7cc8cc5d-eb42-412c-aa69-e71591de075f" />


## Features

- AI-powered conversational chatbot
- Local LLM integration using Ollama
- Llama 3.2 model support
- Groq API integration for cloud deployment
- LangChain prompt templates
- Conversation memory using RunnableWithMessageHistory
- Streamlit-based user interface
- Remembers previous messages during the conversation

## Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- Llama 3.2
- Groq API

## Project Architecture

**Local Execution:**

User → Streamlit UI → LangChain → Ollama → Llama 3.2 → Response

**Cloud Deployment:**

User → Streamlit UI → LangChain → Groq API → AI Model → Response

LangChain conversation memory maintains the previous messages and provides context for future responses.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Local-LLM-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install and Run Ollama

Download Ollama from https://ollama.com/

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

## Cloud Deployment

The application can be deployed using Streamlit Community Cloud.

For cloud deployment, add your Groq API key in the Streamlit Cloud Secrets settings:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never upload your API key to GitHub.

## LangChain Memory

The project uses:

- `InMemoryChatMessageHistory`
- `RunnableWithMessageHistory`
- `MessagesPlaceholder`

These components allow the chatbot to remember previous messages within the current conversation session.

## Example Interaction

**User:** My name is Humaira.

**AI:** Nice to meet you, Humaira!

**User:** What is my name?

**AI:** Your name is Humaira.

## Project Objective

To understand how local Large Language Models work and how LangChain memory can be integrated into a conversational AI application.

## Author

Humairul Jashira M.

B.Sc. Computer Science with Artificial Intelligence
