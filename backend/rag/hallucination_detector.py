class HallucinationDetector:

    def __init__(self, confidence_threshold: int = 70):
        self.confidence_threshold = confidence_threshold

    def check_missing_citations(self, sources: list):
        return len(sources) == 0

    def check_low_confidence(self, confidence: int):
        return confidence < self.confidence_threshold

    def check_unsupported_claims(self, answer: str, context: list):
        if not context:
            return True

        answer_words = set(answer.lower().split())

        context_text = " ".join(context).lower()
        context_words = set(context_text.split())

        overlap = answer_words.intersection(context_words)

        return len(overlap) < 3

    def detect(self, answer: str, context: list, sources: list, confidence: int):
        missing_citations = self.check_missing_citations(sources)
        low_confidence = self.check_low_confidence(confidence)
        unsupported_claims = self.check_unsupported_claims(answer, context)

        hallucination = (
            missing_citations
            or low_confidence
            or unsupported_claims
        )

        supported_sources = len(sources)

        final_confidence = confidence

        if hallucination:
            final_confidence = min(confidence, 60)

        return {
            "hallucination": hallucination,
            "confidence": final_confidence,
            "supported_sources": supported_sources,
            "checks": {
                "missing_citations": missing_citations,
                "low_retrieval_confidence": low_confidence,
                "unsupported_claims": unsupported_claims
            }
        }