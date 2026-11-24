# -*- coding: utf-8 -*-
import fitz

doc = fitz.open(r'C:\Users\sport\.gemini\antigravity\brain\0f93f6ea-672c-4358-9aaa-1853d3483ea0\.user_uploaded\media_1795534903218_fc417efc.pdf')
page0 = doc[0]

PT_TO_M = 13.50 / 510.0
X0_PT = 68.0
Z0_PT = 136.0

def to_m(x_pt, y_pt):
    return (round((x_pt - X0_PT) * PT_TO_M, 2), round((y_pt - Z0_PT) * PT_TO_M, 2))

# Verify Suíte Master window on West wall:
# In zone_suite_master: window is between y=430 and y=490 pt, x=104.8 pt
print("Suíte Master West Window:", to_m(104.8, 430), to_m(104.8, 490))

# Verify Suíte 1 South Window towards Terraço Técnico:
# In zone_suite1: window is at y=433.8 pt, between x=465 and x=535 pt
print("Suíte 1 South Window towards AC terrace:", to_m(465, 433.8), to_m(535, 433.8))

# Verify Banho Master double vanity:
# along west wall (x=221.4 pt), from y=453.8 to 511.9 pt
print("Banho Master Double Vanity:", to_m(221.4, 453.8), to_m(238.3, 511.9))

# Verify Terraço Gourmet barbecue counter:
# along north wall (y=217.7 pt), from x=104.8 to 154.8 pt
print("Terraço Gourmet Barbecue Counter:", to_m(104.8, 217.7), to_m(154.8, 240.4))

# Verify Cozinha North Sink Counter:
# along north wall (y=142.2 pt), from x=221.4 to 399.0 pt
print("Cozinha North Sink Counter:", to_m(221.4, 142.2), to_m(399.0, 160.0))
