# -*- coding: utf-8 -*-
import fitz
from PIL import Image, ImageDraw, ImageFont

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# Render page 0 at 4x zoom
mat = fitz.Matrix(4.0, 4.0)
pix = page0.get_pixmap(matrix=mat, alpha=False)
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

# We want to crop:
# 1. Hall, Lavabo, Cozinha e Entrada: x: 200..560 pt, y: 120..280 pt
# 2. Living & Terraço: x: 60..450 pt, y: 200..400 pt
# 3. Suíte Master, Closet e Banho Master: x: 80..320 pt, y: 380..580 pt
# 4. Circulação, Suíte 2 e Banho 2: x: 260..460 pt, y: 380..580 pt
# 5. Suíte 1, Banho 1 e Terraço Técnico: x: 420..560 pt, y: 250..500 pt

crops = {
    "detail_hall_lavabo_cozinha": (200, 120, 560, 280),
    "detail_living_terraco": (60, 200, 450, 400),
    "detail_suite_master_banho_master": (80, 380, 320, 580),
    "detail_circulacao_suite2_banho2": (260, 380, 460, 580),
    "detail_suite1_banho1_tecnico": (420, 250, 560, 500)
}

for name, (x0, y0, x1, y1) in crops.items():
    px0, py0 = int(x0 * 4.0), int(y0 * 4.0)
    px1, py1 = int(x1 * 4.0), int(y1 * 4.0)
    crop = img.crop((px0, py0, px1, py1))
    crop.save(f"{name}.png")
    print(f"Saved {name}.png ({crop.width}x{crop.height})")
