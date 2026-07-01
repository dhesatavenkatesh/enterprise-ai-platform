from typing import List


class ContextBuilder:

    def __init__(self, max_tokens: int = 1800):
        self.max_tokens = max_tokens

    def estimate_tokens(self, text: str):
        """
        Rough token estimation.
        Approx: 1 token ≈ 0.75 words
        """
        words = len(text.split())
        return int(words / 0.75)

    def remove_duplicates(self, chunks: List[dict]):
        unique = []
        seen = set()

        for chunk in chunks:
            text = chunk["text"]

            if text not in seen:
                seen.add(text)
                unique.append(chunk)

        return unique

    def build_context(self, retrieved_chunks: List[dict]):

        retrieved_chunks = self.remove_duplicates(retrieved_chunks)

        context = []
        sources = []

        total_tokens = 0

        for chunk in retrieved_chunks:

            token_count = self.estimate_tokens(
                chunk["text"]
            )

            if total_tokens + token_count > self.max_tokens:
                break

            context.append(chunk["text"])

            sources.append({
                "file_name": chunk["metadata"].get("file_name"),
                "department": chunk["metadata"].get("department"),
                "chunk_id": chunk["chunk_id"]
            })

            total_tokens += token_count

        return {
            "context": context,
            "sources": sources,
            "token_count": total_tokens
        }