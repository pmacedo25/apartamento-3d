# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')

pages = {
    9: "Banho Suíte Master",
    10: "Banho Suíte 1",
    11: "Banho Suíte 2",
    12: "Lavabo",
    13: "Cozinha",
    14: "Área de Serviço",
    15: "Terraço Gourmet"
}

for p_num, name in pages.items():
    page = doc[p_num]
    # Extract drawings and text
    print(f"\n============================\nPAGE {p_num}: {name}\n============================")
    # Get all text
    for b in page.get_text("blocks"):
        txt = b[4].strip()
        # Look for numbers (cotas in cm or m)
        for line in txt.split('\n'):
            line = line.strip()
            if any(char.isdigit() for char in line) and len(line) <= 10:
                print(f"  [{b[0]:.1f}, {b[1]:.1f}] -> {line}")
