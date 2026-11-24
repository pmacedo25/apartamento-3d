import pdfplumber
import json

SCALE = 37.795275590551185
X_ORIGIN = 50.0
Y_ORIGIN = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # We look for thick black or grey lines (cut walls)
    # Line widths in PDF: 0.24, 0.36, 0.48, 0.6
    wall_lines = []
    for l in p0.lines:
        if 135 <= l['top'] <= 565 and 50 <= l['x0'] <= 560:
            w = l.get('width', 0)
            c = l.get('stroking_color')
            # Check if thick or black line
            if w >= 0.24 or c == (0.0, 0.0, 0.0):
                length = ((l['x1'] - l['x0'])**2 + (l['bottom'] - l['top'])**2)**0.5
                if length >= 5: # filter tiny hatches
                    wall_lines.append({
                        'x1': round((l['x0'] - X_ORIGIN) / SCALE, 3),
                        'z1': round((l['top'] - Y_ORIGIN) / SCALE, 3),
                        'x2': round((l['x1'] - X_ORIGIN) / SCALE, 3),
                        'z2': round((l['bottom'] - Y_ORIGIN) / SCALE, 3),
                        'w': round(w, 2),
                        'color': c,
                        'len': round(length / SCALE, 3)
                    })
                    
    print(f"Total significant lines: {len(wall_lines)}")
    # Find longest lines (main dividing walls and exterior walls)
    long_lines = [l for l in wall_lines if l['len'] >= 1.0]
    print(f"Long lines (>= 1m): {len(long_lines)}")
    
    with open(r'c:\Users\sport\Documents\apartamento\wall_lines.json', 'w') as f:
        json.dump(long_lines, f, indent=2)
