from src.retriever import Retriever
import warnings

warnings.filterwarnings(
    "ignore",
    category=FutureWarning
)
retriever = Retriever()

results = retriever.search(
    "Explain deadlock",
    k=3,
)

print(f"Retrieved {len(results)} documents\n")

for i, doc in enumerate(results, start=1):

    print("=" * 60)

    print(f"Result {i}")

    print()

    print(doc.page_content[:300])

    print()

    print(f"Source : {doc.metadata['source']}")
    print(f"Page   : {doc.metadata['page']}")