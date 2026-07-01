from backend.rag.reranker import run_reranking_pipeline

result = run_reranking_pipeline(
    query="How many annual leave days are allowed?",
    department="hr_docs",
    hybrid_top_k=30,
    rerank_top_k=5
)

print(result)