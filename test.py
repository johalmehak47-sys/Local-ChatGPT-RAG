from src.pdf_loader import PDFLoader

loader = PDFLoader()

documents = loader.load("data/Final_Report_Template_Image_Captioning.pdf")

print(f"Loaded {len(documents)} pages.\n")

for document in documents:
    print("-" * 40)
    print(f"Page: {document.page}")
    print(f"Source: {document.source}")
    print(document.text[:300])