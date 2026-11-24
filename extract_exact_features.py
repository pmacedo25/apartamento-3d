# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

PT_TO_M = 13.50 / 510.0
X0_PT = 68.0
Z0_PT = 136.0

def to_m(x_pt, y_pt):
    return (round((x_pt - X0_PT) * PT_TO_M, 2), round((y_pt - Z0_PT) * PT_TO_M, 2))

# 1. Let's find all Shafts: in CAD, shafts have an 'X' crossing lines inside a rectangle!
# An X has two lines crossing with opposite slopes.
crossing_lines = []
for d in page0.get_drawings():
    r = d['rect']
    if 130 < r.y0 < 560 and 60 < r.x0 < 560:
        for it in d['items']:
            if it[0] == 'l':
                p1, p2 = it[1], it[2]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                if abs(dx) > 5 and abs(dy) > 5:
                    crossing_lines.append((p1.x, p1.y, p2.x, p2.y, r))

print(f"Total potential shaft diagonal lines: {len(crossing_lines)}")

# Let's inspect where the shafts are by looking at rects with diagonals
shaft_candidates = []
for d in page0.get_drawings():
    r = d['rect']
    if 130 < r.y0 < 560 and 60 < r.x0 < 560:
        # Check if rect contains lines that cross from corner to corner
        lines_in_r = []
        for it in d['items']:
            if it[0] == 'l':
                lines_in_r.append(it)
        if len(lines_in_r) >= 2:
            # check if two lines connect opposite corners
            p_pts = [(it[1].x, it[1].y, it[2].x, it[2].y) for it in lines_in_r]
            # check if crossing
            diag_count = 0
            for p in p_pts:
                dx = abs(p[2] - p[0])
                dy = abs(p[3] - p[1])
                if dx > 8 and dy > 8:
                    diag_count += 1
            if diag_count >= 2 and r.width < 100 and r.height < 100:
                shaft_candidates.append(r)

print(f"Shaft candidates found: {len(shaft_candidates)}")
for s in shaft_candidates:
    xm, zm = to_m(s.x0, s.y0)
    wm = round(s.width * PT_TO_M, 2)
    dm = round(s.height * PT_TO_M, 2)
    print(f"Shaft at ({xm}m, {zm}m), size {wm}m x {dm}m (pt: {s.x0:.1f}, {s.y0:.1f}, {s.x1:.1f}, {s.y1:.1f})")
