# Nicholas Carlini - Black-hat LLMs

**Video ID:** 1sd26pWhfmg

**YouTube Link:** https://www.youtube.com/watch?v=1sd26pWhfmg

**Transcript:** [View Transcript](../transcripts/1sd26pWhfmg_Nicholas%20Carlini%20-%20Black-hat%20LLMs%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Nicholas Carlini from Anthropic discusses how modern LLMs can autonomously find and exploit zero-day vulnerabilities in critical software systems.

## Key Takeaway
LLMs now surpass human experts at finding vulnerabilities, fundamentally disrupting decades of attacker-defender balance.

# Insights

## Autonomous Vulnerability Discovery

- LLMs can autonomously find and exploit zero-day vulnerabilities without fancy scaffolding or human guidance.
- Simple prompts asking Claude to find bugs work remarkably well, requiring minimal specialized tooling or frameworks.
- Models find non-trivial bugs that would never be discovered through traditional fuzzing or automated testing approaches.

## Scale of Capability Advancement

- LLMs found multiple heap buffer overflows in the Linux kernel, something Carlini had never achieved himself.
- One discovered bug predates Git itself, existing since 2003, undiscovered for over twenty years by experts.
- Models can exploit smart contract vulnerabilities to recover millions of dollars with exponentially improving success rates.

## Minimal Scaffolding Required

- Basic setup uses Claude Code in a VM with simple prompts: find vulnerabilities and report them.
- Adding file hints enables systematic coverage across entire codebases, finding diverse bugs rather than duplicates.
- No security expertise required from the operator; models write complete exploits including blind SQL injection attacks.

## Exploitation Beyond Discovery

- Models write production-ready exploits, not just proof-of-concepts, including sophisticated multi-stage attacks like Ghost CMS compromise.
- Exploits extract complete database credentials, API keys, and password hashes without authentication through timing-based blind injection.
- Models generate detailed vulnerability reports with flow schematics explaining attack mechanics better than human documentation.

## Historical Inflection Point

- LLMs represent the most significant security development since the internet enabled remote attacks in first place.
- Progress rate shows exponential improvement every few months, matching or exceeding historical solar energy deployment underestimation patterns.
- Within one year, average laptop models will likely match today's best models at vulnerability discovery capabilities.

## Current vs Future Threat

- Today's models already exceed many security researchers' abilities; within a year they'll surpass expert-level practitioners.
- Hundreds of unvalidated Linux kernel crashes exist but cannot be responsibly disclosed without verification infrastructure scaling.
- Malicious actors will soon have access to capabilities currently limited to researchers at frontier AI labs.

## Urgency of Response

- Solutions needed on timescale of months, not years; waiting twelve months will be catastrophically too long.
- Security community needs coordinated effort across all AI labs and security firms, not competitive siloing of defenses.
- Current bug discovery rate outpaces validation and patching capacity, creating dangerous vulnerability disclosure bottleneck.

## Exponential Underestimation Risk

- Like energy forecasters predicting 2040 solar deployment that happened next year, security community risks similar miscalibration.
- Skepticism about LLM capabilities was reasonable years ago but is dangerously outdated given current demonstrated performance.
- Exponentials don't last forever, but assuming immediate plateau rather than continued growth invites catastrophic unpreparedness.
