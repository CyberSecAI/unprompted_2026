# Source to Sink: Improving LLM Vuln Discovery

**Video ID:** bxwEZMhqeR0

**YouTube Link:** https://www.youtube.com/watch?v=bxwEZMhqeR0

**Transcript:** [View Transcript](../transcripts/bxwEZMhqeR0_Scott%20Behrens%20%26%20Justice%20Cassel%20-%20Source%20to%20Sink%EF%BC%9A%20Improving%20LLM%20Vuln%20Discovery%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Scott Behrens and Justice Cassel discuss the transition from simple prompting to complex orchestration frameworks for first-party vulnerability discovery using LLMs.

## Key Takeaway
Reliable vulnerability discovery requires moving beyond shallow pattern matching to data-driven orchestration and rigorous, context-aware benchmarking.

# Insights

## The Hype and Reality Gap
- Initial research began with "simple prompting" and high expectations that LLMs would solve all vulnerability discovery hurdles.
- Early successes in finding SSRF and unsafe serialization felt "magical," but consistency and high variance remained persistent blockers.
- Simple, "brick of text" analysis frequently ignores entire vulnerability classes and generates an unmanageable volume of false positives.

## Architectural Evolution
- Security tooling has evolved from basic input/output loops to sophisticated orchestration frameworks with state and file tracking.
- Shifting to IDE-agnostic architectures via MCP allows for better context injection across diverse development environments.
- Modern frameworks integrate deep tracing and state management to provide more reliable and reproducible security signals to researchers.

## The Economic Cost of Coverage
- Achieving full, comprehensive coverage across an entire enterprise codebase is feasible but requires a significant financial investment.
- Organizations must make strategic architectural trade-offs to balance deep analysis with the realities of LLM API token costs.
- Efficient systems use pre-filtering to ensure expensive reasoning models only process the most security-relevant code segments.

## Deep vs. Shallow Analysis
- Relying on shallow heuristics leads to "directionally useful" but often misleading findings that miss subtle exploit chains.
- Effective agents must be capable of tracing complex taint flows and verifying exploitability rather than just pattern matching.
- Success is measured by an agent's ability to check for downstream sanitization and explain its reasoning with concrete citations.

## Overcoming Model Instability
- Security researchers often experience frustration when models fluctuate between "genius" and "terrible" results after minor prompt adjustments.
- Adding a single tool or changing a line of instruction can drastically alter an agent's efficacy across different runs.
- Durable production systems require continuous, automated metrics gathering to identify and mitigate performance regressions in real-time.

## Contextual Prioritization
- The goal of automated discovery is to enable security teams to "review less more" by focusing on high-risk outliers.
- Contextual prioritization prevents noise by understanding that legitimate logic (e.g., database management) is not a vulnerability.
- Automated systems must be trained to recognize organizational "anti-patterns" to avoid falling into common triage "pits."

## Benchmarking for Repeatability
- Evaluation frameworks must include a "set list" of both verified vulnerabilities and known pitfalls like dead code.
- Repeatability and determinism are the gold standards for move-to-production security agents in first-party discovery.
- Organizations should run thousands of test iterations to ensure that agent success is a result of skill rather than lucky guessing.

## Empowering the Human Reviewer
- AI should function as a speed multiplier for human experts by producing structured summaries and evidence-backed citations.
- Bounded AI conclusions prevent models from inventing facts, ensuring that human time is spent only on verified findings.
- The ultimate role of AI in discovery is to handle the repetitive "bookkeeping" steps, leaving high-level reasoning to the human.
