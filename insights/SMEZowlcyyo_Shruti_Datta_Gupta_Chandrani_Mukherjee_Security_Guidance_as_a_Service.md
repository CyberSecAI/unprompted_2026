# Security Guidance as a Service

**Video ID:** SMEZowlcyyo

**YouTube Link:** https://www.youtube.com/watch?v=SMEZowlcyyo

**Transcript:** [View Transcript](../transcripts/SMEZowlcyyo_Shruti%20Datta%20Gupta%20%26%20Chandrani%20Mukherjee%20-%20Security%20Guidance%20as%20a%20Service%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Shruti Datta Gupta and Chandrani Mukherjee from Adobe present "Security Guidance as a Service," a centralized RAG pipeline that delivers vetted security knowledge across enterprise platforms.

## Key Takeaway
A centralized, automated RAG service democratizes security expertise by delivering consistent, vetted guidance directly into existing developer workflows and tools.

# Insights

## The Scalability Gap
- Extreme security-to-developer ratios make providing personalized, one-on-one guidance impossible across a large enterprise engineering organization.
- Bandwidth constraints often mean security teams only engage with developers after a vulnerability is found, rather than during design.
- Disparate security processes often deliver fragmented or repetitive information, confusing developers about which guidance is current and authoritative.

## Fragmented Documentation Risks
- Documentation created by various security champions and SMEs is often siloed and difficult for the average developer to locate.
- Stale documentation that fails to reach the right person at the right time leads to systemic non-compliance with security policies.
- Transforming passive, natural language documentation into active, context-aware guidance is required to scale security knowledge effectively.

## Limits of Generic LLMs
- Out-of-the-box LLMs provide generic security advice that lacks the necessary context of an organization's specific platform standards and methods.
- Generic answers often fail to account for the unique nuances of proprietary internal tech stacks and specialized security postures.
- There is a high risk of "hallucinated guidance," where AI provides plausible but incorrect advice that could introduce new security flaws.

## Centralizing Vetted Guidance
- "Security Guidance as a Service" democratizes expertise through a platform-agnostic system that provides a single, authoritative source of truth.
- The service ensures that guidance remains consistent whether it is accessed via a Slack bot, a Jira ticket, or an automated review.
- Centralization allows AppSec teams to manage and update organizational security knowledge in one place for global dissemination.

## RAG for Enterprise Security
- The solution utilizes Retrieval-Augmented Generation (RAG) to ground AI responses in the organization's own curated security documentation.
- Using a vetted vector store ensures that AI-generated guidance is highly accurate and strictly aligned with current internal policies.
- RAG significantly minimizes the risk of hallucinations by forcing the model to base its advice on retrieved, verified documentation snippets.

## Automated Ingestion Pipelines
- An automated document injection pipeline maintains the RAG system's accuracy without requiring constant, manual engineering effort.
- The pipeline autonomously monitors documentation URLs, scrapes content, and updates the vector store embeddings whenever a change is detected.
- This automated "freshness" ensures that developers never receive remediation advice based on outdated or superseded security standards.

## Git-Ops Documentation Curation
- Git serves as the primary source of truth, where SMEs and security champions submit documentation metadata via Pull Requests (PRs).
- This Git-based curation workflow provides a transparent and auditable history of all information being fed into the guidance engine.
- Validation steps in the PR process ensure that only high-quality, relevant data is merged into the production vector store.

## Workflow-Integrated Delivery
- The service integrates directly into the Jira ticket flow to provide immediate, actionable remediation steps for identified vulnerabilities.
- Slack integration allows developers to pull vetted security answers into informal chats, speeding up early-stage decision-making.
- Support for MCP servers enables the delivery of security guidance directly into the IDE, keeping the developer within their primary coding environment.
