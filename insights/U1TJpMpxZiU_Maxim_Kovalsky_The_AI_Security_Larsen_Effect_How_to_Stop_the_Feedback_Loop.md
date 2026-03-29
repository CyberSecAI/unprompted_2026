# The AI Security Larsen Effect: How to Stop the Feedback Loop

**Video ID:** U1TJpMpxZiU

**YouTube Link:** https://www.youtube.com/watch?v=U1TJpMpxZiU

**Transcript:** [View Transcript](../transcripts/U1TJpMpxZiU_Maxim%20Kovalsky%20-%20The%20AI%20Security%20Larsen%20Effect%EF%BC%9A%20How%20to%20Stop%20the%20Feedback%20Loop%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Maxim Kovalsky from Consortium explains how he uses an agentic AI loop to systematically validate security vendor claims and automate organizational "matchmaking."

## Key Takeaway
Automating vendor assessment via AI reasoning allows organizations to cut through marketing hyperbole and find evidence-based security solutions.

# Insights

## Matchmaking in a Stormy Era
- Effective matchmaking requires moving past the "who's good" question to deep analysis of use cases and specific risk appetites.
- Organizations must distinguish between the technical fear of an incident and the regulatory fear of an SEC filing.
- A Value-Added Reseller (VAR) must bring technical evidence back to the evaluation process to prevent purely PR-driven decision making.

## Marketing Hype vs. Technical Reality
- The AI security market is currently saturated with unsubstantiated claims of "swarms of autonomous agents" and "99% efficiency."
- Extraordinary claims of sub-30ms latency for comprehensive threat detection are often technically impossible given current model constraints.
- Organizations need a standardized methodology to verify marketing slicks against actual data sheets and GitHub-hosted instrumentation examples.

## Hyper-Growth of the AI Security Market
- The landscape is expanding at an unprecedented rate, with nearly 80 specialized vendors identified in a six-week period.
- On average, four new AI security startups emerge from stealth every six weeks, creating an unmanageable search space for human researchers.
- This high velocity makes automated, agent-driven market analysis a necessity rather than a luxury for modern security teams.

## The Vicious Governance Loop
- The standard governance loop (Review -> POC -> Hold -> Strategy Rebuild) often takes months, while business units ship chatbots in weeks.
- Parallel POCs frequently stall due to a lack of clear evaluation criteria or "analysis paralysis" regarding build vs. buy.
- AI governance must shift from reactive approvals to proactive risk ownership to prevent security from being bypassed entirely by product teams.

## The Agentic Assessment Pipeline
- Kovalsky built an automated loop using Claude to research and QC vendor claims across the entire security ecosystem.
- The pipeline utilizes specialized research and quality control agents to verify findings against technical documentation and public code.
- This automated reasoning loop allows for the continuous, real-time assessment of the market as new vendors and features emerge.

## Finding Substantiating Evidence
- The system automatically extracts evidence from GitHub repos, API documentation, and technical user forums to validate vendor claims.
- A "5/5" confidence rating is only achieved when the AI identifies actual code samples that demonstrate how a capability is instrumented.
- Substantiating evidence ensures that recommendations are grounded in verifiable technical reality rather than "vibe-based" marketing presentations.

## Custom AI Risk Synthesis
- A custom taxonomy was developed by synthesizing the OWASP LLM Top 10, NIST AI RMF, and MITRE ATLAS frameworks.
- This synthesis provides a more comprehensive view of modern AI risk than any single current academic or industry standard.
- Mapping vendor capabilities directly to this consolidated taxonomy allows for objective, cross-vendor comparisons during the evaluation process.

## Automated Implementation Guidance
- The system produces implementation guidance tailored for GRC, cloud engineering, security architecture, and development teams.
- Recommendations are filtered through an organization's existing strategic investments (e.g., Palo Alto, CrowdStrike) to minimize tool redundancy.
- This automated guidance bridges the critical gap between vendor selection and the actual operationalization of security controls.
