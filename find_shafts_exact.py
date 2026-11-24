# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

PT_TO_M = 13.50 / 510.0
X0_PT = 68.0
Z0_PT = 136.0

def to_m(x_pt, y_pt):
    return (round((x_pt - X0_PT) * PT_TO_M, 2), round((y_pt - Z0_PT) * PT_TO_M, 2))

# Find lines with dx > 5 and dy > 5
shaft_crossings = []
for d in page0.get_drawings():
    for it in d['items']:
        if it[0] == 'l':
            p1, p2 = it[1], it[2]
            dx = abs(p2.x - p1.x)
            dy = abs(p2.y - p1.y)
            if 8 < dx < 60 and 8 < dy < 60:
                # bounding box of this line
                min_x = min(p1.x, p2.x)
                max_x = max(p1.x, p2.x)
                min_y = min(p1.y, p2.y)
                max_y = max(p1.y, p2.y)
                shaft_crossings.append((min_x, min_y, max_x, max_y))

# Cluster overlapping boxes
clusters = []
for sc in shaft_crossings:
    matched = False
    for c in clusters:
        if abs(c[0] - sc[0]) < 10 and abs(c[1] - sc[1]) < 10 and abs(c[2] - sc[2]) < 10 and abs(c[3] - sc[3]) < 10:
            c[4] += 1
            matched = True
            break
    if not matched:
        clusters.append([sc[0], sc[1], sc[2], sc[3], 1])

# Clusters with 2 crossing lines are SHAFTS!
shafts = [c for c in clusters if c[4] >= 2]
print(f"Detected {len(shafts)} exact technical shafts (vazio / shaft hidráulico):")
for s in sorted(shafts, key=lambda x: (x[1], x[0])):
    xm, zm = to_m(s[0], s[1])
    wm = round((s[2] - s[0]) * PT_TO_M, 2)
    dm = round((s[3] - s[1]) * PT_TO_M, 2)
    print(f"Shaft: pos=({xm}m, {zm}m), size=({wm}m x {dm}m), pt=({s[0]:.1f}, {s[1]:.1f}, {s[2]:.1f}, {s[3]:.1f})")
