"""
Prompt builder for the RAG pipeline.

This module converts retrieved documents into a structured prompt
that can be sent directly to an LLM.
"""

from langchain_core.documents import Document

from src.prompts.templates import DEFAULT_RAG_TEMPLATE


class PromptBuilder:
    """
    Builds prompts for Retrieval-Augmented Generation (RAG).
    """

    def __init__(
        self,
        template: str = DEFAULT_RAG_TEMPLATE,
        max_documents: int = 5,
        include_metadata: bool = True,
        separator: str | None = None,
        no_context_message: str = "No relevant context was retrieved.",
    ):
        self.template = template
        self.max_documents = max_documents
        self.include_metadata = include_metadata
        self.separator = (
            separator
            if separator is not None
            else "\n\n" + "=" * 80 + "\n\n"
        )
        self.no_context_message = no_context_message

    def build(
        self,
        question: str,
        documents: list[Document]
    ) -> str:
        """
        Build a complete prompt from the user question
        and retrieved documents.
        """

        context = self._build_context(documents)

        return self.template.format(
            context=context,
            question=question,
        )

    def _build_context(
        self,
        documents: list[Document]
    ) -> str:
        """
        Convert retrieved documents into a structured context
        including metadata such as source and page number.
        """

        if not documents:
            return self.no_context_message

        sections = []

        for index, document in enumerate(
            documents[: self.max_documents],
            start=1,
        ):
            metadata = document.metadata or {}

            source = metadata.get("source", "Unknown Source")
            page = metadata.get("page", "Unknown")
            chunk = (
                metadata.get("chunk_id")
                or metadata.get("chunk")
                or index
            )

            section = f"""
Document {index}

Source : {source}
Page   : {page}
Chunk  : {chunk}

Content:
{document.page_content}
""".strip()

            sections.append(section)

        return self.separator.join(sections)