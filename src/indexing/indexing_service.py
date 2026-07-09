from pathlib import Path
import os
import shutil

from src.pdf_loader import PDFLoader
from src.chunker import TextChunker
from src.vector_store import VectorStore

from .hash_utils import HashUtils
from .registry import Registry


class IndexingService:
    """
    Coordinates the complete indexing pipeline.
    """

    def __init__(self):

        self.loader = PDFLoader()

        self.chunker = TextChunker()

        self.vector_store = VectorStore()

        self.registry = Registry()

        self.documents_directory = Path("documents")

        self.documents_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def upload_pdf(self, uploaded_file) -> dict:
        """
        Save an uploaded Streamlit file and index it.

        Returns:
            dict containing status information.
        """

        destination = self.documents_directory / uploaded_file.name

        with open(destination, "wb") as file:
            shutil.copyfileobj(uploaded_file, file)

        already_exists = self.registry.exists(
            HashUtils.sha256(str(destination))
        )

        self.index_pdf(str(destination))

        return {
            "success": True,
            "already_indexed": already_exists,
            "filename": uploaded_file.name,
        }

    def index_pdf(
        self,
        pdf_path: str,
    ) -> None:

        file_hash = HashUtils.sha256(pdf_path)

        if self.registry.exists(file_hash):

            info = self.registry.get(file_hash)

            print("=" * 50)

            print("Document already indexed.\n")

            print(f"Filename           : {info['filename']}")

            print(f"Embedding Provider : {info['provider']}")

            print(f"Indexed At         : {info['indexed_at']}")

            print(f"Chunks             : {info['chunks']}")

            print("=" * 50)

            return

        documents = self.loader.load(pdf_path)

        chunks = self.chunker.split(documents)

        self.vector_store.add_documents(chunks)

        self.registry.register(
            file_hash=file_hash,
            filename=Path(pdf_path).name,
            chunks=len(chunks),
            provider=os.getenv(
                "EMBEDDING_PROVIDER",
                "local",
            ),
            collection="knowledge_base",
        )

        print("\nDocument indexed successfully.")