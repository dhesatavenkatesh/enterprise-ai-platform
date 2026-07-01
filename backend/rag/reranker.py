import time
from sentence_transformers import CrossEncoder

from backend.rag.hybrid_search import hybrid_search


class CrossEncoderReranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, results: list, top_k: int = 5):
        start_time = time.time()

        if not results:
            return {
                "query": query,
                "model": self.model_name,
                "reranked_results": [],
                "retrieval_time": 0,
                "total_candidates": 0
            }

        pairs = [
            [query, result["text"]]
            for result in results
        ]

        scores = self.model.predict(pairs)

        reranked = []

        for index, result in enumerate(results):
            item = result.copy()
            item["rerank_score"] = float(scores[index])
            reranked.append(item)

        reranked = sorted(
            reranked,
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        retrieval_time = time.time() - start_time

        return {
            "query": query,
            "model": self.model_name,
            "retrieval_time": round(retrieval_time, 4),
            "total_candidates": len(results),
            "reranked_results": reranked[:top_k]
        }


def run_reranking_pipeline(
    query: str,
    department: str,
    hybrid_top_k: int = 30,
    rerank_top_k: int = 5
):
    hybrid_results = hybrid_search(
        query=query,
        department=department,
        top_k=hybrid_top_k
    )

    candidates = hybrid_results["results"]

    reranker = CrossEncoderReranker()

    return reranker.rerank(
        query=query,
        results=candidates,
        top_k=rerank_top_k
    )