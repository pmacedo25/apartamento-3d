import json

with open(r'c:\Users\sport\Documents\apartamento\wall_lines.json') as f:
    lines = json.load(f)

print("Sample long wall lines:")
for l in lines[:30]:
    is_horiz = abs(l['z1'] - l['z2']) < 0.05
    is_vert = abs(l['x1'] - l['x2']) < 0.05
    orient = "HORIZ" if is_horiz else ("VERT" if is_vert else "DIAG")
    print(f"{orient:<6} ({l['x1']:5.2f}, {l['z1']:5.2f}) -> ({l['x2']:5.2f}, {l['z2']:5.2f}) len={l['len']:4.2f}m")
