from pathlib import Path
import hashlib


class HashUtils:
    """
    Generates SHA-256 hashes for files.
    """

    @staticmethod
    def sha256(file_path: str | Path) -> str:

        sha = hashlib.sha256()

        with open(file_path, "rb") as file:

            while chunk := file.read(8192):
                sha.update(chunk)

        return sha.hexdigest()