import pdfplumber
import json

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    SCALE = 37.795275590551185
    
    # Let's extract all text with exact coordinates
    words = p0.extract_words()
    
    # Let's see all text on the floorplan
    apt_words = [w for w in words if 120 <= w['top'] <= 600]
    print(f"Total words in apartment: {len(apt_words)}")
    for w in apt_words:
        print(f"{w['text']:<25} x={w['x0']/SCALE:6.2f}m, y={w['top']/SCALE:6.2f}m")
