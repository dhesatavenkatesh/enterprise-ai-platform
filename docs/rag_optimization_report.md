# RAG Performance Optimization Report

## Sprint 7 – Performance Optimization

## Optimization Parameters Tested

- Chunk Size
- Chunk Overlap
- Embedding Models
- Top-K Retrieval
- Hybrid Search Weights
- Re-ranking Thresholds

## Top Benchmark Results

| Rank | Chunk Size | Overlap | Model | Top-K | Hybrid Weight | Rerank Threshold | Accuracy | Latency | Tokens | Cost |
|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 800 | 150 | base | 3 | 0.5 | 0.85 | 0.98 | 398.0 ms | 1800 | $0.0036 |
| 2 | 1000 | 150 | base | 3 | 0.5 | 0.75 | 0.98 | 400.0 ms | 2250 | $0.0045 |
| 3 | 800 | 100 | base | 3 | 0.5 | 0.85 | 0.98 | 403.0 ms | 1800 | $0.0036 |
| 4 | 1000 | 100 | base | 3 | 0.5 | 0.75 | 0.98 | 407.0 ms | 2250 | $0.0045 |
| 5 | 1000 | 100 | base | 3 | 0.7 | 0.85 | 0.98 | 407.0 ms | 2250 | $0.0045 |
| 6 | 1000 | 150 | base | 3 | 0.7 | 0.85 | 0.98 | 407.0 ms | 2250 | $0.0045 |
| 7 | 800 | 150 | base | 3 | 0.7 | 0.85 | 0.98 | 410.0 ms | 1800 | $0.0036 |
| 8 | 800 | 100 | base | 3 | 0.7 | 0.85 | 0.98 | 415.0 ms | 1800 | $0.0036 |
| 9 | 1000 | 150 | base | 3 | 0.7 | 0.75 | 0.98 | 421.0 ms | 2250 | $0.0045 |
| 10 | 1000 | 100 | base | 3 | 0.5 | 0.85 | 0.98 | 427.0 ms | 2250 | $0.0045 |

## Best Configuration

- **Chunk Size:** 800
- **Chunk Overlap:** 150
- **Embedding Model:** base
- **Top-K Retrieval:** 3
- **Hybrid Search Weight:** 0.5
- **Re-ranking Threshold:** 0.85
- **Retrieval Accuracy:** 0.98
- **Latency:** 398.0 ms
- **Token Consumption:** 1800
- **Cost:** $0.0036

## Recommendations

- Use chunk size between 800 and 1000 for enterprise documents.
- Use chunk overlap between 100 and 150 for better context retention.
- Use base embedding model for balanced cost and latency.
- Use large embedding model only for critical knowledge bases.
- Use Top-K 5 for normal queries and Top-K 8 for complex queries.
- Use hybrid search weight 0.5 for balanced semantic and keyword search.
- Use reranking threshold 0.75 to remove weak results.
