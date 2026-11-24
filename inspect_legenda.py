# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

print("=== LEGENDA ITEMS (y0 > 630) ===")
for d in page0.get_drawings():
    r = d['rect']
    if r.y0 > 630 and r.x1 < 400:
        fill = d.get('fill')
        color = d.get('color')
        if fill or color:
            print(f"Rect ({r.x0:.1f}, {r.y0:.1f}, {r.x1:.1f}, {r.y1:.1f}) | fill={fill} | color={color}")
