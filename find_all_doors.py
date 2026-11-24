import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    # In AutoCAD, doors are drawn as 90-degree circular arcs with radius around 0.60 to 0.90 meters!
    # In PDF points, radius of 0.70m is ~26.5 pt, 0.80m is ~30.2 pt.
    # The bounding box width and height of a 90-deg arc is approximately radius!
    door_arcs = []
    for c in p0.curves:
        w_pt = c['width']
        h_pt = c['height']
        w_m = w_pt / SCALE
        h_m = h_pt / SCALE
        # Check if radius is between 0.55m and 0.95m
        if 0.55 <= w_m <= 0.95 and 0.55 <= h_m <= 0.95:
            xm = (c['x0'] - X_ORIG) / SCALE
            zm = (c['top'] - Y_ORIG) / SCALE
            door_arcs.append((xm, zm, w_m, h_m))
            
    print(f"Found {len(door_arcs)} major door arcs in the whole apartment:")
    for d in sorted(door_arcs, key=lambda x: (x[1], x[0])):
        print(f"Door arc at x={d[0]:.2f}m, z={d[1]:.2f}m (radius: {d[2]:.2f}m x {d[3]:.2f}m)")
