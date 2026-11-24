# -*- coding: utf-8 -*-
import pdfplumber

SCALE = 37.77777777777778
X0 = 68.0
Z0 = 136.0

with pdfplumber.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Pillars are drawn with diagonal hatch lines.
    # Rectangles with diagonal lines inside:
    # Let's inspect small diagonal lines
    diag_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X0) / SCALE
        z1 = (l['top'] - Z0) / SCALE
        x2 = (l['x1'] - X0) / SCALE
        z2 = (l['bottom'] - Z0) / SCALE
        dx = abs(x2 - x1)
        dz = abs(z2 - z1)
        if 0.05 <= dx <= 0.40 and 0.05 <= dz <= 0.40 and abs(dx - dz) < 0.05:
            diag_lines.append((round(min(x1, x2), 2), round(max(x1, x2), 2), round(min(z1, z2), 2), round(max(z1, z2), 2)))
            
    print(f"Total diagonal hatch lines found: {len(diag_lines)}")
    # Cluster them by proximity to find pillars!
    clusters = []
    for dl in diag_lines:
        cx = (dl[0] + dl[1]) / 2.0
        cz = (dl[2] + dl[3]) / 2.0
        found = False
        for cl in clusters:
            if abs(cl['cx'] - cx) < 0.45 and abs(cl['cz'] - cz) < 0.45:
                cl['pts'].append((cx, cz))
                cl['min_x'] = min(cl['min_x'], dl[0])
                cl['max_x'] = max(cl['max_x'], dl[1])
                cl['min_z'] = min(cl['min_z'], dl[2])
                cl['max_z'] = max(cl['max_z'], dl[3])
                cl['cx'] = (cl['min_x'] + cl['max_x']) / 2.0
                cl['cz'] = (cl['min_z'] + cl['max_z']) / 2.0
                found = True
                break
        if not found:
            clusters.append({
                'min_x': dl[0], 'max_x': dl[1],
                'min_z': dl[2], 'max_z': dl[3],
                'cx': cx, 'cz': cz,
                'pts': [(cx, cz)]
            })
            
    pillars = [c for c in clusters if len(c['pts']) >= 3]
    print(f"\nFound {len(pillars)} structural pillars (pilares de concreto):")
    pillars.sort(key=lambda p: (p['cz'], p['cx']))
    for i, p in enumerate(pillars):
        w = round(p['max_x'] - p['min_x'], 2)
        d = round(p['max_z'] - p['min_z'], 2)
        cx = round((p['min_x'] + p['max_x']) / 2.0, 2)
        cz = round((p['min_z'] + p['max_z']) / 2.0, 2)
        print(f"Pilar P{i+1:02d}: Center at ({cx:5.2f}, {cz:5.2f}) | W={w:4.2f}m, D={d:4.2f}m | [{p['min_x']:.2f}..{p['max_x']:.2f}, {p['min_z']:.2f}..{p['max_z']:.2f}] (hatches={len(p['pts'])})")
