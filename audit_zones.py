import pdfplumber
import json

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

zones = [
    {"name": "1. Hall de Entrada & Lavabo", "x": (8.5, 13.0), "z": (0.4, 3.5)},
    {"name": "2. Cozinha & Servico", "x": (0.8, 8.8), "z": (0.4, 2.5)},
    {"name": "3. Sala de Estar/Jantar", "x": (3.8, 10.5), "z": (2.2, 7.0)},
    {"name": "4. Terraco Gourmet", "x": (0.3, 4.2), "z": (2.2, 7.0)},
    {"name": "5. Circulacao Intima", "x": (7.0, 10.5), "z": (6.7, 8.5)},
    {"name": "6. Suite 1 & Banho 1", "x": (10.2, 13.5), "z": (3.2, 8.0)},
    {"name": "7. Terraco Tecnico", "x": (10.2, 13.5), "z": (7.7, 9.4)},
    {"name": "8. Suite 2 & Banho 2", "x": (6.2, 10.5), "z": (8.2, 11.2)},
    {"name": "9. Suite Master & Banho Master", "x": (0.8, 6.5), "z": (6.7, 11.2)},
]

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    for z in zones:
        print(f"\n=======================================================")
        print(f"ZONE: {z['name']}")
        print(f"Bounds: X in {z['x']}, Z in {z['z']}")
        print(f"=======================================================")
        
        # Walls
        zone_lines = []
        for l in p0.lines:
            x1 = round((l['x0'] - X_ORIG) / SCALE, 2)
            z1 = round((l['top'] - Y_ORIG) / SCALE, 2)
            x2 = round((l['x1'] - X_ORIG) / SCALE, 2)
            z2 = round((l['bottom'] - Y_ORIG) / SCALE, 2)
            w = l.get('width', 0)
            c = l.get('stroking_color')
            if (z['x'][0] <= x1 <= z['x'][1] and z['z'][0] <= z1 <= z['z'][1]) or \
               (z['x'][0] <= x2 <= z['x'][1] and z['z'][0] <= z2 <= z['z'][1]):
                length = ((x2 - x1)**2 + (z2 - z1)**2)**0.5
                if length >= 0.5:
                    zone_lines.append((x1, z1, x2, z2, round(length, 2), w, c))
                    
        # Group identical or near-identical lines
        unique_segments = []
        for zl in zone_lines:
            p1 = (zl[0], zl[1])
            p2 = (zl[2], zl[3])
            # normalize direction
            if p1 > p2: p1, p2 = p2, p1
            if not any(abs(s[0][0]-p1[0])<0.08 and abs(s[0][1]-p1[1])<0.08 and abs(s[1][0]-p2[0])<0.08 and abs(s[1][1]-p2[1])<0.08 for s in unique_segments):
                unique_segments.append((p1, p2, zl[4]))
                
        print(f"Distinct wall segments found: {len(unique_segments)}")
        for s in sorted(unique_segments, key=lambda x: -x[2])[:12]:
            print(f"  Segment: ({s[0][0]:5.2f}, {s[0][1]:5.2f}) -> ({s[1][0]:5.2f}, {s[1][1]:5.2f}) length = {s[2]:4.2f}m")
