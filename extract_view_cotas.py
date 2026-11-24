# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')

for pno in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    page = doc[pno]
    title = ""
    for b in page.get_text('blocks'):
        if any(w in b[4] for w in ['SUÍTE', 'SALA', 'TERRAÇO', 'BANHO', 'LAVABO', 'COZINHA', 'ÁREA']):
            title = b[4].strip().replace('\n', ' ')
            break
    
    cotas = []
    for w in page.get_text('words'):
        txt = w[4]
        if any(c.isdigit() for c in txt):
            cotas.append(txt)
    print(f"Page {pno:2d} ({title}): Cotas = {cotas[:25]}")
