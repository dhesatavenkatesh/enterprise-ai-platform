import os
from datetime import datetime


class CostOptimizer:

    def __init__(self):
        self.input_token_cost = 0.000002
        self.output_token_cost = 0.000006
        self.embedding_token_cost = 0.0000001
        self.agent_call_cost = 0.001

    def calculate_current_cost(
        self,
        monthly_requests,
        avg_prompt_tokens,
        avg_output_tokens,
        avg_embedding_tokens,
        avg_agent_calls
    ):
        prompt_cost = monthly_requests * avg_prompt_tokens * self.input_token_cost
        output_cost = monthly_requests * avg_output_tokens * self.output_token_cost
        embedding_cost = monthly_requests * avg_embedding_tokens * self.embedding_token_cost
        agent_cost = monthly_requests * avg_agent_calls * self.agent_call_cost

        return prompt_cost + output_cost + embedding_cost + agent_cost

    def calculate_optimized_cost(
        self,
        monthly_requests,
        avg_prompt_tokens,
        avg_output_tokens,
        avg_embedding_tokens,
        avg_agent_calls
    ):
        optimized_prompt_tokens = avg_prompt_tokens * 0.65
        optimized_output_tokens = avg_output_tokens * 0.80
        optimized_embedding_tokens = avg_embedding_tokens * 0.50
        optimized_agent_calls = avg_agent_calls * 0.60

        return self.calculate_current_cost(
            monthly_requests,
            optimized_prompt_tokens,
            optimized_output_tokens,
            optimized_embedding_tokens,
            optimized_agent_calls
        )

    def generate_report(self):
        os.makedirs("docs", exist_ok=True)

        monthly_requests = 1000000
        avg_prompt_tokens = 1200
        avg_output_tokens = 500
        avg_embedding_tokens = 800
        avg_agent_calls = 2

        current_cost = self.calculate_current_cost(
            monthly_requests,
            avg_prompt_tokens,
            avg_output_tokens,
            avg_embedding_tokens,
            avg_agent_calls
        )

        optimized_cost = self.calculate_optimized_cost(
            monthly_requests,
            avg_prompt_tokens,
            avg_output_tokens,
            avg_embedding_tokens,
            avg_agent_calls
        )

        savings = current_cost - optimized_cost
        savings_percentage = (savings / current_cost) * 100

        report_path = "docs/cost_optimization_report.md"

        with open(report_path, "w", encoding="utf-8") as file:
            file.write("# Cost Optimization Report\n\n")
            file.write("## Sprint 7 – Performance Optimization\n\n")

            file.write("## Cost Areas Optimized\n\n")
            file.write("- Prompt Length\n")
            file.write("- Token Usage\n")
            file.write("- Embedding Generation\n")
            file.write("- Vector Search\n")
            file.write("- Agent Calls\n")
            file.write("- API Requests\n\n")

            file.write("## Current Cost Assumptions\n\n")
            file.write(f"- Monthly Requests: {monthly_requests}\n")
            file.write(f"- Average Prompt Tokens: {avg_prompt_tokens}\n")
            file.write(f"- Average Output Tokens: {avg_output_tokens}\n")
            file.write(f"- Average Embedding Tokens: {avg_embedding_tokens}\n")
            file.write(f"- Average Agent Calls: {avg_agent_calls}\n\n")

            file.write("## Cost Comparison\n\n")
            file.write("| Metric | Current | Optimized |\n")
            file.write("|---|---:|---:|\n")
            file.write(f"| Monthly Requests | {monthly_requests} | {monthly_requests} |\n")
            file.write(f"| Prompt Tokens | {avg_prompt_tokens} | {int(avg_prompt_tokens * 0.65)} |\n")
            file.write(f"| Output Tokens | {avg_output_tokens} | {int(avg_output_tokens * 0.80)} |\n")
            file.write(f"| Embedding Tokens | {avg_embedding_tokens} | {int(avg_embedding_tokens * 0.50)} |\n")
            file.write(f"| Agent Calls | {avg_agent_calls} | {round(avg_agent_calls * 0.60, 2)} |\n")
            file.write(f"| Estimated Cost | ${round(current_cost, 2)} | ${round(optimized_cost, 2)} |\n")
            file.write(f"| Estimated Monthly Savings | - | ${round(savings, 2)} |\n")
            file.write(f"| Savings Percentage | - | {round(savings_percentage, 2)}% |\n\n")

            file.write("## Optimization Techniques\n\n")
            file.write("### 1. Prompt Length Optimization\n")
            file.write("- Remove repeated system instructions.\n")
            file.write("- Use short reusable prompt templates.\n")
            file.write("- Send only required context to the model.\n\n")

            file.write("### 2. Token Usage Optimization\n")
            file.write("- Apply max token limits.\n")
            file.write("- Compress long chat history.\n")
            file.write("- Summarize previous conversations before sending to LLM.\n\n")

            file.write("### 3. Embedding Generation Optimization\n")
            file.write("- Cache embeddings using text hash.\n")
            file.write("- Avoid duplicate document embedding.\n")
            file.write("- Batch embedding requests.\n\n")

            file.write("### 4. Vector Search Optimization\n")
            file.write("- Use dynamic Top-K retrieval.\n")
            file.write("- Use metadata filtering by tenant.\n")
            file.write("- Avoid large context retrieval for simple questions.\n\n")

            file.write("### 5. Agent Call Optimization\n")
            file.write("- Use rule-based logic before calling agents.\n")
            file.write("- Avoid calling multiple agents for simple tasks.\n")
            file.write("- Cache agent results for repeated workflows.\n\n")

            file.write("### 6. API Request Optimization\n")
            file.write("- Add rate limiting.\n")
            file.write("- Use Redis caching.\n")
            file.write("- Avoid repeated external API calls.\n\n")

            file.write("## Final Recommendation\n\n")
            file.write("Use tenant-level cost budgets, token monitoring, Redis caching, and nightly cost reports to keep infrastructure and AI usage costs optimized.\n")

        print(f"Report generated: {report_path}")


if __name__ == "__main__":
    optimizer = CostOptimizer()
    optimizer.generate_report()