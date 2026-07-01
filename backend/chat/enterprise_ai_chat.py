from fastapi import APIRouter
from pydantic import BaseModel

from backend.chat.conversation_memory import ConversationMemory
from backend.rag.query_rewriter import QueryRewriter
from backend.rag.reranker import run_reranking_pipeline
from backend.rag.context_builder import ContextBuilder
from backend.rag.hallucination_detector import HallucinationDetector

router = APIRouter(
    prefix="/enterprise-chat",
    tags=["BlackRoth Enterprise AI Chat"]
)

memory = ConversationMemory()
rewriter = QueryRewriter()
context_builder = ContextBuilder()
hallucination_detector = HallucinationDetector()

feedback_store = []
analytics_store = {
    "total_queries": 0,
    "average_confidence": 0,
    "hallucination_count": 0,
    "estimated_cost": 0.0
}


class EnterpriseChatRequest(BaseModel):
    session_id: str
    question: str
    department: str


class FeedbackRequest(BaseModel):
    session_id: str
    rating: int
    comment: str


@router.post("/session")
def create_enterprise_session():
    session_id = memory.create_session()
    return {
        "session_id": session_id,
        "message": "BlackRoth Enterprise AI Chat session created"
    }


@router.post("/")
def enterprise_chat(request: EnterpriseChatRequest):
    session = memory.get_memory(request.session_id)

    if session is None:
        return {
            "error": "Invalid session. Create session first."
        }

    rewritten = rewriter.rewrite(
        request.question,
        session.get("preferences", {})
    )

    reranked = run_reranking_pipeline(
        query=rewritten["rewritten_queries"][0],
        department=request.department,
        hybrid_top_k=30,
        rerank_top_k=5
    )

    chunks = []

    for item in reranked["reranked_results"]:
        chunks.append({
            "chunk_id": item["chunk_id"],
            "text": item["text"],
            "metadata": item["metadata"]
        })

    context = context_builder.build_context(chunks)

    answer = (
        "Based on the retrieved enterprise knowledge, "
        "the relevant policy information has been found. "
        "Please refer to the cited sources for verification."
    )

    confidence = 96 if len(context["sources"]) > 0 else 50

    hallucination_result = hallucination_detector.detect(
        answer=answer,
        context=context["context"],
        sources=context["sources"],
        confidence=confidence
    )

    memory.add_message(
        request.session_id,
        request.question,
        answer
    )

    analytics_store["total_queries"] += 1
    analytics_store["estimated_cost"] += 0.002

    if hallucination_result["hallucination"]:
        analytics_store["hallucination_count"] += 1

    analytics_store["average_confidence"] = confidence

    return {
        "answer": answer,
        "rewritten_queries": rewritten["rewritten_queries"],
        "sources": context["sources"],
        "confidence": hallucination_result["confidence"],
        "hallucination": hallucination_result,
        "retrieval_metrics": {
            "retrieval_time": reranked["retrieval_time"],
            "total_candidates": reranked["total_candidates"]
        },
        "cost": {
            "estimated_request_cost": 0.002
        }
    }


@router.get("/session/{session_id}")
def get_enterprise_session(session_id: str):
    return memory.get_memory(session_id)


@router.post("/feedback")
def submit_feedback(feedback: FeedbackRequest):
    feedback_store.append(feedback.dict())

    return {
        "message": "Feedback submitted successfully",
        "feedback": feedback
    }


@router.get("/analytics")
def get_analytics():
    return {
        "feedback": feedback_store,
        "analytics": analytics_store,
        "response_quality": {
            "hallucination_rate": analytics_store["hallucination_count"],
            "quality_status": "Good"
        },
        "cost_tracking": {
            "estimated_total_cost": analytics_store["estimated_cost"]
        }
    }