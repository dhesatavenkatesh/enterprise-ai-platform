from backend.rag.hallucination_detector import HallucinationDetector

detector = HallucinationDetector()

answer = "Employees receive annual leave days according to company policy."

context = [
    "Employees receive 20 annual leave days per year.",
    "Leave requests must be approved by managers."
]

sources = [
    {
        "file_name": "company_handbook.txt",
        "page_number": 1,
        "chunk_id": "chunk_1"
    }
]

result = detector.detect(
    answer=answer,
    context=context,
    sources=sources,
    confidence=96
)

print(result)