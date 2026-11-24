# -*- coding: utf-8 -*-
import pdfplumber
import math

SCALE = 37.77777777777778 # 1m in pt
# Let's find origin from the outer bounds
# In verify_coords:
# X0 = 68.0 pt (0m), Z0 = 136.0 pt (0m)

with pdfplumber.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Let's inspect curves with size 20..40 pt (doors)
    doors = []
    for c in p0.curves:
        w = c['width']
        h = c['height']
        x0 = c['x0']
        top = c['top']
        if 18 <= max(w, h) <= 40 and min(w, h) >= 10:
            xm = (x0 - 68.0) / SCALE
            zm = (top - 136.0) / SCALE
            wm = max(w, h) / SCALE
            doors.append({
                "x": round(xm, 2), "z": round(zm, 2),
                "w_m": round(wm, 2),
                "pts_rect": (round(x0, 1), round(top, 1), round(c['x1'], 1), round(c['bottom'], 1))
            })
            
    print(f"Found {len(doors)} potential door curves:")
    doors.sort(key=lambda d: (d['z'], d['x']))
    for i, d in enumerate(doors):
        print(f"Door [{i:02d}] at X={d['x']:5.2f}m, Z={d['z']:5.2f}m | width={d['w_m']:4.2f}m | pts={d['pts_rect']}")
