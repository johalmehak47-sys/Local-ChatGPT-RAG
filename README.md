# 📚 Local ChatGPT

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their contents using Google's Gemini LLM.

Built with **Python**, **LangChain**, **ChromaDB**, **Streamlit**, and **Gemini**.

---

## ✨ Features

- 📄 Upload PDF documents
- ✂️ Automatic document chunking
- 🧠 Semantic embeddings
- 💾 Persistent ChromaDB vector database
- 🔍 Semantic similarity search
- 🤖 Gemini-powered answer generation
- 📚 Source-aware responses
- 🚀 Incremental indexing (avoids duplicate indexing)
- 🖥️ Interactive Streamlit interface

---

## 🏗️ Architecture

```
                 User
                   │
                   ▼
             Streamlit UI
                   │
                   ▼
              ChatBot.ask()
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
 Retriever               PromptBuilder
      │                         │
      └────────────┬────────────┘
                   ▼
             Gemini Client
                   │
                   ▼
           Gemini 2.5 Flash
```

---

## 📂 Project Structure

```
project/

│
├── app/
│   ├── app.py
│   ├── components/
│   └── utils/
│
├── src/
│   ├── chatbot/
│   ├── chunker/
│   ├── embeddings/
│   ├── indexing/
│   ├── llm/
│   ├── pdf_loader/
│   ├── prompts/
│   ├── retriever/
│   └── vector_store/
│
├── documents/
├── chroma_db/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=your_api_key

EMBEDDING_PROVIDER=local

LOCAL_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
```

Run the application

```bash
streamlit run app/app.py
```

---

## 🧠 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Google Gemini
- SentenceTransformers

---

## 🚀 Future Improvements

- Conversation memory
- Multiple collections
- Hybrid search
- OCR support
- Image understanding
- User authentication

---

## 📄 License

This project is intended for educational and portfolio purposes.
