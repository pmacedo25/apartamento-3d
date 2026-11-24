import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Let's inspect all lines in this specific bathroom cluster
    cluster_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X_ORIG) / SCALE
        z1 = (l['top'] - Y_ORIG) / SCALE
        x2 = (l['x1'] - X_ORIG) / SCALE
        z2 = (l['bottom'] - Y_ORIG) / SCALE
        
        # Check if line is within [3.5, 9.0] and [6.5, 11.2]
        if (3.5 <= x1 <= 9.0 or 3.5 <= x2 <= 9.0) and (6.5 <= z1 <= 11.2 or 6.5 <= z2 <= 11.2):
            length = ((x2 - x1)**2 + (z2 - z1)**2)**0.5
            if length >= 0.2: # filter tiny ticks
                cluster_lines.append({
                    'x1': round(x1, 2), 'z1': round(z1, 2),
                    'x2': round(x2, 2), 'z2': round(z2, 2),
                    'len': round(length, 2),
                    'w': l.get('width', 0),
                    'color': l.get('stroking_color')
                })
                
    # Sort by length descending
    cluster_lines.sort(key=lambda x: -x['len'])
    print(f"Total lines in cluster: {len(cluster_lines)}")
    for l in cluster_lines[:45]:
        print(f"Line ({l['x1']:5.2f}, {l['z1']:5.2f}) -> ({l['x2']:5.2f}, {l['z2']:5.2f}) len={l['len']:4.2f}m w={l['w']} c={l['color']}")
