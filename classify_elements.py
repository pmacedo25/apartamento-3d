import pdfplumber
import json

SCALE = 37.795275590551185
X_ORIGIN = 50.0
Y_ORIGIN = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Let's inspect all rects (drywalls, columns, shafts)
    rects_data = []
    for r in p0.rects:
        if 135 <= r['top'] <= 565 and 50 <= r['x0'] <= 560:
            c = r.get('non_stroking_color')
            rect_type = 'generic'
            if isinstance(c, (list, tuple)) and len(c) == 3:
                if c[0] < 0.1 and c[1] > 0.4 and c[2] > 0.9:
                    rect_type = 'drywall'
                elif c[0] > 0.9 and c[1] > 0.7 and c[2] < 0.6:
                    rect_type = 'acoustic_masonry'
                elif c[0] > 0.4 and c[1] < 0.1 and c[2] > 0.5:
                    rect_type = 'fill'
                elif c[0] < 0.5 and c[1] > 0.8 and c[2] < 0.1:
                    rect_type = 'carenagem'
                elif c[0] > 0.9 and c[1] > 0.4 and c[2] < 0.1:
                    rect_type = 'ventilation'
                elif abs(c[0] - c[1]) < 0.05 and abs(c[1] - c[2]) < 0.05:
                    rect_type = 'concrete_pillar_or_shaft'
            
            rects_data.append({
                'type': rect_type,
                'x': round((r['x0'] - X_ORIGIN) / SCALE, 3),
                'z': round((r['top'] - Y_ORIGIN) / SCALE, 3),
                'w': round(r['width'] / SCALE, 3),
                'd': round(r['height'] / SCALE, 3),
                'color': c
            })
            
    print(f"Extracted {len(rects_data)} classified rects")
    counts = {}
    for r in rects_data:
        counts[r['type']] = counts.get(r['type'], 0) + 1
    print("Counts by type:", counts)
    
    # Save to json for analysis
    with open(r'c:\Users\sport\Documents\apartamento\rects_classified.json', 'w') as f:
        json.dump(rects_data, f, indent=2)
