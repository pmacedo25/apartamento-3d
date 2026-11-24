from PIL import Image
import pdfplumber

# Scale: 37.79527559 points per meter
SCALE = 37.795275590551185
DPI = 300
PT_TO_PX = DPI / 72.0  # 300 / 72 = 4.16666667 px per point

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    # Find exact lines defining apartment outer perimeter
    # Let's inspect the lines around top (145-165 pt), bottom (585-610 pt), left (50-80 pt), right (540-570 pt)
    top_walls = [l for l in p0.lines if 145 <= l['top'] <= 165 and abs(l['top'] - l['bottom']) < 1.0]
    bottom_walls = [l for l in p0.lines if 585 <= l['top'] <= 610 and abs(l['top'] - l['bottom']) < 1.0]
    left_walls = [l for l in p0.lines if 50 <= l['x0'] <= 80 and abs(l['x0'] - l['x1']) < 1.0]
    right_walls = [l for l in p0.lines if 535 <= l['x0'] <= 568 and abs(l['x0'] - l['x1']) < 1.0]
    
    print(f"Top wall lines count: {len(top_walls)}, y min={min(l['top'] for l in top_walls):.2f}, y max={max(l['top'] for l in top_walls):.2f}")
    print(f"Bottom wall lines count: {len(bottom_walls)}, y min={min(l['top'] for l in bottom_walls):.2f}, y max={max(l['top'] for l in bottom_walls):.2f}")
    print(f"Left wall lines count: {len(left_walls)}, x min={min(l['x0'] for l in left_walls):.2f}, x max={max(l['x0'] for l in left_walls):.2f}")
    print(f"Right wall lines count: {len(right_walls)}, x min={min(l['x0'] for l in right_walls):.2f}, x max={max(l['x0'] for l in right_walls):.2f}")

    # The actual apartment envelope:
    min_x_pt = min(l['x0'] for l in left_walls)
    max_x_pt = max(l['x0'] for l in right_walls)
    min_y_pt = min(l['top'] for l in top_walls)
    max_y_pt = max(l['top'] for l in bottom_walls)
    
    print(f"\nApartment envelope in PT: x=[{min_x_pt:.2f}, {max_x_pt:.2f}], y=[{min_y_pt:.2f}, {max_y_pt:.2f}]")
    width_m = (max_x_pt - min_x_pt) / SCALE
    height_m = (max_y_pt - min_y_pt) / SCALE
    print(f"Apartment envelope in METERS: width = {width_m:.3f} m, depth = {height_m:.3f} m")
