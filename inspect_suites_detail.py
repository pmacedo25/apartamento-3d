import pdfplumber

SCALE = 37.795275590551185
X_ORIG = 50.0
Y_ORIG = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    # Door swings are circular arcs in curves!
    curves = [c for c in p0.curves if 350 <= c['top'] <= 600 and 100 <= c['x0'] <= 450]
    print(f"Total curves (door swings) in region: {len(curves)}")
    for i, c in enumerate(curves):
        # Door radius in meters:
        w_m = c['width'] / SCALE
        h_m = c['height'] / SCALE
        x_m = (c['x0'] - X_ORIG) / SCALE
        z_m = (c['top'] - Y_ORIG) / SCALE
        print(f"Door swing {i}: x={x_m:.2f}m, z={z_m:.2f}m, span = {w_m:.2f}m x {h_m:.2f}m")
