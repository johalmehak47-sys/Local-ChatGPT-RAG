import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from .provider import EmbeddingProvider

load_dotenv()


class GeminiEmbeddingProvider(EmbeddingProvider):

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        self.model = GoogleGenerativeAIEmbeddings(
            model=os.getenv("EMBEDDING_MODEL"),
            google_api_key=api_key,
        )

    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return self.model.embed_documents(texts)

    @property
    def embedding_model(self):
        return self.model