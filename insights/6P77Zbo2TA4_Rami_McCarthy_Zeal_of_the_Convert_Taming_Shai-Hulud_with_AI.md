# Rami McCarthy - Zeal of the Convert： Taming Shai-Hulud with AI

**Video ID:** 6P77Zbo2TA4

**YouTube Link:** https://www.youtube.com/watch?v=6P77Zbo2TA4

**Transcript:** [View Transcript](../transcripts/6P77Zbo2TA4_Rami%20McCarthy%20-%20Zeal%20of%20the%20Convert%EF%BC%9A%20Taming%20Shai-Hulud%20with%20AI%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Rami McCarthy, security researcher at Wiz, discusses analyzing npm supply chain attacks using AI to process leaked data and attribute victims.

## Key Takeaway
AI excels at signal extraction but requires thoughtful harnesses, feedback loops, and skepticism for security work.

# Insights

## AI Code Generation Workflows
- Use RPI loops: Research, Plan, Implementation rather than jumping directly to code generation for better results.
- Plan mode in tools prevents premature implementation and encourages structured thinking before coding begins.
- Building composable utilities and skills compounds your investment as you reuse patterns across projects.

## Data Architecture and AI Limitations
- AI won't question your data abstractions; flat files remain flat unless you redesign storage approaches.
- Flat files work for small datasets but linear scanning becomes IO-bound at scale eventually.
- Transition to indexed databases when query patterns justify infrastructure investment beyond simple bash operations.

## Signal Extraction and Pattern Recognition
- AI excels at identifying metadata patterns like environment variables signifying obscure CI/CD platforms unknown.
- Use AI to generate deterministic scripts encoding patterns rather than repeatedly analyzing raw data.
- Fingerprinting and deduplication via AI dramatically reduces false victim counts in incident response scenarios.

## Feedback Loops for Continuous Improvement
- Sample analysis with AI, codify findings into deterministic rules, then measure coverage uplift systematically.
- Distill AI learnings into concrete detection rules that enable consistent, repeatable, and testable outcomes.
- This human-AI loop scales better than purely manual or purely automated approaches alone.

## Reasoning Models and Creativity
- Large context reasoning models process unformatted bulk data extracting high-signal samples like Fortune companies.
- Models creatively decode JWTs for claims and identify encoded patterns humans might overlook completely.
- Credulity is the downside: models make false connections from weak signals without built-in skepticism.

## Security Tool Fungibility
- Product rules and detectors are becoming fungible; engine characteristics matter more than rule libraries now.
- AI can port 800 TruffleHog detectors to custom engines in 30 minutes changing tool selection.
- Choose engines based on speed, false positive rates, and operational characteristics rather than ruleset size.

## Coverage and Harness Design
- AI takes shortcuts and samples unless harnesses enforce complete coverage with explicit exit criteria loops.
- RALF loops (research, analyze, loop, finalize) prevent models from stopping at convenient top-10 lists.
- Harness design determines behavior; models won't achieve exhaustiveness without being forced to continue iterations.

## Just-In-Time Human-AI Collaboration
- Build throwaway tools for one-time analysis rather than manually reviewing data when patterns emerge.
- Humans identify novel signals AI misses, then feed discoveries to models for systematic implementation.
- Six-stage enrichment pipelines emerge from simple human insights combined with AI's implementation speed effectively.
