import time
import uuid
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name

        try:
            self.model = SentenceTransformer(
                model_name,
                local_files_only=True
            )
            print("Embedding model loaded from local cache.")

        except Exception as e:
            print("Local model load failed:", e)
            print("Trying to download model from Hugging Face...")

            self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text: str):
        start_time = time.time()

        vector = self.model.encode(text).tolist()

        processing_time = time.time() - start_time

        return {
            "embedding_id": str(uuid.uuid4()),
            "model_used": self.model_name,
            "vector_dimension": len(vector),
            "processing_time": processing_time,
            "vector": vector
        }

    def generate_batch_embeddings(self, chunks: list):
        results = []

        for chunk in chunks:
            embedding = self.generate_embedding(chunk["chunk_text"])

            results.append({
                "chunk_number": chunk["chunk_number"],
                "embedding_id": embedding["embedding_id"],
                "model_used": embedding["model_used"],
                "vector_dimension": embedding["vector_dimension"],
                "processing_time": embedding["processing_time"],
                "vector": embedding["vector"]
            })

        return results