# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

PT_TO_M = 13.50 / 510.0
X0_PT = 68.0
Z0_PT = 136.0

def to_m(x_pt, y_pt):
    return (round((x_pt - X0_PT) * PT_TO_M, 2), round((y_pt - Z0_PT) * PT_TO_M, 2))

# In CAD, pillars have dense diagonal lines (hatch). Let's cluster diagonal line endpoints!
# A line with slope ~ -1 or +1, short length:
diagonal_lines = []
for d in page0.get_drawings():
    r = d['rect']
    if 130 < r.y0 < 560 and 60 < r.x0 < 560:
        for it in d['items']:
            if it[0] == 'l': # line
                p1, p2 = it[1], it[2]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                if abs(dx) > 1 and abs(dy) > 1:
                    slope = dy / dx
                    # concrete hatch typically has 45 degree slope (slope ~ 1.0 or -1.0)
                    if 0.5 < abs(slope) < 2.0:
                        diagonal_lines.append((min(p1.x, p2.x), min(p1.y, p2.y), max(p1.x, p2.x), max(p1.y, p2.y)))

print(f"Total concrete hatch lines found: {len(diagonal_lines)}")

# Group nearby diagonal lines into bounding boxes
clusters = []
for l in diagonal_lines:
    matched = False
    for c in clusters:
        # If line touches or is close to cluster box
        if (c[0] - 5 <= l[0] <= c[2] + 5 or c[0] - 5 <= l[2] <= c[2] + 5) and \
           (c[1] - 5 <= l[1] <= c[3] + 5 or c[1] - 5 <= l[3] <= c[3] + 5):
            c[0] = min(c[0], l[0])
            c[1] = min(c[1], l[1])
            c[2] = max(c[2], l[2])
            c[3] = max(c[3], l[3])
            c[4] += 1
            matched = True
            break
    if not matched:
        clusters.append([l[0], l[1], l[2], l[3], 1])

# Filter clusters that have at least 5 hatch lines (real pillars)
pillars = [c for c in clusters if c[4] >= 5]
print(f"Found {len(pillars)} concrete pillars (pilares estruturais):")
for p in sorted(pillars, key=lambda x: (x[1], x[0])):
    x_m, z_m = to_m(p[0], p[1])
    w_m = round((p[2] - p[0]) * PT_TO_M, 2)
    d_m = round((p[3] - p[1]) * PT_TO_M, 2)
    print(f"Pilar: pos=({x_m}m, {z_m}m), size=({w_m}m x {d_m}m), lines={p[4]}, pt=({p[0]:.1f}, {p[1]:.1f}, {p[2]:.1f}, {p[3]:.1f})")
