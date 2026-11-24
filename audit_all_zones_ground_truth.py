# -*- coding: utf-8 -*-
import pdfplumber

SCALE = 37.77777777777778
X0 = 68.0
Z0 = 136.0

with pdfplumber.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf') as pdf:
    p0 = pdf.pages[0]
    
    h_lines = []
    v_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X0) / SCALE
        z1 = (l['top'] - Z0) / SCALE
        x2 = (l['x1'] - X0) / SCALE
        z2 = (l['bottom'] - Z0) / SCALE
        
        # Horizontal
        if abs(z1 - z2) < 0.03 and abs(x2 - x1) > 0.20:
            h_lines.append((round(min(x1, x2), 2), round(max(x1, x2), 2), round(z1, 2), round(abs(x2 - x1), 2)))
        elif abs(x1 - x2) < 0.03 and abs(z2 - z1) > 0.20:
            v_lines.append((round(min(z1, z2), 2), round(max(z1, z2), 2), round(x1, 2), round(abs(z2 - z1), 2)))

    def print_zone(name, x_min, x_max, z_min, z_max):
        print(f"\n=======================================================")
        print(f"ZONE: {name} (X: {x_min}..{x_max}, Z: {z_min}..{z_max})")
        print(f"=======================================================")
        # Distinct H lines
        hl = [l for l in h_lines if z_min <= l[2] <= z_max and not (l[1] < x_min or l[0] > x_max)]
        vl = [l for l in v_lines if x_min <= l[2] <= x_max and not (l[1] < z_min or l[0] > z_max)]
        
        # Dedup by rounded coord
        hl_dedup = {}
        for l in hl:
            key = round(l[2], 2)
            if key not in hl_dedup or l[3] > hl_dedup[key][3]:
                hl_dedup[key] = l
                
        vl_dedup = {}
        for l in vl:
            key = round(l[2], 2)
            if key not in vl_dedup or l[3] > vl_dedup[key][3]:
                vl_dedup[key] = l
                
        print(f"H-Lines ({len(hl_dedup)}):")
        for k in sorted(hl_dedup.keys()):
            l = hl_dedup[k]
            print(f"  Z = {l[2]:5.2f}m | X: {l[0]:5.2f} -> {l[1]:5.2f}m (len={l[3]:4.2f}m)")
            
        print(f"V-Lines ({len(vl_dedup)}):")
        for k in sorted(vl_dedup.keys()):
            l = vl_dedup[k]
            print(f"  X = {l[2]:5.2f}m | Z: {l[0]:5.2f} -> {l[1]:5.2f}m (len={l[3]:4.2f}m)")

    # 1. Cozinha & Área de Serviço
    print_zone("Cozinha & Serviço", 0.0, 4.20, 0.0, 2.50)
    
    # 2. Lavabo & Hall Social
    print_zone("Lavabo & Hall Social", 7.5, 13.5, 0.0, 3.50)
    
    # 3. Suíte 1 & Banho 1 & Terraço Técnico
    print_zone("Suíte 1 & Banho 1 & Técnico", 9.5, 13.5, 2.5, 9.5)
    
    # 4. Terraço Gourmet & Living
    print_zone("Terraço Gourmet & Living", 0.0, 10.5, 2.0, 6.80)
