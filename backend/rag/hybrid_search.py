from rank_bm25 import BM25Okapi

from backend.rag.embedding_service import EmbeddingService
from backend.rag.vector_store import search_documents


SEMANTIC_WEIGHT = 0.65
KEYWORD_WEIGHT = 0.35

embedding_service = EmbeddingService()


# Temporary keyword corpus
# Later this can come from PostgreSQL or ChromaDB
DOCUMENT_CORPUS = [
    {
        "chunk_id": "chunk_1",
        "text": "Employees are entitled to 20 annual leave days per year.",
        "department": "hr_docs",
        "metadata": {
            "file_name": "company_handbook.txt",
            "department": "HR",
            "status": "Approved"
        }
    },
    {
        "chunk_id": "chunk_2",
        "text": "Leave requests must be submitted through the Enterprise AI Platform.",
        "department": "hr_docs",
        "metadata": {
            "file_name": "company_handbook.txt",
            "department": "HR",
            "status": "Approved"
        }
    },
    {
        "chunk_id": "chunk_3",
        "text": "Payroll is processed at the end of every month.",
        "department": "payroll_docs",
        "metadata": {
            "file_name": "payroll_policy.txt",
            "department": "Payroll",
            "status": "Approved"
        }
    }
]


def tokenize(text: str):
    return text.lower().split()


def keyword_search(query: str, department: str, top_k: int = 5):
    filtered_docs = [
        doc for doc in DOCUMENT_CORPUS
        if doc["department"] == department
    ]

    if not filtered_docs:
        return []

    tokenized_corpus = [
        tokenize(doc["text"])
        for doc in filtered_docs
    ]

    bm25 = BM25Okapi(tokenized_corpus)

    query_tokens = tokenize(query)

    scores = bm25.get_scores(query_tokens)

    results = []

    for index, score in enumerate(scores):
        results.append({
            "chunk_id": filtered_docs[index]["chunk_id"],
            "text": filtered_docs[index]["text"],
            "keyword_score": float(score),
            "metadata": filtered_docs[index]["metadata"]
        })

    results = sorted(
        results,
        key=lambda x: x["keyword_score"],
        reverse=True
    )

    return results[:top_k]


def semantic_search(query: str, department: str, top_k: int = 5, metadata_filter=None):
    query_embedding = embedding_service.generate_embedding(query)

    results = search_documents(
        department=department,
        query_embedding=query_embedding["vector"],
        top_k=top_k,
        metadata_filter=metadata_filter
    )

    semantic_results = []

    docs = results.get("documents", [[]])[0]
    ids = results.get("ids", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for i, doc in enumerate(docs):
        distance = distances[i]

        # Chroma returns distance. Lower distance is better.
        semantic_score = 1 / (1 + distance)

        semantic_results.append({
            "chunk_id": ids[i],
            "text": doc,
            "semantic_score": semantic_score,
            "metadata": metadatas[i]
        })

    return semantic_results


def calculate_hybrid_score(semantic_score: float, keyword_score: float):
    return (
        SEMANTIC_WEIGHT * semantic_score
        +
        KEYWORD_WEIGHT * keyword_score
    )


def hybrid_search(
    query: str,
    department: str,
    top_k: int = 5,
    semantic_weight: float = SEMANTIC_WEIGHT,
    keyword_weight: float = KEYWORD_WEIGHT,
    metadata_filter=None
):
    semantic_results = semantic_search(
        query=query,
        department=department,
        top_k=top_k,
        metadata_filter=metadata_filter
    )

    keyword_results = keyword_search(
        query=query,
        department=department,
        top_k=top_k
    )

    combined = {}

    for result in semantic_results:
        chunk_id = result["chunk_id"]

        combined[chunk_id] = {
            "chunk_id": chunk_id,
            "text": result["text"],
            "semantic_score": result["semantic_score"],
            "keyword_score": 0,
            "metadata": result["metadata"]
        }

    for result in keyword_results:
        chunk_id = result["chunk_id"]

        if chunk_id not in combined:
            combined[chunk_id] = {
                "chunk_id": chunk_id,
                "text": result["text"],
                "semantic_score": 0,
                "keyword_score": result["keyword_score"],
                "metadata": result["metadata"]
            }
        else:
            combined[chunk_id]["keyword_score"] = result["keyword_score"]

    final_results = []

    for item in combined.values():
        hybrid_score = (
            semantic_weight * item["semantic_score"]
            +
            keyword_weight * item["keyword_score"]
        )

        item["hybrid_score"] = hybrid_score
        final_results.append(item)

    final_results = sorted(
        final_results,
        key=lambda x: x["hybrid_score"],
        reverse=True
    )

    return {
        "query": query,
        "department": department,
        "semantic_weight": semantic_weight,
        "keyword_weight": keyword_weight,
        "results": final_results[:top_k]
    }