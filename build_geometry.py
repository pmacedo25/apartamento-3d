import json

# Coordinate system:
# X: 0 to 13.50 m (West to East)
# Z: 0 to 11.38 m (North to South)
# Y: 0 to 2.70 m (Up)

walls = [
    # --- EXTERIOR WALLS NORTH (Z = 0.44) ---
    {
        "id": "ext_north_service",
        "x1": 0.95, "z1": 0.44, "x2": 3.95, "z2": 0.44,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "ventilation", "start": 0.5, "width": 1.2, "sill": 1.6, "height": 0.8}]
    },
    {
        "id": "ext_north_kitchen",
        "x1": 3.95, "z1": 0.44, "x2": 8.95, "z2": 0.44,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_lavabo",
        "x1": 8.95, "z1": 0.44, "x2": 10.45, "z2": 0.44,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_recess",
        "x1": 10.45, "z1": 0.44, "x2": 10.45, "z2": 0.85,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_front",
        "x1": 10.45, "z1": 0.85, "x2": 12.30, "z2": 0.85,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "door", "start": 0.45, "width": 0.90, "height": 2.10, "label": "Entrada Social"}]
    },
    {
        "id": "ext_east_hall",
        "x1": 12.30, "z1": 0.85, "x2": 12.30, "z2": 3.25,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_hall_to_bath1",
        "x1": 12.30, "z1": 3.25, "x2": 13.35, "z2": 3.25,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # --- EXTERIOR WALLS EAST (X = 13.35) ---
    {
        "id": "ext_east_bath1",
        "x1": 13.35, "z1": 3.25, "x2": 13.35, "z2": 4.80,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.5, "width": 0.60, "sill": 1.70, "height": 0.60}]
    },
    {
        "id": "ext_east_suite1",
        "x1": 13.35, "z1": 4.80, "x2": 13.35, "z2": 7.75,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.80, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 1"}]
    },
    {
        "id": "ext_east_tech_balcony",
        "x1": 13.35, "z1": 7.75, "x2": 13.35, "z2": 9.20,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_south_tech_balcony",
        "x1": 10.45, "z1": 9.20, "x2": 13.35, "z2": 9.20,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_west_tech_balcony",
        "x1": 10.45, "z1": 8.25, "x2": 10.45, "z2": 9.20,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },

    # --- EXTERIOR WALLS SOUTH (Z = 11.00) ---
    {
        "id": "ext_south_suite2",
        "x1": 7.30, "z1": 11.00, "x2": 10.25, "z2": 11.00,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.70, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 2"}]
    },
    {
        "id": "ext_east_suite2",
        "x1": 10.25, "z1": 8.25, "x2": 10.25, "z2": 11.00,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_south_bath2",
        "x1": 5.75, "z1": 11.00, "x2": 7.30, "z2": 11.00,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.40, "width": 0.60, "sill": 1.70, "height": 0.60}]
    },
    {
        "id": "ext_south_bath_master",
        "x1": 4.25, "z1": 10.90, "x2": 5.75, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.40, "width": 0.60, "sill": 1.70, "height": 0.60}]
    },
    {
        "id": "ext_south_suite_master",
        "x1": 0.94, "z1": 10.90, "x2": 4.25, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.70, "width": 1.80, "sill": 0.90, "height": 1.30, "label": "Janela Suíte Master"}]
    },

    # --- EXTERIOR WALLS WEST (X = 0.40 to 0.94) ---
    {
        "id": "ext_west_suite_master",
        "x1": 0.94, "z1": 6.77, "x2": 0.94, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_west_terrace_balcony",
        "x1": 0.40, "z1": 2.25, "x2": 0.40, "z2": 6.77,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_west_service",
        "x1": 0.95, "z1": 0.44, "x2": 0.95, "z2": 2.25,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "terrace_recess_top",
        "x1": 0.40, "z1": 2.25, "x2": 0.95, "z2": 2.25,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "terrace_recess_bottom",
        "x1": 0.40, "z1": 6.77, "x2": 0.94, "z2": 6.77,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # --- INTERIOR WALLS & PARTITIONS ---

    # 1. Suíte Master / Terraço Gourmet (Z = 6.77)
    {
        "id": "int_master_to_terrace",
        "x1": 0.94, "z1": 6.77, "x2": 3.95, "z2": 6.77,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },
    # 2. Parede principal da Circulação Íntima / Sala (Z = 6.77)
    {
        "id": "int_hallway_to_living",
        "x1": 3.95, "z1": 6.77, "x2": 7.76, "z2": 6.77,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },
    # Vão aberto da circulação: de 7.76 a 8.70 (abertura livre para o corredor íntimo)

    # 3. Suíte Master / Banho Master (X = 4.25)
    {
        "id": "int_master_to_bath_master",
        "x1": 4.25, "z1": 8.35, "x2": 4.25, "z2": 10.90,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.35, "width": 0.70, "height": 2.10, "label": "Banho Master"}]
    },
    # Parede do corredor da Suíte Master (Z = 8.35)
    {
        "id": "int_master_corridor_wall",
        "x1": 3.31, "z1": 8.35, "x2": 5.75, "z2": 8.35,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.15, "width": 0.80, "height": 2.10, "label": "Porta Suíte Master"}]
    },

    # 4. Banho Master / Banho 2 (X = 5.75)
    {
        "id": "int_bath_master_to_bath2",
        "x1": 5.75, "z1": 8.35, "x2": 5.75, "z2": 11.00,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # 5. Banho 2 / Suíte 2 (X = 7.30)
    {
        "id": "int_bath2_to_suite2",
        "x1": 7.30, "z1": 8.25, "x2": 7.30, "z2": 11.00,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.35, "width": 0.70, "height": 2.10, "label": "Banho 2"}]
    },

    # 6. Suíte 2 / Circulação Íntima (Z = 8.25)
    {
        "id": "int_suite2_to_corridor",
        "x1": 7.30, "z1": 8.25, "x2": 10.25, "z2": 8.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.50, "width": 0.80, "height": 2.10, "label": "Porta Suíte 2"}]
    },

    # 7. Divisória Suíte 1 / Circulação & Sala (X = 10.45)
    {
        "id": "int_suite1_to_living",
        "x1": 10.45, "z1": 4.80, "x2": 10.45, "z2": 7.75,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 1.95, "width": 0.80, "height": 2.10, "label": "Porta Suíte 1"}]
    },

    # 8. Divisória Banho 1 / Suíte 1 (Z = 4.80)
    {
        "id": "int_bath1_to_suite1",
        "x1": 10.45, "z1": 4.80, "x2": 13.35, "z2": 4.80,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.60, "width": 0.70, "height": 2.10, "label": "Banho 1"}]
    },

    # 9. Divisória Banho 1 / Hall de Entrada (Z = 3.25)
    {
        "id": "int_bath1_to_hall",
        "x1": 10.45, "z1": 3.25, "x2": 12.30, "z2": 3.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # 10. Suíte 1 / Terraço Técnico (Z = 7.75)
    {
        "id": "int_suite1_to_tech_balcony",
        "x1": 10.45, "z1": 7.75, "x2": 13.35, "z2": 7.75,
        "thick": 0.15, "height": 2.70, "type": "exterior",
        "openings": [{"type": "door", "start": 1.80, "width": 0.75, "height": 2.10, "label": "Porta Técnica AC"}]
    },

    # 11. Divisória Terraço Social Gourmet / Sala de Estar (X = 3.95)
    # GRANDE ESQUADRIA DE CORRER INTEGRADA (Vão livre envidraçado de piso a teto)
    {
        "id": "int_terrace_to_living_glass",
        "x1": 3.95, "z1": 2.25, "x2": 3.95, "z2": 6.77,
        "thick": 0.10, "height": 2.70, "type": "sliding_glass_wall",
        "openings": [{"type": "sliding_glass", "start": 0.20, "width": 4.10, "height": 2.45, "label": "Esquadria de Vidro Terraço"}]
    },

    # 12. Divisória Terraço Gourmet / Área de Serviço (Z = 2.25)
    {
        "id": "int_terrace_to_service",
        "x1": 0.95, "z1": 2.25, "x2": 3.95, "z2": 2.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 2.20, "width": 0.75, "height": 2.10, "label": "Porta Serviço/Terraço"}]
    },

    # 13. Divisória Cozinha / Área de Serviço (X = 3.95)
    {
        "id": "int_kitchen_to_service",
        "x1": 3.95, "z1": 0.44, "x2": 3.95, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.50, "width": 0.90, "height": 2.20, "label": "Passagem Cozinha/Serviço"}]
    },

    # 14. Cozinha / Sala de Jantar (Z = 2.25) - Bancada americana semi-aberta
    {
        "id": "int_kitchen_counter",
        "x1": 3.95, "z1": 2.25, "x2": 7.80, "z2": 2.25,
        "thick": 0.30, "height": 0.92, "type": "countertop", # Bancada de 92cm de altura!
        "openings": []
    },
    {
        "id": "int_kitchen_open_pass",
        "x1": 7.80, "z1": 2.25, "x2": 8.95, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.0, "width": 1.15, "height": 2.40, "label": "Acesso Cozinha"}]
    },

    # 15. Lavabo / Cozinha (X = 8.95)
    {
        "id": "int_lavabo_to_kitchen",
        "x1": 8.95, "z1": 0.44, "x2": 8.95, "z2": 2.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # 16. Lavabo / Sala (Z = 2.25)
    {
        "id": "int_lavabo_to_living",
        "x1": 8.95, "z1": 2.25, "x2": 10.45, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.40, "width": 0.70, "height": 2.10, "label": "Lavabo"}]
    },

    # 17. Hall / Sala (X = 10.45, Z = 0.85 to 3.25)
    # Abertura ampla de transição do hall para o living
    {
        "id": "int_hall_to_living",
        "x1": 10.45, "z1": 2.25, "x2": 10.45, "z2": 3.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.0, "width": 1.00, "height": 2.40, "label": "Entrada Living"}]
    }
]

rooms_data = [
    {
        "id": "hall",
        "name": "Hall de Entrada",
        "area": 4.4,
        "box": [10.45, 0.85, 12.30, 3.25],
        "spawn": [11.37, 1.68, 2.05, 3.14],
        "floor": "porcelain",
        "color": "#e2ded6"
    },
    {
        "id": "lavabo",
        "name": "Lavabo",
        "area": 2.7,
        "box": [8.95, 0.44, 10.45, 2.25],
        "spawn": [9.70, 1.68, 1.40, 0.0],
        "floor": "tile_dark",
        "color": "#c8c4bc"
    },
    {
        "id": "cozinha",
        "name": "Cozinha",
        "area": 9.0,
        "box": [3.95, 0.44, 8.95, 2.25],
        "spawn": [6.45, 1.68, 1.35, 3.14],
        "floor": "porcelain",
        "color": "#ded9cf"
    },
    {
        "id": "servico",
        "name": "Área de Serviço",
        "area": 5.4,
        "box": [0.95, 0.44, 3.95, 2.25],
        "spawn": [2.45, 1.68, 1.35, 0.0],
        "floor": "tile_light",
        "color": "#d5d1c8"
    },
    {
        "id": "terraco",
        "name": "Terraço Gourmet",
        "area": 16.0,
        "box": [0.40, 2.25, 3.95, 6.77],
        "spawn": [2.15, 1.68, 4.50, 1.57],
        "floor": "deck_or_tile",
        "color": "#cfc8ba"
    },
    {
        "id": "sala",
        "name": "Sala de Estar / Jantar",
        "area": 29.4,
        "box": [3.95, 2.25, 10.45, 6.77],
        "spawn": [7.20, 1.68, 4.50, -1.57],
        "floor": "porcelain",
        "color": "#e8e5dc"
    },
    {
        "id": "circulacao",
        "name": "Circulação Íntima",
        "area": 4.0,
        "box": [7.30, 6.77, 10.45, 8.25],
        "spawn": [8.80, 1.68, 7.50, 3.14],
        "floor": "wood",
        "color": "#ded4c3"
    },
    {
        "id": "suite1",
        "name": "Suíte 1",
        "area": 8.5,
        "box": [10.45, 4.80, 13.35, 7.75],
        "spawn": [11.90, 1.68, 6.20, -1.57],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho1",
        "name": "Banho 1",
        "area": 4.5,
        "box": [10.45, 3.25, 13.35, 4.80],
        "spawn": [11.90, 1.68, 4.00, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "terraco_tecnico",
        "name": "Terraço Técnico (Ar Cond.)",
        "area": 4.2,
        "box": [10.45, 7.75, 13.35, 9.20],
        "spawn": [11.90, 1.68, 8.50, 0.0],
        "floor": "concrete",
        "color": "#b8b4ab"
    },
    {
        "id": "suite2",
        "name": "Suíte 2",
        "area": 8.1,
        "box": [7.30, 8.25, 10.25, 11.00],
        "spawn": [8.80, 1.68, 9.60, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho2",
        "name": "Banho 2",
        "area": 4.1,
        "box": [5.75, 8.35, 7.30, 11.00],
        "spawn": [6.50, 1.68, 9.60, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "suite_master",
        "name": "Suíte Master",
        "area": 13.7,
        "box": [0.94, 6.77, 4.25, 10.90],
        "spawn": [2.60, 1.68, 8.80, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho_master",
        "name": "Banho Master (Cuba Dupla)",
        "area": 3.8,
        "box": [4.25, 8.35, 5.75, 10.90],
        "spawn": [5.00, 1.68, 9.60, 0.0],
        "floor": "marble",
        "color": "#dedbd5"
    }
]

model_data = {
    "dimensions": {"width": 13.50, "depth": 11.38, "height": 2.70},
    "rooms": rooms_data,
    "walls": walls
}

js_content = "const APARTMENT_DATA = " + json.dumps(model_data, indent=2) + ";\n"

with open(r'c:\Users\sport\Documents\apartamento\apartment_geometry.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated apartment_geometry.js with {len(walls)} walls and {len(rooms_data)} rooms!")
