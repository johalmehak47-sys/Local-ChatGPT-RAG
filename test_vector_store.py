from src.pdf_loader import PDFLoader
from src.chunker import TextChunker
from src.vector_store import VectorStore

loader = PDFLoader()

documents = loader.load("data/Man's Search for Meaning .pdf")

chunker = TextChunker()

chunks = chunker.split(documents)

store = VectorStore()

store.add_documents(chunks)

print("Documents stored successfully!")