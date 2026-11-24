# -*- coding: utf-8 -*-
from PIL import Image

img = Image.open(r'c:\Users\sport\Documents\apartamento\page_0_hi_res.png')
w, h = img.size

# Coordinates in PDF:
# x: 0 to 595 pt -> 0 to 2480 px (scale = 2480 / 595 = 4.168)
# y: 0 to 842 pt -> 0 to 3509 px (scale = 3509 / 842 = 4.167)
s_x = w / 595.0
s_y = h / 842.0

def crop_zone(name, x0_pt, y0_pt, x1_pt, y1_pt):
    box = (int(x0_pt * s_x), int(y0_pt * s_y), int(x1_pt * s_x), int(y1_pt * s_y))
    cropped = img.crop(box)
    cropped.save(rf'c:\Users\sport\Documents\apartamento\zone_{name}.png')
    print(f'Saved zone_{name}.png {cropped.size}')

crop_zone('cozinha_servico', 50, 130, 260, 260)
crop_zone('terraco_gourmet', 40, 200, 200, 420)
crop_zone('living_hall_lavabo', 200, 130, 560, 320)
crop_zone('banhos_master_e_2', 180, 400, 420, 590)
crop_zone('suite_master', 50, 360, 260, 590)
crop_zone('suite1_banho1_tecnico', 400, 240, 570, 510)
