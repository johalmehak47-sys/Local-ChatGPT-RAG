from langchain_core.documents import Document

from src.prompts.prompt_builder import PromptBuilder


def test_build_returns_prompt():
    builder = PromptBuilder()

    docs = [
        Document(
            page_content="Artificial Intelligence is the simulation of human intelligence."
        )
    ]

    prompt = builder.build(
        question="What is AI?",
        documents=docs,
    )

    assert "What is AI?" in prompt
    assert "Artificial Intelligence" in prompt