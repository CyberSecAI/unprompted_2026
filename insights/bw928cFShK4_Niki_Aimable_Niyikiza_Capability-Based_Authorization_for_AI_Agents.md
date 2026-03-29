# Niki Aimable Niyikiza - Capability-Based Authorization for AI Agents

**Video ID:** bw928cFShK4

**YouTube Link:** https://www.youtube.com/watch?v=bw928cFShK4

**Transcript:** [View Transcript](../transcripts/bw928cFShK4_Niki%20Aimable%20Niyikiza%20-%20Capability-Based%20Authorization%20for%20AI%20Agents%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Capability-Based Authorization for AI Agents

## Overview

**Summary:** AI agent workflows require capability-based authorization to enforce deterministic security constraints at execution time, preventing confused deputy problems through delegation-aware primitives.

**Key Takeaway:** Freeze blast radius upfront; agents can only attenuate authority downstream, never expand it.

---

## Confused Deputy Problem in Multi-Agent Systems

Traditional workload identity fails for AI agents because authorization is determined at deployment time for deterministic services. AI agents reason at runtime, spawn sub-agents unpredictably, creating confused deputy vulnerabilities when given ambient authority instead of derived, task-specific authority.

Agentic workflows are fundamentally non-deterministic, making deployment-time authorization insufficient for runtime security. Current infrastructure primitives lack delegation awareness needed for multi-agent authorization chains.

---

## Capability-Based Authorization Model

Capabilities solve confused deputy problems by encoding authority directly in unforgeable tokens rather than relying on ambient credentials. Dennis and Van Horn introduced this 60+ years ago; Google's Macaroons (2014) modernized it with caveats and attenuation.

DeepMind's CHEM paper (2024) first applied capability systems to AI agents for prompt injection defense. Intelligent AI design paper (Feb 2025) reiterated capabilities as proper framework for multi-agent authorization.

Authorization must happen at execution layer where agents meet real world, not content layer. Deterministic controls required for enterprise infrastructure touching data, money, and critical systems.

---

## Warrant Primitive Design

Warrants have six properties: cryptographically signed by issuer, scoped explicitly to task, ephemeral with short TTLs, holder-bound via proof of possession, verifiable offline without central server, and delegation-aware encoding entire chain.

Monotonic attenuation principle: child agent warrants can never exceed parent scope. Capabilities shrink downstream in delegation chain, preventing privilege escalation regardless of agent reasoning or prompt injection.

Warrants are not secrets—they can travel in HTTP headers. Security comes from cryptographic verification and holder binding, not confidentiality.

---

## Deployment and Integration Patterns

Four deployment models: in-process (middleware hooks for LangGraph, CrewAI, 9 frameworks), sidecar (Envoy extensions for service mesh), gateway (warrant headers verified before API access), MCP proxy (client/server-side for structured tools).

Integration is simple: single line replacement in LangGraph to swap tool node with tenure-enabled version. Python bindings over Rust core enable framework compatibility across ecosystem.

Companies hesitate production deployment without delegation primitives to express policies matching multi-agent architecture. All deployment models aim to meet real infrastructure needs.

---

## Security Properties and Performance

Custom benchmarks with 53 tests and 5,000+ fuzzing scenarios using LLMs to generate adversarial situations. Attack surface reduced from 90% to 0% with clear scope definitions and tenure enforcement.

Tenure doesn't solve prompt injection—it constrains agent execution even when prompt-injected. Authorization frozen at task start regardless of agent reasoning or malicious suggestions in data.

Rust core for cryptography verification ensures sub-millisecond authorization checks. Every action verified with cryptographic proof; offline verification eliminates central server bottleneck.

---

## Map versus Territory Challenge

Constraint logic alone insufficient—path traversals and URL encoding issues emerge in real systems. Three layers needed: map (regex/glob logic), attenuated map (normalized paths/URLs understanding targets), actual map (runtime environment speaking same language).

Open-source execution guards for filesystem and process operations bridge logic to reality. Matching warrant system to sandboxes that understand warrant semantics is critical endgame.

Cryptography and constraints are not the bottleneck—real-world execution semantics are. Security requires deterministic controls at infrastructure boundaries, not just token validation.

---

## Approval Processes and Orchestration

Orchestrator can decide sub-agent scope at runtime within frozen top-level capability bounds. Approval constraints allow actions only if specific key pairs sign off at runtime.

Human-in-loop via approval processes for sensitive operations. Initial warrant can be human-defined or triggered by deterministic processes like alerts or webhooks.

Two modes: orchestrator autonomously delegates within bounds, or approval gates require human/system authorization. Both maintain cryptographic audit trail with unforgeable provenance.

---

## Open Source and Research Directions

Core implementation open source in Rust with Python bindings. Playground at tenure.ai for decoding and testing warrants. Community invited to validate primitive by building with it or breaking it.

No public benchmarks exist for multi-agent authorization testing. Seeking researchers to collaborate on benchmarking frameworks and companies to stress-test with real agentic workflows in production.

Exploring applications across frameworks and new architectures. Looking for partners deploying capability-based authorization at infrastructure scale for enterprise AI systems.
