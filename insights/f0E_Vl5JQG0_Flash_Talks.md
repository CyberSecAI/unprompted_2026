# Flash Talks

**Video ID:** f0E_Vl5JQG0

**YouTube Link:** https://www.youtube.com/watch?v=f0E_Vl5JQG0

**Transcript:** [View Transcript](../transcripts/f0E_Vl5JQG0_Flash%20Talks%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
A collection of rapid-fire talks from [un]prompted 2026 featuring experts like Ilia Shumailov and Chris Blanco on AI trust, "gossip" problems, and the future of cryptography.

## Key Takeaway
AI is enabling "trusted private inference" that challenges traditional cryptography while creating uncontrollable data leakage in multiplayer agent workspaces.

# Insights

## The "Doomed" Sentiment
- A recurring theme among AI security leaders is that the industry is fundamentally unprepared for the speed of current capability leaps.
- Despite this "doomed" outlook, practitioners must focus on enabling secure usage rather than futile attempts to disable or block AI.
- Experts emphasize a dual responsibility: innovating at speed while educating non-technical families and friends about impending AI risks.

## Private Inference via Models
- Trusted AI models are introducing a paradigm shift where "private inference" can replace traditional, complex cryptographic message passing.
- In scenarios requiring a trusted third party, a verified, unbiased model can serve as a secure arbitrator for sensitive multi-party computations.
- This model-based trust allows parties to resolve conflicts or analyze shared data without ever exposing the underlying raw information.

## Solving Yao’s Millionaires' Problem
- AI can solve classic cryptographic challenges, such as comparing values without revealing them, through agreed-upon models and prompts.
- By constraining model inputs and outputs to strict schemas, organizations can achieve secure arbitration without traditional encryption overhead.
- This approach is a "killer app" for trusted execution environments where parties require verifiable auditing of opaque or proprietary code.

## The Single-Player vs. Multi-Player Gap
- Most current research focuses on "single-player" problems: securing one agent on one endpoint interacting with one set of resources.
- Modern productivity platforms (e.g., ClickUp) create a "multi-player" environment where dozens of agents with different access levels coexist.
- Security models designed for isolated agents fail when information can flow between agents in a shared, integrated workspace.

## The Agent "Gossip" Problem
- In shared workspaces, information ingested or summarized by one agent is instantly "overheard" and processed by all other active agents.
- This inter-agent communication happens faster than human oversight can monitor, leading to rapid, recursive data leakage across the enterprise.
- One agent's summarized "intent" can become an unauthorized instruction for another agent, bypassing initial entry-point security controls.

## Offensive Acceleration and Verifiers
- AI provides offensive teams with "cheap verifiers"—deterministic signals like popped shells—that allow for near-instant validation of success.
- Defensive teams are conversely drowning in "suspicious information," which lacks the deterministic clarity needed for high-confidence response.
- The imbalance between offensive verification speed and defensive triage complexity is a primary driver of modern cybersecurity risk.

## Engaging the AI Skeptics
- A critical mission for the security community is engaging with AI skeptics who still doubt the reality of current agentic capabilities.
- Skepticism in leadership positions represents a systemic vulnerability, as it delays the implementation of necessary structural guardrails.
- Practitioners are encouraged to use empathy and education to bring skeptics into the fold before they are blindsided by automated attacks.

## From Chatbots to Agentic Layers
- The industry has fully transitioned from the "chatbot era" to a world where AI agents are a foundational layer of every productivity tool.
- Agents now run on top of other platforms, creating complex, multi-layered sets of permissions and data-sharing dependencies.
- This evolution requires a shift from point-in-time security reviews to continuous, architectural monitoring of agentic "intent" and data flow.
