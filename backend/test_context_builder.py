from backend.rag.context_builder import ContextBuilder

builder = ContextBuilder()

chunks = [
    {
        "chunk_id": "chunk_1",
        "text": "Employees receive 20 annual leave days.",
        "metadata": {
            "file_name": "company_handbook.txt",
            "department": "HR"
        }
    },
    {
        "chunk_id": "chunk_2",
        "text": "Leave requests must be approved by managers.",
        "metadata": {
            "file_name": "company_handbook.txt",
            "department": "HR"
        }
    },
    {
        "chunk_id": "chunk_1",
        "text": "Employees receive 20 annual leave days.",
        "metadata": {
            "file_name": "company_handbook.txt",
            "department": "HR"
        }
    }
]

result = builder.build_context(chunks)

print(result)