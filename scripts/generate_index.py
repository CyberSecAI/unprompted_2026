import os
import re
from urllib.parse import quote

def get_video_id(filename):
    # YouTube ID is 11 chars.
    return filename[:11]

def clean_title(vid, filename):
    # Remove extension and standard suffix
    name = filename.replace(" ｜ [un]prompted 2026.en.srt", "").replace(".en.srt", "")
    # Remove Video ID prefix
    name = name.replace(f"{vid}_", "")
    # Strip underscores and leading/trailing whitespace
    return name.strip('_').strip()

transcripts_dir = 'transcripts'
insights_dir = 'insights'
meta_dir = 'meta'

transcripts = [f for f in os.listdir(transcripts_dir) if f.endswith('.srt')]
insights = [f for f in os.listdir(insights_dir) if f.endswith('.md')]

id_to_transcript = {get_video_id(f): f for f in transcripts}
id_to_insight = {get_video_id(f): f for f in insights}

all_ids = sorted(id_to_transcript.keys())

with open('INDEX.md', 'w', encoding='utf-8') as f:
    f.write('# [un]prompted 2026 Conference Index\n\n')
    
    f.write('## Meta Key Insights\n')
    f.write('*Overarching strategic themes synthesized from recurring topics across multiple conference sessions.*\n\n')
    
    # Hardcoded mapping for Meta Insights based on synthesized files
    meta_mappings = [
        ("AI-Enhanced Developer Security", "META_INSIGHTS.md", "Synthesized themes on Threat Modeling, Just-in-Time Context, and Secure \"Vibe Coding.\""),
        ("Autonomous Vulnerability Research", "META_AVR_AUTONOMOUS_VULN_RESEARCH.md", "AI engines finding zero-days at scale in critical software."),
        ("The Blue Team Pivot", "META_BLUE_TEAM_PIVOT.md", "Rebuilding security teams and incident response around AI reasoning."),
        ("Governance, Risk & Compliance (GRC) for AI", "META_GRC_FOR_AI.md", "Corporate policy, fingerprints, and scaling governance without stifling innovation."),
        ("Architecting Secure Agentic Systems", "META_AGENTIC_SECURITY.md", "Identity, capability-based auth, and robust personal AI infrastructure."),
        ("Prompt Injection & Semantic Attacks", "META_SEMANTIC_ATTACKS.md", "Textual obfuscation, hidden payloads in images, and subverting KYC pipelines."),
        ("Measuring AI Security Efficacy", "META_METRICS_AND_EVAL.md", "Moving beyond \"vibes\" to quantifiable accuracy measurements and benchmarking."),
        ("Economic & Timeline Collapse", "META_TIMELINE_COLLAPSE.md", "8-minute exploits and the dramatically falling cost of zero-day weaponization."),
        ("Semantic Detection & Threat Hunting", "META_SEMANTIC_THREAT_HUNTING.md", "Using YARA-like semantic rules and deception engineering to hunt GenAI threats."),
        ("The Technical Transition: ML vs. LLMs", "META_ML_VS_LLM.md", "Comparing traditional ML models with modern LLMs for security classification and detection."),
        ("Interpretability & \"Glass-Box\" Security", "META_INTERPRETABILITY.md", "Opening the black box of model reasoning to provide security guarantees.")
    ]
    
    for title, m_file, desc in meta_mappings:
        f.write(f"- **[{title}](./{meta_dir}/{m_file})**: {desc}\n")
    
    f.write('\n## Individual Talk Insights\n')
    f.write('*Key Insights from each talk, with links to original video and transcript*\n\n')
    
    f.write('| Video ID | Title | Key Insights | Transcript | Video |\n')
    f.write('| --- | --- | --- | --- | --- |\n')
    
    for vid in all_ids:
        t_file = id_to_transcript.get(vid)
        i_file = id_to_insight.get(vid)
        
        if not t_file:
            continue
            
        title = clean_title(vid, t_file)
        
        insight_link = f"[Insights](./insights/{quote(i_file)})" if i_file else "Pending"
        transcript_link = f"[Transcript](./transcripts/{quote(t_file)})"
        
        video_link = f"[YouTube](https://www.youtube.com/watch?v={vid})"
        
        f.write(f"| `{vid}` | {title} | {insight_link} | {transcript_link} | {video_link} |\n")

print("INDEX.md generated successfully.")
