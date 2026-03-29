# Georgi G - Promp2Pwn - LLMs Winning at Pwn2Own

**Video ID:** c5XAvRbma6Y

**YouTube Link:** https://www.youtube.com/watch?v=c5XAvRbma6Y

**Transcript:** [View Transcript](../transcripts/c5XAvRbma6Y_Georgi%20G%20-%20Promp2Pwn%20-%20LLMs%20Winning%20at%20Pwn2Own%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Promp2Pwn: LLMs Winning at Pwn2Own

## Overview

**Summary:** Security researcher used LLM agents to find Android vulnerabilities, successfully winning Pwn2Own Mobile with bugs discovered through agentic workflows.

**Key Takeaway:** LLM agents excel at pattern-matching security bugs when given specific, structured tasks and explicit guidance.

---

## Agent Design Philosophy

**Treat AI agents like interns requiring explicit instructions** - Successful prompts describe complete thought processes, security primitives, and exploit chains rather than vague objectives.

**Vague objectives lead to token exhaustion and confusion** - Telling agent "find bugs" fails; specifying exact component, entry point, and bug class succeeds.

**Deterministic tasks should never use LLMs** - Attack surface analysis was moved to standalone scripts, saving tokens and improving reliability for predictable operations.

---

## Prompt Engineering Lessons

**Actionable error messages enable agent self-correction** - Generic "error occurred" messages fail; detailed explanations let agents retry with adjusted inputs and succeed.

**Explicit bug class priorities prevent wasted output** - Agents constantly suggested fixes and mitigations; explicitly forbidding this saved tokens and focused effort.

**Breaking tasks into atomic entry points maintains focus** - Instead of "scan this app," successful approach: "scan this component reachable via this intent filter with this data format."

---

## Multi-Agent Architecture Evolution

**Running agents multiple times on same target uncovers different bugs** - Non-deterministic nature means 1-5 runs per entry point with deduplication agent yields better coverage.

**Enforcing strict schemas during generation degrades output quality** - Converting bug reports to JSON as post-processing step preserved report quality versus inline schema enforcement.

**Code deobfuscation as middleware dramatically improves agent performance** - Intercepting source requests to rename obfuscated variables with meaningful names helped agents understand code flow.

---

## Practical Implementation Wins

**JADEX MCP plugin provided essential reverse engineering tools** - HTTP server embedded in JADEX exposed manifest, source code retrieval, and class search via standardized tool interface.

**Separate bug verification agent reduced false positives significantly** - Verifier checked reachability constraints and validated exploit prerequisites, catching impossible-to-trigger vulnerabilities.

**Jinja2 templates enabled shared prompt components across agents** - Managing system prompts as composable snippets avoided duplication across attack surface, hunting, verification, and deduplication agents.

---

## Real-World Success: Samsung Exploit Chain

**First bug: URL validation bypass in Smart Touch Call** - Attacker-controlled URL loaded into WebView with permissive WebChromeClient granting camera, microphone, and geolocation without user prompts.

**Critical prerequisite: vulnerability only triggered during phone calls** - Agent missed this check initially; required second bug to programmatically initiate call via Bixby bypass.

**Second bug: Bixby subdomain validation weakness with XSS** - Any mcsvc.samsung.com subdomain accepted; XSS on subdomain enabled JavaScript execution accessing privileged internal Bixby components.

---

## Future Roadmap Opportunities

**Static analyzer integration with LLM triage** - Let traditional tools generate candidate bugs, use agents to eliminate false positives and assess exploitability.

**Cross-application bug tracking database** - Current limitation: agents only see one app's bugs; exploit chains often require primitives across multiple vulnerable applications.

**Runtime POC generation with ADB and Frida MCPs** - Connect phone to laptop, let agent test triggers, refine exploits using real-time feedback from hooks and logcat events.
