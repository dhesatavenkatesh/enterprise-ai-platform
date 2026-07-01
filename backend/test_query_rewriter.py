from backend.rag.query_rewriter import QueryRewriter

rewriter = QueryRewriter()

memory = {
    "department": "HR",
    "preferences": ["approved documents only"]
}

result = rewriter.rewrite(
    query="leave policy",
    memory=memory
)

print(result)