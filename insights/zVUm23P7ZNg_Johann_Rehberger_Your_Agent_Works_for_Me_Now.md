# Your Agent Works for Me Now

**Video ID:** zVUm23P7ZNg

**YouTube Link:** https://www.youtube.com/watch?v=zVUm23P7ZNg

**Transcript:** [View Transcript](../transcripts/zVUm23P7ZNg_Johann%20Rehberger%20-%20Your%20Agent%20Works%20for%20Me%20Now%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Johann Rehberger, an AI security expert, demonstrates how AI agents can be hijacked via "promptware" to achieve long-term persistence, data exfiltration, and unauthorized system execution.

## Key Takeaway
AI agents are susceptible to sophisticated "promptware" killchains that utilize hidden instructions in tickets, code, and memory to subvert user intent.

# Insights

## Hijacking Agentic Workflows
- Assigning tickets or feature requests to AI agents creates a direct path for attackers to deliver malicious instructions via external platforms like Linear.
- Agents with MCP integration can be tricked into executing unauthorized remote commands as part of their "autonomous" work plan.
- The extreme speed of AI task execution often obscures the inclusion of malicious sub-steps, making manual oversight of complex plans difficult.

## Invisible Unicode Tag Injections
- Advanced prompt injections can be delivered through hidden Unicode tag characters that are entirely invisible to human developers but legible to LLMs.
- AI-integrated IDEs (like Xcode) can be manipulated into decoding these hidden instructions during a routine code review or file analysis.
- These attacks can result in the agent silently modifying source code to include backdoors or exfiltration logic without the user's knowledge.

## Long-Term Memory Poisoning
- Enterprise Copilots can be permanently compromised by injecting malicious payloads into their persistent "long-term memory" via tool calls.
- Memory poisoning allows attackers to falsify an AI's understanding of organizational structure, financial data, or security policies indefinitely.
- Once a memory is poisoned, the agent will continue to provide compromised or malicious guidance across all future conversation turns.

## Transition to "Promptware"
- Prompt injection has evolved from a single-step "trick" into a multi-stage malware lifecycle known as "promptware."
- Promptware follows a traditional cyber killchain: initial delivery, persistence via model memory, and continuous data exfiltration (spyware).
- Shifting industry terminology from "injection" to "promptware" acknowledges the complexity and multi-stage nature of modern agent-based attacks.

## Bypassing Security Guardrails
- Model providers have implemented controls to prevent tool-chaining (e.g., Workspace tools) when a potential prompt injection is detected.
- "Delayed tool invocation" explores techniques to reactivate sensitive tools in later conversation turns after an initial safety check has passed.
- Attackers continuously probe the boundaries of "explicit user intent" to find windows of opportunity where high-privilege capabilities are re-enabled.

## Stealthy Command Smuggling
- Attackers use "smuggling" techniques to obfuscate malicious commands within benign-looking natural language or technical documentation.
- If an agent possesses entitlements for internet access, these smuggled commands can facilitate silent communication with an attacker's C2 server.
- The use of sub-agents implemented as tool calls provides additional layers for attackers to hide their true malicious intent from the primary orchestrator.

## The Zero-Click Calendar Vector
- Calendar invites are a primary vector for zero-click promptware because they are trusted, shared enterprise objects that agents routinely ingest.
- Malicious descriptions in invites can hijack an agent the moment it summarizes a user's daily meetings, requiring no manual user trigger.
- This demonstrates the fundamental danger of allowing agents to treat text from external, untrusted productivity apps as authoritative instructions.

## AI Watermarking and Defense
- Identifying and proving that a malicious payload originated from an LLM requires standardized watermarking and provenance techniques.
- Effective defense against promptware necessitates a collaborative effort between security researchers, IDE developers, and model providers.
- As attackers leverage "unlimited tokens" for automated exploitation, defensive systems must move toward real-time, AI-driven verification of agent intent.
