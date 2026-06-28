from dataclasses import dataclass


@dataclass
class Document:
    """
    Represents one page (or later, one chunk) of text
    together with its metadata.
    """

    text: str
    page: int
    source: str