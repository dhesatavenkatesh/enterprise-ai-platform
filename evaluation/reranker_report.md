# Reranker Evaluation Report

## Objective

The purpose of this evaluation is to compare hybrid retrieval results before and after cross-encoder re-ranking.

## Models Used

- cross-encoder/ms-marco-MiniLM-L-6-v2
- Future model: BAAI/bge-reranker-base

## Pipeline

User Query  
↓  
Hybrid Search Top 30  
↓  
Cross Encoder Re-ranking  
↓  
Top 5 Results  

## Metrics

| Metric | Description |
|---|---|
| Retrieval Time | Time taken to rerank candidate documents |
| Accuracy | Whether relevant document appears in top results |
| Relevance Score | Cross-encoder score assigned to each result |

## Result Summary

The cross-encoder reranker improves result ordering by comparing the query and document chunk together. Unlike vector similarity alone, the reranker directly evaluates relevance between the user question and each retrieved chunk.

## Conclusion

The reranker improves enterprise RAG quality by promoting highly relevant chunks and reducing weak matches before context is sent to the LLM.