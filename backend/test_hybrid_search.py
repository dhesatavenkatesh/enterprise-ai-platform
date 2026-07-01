from backend.rag.hybrid_search import hybrid_search

result = hybrid_search(
    query="How many annual leave days are allowed?",
    department="hr_docs",
    top_k=5
)

print(result)