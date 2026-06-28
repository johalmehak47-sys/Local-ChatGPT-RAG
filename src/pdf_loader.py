from pathlib import Path
from pypdf import PdfReader

from src.doc import Document


class PDFLoader:
    """
    Reads a PDF file and converts every page
    into a Document object.
    """

    def load(self, pdf_path: str | Path) -> list[Document]:

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

        reader = PdfReader(path)

        documents = []

        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if text:

                documents.append(
                    Document(
                        text=text,
                        page=page_number,
                        source=path.name,
                    )
                )

        return documents