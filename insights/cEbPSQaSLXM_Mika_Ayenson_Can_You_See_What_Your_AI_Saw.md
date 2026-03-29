# “Can You See What Your AI Saw?”

**Video ID:** cEbPSQaSLXM

**YouTube Link:** https://www.youtube.com/watch?v=cEbPSQaSLXM

**Transcript:** [View Transcript](../transcripts/cEbPSQaSLXM_Mika%20Ayenson%20-%20%EF%BC%82Can%20You%20See%20What%20Your%20AI%20Saw%EF%BC%9F%EF%BC%82%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Mika Ayenson, Lead for Threat Research at Elastic, explores the critical gap in endpoint security where human and AI agent actions produce identical, unauditable telemetry.

## Key Takeaway
EDR systems suffer from a "broken attribution" model because they cannot distinguish between legitimate human intent and model-driven system execution.

# Insights

## The Busy Extension Landscape
- Users are adopting new AI extensions and SDKs at a speed that significantly outpaces traditional organizational security audit cycles.
- Silent connections from extensions to unknown external domains highlight the growing risk of unvetted or malicious third-party AI tools.
- The decentralized nature of extension installation makes it difficult for security teams to maintain a comprehensive inventory of local AI capabilities.

## Agents as Privileged Executors
- Modern AI agents are high-privilege system executors that autonomously spawn shells, modify local files, and initiate network calls.
- Heavy use of tools like Cursor and Claude for coding means that a significant portion of a developer's local activity is now model-driven.
- These agents represent a massive expansion of the endpoint threat surface, moving beyond text generation to active, real-time system manipulation.

## The Intent Attribution Gap
- Telemetry from human developers and AI agents is nearly identical, sharing the same process IDs (PIDs), user contexts, and command-line syntax.
- Current EDR (Endpoint Detection and Response) tools lack the high-level context required to determine if a human or an LLM initiated an action.
- This invisibility gap prevents security teams from accurately auditing the root cause of suspicious or unauthorized system behaviors.

## Broken Visibility Models
- Traditional security systems are siloed, focusing on endpoint signals while remaining blind to the "thought process" of the underlying AI model.
- Without a link between an agent's reasoning trace and the resulting system call, defenders cannot verify if an action was malicious.
- This structural blindness makes it impossible to distinguish between a user-requested task and a payload executed via indirect prompt injection.

## Triaging AI "DNA"
- Detection engineers should begin by identifying endpoints with high host counts connecting to known AI model provider DNS records.
- Relying on unsigned binary detection is increasingly ineffective, as the most powerful and dangerous AI tools are typically signed and trusted.
- Monitoring process ancestry—specifically when IDEs spawn non-standard shells—can reveal the unique execution "DNA" of AI-driven activity.

## Targeting AI Configuration Paths
- Monitoring unauthorized file writes to local AI configuration and "skills" paths is a high-fidelity signal for identifying agent tampering.
- Attackers target these configuration files to establish long-term persistence and redirect the agent's future reasoning toward malicious goals.
- Protecting the local agent's instruction set is as critical as protecting traditional system binaries in the modern AI-assisted workspace.

## The "YOLO" Execution Risk
- The speed of AI execution encourages a "YOLO" (click-and-go) culture where users approve complex plans without a thorough technical audit.
- Malicious instructions delivered via injection can establish persistence and exfiltrate data in the seconds it takes for a user to walk away.
- The rapid cadence of automated execution maximizes the probability of successful exploitation before any human-in-the-loop oversight can occur.

## Toward Intent-Aware Detection
- Achieving robust security requires moving toward "intent-aware" monitoring that bridges the model's reasoning layer with the system's execution layer.
- Elastic is developing specialized rules to detect credential theft via GenAI tools and identifying unusual behavioral patterns in AI-spawned processes.
- Restoring auditability depends on the industry's ability to watermark and track the provenance of every model-driven system instruction.
