# Local AI Chatbot with LangChain Memory

## Project Overview

Local AI Chatbot is a simple conversational AI application built using a locally running Large Language Model (LLM). It uses Llama 3.2 through Ollama and LangChain to maintain conversation history and remember previous user messages.

## Features

- Runs locally using Ollama.
- Powered by Llama 3.2.
- LangChain conversation memory.
- Remembers previous messages during the session.
- Interactive chatbot interface using Streamlit.
- No OpenAI API key required.

## Technologies Used

- Python
- Ollama
- Llama 3.2
- LangChain
- Streamlit

## Project Structure

```text
Local-LLM-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Install Ollama

Download Ollama from https://ollama.com/download

### 2. Download the LLM

```bash
ollama pull llama3.2
```

### 3. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Local-LLM-Chatbot
```

### 4. Create Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

## How It Works

1. User enters a message.
2. LangChain retrieves previous conversation history.
3. Ollama processes the prompt using Llama 3.2.
4. The chatbot generates a response.
5. LangChain stores the conversation for future interactions.

## Memory Implementation

The application uses LangChain's `RunnableWithMessageHistory` and `InMemoryChatMessageHistory` to maintain conversation history within the current session.

## Note

Conversation memory is stored temporarily in memory and is not permanently saved after restarting the application.

## Author

Humairul Jashira
