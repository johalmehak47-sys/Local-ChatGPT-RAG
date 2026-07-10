# Local ChatGPT
### AI-Powered Document Assistant using Retrieval-Augmented Generation (RAG)

Local ChatGPT is a Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and interact with them through natural language conversations. Instead of relying solely on the knowledge of a Large Language Model (LLM), the application retrieves relevant information from user-provided documents and generates context-aware responses using Google's Gemini model.

The project demonstrates the complete RAG workflow, including document ingestion, semantic chunking, embedding generation, vector indexing, semantic retrieval, prompt engineering, and answer generation through a modular software architecture.

---

## Features

- Upload PDF documents directly through the web interface
- Automatic document parsing and semantic chunking
- Local embedding generation using Sentence Transformers
- Persistent vector database using ChromaDB
- Semantic similarity search for relevant context retrieval
- Context-grounded answer generation using Google Gemini
- SHA-256 hash-based duplicate document detection
- Incremental indexing to avoid redundant processing
- Modular and extensible architecture
- Interactive Streamlit interface
- Knowledge base statistics dashboard

---

## System Architecture

```
                           User
                             │
                             ▼
                     Streamlit Interface
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
      PDF Upload                         Chat Interface
            │                                 │
            ▼                                 ▼
     IndexingService                    ChatBot.ask()
            │                                 │
            ▼                                 ▼
      PDF Loader                         Retriever
            │                                 │
            ▼                                 ▼
      Text Chunker                    Similarity Search
            │                                 │
            ▼                                 ▼
     Embedding Model                 Prompt Builder
            │                                 │
            ▼                                 ▼
        ChromaDB                     Gemini Client
            │                                 │
            └────────────────┬────────────────┘
                             ▼
                       Final Response
```

---

## Project Structure

```
Local-ChatGPT/
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
├── chroma_db/
├── documents/
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| UI | Streamlit |
| PDF Processing | PyPDF |
| Configuration | python-dotenv |

---

## RAG Pipeline

The application follows the standard Retrieval-Augmented Generation workflow.

```
PDF Upload
      │
      ▼
Document Parsing
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Vector Storage (ChromaDB)
      │
      ▼
Semantic Retrieval
      │
      ▼
Prompt Construction
      │
      ▼
Gemini LLM
      │
      ▼
Grounded Response
```

---

## Indexing Pipeline

Every uploaded document goes through the following stages:

1. Upload validation
2. SHA-256 hash generation
3. Duplicate detection
4. PDF parsing
5. Semantic chunk creation
6. Embedding generation
7. ChromaDB indexing
8. Registry update

Duplicate documents are automatically skipped, preventing unnecessary storage and embedding computation.

---

## Key Design Decisions

### Modular Architecture

Each component has a single responsibility.

- PDFLoader handles document parsing.
- TextChunker performs semantic chunking.
- VectorStore manages ChromaDB operations.
- Retriever performs semantic search.
- PromptBuilder constructs LLM prompts.
- GeminiClient communicates with Gemini.
- ChatBot orchestrates the complete RAG workflow.
- IndexingService manages document ingestion and indexing.

---

### Persistent Knowledge Base

Instead of embedding documents every time the application starts, embeddings are stored permanently in ChromaDB.

This significantly reduces startup time and enables incremental indexing.

---

### Duplicate Detection

The application computes a SHA-256 hash for every uploaded document.

If the document has already been indexed, it is skipped automatically.

This prevents duplicate vectors from being stored.

---

### Prompt Engineering

The prompt explicitly instructs the language model to:

- Answer only using retrieved document context.
- Avoid hallucinations.
- Clearly indicate when information is unavailable.
- Reference document sources whenever applicable.

---

## Installation

Clone the repository

```bash
git clone https://github.com/<username>/Local-ChatGPT-RAG.git

cd Local-ChatGPT-RAG
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY

GEMINI_MODEL=gemini-2.5-flash

EMBEDDING_PROVIDER=local

LOCAL_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

BATCH_SIZE=16

COLLECTION_NAME=knowledge_base

CHROMA_DB_DIR=chroma_db
```

---

## Running the Application

```bash
streamlit run app/app.py
```

---

## Screenshots

> Add screenshots after deployment.

### Main Interface

```
assets/home.png
```

### Upload Workflow

```
assets/upload.png
```

### Chat Interface

```
assets/chat.png
```

---

## Current Capabilities

- PDF upload
- Automatic indexing
- Persistent vector database
- Duplicate detection
- Semantic retrieval
- Context-aware answer generation
- Interactive document chat
- Modular architecture

---

## Current Limitations

- Supports PDF documents only
- Single-user application
- No OCR support for scanned PDFs
- No conversation memory (planned for Version 2.0)
- No multi-document collections
- Cloud deployment not included in Version 1.0

---

## Version Roadmap

### Version 1.0

- End-to-end RAG pipeline
- Streamlit interface
- Incremental indexing
- Persistent knowledge base
- Gemini integration

### Version 2.0 (Planned)

- AI Teaching Mode
- Intelligent document summarization
- Cross-document reasoning
- Desktop application
- Multiple document collections
- Conversation memory
- OCR support
- Hybrid search
- Knowledge graph

---

## Future Improvements

- Local LLM support (Ollama / LM Studio)
- Streaming responses
- Citation cards
- Export chat history
- Authentication
- Cloud deployment
- REST API
- Docker support

---

## Repository

GitHub Repository

```
https://github.com/<your-username>/Local-ChatGPT-RAG
```

Live Demo

```
Coming Soon
```

---

## License

This project is released under the MIT License.

---

## Author

**Mehakdeep Singh**

Computer Science Undergraduate

Thapar Institute of Engineering and Technology

Interested in Artificial Intelligence, Retrieval-Augmented Generation, Software Engineering, and Intelligent Knowledge Systems.

---
