from langchain.text_splitter import RecursiveCharacterTextSplitter

from src.doc import Document


class TextChunker:
    """
    Splits documents into smaller overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:

        chunks = []
        chunk_counter=0
        for document in documents:

            split_texts = self.splitter.split_text(
                document.text
            )

            for text in split_texts:
                chunk_counter +=1 
                chunks.append(
                    Document(
                        text=text,
                        metadata={
                            **document.metadata,
                            "chunk_id": chunk_counter,
                        },
                    )
                )

        return chunks