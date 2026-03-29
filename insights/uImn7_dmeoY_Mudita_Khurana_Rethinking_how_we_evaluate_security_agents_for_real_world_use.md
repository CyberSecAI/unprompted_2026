# Rethinking how we evaluate security agents for real-world use

**Video ID:** uImn7_dmeoY

**YouTube Link:** https://www.youtube.com/watch?v=uImn7_dmeoY

**Transcript:** [View Transcript](../transcripts/uImn7_dmeoY_Mudita%20Khurana%20-%20Rethinking%20how%20we%20evaluate%20security%20agents%20for%20real-world%20use%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Mudita Khurana introduces CLASP, a capability-centric evaluation framework that moves beyond brittle, outcome-only scoring to measure agent explainability and reliability.

## Key Takeaway
Reliable AI security requires moving from outcome-focused benchmarks to capability-centric evaluations that verify an agent's underlying reasoning skills.

# Insights

## Outcome-Only Scoring Failures
- Traditional benchmarks that only measure success rates (e.g., "80%") fail to explain why an agent worked or why it failed.
- High outcome scores do not guarantee that an agent will remain stable or effective when moved to new infrastructure.
- Outcome focused metrics hide underlying brittle skills, making it impossible to systematically improve an agent to hit 95-100% success.

## Shallow vs. Deep Reasoning
- Security agents often achieve "success" through superficial pattern matching rather than deep analysis like taint-flow tracing.
- Finding a bug without understanding exploitability or evidence is a failure of logic that leads to incomplete security patches.
- Security is a continuous workflow; agents that cannot carry context between stages (find -> exploit -> patch) break the end-to-end mission.

## The CLASP Framework
- CLASP (Capability-Centric Evaluation) provides six specific rubrics to measure essential agentic skills like reasoning, memory, and planning.
- The framework prioritizes "how" a result was achieved over the simple binary of "did it find the bug."
- Rubrics distinguish between "brittle" (static, non-responsive) and "adaptive" (feedback-driven, dynamic) agent execution styles.

## Skill Attribution per Task
- Different security roles require different capability sets; for instance, reconnaissance agents require breadth more than reasoning depth.
- Enumerative tasks (recon) are most successful when agents extensively map targets rather than stopping to reason deeply about initial findings.
- Skill attribution allows developers to identify exactly which agent capability needs optimization for a specific functional security role.

## LLM as a Judge
- CLASP can be operationalized using an "LLM as a Judge" pipeline that evaluates agent reasoning traces against the framework's rubrics.
- Providing a judge with the CLASP rubrics enables automated, objective scoring of planning and tool-calling capabilities.
- This feedback loop allows for rapid, iterative refinement of agent prompts and tools without requiring manual human review of every case.

## Evidence-Centered Benchmarking
- High-fidelity evaluation involves building test scenarios of varying complexity based on "evidence-centered benchmark design."
- Tests must measure an agent's ability to adapt its execution plan in response to dynamic environmental feedback.
- Brittle agents statically follow tool orders, while robust agents use retrieved information to intelligently re-plan their next investigation steps.

## Workflow Observability
- Baking deep observability into agent workflows is foundational for capturing the data required for capability-centric evaluation.
- Developers must have access to retrieved contexts, full reasoning traces, and every tool call to score agents accurately.
- Comprehensive observability enables the discovery of "hallucinated reasoning" where an agent gives the right answer for the wrong reasons.

## Principles of Reliable Autonomy
- Capability-centric evaluation transforms agent development from an experimental "vibe check" into a rigorous engineering discipline.
- Consistent, sound reasoning is the only way to build the organizational trust required to deploy autonomous agents in production.
- Building adaptive agents ensures that security automation remains effective even as the underlying technical environment evolves.
