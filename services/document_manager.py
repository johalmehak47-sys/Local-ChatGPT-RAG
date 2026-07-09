"""
Document management service.

Responsible for handling uploaded documents and
triggering the indexing pipeline.
"""

from pathlib import Path
import shutil


class DocumentManager:
    """
    Handles document upload and indexing.
    """

    def __init__(
        self,
        documents_directory: Path,
        indexer,
    ):
        self.documents_directory = documents_directory
        self.indexer = indexer

        self.documents_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_document(
        self,
        uploaded_file,
    ) -> Path:
        """
        Save an uploaded PDF to disk.
        """

        destination = (
            self.documents_directory /
            uploaded_file.name
        )

        with open(destination, "wb") as file:
            shutil.copyfileobj(
                uploaded_file,
                file,
            )

        return destination

    def upload(
        self,
        uploaded_file,
    ):
        """
        Save and index a document.
        """

        path = self.save_document(
            uploaded_file
        )

        self.indexer.index_documents()

        return path