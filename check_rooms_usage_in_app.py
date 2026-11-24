# -*- coding: utf-8 -*-

with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['APARTMENT_DATA.rooms', 'room.', 'r.box', 'r.id', 'r.name', 'r.label_pos']):
        print(f"Line {i+1:4d}: {line.strip()}")
