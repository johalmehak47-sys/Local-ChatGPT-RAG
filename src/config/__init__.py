"""
Application configuration.
"""

from .settings import (
    BATCH_SIZE,
    EMBEDDING_PROVIDER,
    GEMINI_API_KEY,
    GEMINI_MODEL,
    LOCAL_EMBEDDING_MODEL,
)

__all__ = [
    "BATCH_SIZE",
    "EMBEDDING_PROVIDER",
    "GEMINI_API_KEY",
    "GEMINI_MODEL",
    "LOCAL_EMBEDDING_MODEL",
]