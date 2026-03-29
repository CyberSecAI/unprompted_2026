# PleaseFix

**Video ID:** yUqBC3mc544

**YouTube Link:** https://www.youtube.com/watch?v=yUqBC3mc544

**Transcript:** [View Transcript](../transcripts/yUqBC3mc544_Gadi%20Evron%20on%20behalf%20of%20Zenity%20-%20PleaseFix%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Gadi Evron, on behalf of Zenity Labs, demonstrates how agentic browsers can be compromised via zero-click prompt injections in calendar invites.

## Key Takeaway
Agentic browsers act under the user's identity, creating a critical security gap where external data can autonomously hijack user intent.

# Insights

## Rise of Agentic Browsers
- Agentic browsers (like Comet) represent the next major wave of AI adoption, moving beyond simple static chatbots.
- These browsers bring massive productivity gains but introduce severe risks by autonomously navigating the web on behalf of users.
- Unlike traditional browsers, agentic entities process web content as potential instructions, fundamentally changing the application threat model.

## Intent Collision Attacks
- "Intent collision" occurs when an attacker's instructions, hidden in web data, override the user's original goal or intent.
- Malicious payloads can be embedded in trusted objects like calendar invites that users frequently ask agents to summarize.
- Collision allows attackers to trick agents into performing high-privilege actions that the user neither authorized nor intended to trigger.

## Zero-Click Data Exfiltration
- Zenity Labs research presented the first verified zero-click attack vector targeting the agentic AI software ecosystem.
- Attackers deliver payloads via calendar invite descriptions or by manipulating the logic of the "Accept" button UI components.
- The attack is activated as soon as the agent interacts with the malicious item, requiring no direct action from the human.

## Unauthorized File System Access
- Many agentic browsers are granted local file system access to "help" users manage, upload, or summarize their local documents.
- Malicious instructions can trick the browser into autonomously searching for, reading, and exfiltrating sensitive files to an external server.
- Users are often oblivious to the breach, perceiving only minor rendering errors while their local data is being systematically stolen.

## Session and Account Hijacking
- Because agents operate within the user's authenticated session, they have access to logged-in services like 1Password and Google Workspace.
- Exploiting features like "autocomplete" allows agents to bypass traditional authentication prompts and perform account-level management tasks.
- Attackers can leverage this to steal account recovery kits, change security settings, or perform unauthorized lateral movement into other apps.

## Abusing Calendar Invites
- Calendar invites are an ideal attack vector because they are trusted, shared objects that easily penetrate traditional organizational perimeters.
- PAYLOADS can be hidden in long event descriptions, comment internals, or system reminders that are rarely audited by security teams.
- MIMICKING internal meeting formats increases the likelihood that both the user and the agent will treat the invite as authoritative.

## Broken Browser Security Models
- Traditional browser security boundaries (like Same-Origin Policy) are insufficient for agents that interpret data as executable commands.
- There is currently no reliable way to distinguish between "passive" web content and "active" agent instructions within the same stream.
- This represents a fundamental architectural failure that requires the industry to completely rethink browser security for the AI age.

## Trusting Agentic Entities
- Organizations must treat agentic browsers as highly privileged and potentially untrusted entities within their security architecture.
- Relying on model-level safety filters is ineffective when an agent possesses deep system integration and authenticated session access.
- The "PleaseFix" research highlights the urgent need for specialized guardrails that gate high-risk browser capabilities based on verified intent.
