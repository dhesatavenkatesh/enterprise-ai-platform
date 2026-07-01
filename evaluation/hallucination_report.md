# Hallucination Detection Report

## Objective

The hallucination detection engine checks whether the generated answer is supported by retrieved enterprise knowledge.

## Checks Implemented

| Check | Purpose |
|---|---|
| Missing Citations | Ensures every answer has source references |
| Low Retrieval Confidence | Flags answers with weak retrieval confidence |
| Unsupported Claims | Detects answers that do not overlap with retrieved context |
| Fabricated Information | Prevents unsupported enterprise claims |

## Output Format

```json
{
  "hallucination": false,
  "confidence": 97,
  "supported_sources": 5
}