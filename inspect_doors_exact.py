import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Let's inspect door 7.03, 7.43 (Suite Master door)
    # door 8.00, 8.39 (Suite 2 door)
    # door 5.26, 8.44 (Banho Master door)
    # door 7.13, 8.52 (Banho 2 door)
    
    # Let's check lines around x in [6.5, 8.5] and z in [7.0, 9.2]
    print("--- LINES AROUND SUITE 2 AND BANHO 2 DOORS ---")
    door_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X_ORIG) / SCALE
        z1 = (l['top'] - Y_ORIG) / SCALE
        x2 = (l['x1'] - X_ORIG) / SCALE
        z2 = (l['bottom'] - Y_ORIG) / SCALE
        if 6.0 <= x1 <= 9.0 and 7.0 <= z1 <= 9.5:
            length = ((x2 - x1)**2 + (z2 - z1)**2)**0.5
            if length > 0.1:
                door_lines.append((round(x1, 2), round(z1, 2), round(x2, 2), round(z2, 2), round(length, 2)))
                
    for dl in sorted(door_lines, key=lambda x: (x[1], x[0])):
        print(f"Line from ({dl[0]:5.2f}, {dl[1]:5.2f}) to ({dl[2]:5.2f}, {dl[3]:5.2f}) len={dl[4]:4.2f}m")
