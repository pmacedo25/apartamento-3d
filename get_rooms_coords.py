import pdfplumber

SCALE = 37.795275590551185
X_ORIGIN = 50.0
Y_ORIGIN = 135.0

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    words = p0.extract_words()
    apt_words = [w for w in words if 135 <= w['top'] <= 565 and 50 <= w['x0'] <= 560]
    for w in apt_words:
        x_m = (w['x0'] - X_ORIGIN) / SCALE
        z_m = (w['top'] - Y_ORIGIN) / SCALE
        text = w['text'].upper()
        if any(k in text for k in ['HALL', 'LAVABO', 'COZINHA', 'ÁREA', 'SERVIÇO', 'TERRAÇO', 'SALA', 'CIRCULAÇÃO', 'SUÍTE', 'BANHO', 'TÉCNICO']):
            print(f"{w['text']:<15} X = {x_m:5.2f}m, Z = {z_m:5.2f}m")
