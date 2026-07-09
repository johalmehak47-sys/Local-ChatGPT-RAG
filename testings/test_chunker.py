# from src.pdf_loader import PDFLoader
# from src.chunker import TextChunker

# loader = PDFLoader()
# documents = loader.load("data/Final_Report_Template_Image_Captioning.pdf")

# chunker = TextChunker()

# chunks = chunker.split(documents)

# print(f"Pages loaded : {len(documents)}")
# print(f"Chunks created : {len(chunks)}")

# print()

# print(chunks[0].text)
from src.pdf_loader import PDFLoader
from src.chunker import TextChunker

# Load PDF
loader = PDFLoader()
documents = loader.load("data/Man's Search for Meaning .pdf")

# Chunk the documents
chunker = TextChunker()
chunks = chunker.split(documents)

print("=" * 80)
print("PDF CHUNKING TEST")
print("=" * 80)

print(f"\nPages Loaded   : {len(documents)}")
print(f"Chunks Created : {len(chunks)}")

print("\n" + "=" * 80)
print("GENERATED CHUNKS")
print("=" * 80)

for chunk in chunks:

    print(f"\n{'=' * 80}")
    print(f"Chunk ID : {chunk.metadata['chunk_id']}")
    print(f"Page     : {chunk.metadata['page']}")
    print(f"Source   : {chunk.metadata['source']}")
    print("-" * 80)

    print(chunk.text)

    print("-" * 80)
    print(f"Chunk Length : {len(chunk.text)} characters")