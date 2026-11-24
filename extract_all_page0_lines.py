# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# Let's inspect the exact lines bounding every room on Page 0!
# We can find all line segments on Page 0 between y=130 and y=560.
lines = []
for d in page0.get_drawings():
    for it in d['items']:
        if it[0] == 'l':
            p1, p2 = it[1], it[2]
            if 130 <= p1.y <= 570 or 130 <= p2.y <= 570:
                lines.append((round(p1.x, 1), round(p1.y, 1), round(p2.x, 1), round(p2.y, 1)))

print(f"Total lines on Page 0 floor plan: {len(lines)}")
