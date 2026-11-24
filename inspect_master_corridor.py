import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    print("--- LINES IN CORRIDOR / ENTRY OF SUITE MASTER ---")
    corridor_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X_ORIG) / SCALE
        z1 = (l['top'] - Y_ORIG) / SCALE
        x2 = (l['x1'] - X_ORIG) / SCALE
        z2 = (l['bottom'] - Y_ORIG) / SCALE
        if 4.0 <= x1 <= 8.5 and 6.6 <= z1 <= 8.5:
            length = ((x2 - x1)**2 + (z2 - z1)**2)**0.5
            if length > 0.15:
                corridor_lines.append((round(x1, 2), round(z1, 2), round(x2, 2), round(z2, 2), round(length, 2)))
                
    for cl in sorted(corridor_lines, key=lambda x: (x[1], x[0])):
        print(f"Line from ({cl[0]:5.2f}, {cl[1]:5.2f}) to ({cl[2]:5.2f}, {cl[3]:5.2f}) len={cl[4]:4.2f}m")
