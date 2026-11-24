import pdfplumber
import json
import math

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # 1. Extract all door arcs (curves with radius between 0.55m and 1.0m)
    door_arcs = []
    for c in p0.curves:
        w_m = c['width'] / SCALE
        h_m = c['height'] / SCALE
        if 0.55 <= w_m <= 1.0 and 0.55 <= h_m <= 1.0:
            xm = (c['x0'] - X_ORIG) / SCALE
            zm = (c['top'] - Y_ORIG) / SCALE
            # avoid duplicates (curves often duplicated for fill/stroke)
            if not any(abs(d['x'] - xm) < 0.05 and abs(d['z'] - zm) < 0.05 for d in door_arcs):
                door_arcs.append({'x': round(xm, 2), 'z': round(zm, 2), 'w': round(w_m, 2), 'h': round(h_m, 2)})
                
    door_arcs.sort(key=lambda d: (d['z'], d['x']))
    print(f"=== GROUND TRUTH DOORS DETECTED IN PDF ({len(door_arcs)}) ===")
    for idx, d in enumerate(door_arcs):
        print(f"Door {idx+1:2d}: at X = {d['x']:5.2f}m, Z = {d['z']:5.2f}m | Span = {d['w']:4.2f}m x {d['h']:4.2f}m")

    # 2. Extract classified rectangles (pilares, drywall, alvenaria acústica, shafts, dutos)
    rects_by_type = {}
    for r in p0.rects:
        if 135 <= r['top'] <= 565 and 50 <= r['x0'] <= 560:
            c = r.get('non_stroking_color')
            rtype = 'Outro'
            if isinstance(c, (list, tuple)) and len(c) == 3:
                if c[0] < 0.1 and c[1] > 0.4 and c[2] > 0.9: rtype = 'Drywall'
                elif c[0] > 0.9 and c[1] > 0.7 and c[2] < 0.6: rtype = 'Alvenaria Acustica'
                elif c[0] < 0.5 and c[1] > 0.8 and c[2] < 0.1: rtype = 'Carenagem'
                elif c[0] > 0.9 and c[1] > 0.4 and c[2] < 0.1: rtype = 'Ventilacao'
                elif abs(c[0] - c[1]) < 0.05 and abs(c[1] - c[2]) < 0.05: rtype = 'Pilar/Shaft'
            
            xm = round((r['x0'] - X_ORIG) / SCALE, 2)
            zm = round((r['top'] - Y_ORIG) / SCALE, 2)
            wm = round(r['width'] / SCALE, 2)
            hm = round(r['height'] / SCALE, 2)
            rects_by_type.setdefault(rtype, []).append({'x': xm, 'z': zm, 'w': wm, 'h': hm})

    print("\n=== CLASSIFIED ELEMENTS (COLUMNS, SHAFTS, DRYWALL) ===")
    for t, items in rects_by_type.items():
        print(f"-> {t}: {len(items)} items")

    # 3. Extract major long wall lines (>= 0.8m)
    lines_major = []
    for l in p0.lines:
        if 135 <= l['top'] <= 565 and 50 <= l['x0'] <= 560:
            w = l.get('width', 0)
            c = l.get('stroking_color')
            if w >= 0.24 or c == (0.0, 0.0, 0.0):
                x1 = round((l['x0'] - X_ORIG) / SCALE, 2)
                z1 = round((l['top'] - Y_ORIG) / SCALE, 2)
                x2 = round((l['x1'] - X_ORIG) / SCALE, 2)
                z2 = round((l['bottom'] - Y_ORIG) / SCALE, 2)
                length = math.hypot(x2 - x1, z2 - z1)
                if length >= 0.80:
                    lines_major.append({'x1': x1, 'z1': z1, 'x2': x2, 'z2': z2, 'len': round(length, 2)})

    print(f"\n=== MAJOR WALL LINES DETECTED ({len(lines_major)}) ===")
    # Group by orientation
    horizs = [l for l in lines_major if abs(l['z1'] - l['z2']) < 0.05]
    verts = [l for l in lines_major if abs(l['x1'] - l['x2']) < 0.05]
    print(f"Horizontal wall lines: {len(horizs)}")
    print(f"Vertical wall lines: {len(verts)}")
