import pdfplumber
import json

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Scale: 37.79527559 points per meter
    SCALE = 37.795275590551185
    
    # Let's inspect all blue rects (drywall)
    drywalls = []
    for r in p0.rects:
        c = r.get('non_stroking_color')
        # Blue color for drywall: (0.0, 0.496..., 1.0)
        if isinstance(c, (list, tuple)) and len(c) == 3:
            if c[0] < 0.1 and c[1] > 0.4 and c[2] > 0.9:
                drywalls.append({
                    'x': (r['x0']) / SCALE,
                    'y': (r['top']) / SCALE,
                    'w': (r['width']) / SCALE,
                    'h': (r['height']) / SCALE
                })
                
    # Acoustic block masonry: (1.0, 0.75, 0.496)
    acoustic_blocks = []
    for r in p0.rects:
        c = r.get('non_stroking_color')
        if isinstance(c, (list, tuple)) and len(c) == 3:
            if c[0] > 0.9 and c[1] > 0.7 and c[2] < 0.6:
                acoustic_blocks.append({
                    'x': (r['x0']) / SCALE,
                    'y': (r['top']) / SCALE,
                    'w': (r['width']) / SCALE,
                    'h': (r['height']) / SCALE
                })
                
    print(f"Extracted {len(drywalls)} drywall segments")
    print(f"Extracted {len(acoustic_blocks)} acoustic block segments")
    if drywalls:
        print("Sample drywall:", drywalls[0])
    if acoustic_blocks:
        print("Sample acoustic block:", acoustic_blocks[0])
