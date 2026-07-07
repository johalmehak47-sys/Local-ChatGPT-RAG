import os
from dotenv import load_dotenv

from .gemini_provider import GeminiEmbeddingProvider
from .local_provider import LocalEmbeddingProvider

load_dotenv()


class EmbeddingFactory:

    @staticmethod
    def create():

        provider = os.getenv(
            "EMBEDDING_PROVIDER",
            "local",
        ).lower()

        if provider == "gemini":
            return GeminiEmbeddingProvider()

        if provider == "local":
            return LocalEmbeddingProvider()

        raise ValueError(
            f"Unknown embedding provider: {provider}"
        )