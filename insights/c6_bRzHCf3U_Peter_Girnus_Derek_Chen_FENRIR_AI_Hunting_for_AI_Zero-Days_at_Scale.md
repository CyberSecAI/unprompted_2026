# Peter Girnus & Derek Chen - FENRIR： AI Hunting for AI Zero-Days at Scale

**Video ID:** c6_bRzHCf3U

**YouTube Link:** https://www.youtube.com/watch?v=c6_bRzHCf3U

**Transcript:** [View Transcript](../transcripts/c6_bRzHCf3U_Peter%20Girnus%20%26%20Derek%20Chen%20-%20FENRIR%EF%BC%9A%20AI%20Hunting%20for%20AI%20Zero-Days%20at%20Scale%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# FENRIR: AI Hunting for AI Zero-Days at Scale

## Overview

**Summary:** FENRIR combines static analysis with multi-stage LLM triage to find zero-day vulnerabilities, achieving 2.5x more discoveries with 80% fewer false positives.

**Key Takeaway:** Cascade architecture eliminates 60% noise before expensive LLM analysis, enabling scalable vulnerability discovery.

---

## Multi-Stage Cascade Architecture

**Static analysis filters millions before LLM involvement:** YARA scans millions of lines in seconds, Semgrep and CodeQL filter candidates before any LLM token consumption.

**L1 triage uses fast models to eliminate obvious false positives:** 50-line context with Sonnet removes 60% of findings with single API calls, preventing expensive deep analysis.

**L2 deep verify uses agentic workflows in sandboxes:** Opus agents with full execution privileges autonomously collect context, trace data flows, and generate exploit POCs.

---

## Cost and Context Efficiency

**Pre-filtering saves massive token costs before LLM usage:** No AI tokens spent in static analysis phase; cascade drops findings from 500 to 10-25 high-confidence cases.

**Median cost per finding is $0.61, per vulnerability $8.80:** 100K tokens typical, can scale to 1M+ for complex multi-file data flow analysis in large repositories.

**Context efficiency through weighted dynamic token allocation:** Tokens intelligently allocated to relevant code sections rather than static distribution across entire analysis.

---

## Correlation and Signal Quality

**Multi-scanner correlation creates high-confidence signals:** Different tools pointing to same CWE class within 15 lines provides strong confidence and valuable context.

**CWE-specific prompts outperform generic vulnerability queries:** Asking "can this be CWE-79?" gives narrower target than "is this a vulnerability?", improving accuracy significantly.

**Reachability-first triage filters unreachable code immediately:** Documentation, test cases, and unreachable code eliminated early as not interesting from vulnerability hunting perspective.

---

## Agentic Deep Verification

**Forced reflection reduces hallucination and shallow reasoning:** Built-in adversarial component makes model argue against itself, preventing premature conclusions and lazy classification attempts.

**Agents autonomously collect context without pre-allocation:** LLMs know domain knowledge, trace data flows, build call graphs, and determine what context they need independently.

**Full sandbox execution enables POC generation and verification:** Agents write Python scripts, execute bash commands, and validate exploitability with complete write and execution privileges.

---

## Production Results and Impact

**60+ CVEs disclosed with 100+ in pre-disclosure pipeline:** All high or critical severity; system focuses on meaningful security impact rather than medium-severity findings.

**70% faster disclosure rate with 3x team productivity increase:** Researchers review 10-25 auto-generated reports instead of 500 raw alerts, complete with POCs and disclosure packages.

**System evolved through multiple LLM generations successfully:** Architecture survived transitions from early reasoning models through expanding context windows to current 1M+ token capabilities.

---

## Bi-Directional Intelligence Loop

**Zero-day discoveries feed into end-day vulnerability tracking:** NVIDIA Isaac vulnerability immediately tracked in Mimir; 23 autonomous agents rescanned after patch release.

**Patch analysis revealed bypass and newly introduced bugs:** Agents analyzed patch commits and found two additional vulnerabilities, including incomplete fix and new introduction.

**AI securing AI ecosystem creates massive vulnerability surface:** System targets AI frameworks and components with huge attack surfaces rather than traditional old code.

---

## System Architecture Innovations

**Kill chain analysis models exploit paths for faster surface identification:** Exploit path modeling prioritizes risky attack surfaces, accelerating discovery of critical vulnerabilities.

**Dynamic priority scoring surfaces most severe vulnerabilities immediately:** Scoring engine ranks findings to ensure critical issues reach disclosure teams without delay.

**Multi-vendor AI approach maintains flexibility across model evolution:** Architecture designed to incorporate new capabilities like extended thinking and adversarial interrogation for memory corruption.
