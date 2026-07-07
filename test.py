from src.pdf_loader import PDFLoader

loader = PDFLoader()

documents = loader.load("data/Man's Search for Meaning .pdf")

print(f"Loaded {len(documents)} pages.\n")

for document in documents:
    print("-" * 40)
    print(f"Page: {document.metadata['page']}")
    print(f"Source: {document.metadata['source']}")
    print(document.text[:300])