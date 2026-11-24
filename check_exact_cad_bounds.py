# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# Let's inspect the drawings on page 0
drawings = page0.get_drawings()

# Let's find rects or lines in the apartment region (x from 50 to 580, y from 100 to 600)
# Look for walls by line color or rect fill
# The legend on page 0 shows:
# Drywall: blue (0.0, 0.496, 1.0)
# Alvenaria bloco: peach/orange (1.0, 0.75, 0.496)
# Pilar concreto: diagonal hatch
# Shaft/vazio: 'X' rectangle

blue_paths = []
peach_paths = []

for d in drawings:
    rect = d['rect']
    if 50 <= rect.x0 <= 580 and 100 <= rect.y0 <= 600:
        color = d.get('color')
        fill = d.get('fill')
        if color:
            r, g, b = color[:3]
            if b > 0.8 and r < 0.2: # Blue drywall
                blue_paths.append((rect, d))
            elif r > 0.8 and g > 0.6 and b < 0.6: # Peach masonry
                peach_paths.append((rect, d))

print(f"Found {len(blue_paths)} blue drywall paths, {len(peach_paths)} peach masonry paths.")

# Let's find min and max x and y of these paths:
all_pts = []
for rect, d in blue_paths + peach_paths:
    all_pts.extend([(rect.x0, rect.y0), (rect.x1, rect.y1)])

min_x = min(p[0] for p in all_pts)
max_x = max(p[0] for p in all_pts)
min_y = min(p[1] for p in all_pts)
max_y = max(p[1] for p in all_pts)

print(f"Apartment walls extent in PDF points: X: [{min_x:.1f}, {max_x:.1f}], Y: [{min_y:.1f}, {max_y:.1f}]")
print(f"Width = {max_x - min_x:.1f} pt, Height = {max_y - min_y:.1f} pt")
