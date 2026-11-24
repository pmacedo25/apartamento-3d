import base64

with open(r'c:\Users\sport\Documents\apartamento\apartment_floor_plan.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

print('Base64 length:', len(b64))
with open(r'c:\Users\sport\Documents\apartamento\plan_image_b64.js', 'w', encoding='utf-8') as f:
    f.write('const APARTMENT_PLAN_B64 = "data:image/png;base64,' + b64 + '";\n')

print('Saved plan_image_b64.js successfully!')
