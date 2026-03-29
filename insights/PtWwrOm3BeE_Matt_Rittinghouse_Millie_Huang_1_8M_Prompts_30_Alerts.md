# 1.8M Prompts, 30 Alerts

**Video ID:** PtWwrOm3BeE

**YouTube Link:** https://www.youtube.com/watch?v=PtWwrOm3BeE

**Transcript:** [View Transcript](../transcripts/PtWwrOm3BeE_Matt%20Rittinghouse%20%26%20Millie%20Huang%20-%201.8M%20Prompts%2C%2030%20Alerts%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Matt Rittinghouse and Millie Huang from Salesforce describe how they utilized ensemble anomaly detection at the execution layer to reduce 1.8 million prompts to 30 high-fidelity alerts.

## Key Takeaway
Effective AI security requires shifting detection from content moderation to multi-axis anomaly monitoring at the system execution layer.

# Insights

## Beyond the Chatbot Era
- The industry has transitioned from simple conversational chatbots to autonomous agents that act as privileged system executors.
- Modern agents possess the capability to autonomously call APIs, query databases, and execute code on core infrastructure.
- The threat surface has shifted from simple "bad words" detection to preventing unauthorized or malicious system executions and logic abuse.

## Multi-Tenant Defense Scale
- Salesforce monitors over 55,000 organizations with 12,000+ unique daily active agents, each with custom, proprietary business logic.
- Wildly varying agent behaviors make traditional static signatures and manual rule tuning impossible to maintain at scale.
- A "black box" defense approach is mandatory because security teams cannot inspect or train models on sensitive, private customer prompt data.

## Execution vs. Reasoning Layers
- Content moderation (the "Trust Layer") primarily polices the reasoning layer—the dialogue between the user and the LLM.
- While reasoning filters catch toxicity and obvious injection, they cannot observe the actual system calls triggered by the model's output.
- Durable security must reside at the execution layer, monitoring the specific actions and resource invocations performed by the agent.

## Post-Generation Blindness
- A prompt may be deemed "safe" by initial filters, yet still result in an agent plan that performs unauthorized data access.
- Malicious actions like privilege escalation or data exfiltration often occur after the model has finished its text generation.
- High-fidelity signals from the execution layer are required to transition from simple flagging to confident, automated inline blocking.

## Multi-Axis Anomaly Detection
- AI anomaly detection must expand beyond the user level to include the specific context of the agent and the organization.
- Critical axes for monitoring include historical user behavior, agent-specific resource access patterns, and organizational data norms.
- Correlating these multiple streams provides the necessary behavioral context to distinguish between malicious intent and benign custom logic.

## Ensemble Noise Reduction
- Standalone anomaly detection is notoriously noisy and prone to false positives, especially in highly customized environments.
- Ensemble models pair multiple context levels (User + Agent + Org) to filter out noise and surface only the most significant deviations.
- This multi-layered mathematical approach enabled the reduction of 1.8 million daily prompts into just 30 manageable, high-priority alerts.

## Quantifying Agent Intent
- Malicious intent is quantified by monitoring agents for access to resources or tables they do not typically interact with.
- Monitored features include the frequency of access, the specific types of data operations (e.g., SELECT vs. DELETE), and tool usage.
- Hypothesis-driven modeling allow data scientists to build effective security filters around otherwise unpredictable and "custom" agent behaviors.

## Securing the Digital Workforce
- Protecting a digitalized workforce (Agentforce) requires security that evolves at the same speed as the legitimate business logic.
- Defense strategies must work hand-in-hand with model reasoning while strictly adhering to rigorous customer data privacy boundaries.
- The shift to agentic ecosystems necessitates a fundamental rethink of detection engineering, moving from text-matching to system-behavior analysis.
