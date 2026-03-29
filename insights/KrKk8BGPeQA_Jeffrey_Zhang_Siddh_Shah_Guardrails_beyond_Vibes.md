# Guardrails beyond Vibes

**Video ID:** KrKk8BGPeQA

**YouTube Link:** https://www.youtube.com/watch?v=KrKk8BGPeQA

**Transcript:** [View Transcript](../transcripts/KrKk8BGPeQA_Jeffrey%20Zhang%20%26%20Siddh%20Shah%20-%20Guardrails%20beyond%20Vibes%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Jeffrey Zhang and Siddh Shah from Stripe discuss the architecture and production deployment of AI agents for threat modeling and security routing.

## Key Takeaway
Successful production security agents require balancing multi-agent architectures with rigorous, data-driven guardrails to eliminate hallucinations and latency.

# Insights

## Production Security Challenges
- Massive volumes of incoming security review requests often overwhelm the limited capacity of human security engineering teams.
- Correctly routing users to specialized security teams is a significant operational bottleneck that AI can effectively address.
- Automated guidance must be highly accurate to avoid creating additional "re-work" for human engineers and developers.

## The Hallucination Problem
- LLMs frequently hallucinate internal documentation, proprietary terms, and organizational structures, which erodes trust in security automation.
- Incorrect routing or guidance requires manual intervention to correct, which ultimately defeats the purpose of the automation.
- Robust guardrails are required to ensure agents rely exclusively on verified, company-specific information rather than general model knowledge.

## Threat Modeling Architecture
- Stripe's threat modeling system utilizes a modular multi-agent structure consisting of an orchestrator, input agents, and specialized reviewers.
- For high-stakes security analysis, accuracy is prioritized over speed, resulting in an asynchronous, long-running processing model.
- Input agents are dedicated to gathering context from disparate sources like Jira, Slack threads, and internal Google Docs.

## Specialized Security Agents
- Utilizing specialized agents for specific domains (e.g., third-party integrations) significantly improves guidance quality over general-purpose models.
- A mandatory baseline of security questions (e.g., data sensitivity, auth protocols) ensures that every AI-generated review is complete.
- Intentional tool selection provides models with company-specific risk and mitigation contexts that are immediately actionable for developers.

## Sequential Workflow Benefits
- Adopting a sequential agent flow (Input -> Analysis -> Output) ensures predictable behavior and prevents critical steps from being skipped.
- Limiting orchestrator agency prevents the system from making incorrect "shortcuts" that might overlook subtle security requirements.
- Future hybrid models may allow orchestrators to add specialized agents on top of a fixed, mandatory core review baseline.

## Evolution of Security Routing
- Routing initially launched as a fast, one-step LLM call using a simple prompt with pre-loaded team context.
- Simple prompts struggled with internal jargon and proprietary project names, leading to frequent and high-impact hallucinations.
- Transitioning to an agentic structure with self-research capabilities improved accuracy but initially caused unacceptably high latency (10 minutes).

## Performance Optimization
- High-latency security agents create user friction and are unsuitable for conversational or time-sensitive support workflows.
- Toolsets were iteratively pruned to the absolute minimum necessary to maintain accuracy while drastically reducing model run time.
- Performance was optimized by continuously testing the agent against a "ground truth" set of verified baseline questions and answers.

## Evaluation Beyond "Vibes"
- Moving past superficial "vibe-based" assessments to quantifiable accuracy measurements is critical for shipping production-grade security tools.
- Defining objective success criteria allows for reliable monitoring of regressions as models and tools are updated or optimized.
- Meeting users where they are requires a focus on both technical rigor and the practical usability of the AI's output.
