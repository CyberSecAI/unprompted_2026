# Training BrowseSafe: Lessons from Detecting Prompt Injection

**Video ID:** Fzgqx1MauJg

**YouTube Link:** https://www.youtube.com/watch?v=Fzgqx1MauJg

**Transcript:** [View Transcript](../transcripts/Fzgqx1MauJg_Kyle%20Polley%20-%20Training%20BrowseSafe%EF%BC%9A%20Lessons%20from%20Detecting%20Prompt%20Injection%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Kyle Polley, Security Lead at Perplexity AI, discusses BrowseSafe, a specialized classifier and benchmark for detecting prompt injection in agentic AI systems.

## Key Takeaway
Robust prompt injection defense requires moving beyond keyword heuristics to understanding malicious intent and managing real-world "distractors."

# Insights

## Agentic AI Vulnerabilities
- Agentic tools like AI browsers (Comet) and computers are highly susceptible to both direct and indirect prompt injection.
- Injections occur when agents ingest untrusted content from the web or file systems and treat it as instruction.
- The core problem is the LLM's inherent difficulty in distinguishing between system prompts, user input, and external tool output.

## Taxonomy of Prompt Injection
- Basic attacks include system prompt leak requests and instructions to "ignore all previous instructions" to hijack model behavior.
- Advanced attacks utilize complex context manipulation and social engineering to trick models into performing seemingly benign but malicious actions.
- Multi-language attacks (e.g., using Hebrew or Spanish) can confuse models into bypassing safety filters and following malicious instructions.

## Failures of Existing Benchmarks
- Many open-source benchmarks and models are unrealistic and fail to capture the complexity of actual production-level attacks.
- Existing evaluation frameworks often lack the diversity of attack types and injection vectors encountered in the wild.
- Current detection models frequently rely on simple keyword matching rather than a deep analysis of message intent.

## The Problem of Distractors
- Real-world "distractors," such as cookie consent banners, often trigger false positives in simple prompt injection classifiers.
- Language in cookie banners ("Important", "Accept to proceed") mimics the urgent, instructional tone often used in malicious injections.
- Adding just a few distractors can significantly degrade classifier accuracy, proving that simple heuristics are insufficient for live environments.

## BrowseSafe Bench
- BrowseSafe Bench is a high-fidelity, open-sourced dataset derived from actual prompt injection attempts observed in production.
- The dataset includes a pipeline for deanonymizing and classifying attacks into a detailed, specific taxonomy.
- It is designed to provide a more realistic and challenging evaluation framework than traditional, synthetic open-source benchmarks.

## BrowseSafe Classifier
- BrowseSafe is a specialized classifier purpose-built to detect prompt injection with high precision and low latency in production.
- Unlike keyword-based filters, it focuses on identifying malicious intent within the context of the agent's current task.
- It serves as a critical safety layer for agentic systems that must interact with untrusted or adversarial web content.

## Deployment Lessons
- Deploying safety classifiers in production requires a careful balance between detection thoroughness and system response latency.
- Tailoring the classifier to specific product attack vectors (browser vs. file system) is essential for maintaining high performance.
- Continuous monitoring and data collection are required to stay ahead of attackers who constantly iterate on their injection techniques.

## Guidance for AI Builders
- Developers must treat all external tool outputs as untrusted and potentially adversarial by default.
- Relying on system prompt guardrails alone is insufficient; a dedicated, intent-based safety classifier is a necessary defense layer.
- Evaluating applications against realistic benchmarks like BrowseSafe Bench is the only way to confirm true resistance to prompt injection.
