from dataclasses import dataclass, field


@dataclass
class Document:

    text: str

    metadata: dict = field(default_factory=dict)
# @dataclass
# class Document:

#     text: str

#     metadata: dict = field(default_factory=dict)

#     embedding: list[float] | None = None