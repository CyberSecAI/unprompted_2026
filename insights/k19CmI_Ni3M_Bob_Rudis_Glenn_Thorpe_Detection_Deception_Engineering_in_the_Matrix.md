# Detection & Deception Engineering in the Matrix

**Video ID:** k19CmI_Ni3M

**YouTube Link:** https://www.youtube.com/watch?v=k19CmI_Ni3M

**Transcript:** [View Transcript](../transcripts/k19CmI_Ni3M_Bob%20Rudis%20%26%20Glenn%20Thorpe%20-%20Detection%20%26%20Deception%20Engineering%20in%20the%20Matrix%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Bob Rudis and Glenn Thorpe from Grey Noise introduce "Orbee," an internal AI threat intelligence analyst that sifts through planetary-scale honeypot data to find zero-day signals.

## Key Takeaway
Managing planetary-scale telemetry requires AI analysts that utilize modular "skill systems" to autonomously prioritize signals within massive volumes of noise.

# Insights

## Scaling Beyond Human Bandwidth
- Grey Noise Labs operates a global sensor grid across 90+ countries, capturing tens of terabytes of session and packet data monthly.
- A small startup team cannot manually analyze 20 million daily documents to identify novel threat actor TTPs or zero-day exploits.
- Scaling threat intelligence requires a shift from manual data triage to AI-orchestrated analysis that can operate 24/7 without fatigue.

## Born from "React to Shell"
- Orbee's creation was a direct response to the "React to Shell" vulnerability, which triggered a massive wave of automated attacks in 2025.
- Grey Noise observed over 70,000 unique, AI-generated payloads from thousands of different ASNs targeting this specific vulnerability.
- The diversity and volume of these automated network fingerprints proved impossible to categorize without advanced AI reasoning capabilities.

## The "Empty Head" Problem
- General-purpose LLMs fire up with an "empty head" regarding specific organizational data and specialized security research skills.
- Without custom context, AI models are often as dangerous as "a teenager with a flamethrower and Wikipedia"—high power but low utility.
- Existing "Security Foundation Models" have largely underperformed in real-world intelligence tasks compared to modular, task-specific agent systems.

## Structured Skill System
- Orbee utilizes a "skill system" where specialized workflows, resources, and toolsets are loaded dynamically into the model's context.
- Each skill is a structured directory containing targeted system prompts that define a specific phase of the threat intelligence lifecycle.
- This architecture allows the agent to coordinate across 16+ MCP servers while maintaining a small and efficient memory footprint.

## Limitations of Hosted Code Environments
- The team initially used customized hosted environments (e.g., Claude Code) but quickly surpassed their operational and coordination limits.
- Future intelligence platforms require local, purpose-built agent runtimes to manage the high-velocity data flows required for global telemetry analysis.
- Offloading heavy data processing to local tools like DuckDB allows the LLM to focus exclusively on high-level reasoning and synthesis.

## Multi-Phase Workflow Orchestration
- Orbee executes investigations through six distinct workflow phases, from initial discovery to final, structured threat reporting.
- Autonomous planning enables the agent to pivot its investigation strategy based on the initial artifacts it discovers in the honeypot fleet.
- This multi-stage orchestration ensures that findings are not just identified but also thoroughly validated and cross-referenced with external intelligence.

## AI-Driven Deception Engineering
- "Detection environments" (honeypots) are the primary sensors for Orbee, providing raw, uninterpreted signals of system or state changes.
- AI reasoning enables the automatic generation of new, realistic honeypot configurations to catch emerging or specialized attacker TTPs.
- Combining deception engineering with AI-driven analysis creates a self-reinforcing loop that identifies "evil" at "superhuman" speeds.

Topic 8: Signal Extraction at Scale
- Orbee's primary value is extracting meaningful "signal" from more than 50 TB of noisy network session and packet data.
- The system produces structured, reproducible artifacts that allow human analysts to verify and implement protections for customers instantly.
- Automating the intelligence pipeline is the only viable path for blue teams to stay competitive against AI-accelerated offensive operations.
