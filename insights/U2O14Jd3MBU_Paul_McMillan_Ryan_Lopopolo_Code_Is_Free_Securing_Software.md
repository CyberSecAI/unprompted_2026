# Code Is Free: Securing Software

**Video ID:** U2O14Jd3MBU

**YouTube Link:** https://www.youtube.com/watch?v=U2O14Jd3MBU

**Transcript:** [View Transcript](../transcripts/U2O14Jd3MBU_Paul%20McMillan%20%26%20Ryan%20Lopopolo%20-%20Code%20Is%20Free%EF%BC%9A%20Securing%20Software%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Paul McMillan and Ryan Lopopolo from OpenAI discuss how the "code is free" era allows security teams to replace stiff vendor tools with automated, checked-in security logic.

## Key Takeaway
Durable security requires moving threat models and expert judgments out of siloed docs and directly into the version-controlled codebase.

# Insights

## High Cost of Legacy Security
- Traditional security depends on lengthy vendor evaluation cycles, expensive contracts, and inflexible, centralized dashboards.
- Compliance-focused tooling is often too stiff to handle specialized engineering edge cases or legacy infrastructure assumptions.
- Organizations often spend more time trying to integrate external "solutions" than it would take to build targeted, custom security logic in-house.

## The "Code is Free" Philosophy
- In the era of advanced LLMs, the cost of writing, integrating, and maintaining custom security software has dropped to near zero.
- Security teams no longer need expensive consultants to tell them how to improve; they can simply ask an LLM to implement their own known requirements.
- Any desired security outcome can be achieved by askings a model to write a tailored integration specifically for the organization's unique environment.

## Threat Models as Versioned Code
- Threat models trapped in Slack threads or static Google Docs are functionally useless because they become stale and are never read by engineers.
- Checking threat models into the repository as text files makes them "legible" and actionable for both human developers and AI agents.
- Version-controlled threat models provide a durable, single source of truth that informs every phase of the software development lifecycle.

## Automating PR Security Gates
- LLM agents should be integrated into CI/CD to verify that every PR remains aligned with the checked-in organizational threat model.
- Implementing these automated security gates requires minimal effort—often as little as 40 lines of YAML in a GitHub Actions workflow.
- This process ensures that no material code change can invalidate previous security assumptions or risk acceptances without an automated flag.

## Treating Humans as Tools
- Organizations should pivot to treating human experts like "tools" that can be programmatically "invoked" by AI agents to resolve ambiguity.
- Agents can autonomously tag SMEs via CLI for targeted reviews only when a code change materially conflicts with established security documentation.
- This "human-in-the-loop" model ensures that human time is only spent on the most complex and non-deterministic security decisions.

## Durably Encoding Expert Judgment
- Collective organizational expertise is limited by synchronous human attention; automation allows this knowledge to be applied asynchronously and at scale.
- Automated "judgments"—binary security checks integrated into CI—ensure that expert security "golden threads" are followed in every commit.
- This approach transforms security from a point-in-time review process into a continuous, self-reinforcing property of the codebase.

## The "Zero Manual Code" Paradigm
- Rapidly growing products (1M+ lines of code) are being built by leaning entirely on coding models and versioned natural language prompts.
- When logic is stored as prompts in the codebase, it becomes easier to audit, update, and secure compared to traditional opaque binary code.
- This paradigm shift enables teams to scale their security and engineering hands without increasing operational friction or vendor dependency.

## Moving Toward Asynchronous Safety
- Replacing synchronous human-only security reviews with automated CI tests is the only way to scale security at AI-accelerated development speeds.
- Non-interactive agents running in CI provide real-time, high-fidelity security feedback to developers without requiring a meeting or a ticket.
- Success in modern security comes from "just asking" for the integration you need rather than waiting for a third-party vendor to provide it.
