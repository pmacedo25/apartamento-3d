# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

wall_fills = {
    "drywall_blue": (0.0, 0.496, 1.0),
    "masonry_peach": (1.0, 0.75, 0.496),
    "fill_purple": (0.438, 0.0, 0.586),
    "carenagem_green": (0.43, 0.867, 0.0),
    "vent_orange": (1.0, 0.496, 0.0)
}

extracted = []

for d in page0.get_drawings():
    rect = d['rect']
    # Filter apartment region
    if 50 <= rect.x0 <= 580 and 100 <= rect.y0 <= 600:
        f = d.get('fill')
        if f:
            f_rounded = tuple(round(c, 3) for c in f[:3])
            for wtype, target in wall_fills.items():
                if f_rounded == target:
                    extracted.append({
                        "type": wtype,
                        "rect": (round(rect.x0, 2), round(rect.y0, 2), round(rect.x1, 2), round(rect.y1, 2)),
                        "items": len(d.get("items", []))
                    })

print(f"Total CAD wall polygons extracted: {len(extracted)}")
by_type = {}
for e in extracted:
    by_type[e["type"]] = by_type.get(e["type"], 0) + 1
print("Count by type:", by_type)

# Let's inspect all extracted walls sorted by y0, then x0
extracted.sort(key=lambda e: (e["rect"][1], e["rect"][0]))
for i, e in enumerate(extracted):
    r = e["rect"]
    w = round(r[2] - r[0], 2)
    h = round(r[3] - r[1], 2)
    print(f"[{i:02d}] {e['type']:15s} | x: {r[0]:6.2f} -> {r[2]:6.2f} (w={w:5.2f}) | y: {r[1]:6.2f} -> {r[3]:6.2f} (h={h:5.2f})")
