# -*- coding: utf-8 -*-
import pdfplumber

SCALE = 37.77777777777778
X0 = 68.0
Z0 = 136.0

with pdfplumber.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf') as pdf:
    p0 = pdf.pages[0]
    
    # Extract all horizontal lines in meters
    h_lines = []
    v_lines = []
    for l in p0.lines:
        x1 = (l['x0'] - X0) / SCALE
        z1 = (l['top'] - Z0) / SCALE
        x2 = (l['x1'] - X0) / SCALE
        z2 = (l['bottom'] - Z0) / SCALE
        
        # Horizontal
        if abs(z1 - z2) < 0.03 and abs(x2 - x1) > 0.15:
            h_lines.append((round(min(x1, x2), 2), round(max(x1, x2), 2), round(z1, 2), round(abs(x2 - x1), 2)))
        elif abs(x1 - x2) < 0.03 and abs(z2 - z1) > 0.15:
            v_lines.append((round(min(z1, z2), 2), round(max(z1, z2), 2), round(x1, 2), round(abs(z2 - z1), 2)))
            
    print("=== HORIZONTAL WALL LINES (Z between 6.0 and 9.5) ===")
    for hl in sorted(h_lines, key=lambda l: (l[2], l[0])):
        if 6.0 <= hl[2] <= 9.5 and 4.0 <= hl[0] <= 9.0:
            print(f"H-Line at Z={hl[2]:5.2f}m | X: {hl[0]:5.2f} -> {hl[1]:5.2f}m (len={hl[3]:4.2f}m)")
            
    print("\n=== VERTICAL WALL LINES (X between 4.0 and 9.0) ===")
    for vl in sorted(v_lines, key=lambda l: (l[2], l[0])):
        if 4.0 <= vl[2] <= 9.0 and 6.0 <= vl[0] <= 9.5:
            print(f"V-Line at X={vl[2]:5.2f}m | Z: {vl[0]:5.2f} -> {vl[1]:5.2f}m (len={vl[3]:4.2f}m)")
