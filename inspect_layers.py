import pdfplumber

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    print(f"Total lines: {len(p0.lines)}")
    print(f"Total curves: {len(p0.curves)}")
    print(f"Total rects: {len(p0.rects)}")
    
    # Check colors used in lines
    stroke_colors = set()
    for l in p0.lines:
        c = l.get('stroking_color')
        if isinstance(c, (list, tuple)):
            stroke_colors.add(tuple(c))
        else:
            stroke_colors.add(c)
    print("Stroke colors in lines:", stroke_colors)
    
    # Check rect fills
    fill_colors = set()
    for r in p0.rects:
        c = r.get('non_stroking_color')
        if isinstance(c, (list, tuple)):
            fill_colors.add(tuple(c))
        else:
            fill_colors.add(c)
    print("Fill colors in rects:", fill_colors)
