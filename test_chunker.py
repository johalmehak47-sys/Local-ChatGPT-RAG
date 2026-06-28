from src.pdf_loader import PDFLoader
from src.chunker import TextChunker

loader = PDFLoader()
documents = loader.load("data/Final_Report_Template_Image_Captioning.pdf")

chunker = TextChunker()

chunks = chunker.split(documents)

print(f"Pages loaded : {len(documents)}")
print(f"Chunks created : {len(chunks)}")

print()

print(chunks[0].text)