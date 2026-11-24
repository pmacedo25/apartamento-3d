# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

# Inspect all text in the bottom half of page 0
print("=== TEXT IN SUÍTES / BANHOS REGION (y >= 380) ===")
for b in page0.get_text("blocks"):
    if b[1] >= 380 and b[3] <= 600 and b[0] >= 80 and b[2] <= 550:
        print(f"[{b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}] -> {b[4].strip().replace(chr(10), ' | ')}")

# Now let's inspect the enlarged pages:
# Page 4 is Suíte Master
# Page 5 is Suíte 1
# Page 6 is Suíte 2
# Page 9 is Banho Master
# Page 11 is Banho 2

for p_num in [4, 6, 9, 11]:
    p = doc[p_num]
    print(f"\n=== PAGE {p_num} TEXT ===")
    for b in p.get_text("blocks"):
        txt = b[4].strip()
        if len(txt) > 0 and not "CONSTRUCOMPANY" in txt and not "CREA" in txt and not "ART" in txt:
            print(f"  P{p_num} [{b[0]:.1f}, {b[1]:.1f}] -> {txt.replace(chr(10), ' | ')}")
