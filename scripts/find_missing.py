import os
import re

def normalize(name):
    # Remove file extensions
    name = os.path.splitext(name)[0]
    # Remove standard suffix if present
    name = name.replace(" ｜ [un]prompted 2026.en", "")
    name = name.replace(" ｜ [un]prompted 2026", "")
    # Replace non-alphanumeric with underscores
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    # Collapse multiple underscores
    name = re.sub(r'_+', '_', name)
    # Trim underscores
    name = name.strip('_')
    return name

transcripts = os.listdir('transcripts')
insights = os.listdir('insights')

insight_names = {normalize(f) for f in insights}
missing = []

for t in sorted(transcripts):
    if normalize(t) not in insight_names:
        missing.append(t)

for m in missing:
    print(m)
