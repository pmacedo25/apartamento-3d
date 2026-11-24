# -*- coding: utf-8 -*-
import fitz, json

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# Page 0 has exact vector drawings of all architectural elements.
# Let's inspect all text and numbers (cotas) on Page 0 to see every measurement given in the plan.
cotas = []
for w in page0.get_text('words'):
    txt = w[4]
    # Check if number like '120', '80', '70', '270', '140', '1.20', etc.
    if any(c.isdigit() for c in txt):
        cotas.append((txt, round(w[0], 1), round(w[1], 1), round(w[2], 1), round(w[3], 1)))

print(f"Total numeric annotations/cotas on page 0: {len(cotas)}")
for c in cotas[:30]:
    print(c)
