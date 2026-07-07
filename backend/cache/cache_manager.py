import redis
import json
import hashlib
from datetime import timedelta


class CacheManager:
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )

    def generate_key(self, prefix, value):
        hashed_value = hashlib.sha256(str(value).encode()).hexdigest()
        return f"{prefix}:{hashed_value}"

    def set_cache(self, key, value, ttl=300):
        self.redis_client.setex(
            key,
            timedelta(seconds=ttl),
            json.dumps(value)
        )

    def get_cache(self, key):
        data = self.redis_client.get(key)

        if data:
            return json.loads(data)

        return None

    def delete_cache(self, key):
        self.redis_client.delete(key)

    def clear_cache_by_pattern(self, pattern):
        keys = self.redis_client.keys(pattern)

        if keys:
            self.redis_client.delete(*keys)

    # Authentication Sessions
    def cache_auth_session(self, session_id, user_data):
        key = self.generate_key("auth_session", session_id)
        self.set_cache(key, user_data, ttl=3600)

    def get_auth_session(self, session_id):
        key = self.generate_key("auth_session", session_id)
        return self.get_cache(key)

    # User Profiles
    def cache_user_profile(self, user_id, profile_data):
        key = self.generate_key("user_profile", user_id)
        self.set_cache(key, profile_data, ttl=1800)

    def get_user_profile(self, user_id):
        key = self.generate_key("user_profile", user_id)
        return self.get_cache(key)

    # Chat History
    def cache_chat_history(self, chat_id, messages):
        key = self.generate_key("chat_history", chat_id)
        self.set_cache(key, messages, ttl=1800)

    def get_chat_history(self, chat_id):
        key = self.generate_key("chat_history", chat_id)
        return self.get_cache(key)

    # Embeddings
    def cache_embedding(self, text, embedding):
        key = self.generate_key("embedding", text)
        self.set_cache(key, embedding, ttl=86400)

    def get_embedding(self, text):
        key = self.generate_key("embedding", text)
        return self.get_cache(key)

    # RAG Search Results
    def cache_rag_result(self, query, result):
        key = self.generate_key("rag_result", query)
        self.set_cache(key, result, ttl=600)

    def get_rag_result(self, query):
        key = self.generate_key("rag_result", query)
        return self.get_cache(key)

    # Prompt Templates
    def cache_prompt_template(self, template_name, template_data):
        key = self.generate_key("prompt_template", template_name)
        self.set_cache(key, template_data, ttl=86400)

    def get_prompt_template(self, template_name):
        key = self.generate_key("prompt_template", template_name)
        return self.get_cache(key)

    # Frequently Accessed Documents
    def cache_document(self, document_id, document_data):
        key = self.generate_key("document", document_id)
        self.set_cache(key, document_data, ttl=3600)

    def get_document(self, document_id):
        key = self.generate_key("document", document_id)
        return self.get_cache(key)

    # Cache Invalidation
    def invalidate_user_cache(self, user_id):
        self.clear_cache_by_pattern(f"user_profile:*{user_id}*")

    def invalidate_chat_cache(self):
        self.clear_cache_by_pattern("chat_history:*")

    def invalidate_rag_cache(self):
        self.clear_cache_by_pattern("rag_result:*")

    # Cache Warming
    def warm_cache(self):
        print("Warming cache...")

        self.cache_prompt_template(
            "default_chat_prompt",
            {
                "template": "You are a secure enterprise AI assistant.",
                "version": "1.0"
            }
        )

        self.cache_document(
            "hr_policy",
            {
                "title": "HR Leave Policy",
                "content": "Employees are eligible for annual leave."
            }
        )

        print("Cache warming completed.")

    # Benchmark
    def benchmark_cache(self):
        import time

        sample_data = {
            "message": "This is test cache data",
            "user": "admin"
        }

        key = self.generate_key("benchmark", "test")

        start_without_cache = time.time()
        data_without_cache = sample_data
        end_without_cache = time.time()

        self.set_cache(key, sample_data, ttl=300)

        start_with_cache = time.time()
        data_with_cache = self.get_cache(key)
        end_with_cache = time.time()

        print("Without Cache Time:", round((end_without_cache - start_without_cache) * 1000, 4), "ms")
        print("With Cache Time:", round((end_with_cache - start_with_cache) * 1000, 4), "ms")


if __name__ == "__main__":
    cache = CacheManager()

    cache.warm_cache()

    cache.cache_user_profile(
        "user_1",
        {
            "name": "Admin User",
            "role": "Admin",
            "tenant": "Tenant A"
        }
    )

    profile = cache.get_user_profile("user_1")
    print("Cached User Profile:", profile)

    cache.cache_rag_result(
        "What is leave policy?",
        {
            "answer": "Employees can apply leave using HR workflow.",
            "source": "HR Policy Document"
        }
    )

    rag_result = cache.get_rag_result("What is leave policy?")
    print("Cached RAG Result:", rag_result)

    cache.benchmark_cache()