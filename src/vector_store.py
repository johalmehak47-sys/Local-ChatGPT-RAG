import os

from dotenv import load_dotenv
from langchain_chroma import Chroma

from src.doc import Document
from src.embeddings.factory import EmbeddingFactory

load_dotenv()


class VectorStore:
    """
    Stores document chunks and their embeddings in ChromaDB.
    """

    def __init__(self):
        embedder = EmbeddingFactory.create()

        self.db = Chroma(
            collection_name="knowledge_base",
            embedding_function=embedder.embedding_model,
            persist_directory="database/chroma_db",
        )

        self.batch_size = int(
            os.getenv("BATCH_SIZE", 32)
        )

    def _create_batches(
        self,
        documents: list[Document],
    ):
        """
        Yields batches of documents for efficient indexing.
        """

        for i in range(
            0,
            len(documents),
            self.batch_size,
        ):
            yield documents[
                i:i + self.batch_size
            ]

    def add_documents(
        self,
        documents: list[Document],
    ) -> None:
        """
        Adds a list of Document objects to the vector database.
        """

        total_batches = (
            len(documents)
            + self.batch_size
            - 1
        ) // self.batch_size

        for index, batch in enumerate(
            self._create_batches(documents),
            start=1,
        ):

            print(
                f"Indexing batch "
                f"{index}/{total_batches}"
            )

            texts = []
            metadatas = []
            ids = []

            for document in batch:
                texts.append(document.text)
                metadatas.append(document.metadata)
                ids.append(
                    f"chunk_{document.metadata['chunk_id']}"
                )

            try:
                self.db.add_texts(
                    texts=texts,
                    metadatas=metadatas,
                    ids=ids,
                )

            except Exception as e:
                print(
                    f"Failed batch {index}/{total_batches}: {e}"
                )
                raise