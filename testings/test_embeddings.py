import warnings

warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)

from src.pdf_loader import PDFLoader
from src.chunker import TextChunker
from src.embeddings.factory import EmbeddingFactory


loader = PDFLoader()
documents = loader.load("data/Man's Search for Meaning .pdf")

chunker = TextChunker()
documents = chunker.split(documents)

provider = EmbeddingFactory.create()

texts = [doc.text for doc in documents]

embeddings = provider.embed(texts)

print(f"Documents : {len(documents)}")
print(f"Embeddings : {len(embeddings)}")
print(f"Embedding Dimension : {len(embeddings[0])}")