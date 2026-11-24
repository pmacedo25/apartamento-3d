import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    print("--- LINES AROUND BANHO MASTER AND SUITE MASTER ---")
    master_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X_ORIG) / SCALE
        z1 = (l['top'] - Y_ORIG) / SCALE
        x2 = (l['x1'] - X_ORIG) / SCALE
        z2 = (l['bottom'] - Y_ORIG) / SCALE
        if 3.8 <= x1 <= 6.5 and 6.5 <= z1 <= 11.0:
            length = ((x2 - x1)**2 + (z2 - z1)**2)**0.5
            if length > 0.1:
                master_lines.append((round(x1, 2), round(z1, 2), round(x2, 2), round(z2, 2), round(length, 2)))
                
    for ml in sorted(master_lines, key=lambda x: (x[1], x[0])):
        print(f"Line from ({ml[0]:5.2f}, {ml[1]:5.2f}) to ({ml[2]:5.2f}, {ml[3]:5.2f}) len={ml[4]:4.2f}m")
