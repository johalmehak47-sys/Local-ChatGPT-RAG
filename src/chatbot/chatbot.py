"""
Main chatbot orchestration class.
"""

from langchain_core.documents import Document

from src.llm.base_llm import BaseLLM
from src.llm.gemini_client import GeminiClient
from src.prompts.prompt_builder import PromptBuilder
from src.retriever import Retriever


class ChatBot:
    """
    Orchestrates the Retrieval-Augmented Generation pipeline.
    """

    def __init__(
        self,
        retriever: Retriever | None = None,
        prompt_builder: PromptBuilder | None = None,
        llm: BaseLLM | None = None,
    ):
        self.retriever = retriever or Retriever()
        self.prompt_builder = prompt_builder or PromptBuilder()
        self.llm = llm or GeminiClient()

    def ask(self, question: str) -> str:
        """
        Answer a user question using the RAG pipeline.
        """

        documents: list[Document] = self.retriever.search(question)

        prompt = self.prompt_builder.build(
            question=question,
            documents=documents,
        )

        answer = self.llm.generate(prompt)

        return answer