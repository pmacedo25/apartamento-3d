import pdfplumber

with pdfplumber.open(r'C:\Users\sport\Downloads\CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf') as pdf:
    p0 = pdf.pages[0]
    words = p0.extract_words()
    print("Room labels found on Page 1:")
    for w in words:
        text = w['text'].upper()
        if any(k in text for k in ['HALL', 'LAVABO', 'COZINHA', 'ÁREA', 'SERVIÇO', 'TERRAÇO', 'SALA', 'JANTAR', 'CIRCULAÇÃO', 'SUÍTE', 'BANHO', 'TÉCNICO']):
            print(f"{w['text']:<18} x0={w['x0']:<6.1f} top={w['top']:<6.1f} x1={w['x1']:<6.1f} bottom={w['bottom']:<6.1f}")
