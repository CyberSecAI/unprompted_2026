# Operation Pale Fire

**Video ID:** SUa1nta8FGQ

**YouTube Link:** https://www.youtube.com/watch?v=SUa1nta8FGQ

**Transcript:** [View Transcript](../transcripts/SUa1nta8FGQ_Wes%20Ring%20%26%20Josiah%20Peedikayil%20-%20Operation%20Pale%20Fire%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Wes Ring and Josiah Peedikayil from Block detail "Operation Pale Fire," a red team engagement that used a stealthy prompt injection in Google Calendar to compromise an AI agent.

## Key Takeaway
Common enterprise tools like Google Calendar can be used to stealthily deliver operationalized prompt injections that achieve full system code execution.

# Insights

## Red Teaming at Block
- Red team operations at Block simulate sophisticated external adversaries (APTs) to identify and remediate deep-seated structural vulnerabilities.
- Engagement goals are typically high-impact and objective-oriented, often focusing on financial systems or sensitive data access.
- Operations emphasize extreme evasion to bypass a highly skilled blue team that monitors for any non-standard system or network activity.

## The Goose AI Agent
- Goose is a developer-focused AI agent created by Block, designed with a "builder mindset" and since released as an open-source project.
- The agent natively supports a developer shell tool call, allowing it to execute arbitrary shell commands on the host machine.
- Goose is highly extensible, integrating with multiple LLM providers and a marketplace of both internal and external MCP servers.

## Operationalizing Attacks
- The primary goal of Operation Pale Fire was to move past theoretical research and actually operationalize a stealthy, end-to-end AI attack.
- Operationalization requires creating an injection that remains hidden in plain sight and completely bypasses existing automated content filters.
- The target objective was to leverage the agent's privileged access to gain unauthorized code execution on a standard corporate laptop.

## Google Calendar as a Vector
- The red team targeted an internal MCP for Google Calendar that ingested untrusted event descriptions directly into the agent's context.
- Google Calendar's API allowed attackers to stealthily schedule meetings with employees without triggering any proactive email notifications.
- By disabling notifications, malicious invites would appear on an employee's calendar without any immediate sign of external interference.

## Stealthy Payload Delivery
- Attackers can embed massive prompt injection payloads in the "description" field of a calendar invite, which is rarely scrutinized by human users.
- Shared calendars can be maliciously renamed (e.g., "Corporate Sync") to perfectly mimic legitimate internal organizational resources.
- The minimal indicators of external origin, such as small italicized "created by" flags, are insufficient for alerting typical enterprise users.

## Zero-Click Execution Path
- Attacks can be staged by enumerating employee directories and pushing invites that list only the target employee as a visible guest.
- The malicious payload is activated when the user asks the agent to perform a routine task, such as "summarize my meetings for the day."
- This creates a zero-click path to compromise where the agent's helpfulness is directly exploited to execute the attacker's hidden commands.

## Exploiting Developer Tools
- The operation demonstrated that Goose's built-in developer shell could be tricked into executing malicious scripts via a calendar-delivered injection.
- This highlights the extreme risk of providing AI agents with high-privilege tools without corresponding high-fidelity input validation.
- Privilege escalation is a near-certainty when agents with "builder" capabilities are allowed to ingest untrusted data from common productivity apps.

## Lessons for Defense
- Traditional blue team monitoring must evolve to detect the subtle, context-dependent actions of compromised or manipulated AI agents.
- Security for agentic systems must be applied at the execution layer, specifically gating high-risk tool calls like shell command execution.
- Operation Pale Fire proves that securing the "reasoning layer" is not enough when agents are deeply integrated into common enterprise communication channels.
