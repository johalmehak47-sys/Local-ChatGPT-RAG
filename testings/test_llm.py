from src.llm.gemini_client import GeminiClient

client = GeminiClient()

response = client.generate(
    "In one sentence, what is Artificial Intelligence?"
)

print(response)