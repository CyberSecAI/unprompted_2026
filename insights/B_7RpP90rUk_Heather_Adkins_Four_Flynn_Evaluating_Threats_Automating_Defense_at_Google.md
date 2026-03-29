# Heather Adkins &  Four Flynn - Evaluating Threats & Automating Defense at Google

**Video ID:** B_7RpP90rUk

**YouTube Link:** https://www.youtube.com/watch?v=B_7RpP90rUk

**Transcript:** [View Transcript](../transcripts/B_7RpP90rUk_Heather%20Adkins%20%26%20%20Four%20Flynn%20-%20Evaluating%20Threats%20%26%20Automating%20Defense%20at%20Google%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Evaluating Threats & Automating Defense at Google

**Speakers:** Heather Adkins (Google CISO), Four Flynn (DeepMind CISO)

## Overview

**Summary:** Google's Big Sleep and Code Mender use AI agents to find and fix deep vulnerabilities before attackers exploit them.

**Key Takeaway:** The "vuln apocalypse" is coming - AI will find every vulnerability in every system soon.

---

## The Vulnerability Crisis Ahead

**AI-powered hacking tools are emerging rapidly.** Billion dollars in VC funding targeting vulnerability discovery, pentesting, and red team simulation frameworks.

**Vulnerability discovery is accelerating exponentially.** NVD has 30,000 backlog, 35% increase in CVEs between 2024-2025, not counting undisclosed bugs.

**Traditional CVSS scoring will become meaningless.** When AI can find every bug, we need new ways to prioritize and rank vulnerabilities.

---

## Big Sleep: AI-Powered Vulnerability Discovery

**Big Sleep recreates expert researcher expertise using agentic AI.** Project Zero's decades of deep vulnerability research encoded into hypothesis-driven, self-testing AI agents.

**System achieves zero false positives through proof-of-exploitation.** Every reported bug includes working exploit code, eliminating AI slop and ensuring developer trust.

**Finding expert-level bugs in hours instead of months.** Traditional researchers take 30+ days for deep bugs; Big Sleep compresses this to automated discovery.

**Tools include debugger, code browser, Python interpreter for scripting.** Agentic loop constantly builds hypotheses, writes test code, and validates findings iteratively.

**Architecture understanding comes from past vulnerabilities and variant analysis.** System learns from historical bug patterns to identify similar weaknesses in codebases.

**Big Sleep finds vulnerabilities that fuzzers miss entirely.** Discovering bugs at depths OSS-Fuzz cannot reach, proving superiority over traditional automated testing.

---

## Code Mender: Autonomous Patch Generation

**Code Mender handles three critical requirements for patches.** Fixes vulnerability, preserves functionality, honors original developer's coding idioms for easy acceptance.

**Multiple verification stages ensure patch quality before submission.** Fuzzing before/after, formal verification, differential testing, LLM review all required for candidate approval.

**178 autonomously generated fixes now live in open source.** Successful deployments in libwebp, Chrome pointer hardening, and other critical infrastructure without human intervention.

**Validation failures feed back into LLM context window.** System learns from rejected patches to improve next generation of candidates through iterative refinement.

**Hardening mode proactively protects pointers before vulnerabilities exist.** AI identifies and patches potential buffer overflows preventively throughout entire codebase sections.

**Quality over speed is deliberate strategic choice.** Google prioritizes community trust and zero developer toil over rapid deployment of potentially flawed patches.

---

## The Vision: Eliminate All Software Vulnerabilities

**Goal is eliminating every software vulnerability on Earth.** Not hyperbole - genuine ambition to create legacy of vulnerability-free code for future generations.

**Three-pronged approach covers legacy, new code, and AI-generated code.** Find/fix existing bugs, harden current codebases, ensure AI coding assistants generate secure code by default.

**Memory safety bugs are primary but not exclusive target.** Techniques apply to web vulnerabilities and shallow bugs; verification methods differ but principles transfer.

**Real-time integration into developer workflow is critical.** Catching bugs before launch rather than discovering them in production brownfield deployments.

---

## The Deployment Challenge

**Cost-effectiveness and scale are non-negotiable requirements.** Must analyze billions of lines of code continuously without prohibitive compute expenses.

**Patch deployment speed remains unsolved organizational problem.** Technology can generate perfect patches instantly, but applying them timely across organizations lacks AI solution.

**Community trust drives adoption velocity of automated systems.** High verification standards necessary even if competitors ship faster with lower quality outputs.

---

## Technical Architecture Insights

**Agentic reasoning loops mimic expert researcher thought patterns.** Standing in corner with coffee thinking "I can't get that bug" - this is what LLM reasoning loop recreates.

**Deep codebase expertise is phase one foundation requirement.** Understanding architecture, past vulnerabilities, variant patterns essential before hypothesis generation begins.

**Business logic vulnerabilities remain outside current research scope.** Focus on infrastructure components like V8, ffmpeg that handle untrusted input rather than application-specific logic.
