from src.pdf_loader import PDFLoader
from src.chunker import TextChunker
from src.embeddings import EmbeddingGenerator

loader = PDFLoader()
documents = loader.load("data/Final_Report_Template_Image_Captioning.pdf")

chunker = TextChunker()
chunks = chunker.split(documents)

embedder = EmbeddingGenerator()
vectors = embedder.embed_documents(chunks)

print(f"Chunks : {len(chunks)}")
print(f"Embeddings : {len(vectors)}")

print()

print(f"Embedding Dimension : {len(vectors[0])}")