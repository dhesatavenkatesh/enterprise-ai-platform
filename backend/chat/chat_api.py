from fastapi import APIRouter
from pydantic import BaseModel

from backend.chat.conversation_memory import ConversationMemory
from backend.rag.query_rewriter import QueryRewriter
from backend.rag.reranker import run_reranking_pipeline
from backend.rag.context_builder import ContextBuilder


router = APIRouter(
    prefix="/chat",
    tags=["Enterprise Chat"]
)

memory = ConversationMemory()
rewriter = QueryRewriter()
builder = ContextBuilder()


class ChatRequest(BaseModel):
    session_id: str
    question: str
    department: str


@router.post("/session")
def create_session():
    session_id = memory.create_session()
    return {
        "session_id": session_id,
        "message": "Chat session created"
    }


@router.post("/")
def enterprise_chat(request: ChatRequest):
    memory_data = memory.get_memory(request.session_id)

    if memory_data is None:
        return {
            "error": "Session not found. Create session first using /chat/session"
        }

    preferences = memory_data.get("preferences", {})

    rewritten = rewriter.rewrite(
        request.question,
        preferences
    )

    reranked = run_reranking_pipeline(
        query=rewritten["rewritten_queries"][0],
        department=request.department
    )

    chunks = []

    for item in reranked["reranked_results"]:
        chunks.append({
            "chunk_id": item["chunk_id"],
            "text": item["text"],
            "metadata": item["metadata"]
        })

    context = builder.build_context(chunks)

    answer = (
        "This is a simulated enterprise response generated "
        "from the retrieved knowledge base context."
    )

    memory.add_message(
        request.session_id,
        request.question,
        answer
    )

    return {
        "answer": answer,
        "sources": context["sources"],
        "confidence": 96
    }


@router.get("/session/{session_id}")
def get_session(session_id: str):
    return memory.get_memory(session_id)


@router.post("/history")
def get_history(session_id: str):
    return memory.get_memory(session_id)


@router.delete("/history")
def delete_history(session_id: str):
    return memory.clear_session(session_id)