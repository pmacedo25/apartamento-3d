# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')

print("=== CHECKING PAGE 0 TEXT DETAILS ===")
page0 = doc[0]
for b in page0.get_text("blocks"):
    txt = b[4].strip()
    if any(k in txt.lower() for k in ["hall", "lavabo", "roupeiro", "circ", "suíte", "banho", "cozinha", "serviço", "terraço", "living", "técnico", "pilar", "shaft", "p-", "j-"]):
        print(f"[{b[0]:.1f}, {b[1]:.1f}] -> {txt.replace(chr(10), ' | ')}")
