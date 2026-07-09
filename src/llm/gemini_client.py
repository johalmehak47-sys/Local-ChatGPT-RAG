"""
Gemini implementation of the BaseLLM interface.
"""

import time

from google import genai
from google.genai import errors

from src.config import GEMINI_API_KEY, GEMINI_MODEL
from src.llm.base_llm import BaseLLM


class GeminiClient(BaseLLM):
    """
    Gemini implementation of BaseLLM.

    Features
    --------
    - Automatic retries
    - Exponential backoff
    - Cleaner error messages
    """

    def __init__(
        self,
        api_key: str = GEMINI_API_KEY,
        model_name: str = GEMINI_MODEL,
        max_retries: int = 5,
    ):

        self.client = genai.Client(
            api_key=api_key,
        )

        self.model_name = model_name
        self.max_retries = max_retries

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from Gemini.

        Automatically retries temporary failures
        such as 503 (high demand) and 429
        (rate limiting).
        """

        for attempt in range(1, self.max_retries + 1):

            try:

                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                )

                return response.text

            except (
                errors.ServerError,
                errors.ClientError,
            ) as error:

                if attempt == self.max_retries:
                    raise RuntimeError(
                        f"Gemini request failed after "
                        f"{self.max_retries} attempts."
                    ) from error

                wait_time = 2 ** (attempt - 1)

                print(
                    f"\nGemini temporarily unavailable "
                    f"(Attempt {attempt}/{self.max_retries})."
                )

                print(
                    f"Retrying in {wait_time} seconds...\n"
                )

                time.sleep(wait_time)

            except Exception as error:

                raise RuntimeError(
                    f"Unexpected Gemini error: {error}"
                ) from error