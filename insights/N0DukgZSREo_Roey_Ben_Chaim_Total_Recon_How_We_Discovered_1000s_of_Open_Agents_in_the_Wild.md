# Total Recon: How We Discovered 1000s of Open Agents in the Wild

**Video ID:** N0DukgZSREo

**YouTube Link:** https://www.youtube.com/watch?v=N0DukgZSREo

**Transcript:** [View Transcript](../transcripts/N0DukgZSREo_Roey%20Ben%20Chaim%20-%20Total%20Recon%EF%BC%9A%20How%20We%20Discovered%201000s%20of%20Open%20Agents%20in%20the%20Wild%20%EF%BD%9C%20%5Bun%5Dprompted%202026.en.srt)

---

# Overview

## Summary
Roey Ben Chaim demonstrates how tens of thousands of AI agents can be discovered via OSINT, many of which provide unauthenticated access to sensitive enterprise data.

## Key Takeaway
AI agents are discoverable web applications that often serve as insecure, unauthenticated gateways into deep enterprise resources and data.

# Insights

## The Concept of Agent Recon
- AI agents are fundamentally web applications that leave traditional discoverable breadcrumbs like API endpoints, discoverable resources, and iframes.
- "Agent Recon" involves identifying and mapping the capabilities of these agents across various platforms using standard OSINT techniques.
- Research has identified tens of thousands of exposed agents, with thousands being entirely unauthenticated and open to public access.

## Agents as Enterprise Gateways
- Unlike simple chatbots, enterprise agents are often integrated with sensitive internal data sources and possess embedded system credentials.
- Compromised or exposed agents can allow attackers to not only read sensitive documents but also modify internal organizational data.
- This high level of integration makes exposed agents one of the most critical and high-impact risks in the modern AI landscape.

## Exploiting Common Patterns
- Attackers leverage common design patterns and out-of-the-box configurations to systematically identify vulnerable agent resources.
- Predictable URL structures and default naming conventions (e.g., "Copilot One", "Test AI Bot") significantly reduce the search space for discovery.
- Security by obscurity is ineffective against automated, web-scale fuzzing and enumeration of default agent addresses.

## Copilot Studio Vulnerabilities
- Microsoft Copilot Studio resources are essentially websites with embedded agents whose URLs contain predictable, resolvable components.
- Default environments are created using a "default" prefix followed by a tenant ID, which can be resolved using undocumented APIs.
- While solution prefixes have some entropy, they are frequently fuzzed to discover the specific agents active within a given tenant.

## Tenant and Agent Enumeration
- Attackers can fetch an organization's internal tenant ID through undocumented Microsoft APIs by simply providing a corporate domain name.
- Once a tenant ID is known, it becomes possible to enumerate all agents in the environment, including poorly secured dev and sandbox bots.
- Systematic enumeration allows attackers to map an organization's entire internal AI capability and identify the weakest entry points.

## OpenAI Agent Builder Risks
- Agent Builder allows developers to manage their own deployments, which frequently leads to insecure configurations on platforms like Vercel.
- Use of OpenAI's recommended GitHub starter kits creates a predictable attack surface due to the use of well-known filenames and paths.
- Verifying the existence of an agent involves simple API calls to check for active sessions and verified addresses.

## Custom GPT Attack Surface
- Custom GPTs, while useful, inherently increase an organization's attack surface by exposing internal capabilities and data connectors.
- By design, the Default tools and system instructions of many custom GPTs can be identified or inferred by external users.
- Publicly accessible GPTs can provide a roadmap for attackers to understand an organization's internal AI workflows and data structures.

## Failure of Traditional Obscurity
- Relying on "unlisted" URLs or non-obvious prefixes is insufficient for protecting agents that have access to high-value enterprise data.
- All AI agents must be treated as production-grade applications with mandatory, robust authentication and authorization controls.
- The sheer scale of discovered agents proves that current deployment practices are lagging behind the capabilities of automated reconnaissance tools.
