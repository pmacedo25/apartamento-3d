# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# All vector drawings on page 0
drawings = page0.get_drawings()

def analyze_box(box_name, x0, y0, x1, y1):
    print(f"\n=======================================================")
    print(f"ANALYZING: {box_name} [x: {x0}..{x1}, y: {y0}..{y1}]")
    print(f"=======================================================")
    
    # Text inside box
    texts = []
    for b in page0.get_text("blocks"):
        if b[0] >= x0 - 10 and b[2] <= x1 + 10 and b[1] >= y0 - 10 and b[3] <= y1 + 10:
            texts.append(b[4].strip().replace('\n', ' '))
    print(f"Texts: {texts}")
    
    # Lines inside box
    horizontal_lines = []
    vertical_lines = []
    for d in drawings:
        r = d['rect']
        if r.x0 >= x0 - 5 and r.x1 <= x1 + 5 and r.y0 >= y0 - 5 and r.y1 <= y1 + 5:
            # check items
            for it in d.get('items', []):
                if it[0] == 'l': # line
                    p1, p2 = it[1], it[2]
                    # check if horizontal or vertical
                    if abs(p1.y - p2.y) < 1.0 and abs(p1.x - p2.x) > 5.0: # horizontal line
                        horizontal_lines.append((round(min(p1.x, p2.x), 1), round(max(p1.x, p2.x), 1), round(p1.y, 1)))
                    elif abs(p1.x - p2.x) < 1.0 and abs(p1.y - p2.y) > 5.0: # vertical line
                        vertical_lines.append((round(min(p1.y, p2.y), 1), round(max(p1.y, p2.y), 1), round(p1.x, 1)))
    
    # Sort and group lines
    # Dedup
    horizontal_lines = sorted(list(set(horizontal_lines)), key=lambda x: x[2])
    vertical_lines = sorted(list(set(vertical_lines)), key=lambda x: x[2])
    
    print(f"Distinct Horizontal Wall Lines ({len(horizontal_lines)}):")
    for l in horizontal_lines[:15]:
        print(f"  y = {l[2]:5.1f} | x from {l[0]:5.1f} to {l[1]:5.1f} (len = {l[1]-l[0]:5.1f} pt)")
    if len(horizontal_lines) > 15:
        print(f"  ... and {len(horizontal_lines)-15} more")
        
    print(f"Distinct Vertical Wall Lines ({len(vertical_lines)}):")
    for l in vertical_lines[:15]:
        print(f"  x = {l[2]:5.1f} | y from {l[0]:5.1f} to {l[1]:5.1f} (len = {l[1]-l[0]:5.1f} pt)")
    if len(vertical_lines) > 15:
        print(f"  ... and {len(vertical_lines)-15} more")

# 1. Cozinha & Área de Serviço
analyze_box("Cozinha & Área de Serviço", 80, 130, 410, 240)

# 2. Hall Social, Lavabo e Entrada
analyze_box("Hall Social & Lavabo", 400, 130, 560, 270)

# 3. Suíte Master, Closet e Banho Master
analyze_box("Suíte Master & Banho Master", 80, 420, 310, 580)

# 4. Suíte 2 e Banho 2
analyze_box("Suíte 2 & Banho 2", 290, 420, 460, 580)

# 5. Suíte 1, Banho 1 e Terraço Técnico
analyze_box("Suíte 1, Banho 1 & Terraço Técnico", 440, 260, 560, 500)

# 6. Circulação Íntima (Corredor)
analyze_box("Circulação Íntima", 280, 380, 450, 460)
