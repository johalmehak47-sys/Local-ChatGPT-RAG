from langchain_huggingface import HuggingFaceEmbeddings

from .provider import EmbeddingProvider


class LocalEmbeddingProvider(EmbeddingProvider):

    def __init__(self):

        self.model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            encode_kwargs={
                "normalize_embeddings": True,
            },
        )

    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return self.model.embed_documents(texts)

    @property
    def embedding_model(self):
        return self.model