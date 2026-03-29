# SIFT-FIND EVIL! I Gave Claude Code R00t on DFIR SIFT Workstation

**Video ID:** OsUg3TlAqjQ

**YouTube Link:** https://www.youtube.com/watch?v=OsUg3TlAqjQ

**Transcript:** [View Transcript](../transcripts/OsUg3TlAqjQ_Rob%20T.%20Lee%20-%20SIFT-FIND%20EVIL%21%20I%20Gave%20Claude%20Code%20R00t%20on%20DFIR%20SIFT%20Workstation%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Rob T. Lee, creator of the SIFT workstation, demonstrates how giving Claude Code root access to forensic tools accelerates incident response from days to minutes.

## Key Takeaway
Integrating AI reasoning directly into vetted forensic workstations (SIFT) enables near-instant, autonomous discovery and reporting of complex threats.

# Insights

## Incident Response Bottlenecks
- Traditional manual digital forensics and incident response (DFIR) tasks typically require several days or even weeks for a single system.
- Critical but slow processes include cache analysis, prefetch investigation, event log correlation, and building complex activity timelines.
- The sheer volume of forensic data and specialized CLI commands creates a significant barrier to rapid, large-scale system analysis.

## Matching AI Speed with AI Speed
- Offensive AI operations have moved from days to seconds, necessitating a corresponding leap in automated defensive forensic capabilities.
- Defensive teams must adopt AI-driven reasoning to stay ahead of automated, rapidly evolving offensive supply chain and infrastructure attacks.
- Initial experiments demonstrate that a full day of manual forensics can be condensed into approximately 14 minutes of AI-driven analysis.

## Claude Code on SIFT Workstation
- The SIFT workstation provides a stable, highly vetted environment with over 18 years of refined digital forensic tool development.
- Granting Claude Code root access allows the AI to natively orchestrate the entire forensic suite without requiring human CLI input.
- This combination pairs advanced large language model reasoning with the industrial-strength execution capabilities of the SIFT workstation.

## Autonomous Tool Training
- Claude was trained on the SIFT suite by autonomously analyzing man pages, running help commands, and identifying relevant tool flags.
- By ingestive public guides and internal documentation, the AI developed its own internal "skills" for specialized forensic tasks.
- The AI successfully built its own instruction sets (`skills.md`) to map high-level user questions to specific forensic command-line executions.

## Automated Memory Forensics
- In production demos, Claude analyzed raw memory images to find "evil" without being told exactly which forensic steps to take.
- The AI autonomously identified malicious masquerading binaries (e.g., `p.exe` in temp) and correlated them with suspicious system processes.
- Memory analysis, which previously required hours of human attention, was completed from ingestion to reporting in under 18 minutes.

## High-Fidelity IR Reporting
- Claude generates structured, comprehensive IR reports that include system profiles, threat actor context, and complete attack chain mapping.
- Automated reporting captures malware persistence, code injection analysis, C2 network connections, and hierarchical process trees.
- The AI constructs accurate chronological timelines by reasoning across multiple forensic artifacts, a task traditionally prone to human error.

## The Human-AI IR Partnership
- AI does not replace the human investigator but requires a trained DFIR professional to direct, comprehend, and validate the findings.
- A foundational understanding of forensic principles is still necessary to interpret the AI's high-fidelity output and ensure accuracy.
- This shift threatens traditional IR business models that rely on manual hours, representing a fundamental "game changer" for the industry.

## Future of Forensic Workstations
- The era of "manual hands-on-typing" for forensics is transitioning toward AI-orchestrated, autonomous forensic workflows.
- Future forensic workstations will likely be built around AI reasoning agents that can explore system data at "superhuman" speed.
- Scaling these capabilities through AI is the only viable path for protecting increasingly complex and fast-moving modern enterprise networks.
