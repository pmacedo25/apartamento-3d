# -*- coding: utf-8 -*-
import fitz
import json
import math
from PIL import Image, ImageDraw, ImageFont

# 1. Load PDF
doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page = doc[0]

# Render page 0 at 4x scale (approx 288 DPI)
scale = 4.0
mat = fitz.Matrix(scale, scale)
pix = page.get_pixmap(matrix=mat, alpha=False)
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

# Load our geometry from build_geometry.py
import build_geometry as bg

# Coordinate mapping:
# In verify_coords:
# PT_TO_M = 13.50 / 510.0 => 1m = 37.7777 pt
# X0_PT = 68.0 pt
# Z0_PT = 136.0 pt
# Therefore:
# x_pt = X0_PT + X_m * (510.0 / 13.50)
# y_pt = Z0_PT + Z_m * (510.0 / 13.50)
# pixel_x = x_pt * scale
# pixel_y = y_pt * scale

def m_to_px(xm, zm):
    x_pt = 68.0 + xm * (510.0 / 13.50)
    y_pt = 136.0 + zm * (510.0 / 13.50)
    return (x_pt * scale, y_pt * scale)

# Create an overlay image
overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(overlay)

# Draw walls as semi-transparent red lines / boxes
for w in bg.walls:
    p1 = m_to_px(w["x1"], w["z1"])
    p2 = m_to_px(w["x2"], w["z2"])
    draw.line([p1, p2], fill=(255, 0, 0, 200), width=int(w["thick"] * 37.777 * scale))

# Draw pillars as blue boxes
for p in bg.pillars:
    p1 = m_to_px(p["x"] - p["w"]/2, p["z"] - p["d"]/2)
    p2 = m_to_px(p["x"] + p["w"]/2, p["z"] + p["d"]/2)
    draw.rectangle([p1, p2], fill=(0, 0, 255, 120), outline=(0, 0, 255, 255), width=2)

# Draw shafts as green boxes
for s in bg.shafts:
    p1 = m_to_px(s["x"] - s["w"]/2, s["z"] - s["d"]/2)
    p2 = m_to_px(s["x"] + s["w"]/2, s["z"] + s["d"]/2)
    draw.rectangle([p1, p2], fill=(0, 200, 0, 120), outline=(0, 150, 0, 255), width=2)

# Draw fixtures as orange boxes
for f in bg.fixtures:
    p1 = m_to_px(f["x"] - f["w"]/2, f["z"] - f["d"]/2)
    p2 = m_to_px(f["x"] + f["w"]/2, f["z"] + f["d"]/2)
    draw.rectangle([p1, p2], fill=(255, 165, 0, 140), outline=(200, 100, 0, 255), width=2)

# Composite
composite = Image.alpha_composite(img.convert("RGBA"), overlay)

# Save full overlay
composite.convert("RGB").save("full_overlay.png")
print("Saved full_overlay.png")

# Now crop individual zones for detailed visual verification
zones = {
    "zone_1_cozinha_servico": (0.0, 0.0, 5.0, 3.5),
    "zone_2_terraco_gourmet": (0.0, 1.8, 6.0, 7.5),
    "zone_3_living_lavabo_hall": (5.0, 0.0, 13.5, 7.0),
    "zone_4_suite_master_banho": (0.0, 6.5, 8.0, 11.5),
    "zone_5_suite2_banho2": (6.0, 7.0, 11.0, 11.5),
    "zone_6_suite1_banho1_tec": (9.5, 2.5, 13.5, 9.5),
    "zone_7_circulacao_central": (5.5, 5.5, 9.5, 9.0)
}

for name, (x1m, z1m, x2m, z2m) in zones.items():
    px1, py1 = m_to_px(x1m, z1m)
    px2, py2 = m_to_px(x2m, z2m)
    # Clamp to image
    px1 = max(0, min(img.width, px1))
    py1 = max(0, min(img.height, py1))
    px2 = max(0, min(img.width, px2))
    py2 = max(0, min(img.height, py2))
    crop_comp = composite.crop((px1, py1, px2, py2))
    crop_orig = img.crop((px1, py1, px2, py2))
    
    # Save side-by-side: Original CAD | CAD with 3D Model Overlay
    sbs = Image.new("RGB", (crop_comp.width * 2 + 10, crop_comp.height), (240, 240, 240))
    sbs.paste(crop_orig, (0, 0))
    sbs.paste(crop_comp.convert("RGB"), (crop_comp.width + 10, 0))
    sbs.save(f"audit_{name}.png")
    print(f"Saved audit_{name}.png")
