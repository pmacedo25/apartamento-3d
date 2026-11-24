# Validation script for apartment room areas and dimensions
rooms = {
    "Hall de Entrada": {"w": 1.85, "d": 2.40, "area": 1.85 * 2.40},
    "Lavabo": {"w": 1.50, "d": 1.80, "area": 1.50 * 1.80},
    "Cozinha": {"w": 5.00, "d": 1.81, "area": 5.00 * 1.81},
    "Área de Serviço": {"w": 3.00, "d": 1.81, "area": 3.00 * 1.81},
    "Sala de Estar / Jantar": {"w": 6.50, "d": 4.52, "area": 6.50 * 4.52},
    "Terraço Social Gourmet": {"w": 3.55, "d": 4.52, "area": 3.55 * 4.52},
    "Circulação Íntima": {"w": 2.69, "d": 1.48, "area": 2.69 * 1.48},
    "Suíte Master": {"w": 3.31, "d": 4.13, "area": 3.31 * 4.13},
    "Banho Master (Cuba Dupla)": {"w": 1.50, "d": 2.55, "area": 1.50 * 2.55},
    "Suíte 2": {"w": 2.95, "d": 2.75, "area": 2.95 * 2.75},
    "Banho 2": {"w": 1.55, "d": 2.65, "area": 1.55 * 2.65},
    "Suíte 1": {"w": 2.90, "d": 2.95, "area": 2.90 * 2.95},
    "Banho 1": {"w": 2.90, "d": 1.55, "area": 2.90 * 1.55},
    "Terraço Técnico": {"w": 2.90, "d": 1.45, "area": 2.90 * 1.45},
}

total_useful_area = sum(r["area"] for r in rooms.values())
print(f"Total Useful Floor Area: {total_useful_area:.2f} m²")
for name, data in rooms.items():
    print(f" - {name:<26}: {data['w']:4.2f}m x {data['d']:4.2f}m = {data['area']:5.2f} m²")
