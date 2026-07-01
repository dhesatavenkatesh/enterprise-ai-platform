class QueryRewriter:
    def __init__(self):
        self.synonyms = {
            "leave": [
                "annual leave",
                "vacation policy",
                "leave entitlement",
                "leave guidelines"
            ],
            "salary": [
                "payroll",
                "compensation",
                "monthly pay",
                "employee salary"
            ],
            "security": [
                "IT security",
                "cybersecurity",
                "password policy",
                "data protection"
            ],
            "benefits": [
                "employee benefits",
                "insurance",
                "bonus",
                "provident fund"
            ]
        }

        self.acronyms = {
            "hr": "human resources",
            "it": "information technology",
            "wfh": "work from home",
            "mfa": "multi-factor authentication",
            "rbac": "role based access control"
        }

    def expand_synonyms(self, query: str):
        expanded_terms = []

        words = query.lower().split()

        for word in words:
            if word in self.synonyms:
                expanded_terms.extend(self.synonyms[word])

        return expanded_terms

    def expand_acronyms(self, query: str):
        expanded_terms = []

        words = query.lower().split()

        for word in words:
            if word in self.acronyms:
                expanded_terms.append(self.acronyms[word])

        return expanded_terms

    def context_aware_rewrite(self, query: str, memory: dict | None = None):
        context_terms = []

        if memory:
            department = memory.get("department")

            if department:
                context_terms.append(f"department: {department}")

            preferences = memory.get("preferences", [])

            if preferences:
                context_terms.extend(preferences)

        return context_terms

    def llm_assisted_rewrite(self, query: str):
        # Placeholder for future LLM-based rewriting
        return [
            f"Detailed enterprise query about {query}",
            f"Company policy related to {query}"
        ]

    def rewrite(self, query: str, memory: dict | None = None):
        rewritten_queries = [query]

        rewritten_queries.extend(self.expand_synonyms(query))
        rewritten_queries.extend(self.expand_acronyms(query))
        rewritten_queries.extend(self.context_aware_rewrite(query, memory))
        rewritten_queries.extend(self.llm_assisted_rewrite(query))

        # Remove duplicates
        rewritten_queries = list(dict.fromkeys(rewritten_queries))

        return {
            "original_query": query,
            "rewritten_queries": rewritten_queries
        }