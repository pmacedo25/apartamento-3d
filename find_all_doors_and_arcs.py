# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

curves = []
for d in page0.get_drawings():
    r = d['rect']
    if 50 <= r.x0 <= 580 and 100 <= r.y0 <= 600:
        has_curve = False
        for it in d.get('items', []):
            if it[0] == 'c': # cubic bezier curve
                has_curve = True
                break
        if has_curve:
            w = r.x1 - r.x0
            h = r.y1 - r.y0
            # Door swings are typically 20 to 40 pt (approx 0.60 to 0.90 m)
            if 15 <= max(w, h) <= 45:
                curves.append((round(r.x0, 1), round(r.y0, 1), round(r.x1, 1), round(r.y1, 1), round(w, 1), round(h, 1)))

print(f"Total potential door swings found: {len(curves)}")
# Dedup
curves = sorted(list(set(curves)), key=lambda c: (c[1], c[0]))
for i, c in enumerate(curves):
    print(f"Door swing [{i:02d}]: at x: {c[0]:5.1f}..{c[2]:5.1f} (w={c[4]:4.1f} pt), y: {c[1]:5.1f}..{c[3]:5.1f} (h={c[5]:4.1f} pt)")
