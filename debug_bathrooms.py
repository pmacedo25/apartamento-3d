import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Let's find rects in the region
    rects = []
    for r in p0.rects:
        # In meters:
        xm = (r['x0'] - X_ORIG) / SCALE
        zm = (r['top'] - Y_ORIG) / SCALE
        wm = r['width'] / SCALE
        hm = r['height'] / SCALE
        c = r.get('non_stroking_color')
        if 3.0 <= xm <= 10.5 and 6.0 <= zm <= 11.5:
            rects.append({'xm': round(xm, 2), 'zm': round(zm, 2), 'wm': round(wm, 2), 'hm': round(hm, 2), 'color': c})
            
    print(f"Rects in region: {len(rects)}")
    for r in rects:
        print(r)
        
    # Let's inspect all thick lines (walls)
    thick_lines = []
    for l in p0.lines:
        xm1 = (l['x0'] - X_ORIG) / SCALE
        zm1 = (l['top'] - Y_ORIG) / SCALE
        xm2 = (l['x1'] - X_ORIG) / SCALE
        zm2 = (l['bottom'] - Y_ORIG) / SCALE
        w = l.get('width', 0)
        c = l.get('stroking_color')
        if (3.0 <= xm1 <= 10.5 and 6.0 <= zm1 <= 11.5) or (3.0 <= xm2 <= 10.5 and 6.0 <= zm2 <= 11.5):
            if w >= 0.24 or c == (0.0, 0.0, 0.0):
                thick_lines.append((round(xm1, 2), round(zm1, 2), round(xm2, 2), round(zm2, 2), w, c))
                
    print(f"\nThick lines (walls) in region: {len(thick_lines)}")
    # Print distinct wall segments
    unique_walls = sorted(list(set((l[0], l[1], l[2], l[3]) for l in thick_lines)))
    for uw in unique_walls[:40]:
        print(f"Wall line: ({uw[0]:5.2f}, {uw[1]:5.2f}) -> ({uw[2]:5.2f}, {uw[3]:5.2f})")
