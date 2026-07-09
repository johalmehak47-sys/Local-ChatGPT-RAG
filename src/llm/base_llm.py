"""
Abstract base class for Large Language Model providers.
"""

from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Interface for all LLM providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response for the given prompt.

        Args:
            prompt: Fully formatted prompt.

        Returns:
            Generated response text.
        """
        raise NotImplementedError