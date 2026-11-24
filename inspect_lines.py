import pdfplumber

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    SCALE = 37.795275590551185
    
    # Legend starts around top = 650 (y ~ 17.2 m)
    # Apartment is roughly from top = 130 to top = 600 (y ~ 3.4 m to 15.8 m)
    # x roughly from x0 = 50 to 550 (x ~ 1.3 m to 14.5 m)
    
    apt_lines = []
    for l in p0.lines:
        if 120 < l['top'] < 610 and 120 < l['bottom'] < 610:
            if 50 < l['x0'] < 550 and 50 < l['x1'] < 550:
                apt_lines.append(l)
                
    print(f"Total lines in apartment area: {len(apt_lines)}")
    
    # Check orientation: horizontal vs vertical lines
    horizontals = [l for l in apt_lines if abs(l['top'] - l['bottom']) < 0.5]
    verticals = [l for l in apt_lines if abs(l['x0'] - l['x1']) < 0.5]
    diagonals = [l for l in apt_lines if abs(l['top'] - l['bottom']) >= 0.5 and abs(l['x0'] - l['x1']) >= 0.5]
    print(f"Horizontal lines: {len(horizontals)}")
    print(f"Vertical lines: {len(verticals)}")
    print(f"Diagonal / slant lines: {len(diagonals)}")
