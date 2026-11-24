# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# Origin of coordinate system used in 3D:
# In measure_envelope.py:
# x_left = 68.0 pt -> X=0
# x_right = 578.0 pt -> X=13.50 m
# pt_to_m = 13.50 / (578.0 - 68.0) = 13.50 / 510.0 = 0.026470588 (or 1m = 37.777 pt)
# y_top = 136.0 pt -> Z=0
# y_bottom = 566.0 pt -> Z=11.38 m

PT_TO_M = 13.50 / 510.0
X0_PT = 68.0
Z0_PT = 136.0

def to_m(x_pt, y_pt):
    return (round((x_pt - X0_PT) * PT_TO_M, 2), round((y_pt - Z0_PT) * PT_TO_M, 2))

# Find shafts (rectangles with X crosses) and concrete pillars and fills
print("=== SHAFTS AND SPECIAL FILLS ACROSS THE APARTMENT ===")
for d in page0.get_drawings():
    r = d['rect']
    if 100 < r.y0 < 610 and 50 < r.x0 < 560:
        fill = d.get('fill')
        # Check special colors
        if fill:
            x_m, z_m = to_m(r.x0, r.y0)
            w_m = round(r.width * PT_TO_M, 2)
            d_m = round(r.height * PT_TO_M, 2)
            # Filter tiny or huge
            if 0.1 <= w_m <= 5.0 and 0.1 <= d_m <= 5.0:
                print(f"Fill {fill} at ({x_m}m, {z_m}m) size {w_m}m x {d_m}m (rect: {r.x0:.1f}, {r.y0:.1f}, {r.x1:.1f}, {r.y1:.1f})")
