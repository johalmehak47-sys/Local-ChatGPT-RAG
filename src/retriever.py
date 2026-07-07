from langchain_chroma import Chroma
from src.embeddings.factory import EmbeddingFactory



class Retriever:
    """
    Retrieves the most relevant documents from the vector database.
    """

    def __init__(self):
        embedder = EmbeddingFactory.create()

        self.db = Chroma(
            collection_name="knowledge_base",
            embedding_function=embedder.embedding_model,
            persist_directory="database/chroma_db",
        )

    def search(
        self,
        query: str,
        k: int = 3,
    ):
        """
        Returns the top-k most relevant documents for the query.
        """

        return self.db.similarity_search(
            query=query,
            k=k,
        )