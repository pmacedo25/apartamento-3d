# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')

pages_to_inspect = {
    4: "Suíte Master e Banho Master",
    5: "Suíte 2 e Banho 2",
    6: "Suíte 1, Banho 1 e Terraço Técnico",
    7: "Living, Lavabo e Circulação",
    8: "Terraço Gourmet",
    9: "Cozinha e Área de Serviço"
}

for page_num, title in pages_to_inspect.items():
    page = doc[page_num]
    text_instances = page.get_text("blocks")
    print(f"\n=======================================================")
    print(f"PAGE {page_num}: {title} (Total blocks: {len(text_instances)})")
    print(f"=======================================================")
    
    # Filter text blocks with cotas or architectural names
    for b in text_instances:
        txt = b[4].strip()
        # Look for numbers with commas or dots (cotas), or room/wall labels
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        for l in lines:
            if any(term in l.lower() for term in ["suíte", "banho", "living", "dormitório", "closet", "cozinha", "serviço", "lavabo", "pilar", "shaft", "porta", "janela", "esquadria", "cuba", "bancada", "tanque", "alvenaria", "drywall", "h="]):
                print(f"  [LABEL] {l} (at x={b[0]:.1f}, y={b[1]:.1f})")
            elif any(c in l for c in [",", "."]) and len(l) <= 8 and any(char.isdigit() for char in l):
                print(f"  [COTA]  {l} (at x={b[0]:.1f}, y={b[1]:.1f})")
