import json
from pathlib import Path
from datetime import datetime


class Registry:
    """
    Manages the registry of indexed documents.
    """

    def __init__(
        self,
        registry_path: str = "database/indexed_files.json",
    ):

        self.registry_path = Path(registry_path)

        self.registry_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.registry_path.exists():

            self.save({})

    def load(self) -> dict:

        with open(
            self.registry_path,
            "r",
        ) as file:

            return json.load(file)

    def save(
        self,
        registry: dict,
    ) -> None:

        with open(
            self.registry_path,
            "w",
        ) as file:

            json.dump(
                registry,
                file,
                indent=4,
            )

    def exists(
        self,
        file_hash: str,
    ) -> bool:

        registry = self.load()

        return file_hash in registry

    def get(
        self,
        file_hash: str,
    ) -> dict | None:

        registry = self.load()

        return registry.get(file_hash)

    def register(
        self,
        file_hash: str,
        filename: str,
        chunks: int,
        provider: str,
        collection: str,
    ) -> None:

        registry = self.load()

        registry[file_hash] = {

            "filename": filename,

            "indexed_at": datetime.now().isoformat(),

            "chunks": chunks,

            "provider": provider,

            "collection": collection,
        }

        self.save(registry)