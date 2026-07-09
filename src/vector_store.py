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

        self.collection_name = os.getenv(
            "CHROMA_COLLECTION",
            "knowledge_base",
        )

        self.db = Chroma(
            collection_name=self.collection_name,
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
        Yield batches of documents for efficient indexing.
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
        Add document chunks to the vector database.
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
                    f"Failed batch "
                    f"{index}/{total_batches}: {e}"
                )

                raise

    def collection_exists(
        self,
    ) -> bool:
        """
        Check whether the Chroma collection exists.
        """

        try:

            self.db._collection.count()

            return True

        except Exception:

            return False

    def get_chunk_count(
        self,
    ) -> int:
        """
        Return the total number of indexed chunks.
        """

        if not self.collection_exists():

            return 0

        return self.db._collection.count()

    def get_collection_name(
        self,
    ) -> str:
        """
        Return the active collection name.
        """

        return self.collection_name

    def get_stats(
        self,
    ) -> dict:
        """
        Return vector store statistics.
        """

        return {
            "ready": self.collection_exists(),
            "collection": self.get_collection_name(),
            "chunks": self.get_chunk_count(),
        }