# From OSINT Chaos to Knowledge Graph

**Video ID:** lib_KZKISOo

**YouTube Link:** https://www.youtube.com/watch?v=lib_KZKISOo

**Transcript:** [View Transcript](../transcripts/lib_KZKISOo_Dongdong%20Sun%20-%20From%20OSINT%20Chaos%20to%20Knowledge%20Graph%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Dongdong Sun, Machine Learning Engineer at Palo Alto Networks, demonstrates how to use AI to structure chaotic OSINT data into an interconnected knowledge graph.

## Key Takeaway
Transforming unstructured threat reports into AI-driven knowledge graphs creates an actionable, interconnected map of the global threat landscape.

# Insights

## The OSINT Scaling Problem
- OSINT is a free but high-effort resource that requires significant structuring before it can be used for automated tasks.
- Tracking 200+ sources and 10,000+ weekly reports is impossible for human teams, leading to massive intelligence consumption gaps.
- Critical contextual clues are often buried in unstructured text, making them difficult to extract via traditional automated security tools.

## Limitations of Raw Indicator Feeds
- Standard IOC feeds provide data for blocking but lack the necessary context to understand broader attacker intent or campaigns.
- Relying exclusively on hashes and IPs prevents security teams from mapping the subtle relationships between diverse threat actor TTPs.
- High-quality intelligence requires preserving the semantic "connective tissue" between an indicator and its role in a specific attack.

## Knowledge Graph Advantages
- Cybersecurity data is inherently interconnected, with natural relationships between actors, malware, specific vulnerabilities, and their intended victims.
- Knowledge graphs provide a semi-structured format that remains machine-readable while retaining the high-level context humans need for analysis.
- Transforming data into graphs allow for the automated discovery of overlapping artifacts across reports from different security vendors.

## STIX and Machine Readability
- While STIX is the standard for machine-to-machine exchange, it is often too verbose and complex for direct human ingestion.
- Purely structured formats can lose the nuanced "clues" found in natural language descriptions of sophisticated zero-day exploits.
- Graphs bridge the gap by enforcing structural constraints while utilizing unstructured text to maintain explanatory and reasoning power.

## AI-Augmented Intelligence Extraction
- AI agents can autonomously parse dense, 10-page reports and extract entities and relationships in a matter of minutes.
- Manual extraction by human researchers typically takes an hour per report, creating a significant bottleneck in intelligence production.
- Automating this "data entry" phase allows elite threat researchers to focus on high-value proactive hunting and strategic decision making.

## Multi-Step Extraction Pipelines
- Achieving reliable extraction requires a multi-stage pipeline rather than a single "one-shot" call to a large language model.
- A "router" agent identifies security-relevant report sections before passing them to specialized sub-agents for granular entity parsing.
- This structured approach ensures that complex reports with hundreds of interconnected relationships are processed with high technical accuracy.

## Interconnected Campaign Mapping
- Knowledge graphs enable the identification of common attack patterns (e.g., ingress transfer methods) shared across unrelated malicious campaigns.
- Expanding node relationships allows for the discovery of hidden links between current threats and historical, long-forgotten vulnerabilities.
- This granular perspective provides a superior strategic view of the global threat landscape compared to siloed, per-vendor report analysis.

## Proactive Intelligence Querying
- Structured knowledge graphs allow security teams to proactively query their data for specific actor profiles or malware usage patterns.
- Moving to a natural language interface for threat data enables faster correlation between new log indicators and existing global research.
- Integrating LLMs with structured graphs provides a continuously updated, queryable interface for making enterprise-wide, risk-informed security decisions.
