# from langchain_chroma import Chroma

# from src.embeddings.factory import EmbeddingFactory

# embedder = EmbeddingFactory.create()

# db = Chroma(
#     collection_name="knowledge_base",
#     embedding_function=embedder.embedding_model,
#     persist_directory="database/chroma_db",
# )

# print(db._collection.count())
from src.retriever import Retriever
from src.prompts.prompt_builder import PromptBuilder
from src.llm.gemini_client import GeminiClient
import warnings

warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
)

retriever = Retriever()

prompt_builder = PromptBuilder()

llm = GeminiClient()

question = input("Ask a question: ")

documents = retriever.search(question)


print("\nRetrieved Documents:\n")

for i, doc in enumerate(documents, start=1):
    print(f"----- Document {i} -----")
    print(doc.page_content[:300])
    print()
prompt = prompt_builder.build(
    question=question,
    documents=documents,
)

answer = llm.generate(prompt)

print("\nAnswer:\n")
print(answer)