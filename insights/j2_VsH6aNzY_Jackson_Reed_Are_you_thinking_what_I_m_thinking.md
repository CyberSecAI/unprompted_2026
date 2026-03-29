# Are you thinking what I'm thinking?

**Video ID:** j2_VsH6aNzY

**YouTube Link:** https://www.youtube.com/watch?v=j2_VsH6aNzY

**Transcript:** [View Transcript](../transcripts/j2_VsH6aNzY_Jackson%20Reed%20-%20Are%20you%20thinking%20what%20I%27m%20thinking%EF%BC%9F%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Jackson Reed demonstrates a "reasoning injection" vulnerability where cryptographically signed "thinking" blocks can be replayed across conversations to hijack AI intent.

## Key Takeaway
Replaying signed reasoning blocks allows attackers to bypass provenance checks and force unauthorized internal "thoughts" into AI agents.

# Insights

## Introduction to Reasoning Blocks
- Modern LLMs (like GPT-4o and Claude 3.5) emit specialized "thinking" tokens used to plan and enrich the context of their responses.
- These internal reasoning paths are designed to improve the model's logical consistency and provide higher-quality answers to complex prompts.
- While often hidden from end-users, these blocks are transmitted as part of the raw API payload between the provider and the client.

## Cryptographic "Thought" Protection
- Providers like OpenAI and Anthropic use HMAC signatures or encrypted blobs to ensure the integrity of these reasoning blocks.
- The primary goal of these signatures is to prevent users from tampering with or falsifying the model's internal reasoning process.
- If a reasoning block is modified without a valid signature, the API will reject the message as an unauthorized or invalid request.

## The Reasoning Replay Vector
- Research discovered that while reasoning blocks cannot be easily edited, they can be "replayed" across different user sessions and API keys.
- An attacker can harvest a signed, valid reasoning block from one conversation and "inject" it into another entirely unrelated dialogue.
- This replay attack succeeds because the provider's validation often only checks if the signature is valid, not if it matches the current session context.

## Hijacking Model Intent
- Replaying a harvested block forces the target model to adopt a pre-defined "thought" as its own internal state for the current turn.
- In technical demos, injecting a reasoning block about one topic caused the model to "confess" to thinking about that topic in an unrelated turn.
- This technique provides a much more powerful "steering" mechanism than traditional prompting because the model treats the block as verified internal logic.

## Failure of Context Locking
- Most model APIs lack "context locking," which would cryptographically bind a reasoning block to a specific, unique conversation ID.
- The absence of this binding allows reasoning injections to move laterally across accounts and different organizational environments.
- Context-free signatures represent a significant gap in the initial threat modeling of the industry's most popular reasoning models.

## Provider Implementation Variances
- While OpenAI and Anthropic focused on verifying that thoughts originated from their models, Gemini implemented signatures in a way that incidentally mitigates replays.
- The vulnerability highlights a persistent trade-off between the flexibility of conversation APIs and the need for strict session-based security.
- Jackson theorizes that the replay vector was overlooked because the industry prioritized origin verification over contextual session integrity.

## Operationalizing Injections
- Attackers can build automated harnesses to "duplicate and edit" conversation turns, facilitating the rapid delivery of harvested reasoning payloads.
- Reasoning injections can be used to bypass safety filters that might otherwise block suspicious or adversarial natural language inputs.
- These "smuggled" thoughts can be leveraged to trick agents into performing unauthorized tool calls or manipulating persistent long-term memory.

## Future of AI Provenance
- If internal reasoning can be replayed and manipulated, the entire concept of AI "explainability" and provenance is undermined.
- Future security standards must require that all internal model metadata be cryptographically bound to a unique user and session context.
- Security researchers must shift from auditing model outputs to verifying the integrity and contextual relevance of the entire reasoning chain.
