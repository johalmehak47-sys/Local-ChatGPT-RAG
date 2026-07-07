from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):

    @abstractmethod
    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        pass

    @property
    @abstractmethod
    def embedding_model(self):
        pass