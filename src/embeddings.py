from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.doc import Document

load_dotenv()


class EmbeddingGenerator:
    """
    Creates embeddings for Document objects.
    """

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found."
            )

        self.model = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key,
)

    def embed_documents(
        self,
        documents: list[Document],
    ) -> list[list[float]]:

        texts = [
            document.text
            for document in documents
        ]

        embeddings = self.model.embed_documents(
            texts
        )

        return embeddings