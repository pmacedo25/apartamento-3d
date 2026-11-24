import json

# Coordinate system:
# X: 0 to 13.50 m (West to East)
# Z: 0 to 11.38 m (North to South)
# Y: 0 to 2.70 m (Up)

walls = [
    # ==========================================
    # --- EXTERIOR WALLS NORTH (Z = 0.44) ---
    # ==========================================
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

    # ==========================================
    # --- EXTERIOR WALLS EAST (X = 13.35) ---
    # ==========================================
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

    # ==========================================
    # --- EXTERIOR WALLS SOUTH (Z = 10.90 / 11.00) ---
    # ==========================================
    {
        "id": "ext_south_suite2",
        "x1": 7.76, "z1": 11.00, "x2": 10.25, "z2": 11.00,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.50, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 2"}]
    },
    {
        "id": "ext_east_suite2",
        "x1": 10.25, "z1": 8.35, "x2": 10.25, "z2": 11.00,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_south_bath2",
        "x1": 6.34, "z1": 10.90, "x2": 7.76, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.40, "width": 0.60, "sill": 1.70, "height": 0.60, "label": "Janela Banho 2"}]
    },
    {
        "id": "ext_south_bath_master",
        "x1": 4.45, "z1": 10.90, "x2": 6.34, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.60, "width": 0.70, "sill": 1.70, "height": 0.60, "label": "Janela Banho Master"}]
    },
    {
        "id": "ext_south_suite_master",
        "x1": 0.94, "z1": 10.90, "x2": 4.45, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.80, "width": 1.80, "sill": 0.90, "height": 1.30, "label": "Janela Suíte Master"}]
    },

    # ==========================================
    # --- EXTERIOR WALLS WEST (X = 0.40 to 0.94) ---
    # ==========================================
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

    # ==========================================
    # --- PAREDES REVISADAS: SUÍTE MASTER, BANHO MASTER, BANHO 2 E SUÍTE 2 ---
    # ==========================================

    # 1. Parede Norte da Suíte Master (Divisória com Terraço e Sala de Estar)
    # Vai de X=0.94 até X=7.76 em Z=6.77 (parede sólida contínua)
    {
        "id": "int_master_to_terrace_and_living",
        "x1": 0.94, "z1": 6.77, "x2": 7.76, "z2": 6.77,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # 2. Parede divisória entre Circulação Íntima e Suíte Master (X = 7.76, Z = 6.77 a 8.35)
    # Contém a PORTA DE ENTRADA da Suíte Master!
    {
        "id": "int_corridor_to_suite_master",
        "x1": 7.76, "z1": 6.77, "x2": 7.76, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            # Início em 0.62m (Z=7.39m), largura 0.80m até 1.42m (Z=8.19m)
            {"type": "door", "start": 0.62, "width": 0.80, "height": 2.10, "label": "Porta Suíte Master"}
        ]
    },

    # 3. Parede Oeste do Banho Master (Divisória entre Suíte Master Dormitório e Banho Master)
    # X = 4.45, de Z = 8.35 até Z = 10.90. PAREDE 100% FECHADA/SÓLIDA! SEM PORTA!
    {
        "id": "int_master_to_bath_master_solid",
        "x1": 4.45, "z1": 8.35, "x2": 4.45, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [] # TOTALMENTE FECHADA!
    },

    # 4. Parede Norte do Banho Master (com a porta vinda do closet/corredor da Suíte Master)
    # Z = 8.35, de X = 4.45 até X = 6.34 (comprimento = 1.89m)
    # Porta do Banho Master de 0.70m localizada entre X=5.22 e X=5.92!
    {
        "id": "int_bath_master_north_wall",
        "x1": 4.45, "z1": 8.35, "x2": 6.34, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            # Início em 0.77m (X=5.22m), largura 0.70m
            {"type": "door", "start": 0.77, "width": 0.70, "height": 2.10, "label": "Porta Banho Master"}
        ]
    },

    # 5. Parede Divisória entre Banho Master e Banho 2 (X = 6.34, Z = 8.35 a 10.90)
    # PAREDE 100% FECHADA/SÓLIDA com shaft hidráulico!
    {
        "id": "int_bath_master_to_bath2_solid",
        "x1": 6.34, "z1": 8.35, "x2": 6.34, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [] # TOTALMENTE FECHADA!
    },

    # 6. Parede Norte do Banho 2 (Z = 8.35, de X = 6.34 a X = 7.76)
    # PAREDE 100% FECHADA/SÓLIDA (divisória entre Banho 2 e o corredor/circulação)!
    {
        "id": "int_bath2_north_wall_solid",
        "x1": 6.34, "z1": 8.35, "x2": 7.76, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [] # TOTALMENTE FECHADA!
    },

    # 7. Parede Leste do Banho 2 (Divisória entre Banho 2 e Suíte 2)
    # X = 7.76, de Z = 8.35 até Z = 10.90. Contém a PORTA DO BANHO 2 (abrindo para a Suíte 2)!
    {
        "id": "int_bath2_to_suite2",
        "x1": 7.76, "z1": 8.35, "x2": 7.76, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            # Início em 0.13m (Z=8.48m), largura 0.70m (até Z=9.18m)
            {"type": "door", "start": 0.13, "width": 0.70, "height": 2.10, "label": "Porta Banho 2"}
        ]
    },

    # 8. Parede Norte da Suíte 2 (Divisória com a Circulação Íntima)
    # Z = 8.35, de X = 7.76 até X = 10.25 (comprimento = 2.49m). Contém a PORTA DE ENTRADA da Suíte 2!
    {
        "id": "int_corridor_to_suite2",
        "x1": 7.76, "z1": 8.35, "x2": 10.25, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            # Início em 0.20m (X=7.96m), largura 0.80m (até X=8.76m)
            {"type": "door", "start": 0.20, "width": 0.80, "height": 2.10, "label": "Porta Suíte 2"}
        ]
    },

    # ==========================================
    # --- DEMAIS PAREDES INTERNAS ---
    # ==========================================

    # Divisória Suíte 1 / Circulação & Sala (X = 10.45)
    {
        "id": "int_suite1_to_living",
        "x1": 10.45, "z1": 4.80, "x2": 10.45, "z2": 7.75,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 1.95, "width": 0.80, "height": 2.10, "label": "Porta Suíte 1"}]
    },

    # Divisória Banho 1 / Suíte 1 (Z = 4.80)
    {
        "id": "int_bath1_to_suite1",
        "x1": 10.45, "z1": 4.80, "x2": 13.35, "z2": 4.80,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.60, "width": 0.70, "height": 2.10, "label": "Porta Banho 1"}]
    },

    # Divisória Banho 1 / Hall de Entrada (Z = 3.25)
    {
        "id": "int_bath1_to_hall",
        "x1": 10.45, "z1": 3.25, "x2": 12.30, "z2": 3.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Suíte 1 / Terraço Técnico (Z = 7.75)
    {
        "id": "int_suite1_to_tech_balcony",
        "x1": 10.45, "z1": 7.75, "x2": 13.35, "z2": 7.75,
        "thick": 0.15, "height": 2.70, "type": "exterior",
        "openings": [{"type": "door", "start": 1.80, "width": 0.75, "height": 2.10, "label": "Porta Técnica AC"}]
    },

    # Divisória Terraço Social Gourmet / Sala de Estar (X = 3.95)
    # GRANDE ESQUADRIA DE CORRER INTEGRADA (Vão livre envidraçado de piso a teto)
    {
        "id": "int_terrace_to_living_glass",
        "x1": 3.95, "z1": 2.25, "x2": 3.95, "z2": 6.77,
        "thick": 0.10, "height": 2.70, "type": "sliding_glass_wall",
        "openings": [{"type": "sliding_glass", "start": 0.20, "width": 4.10, "height": 2.45, "label": "Esquadria de Vidro Terraço"}]
    },

    # Divisória Terraço Gourmet / Área de Serviço (Z = 2.25)
    {
        "id": "int_terrace_to_service",
        "x1": 0.95, "z1": 2.25, "x2": 3.95, "z2": 2.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 2.20, "width": 0.75, "height": 2.10, "label": "Porta Serviço/Terraço"}]
    },

    # Divisória Cozinha / Área de Serviço (X = 3.95)
    {
        "id": "int_kitchen_to_service",
        "x1": 3.95, "z1": 0.44, "x2": 3.95, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.50, "width": 0.90, "height": 2.20, "label": "Passagem Cozinha/Serviço"}]
    },

    # Cozinha / Sala de Jantar (Z = 2.25) - Bancada americana semi-aberta
    {
        "id": "int_kitchen_counter",
        "x1": 3.95, "z1": 2.25, "x2": 7.80, "z2": 2.25,
        "thick": 0.30, "height": 0.92, "type": "countertop",
        "openings": []
    },
    {
        "id": "int_kitchen_open_pass",
        "x1": 7.80, "z1": 2.25, "x2": 8.95, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.0, "width": 1.15, "height": 2.40, "label": "Acesso Cozinha"}]
    },

    # Lavabo / Cozinha (X = 8.95)
    {
        "id": "int_lavabo_to_kitchen",
        "x1": 8.95, "z1": 0.44, "x2": 8.95, "z2": 2.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Lavabo / Sala (Z = 2.25)
    {
        "id": "int_lavabo_to_living",
        "x1": 8.95, "z1": 2.25, "x2": 10.45, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.40, "width": 0.70, "height": 2.10, "label": "Lavabo"}]
    },

    # Hall / Sala (X = 10.45, Z = 0.85 to 3.25)
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
        "box": [7.76, 6.77, 10.45, 8.35],
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
        "box": [7.76, 8.35, 10.25, 11.00],
        "spawn": [8.80, 1.68, 9.60, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho2",
        "name": "Banho 2",
        "area": 4.1,
        "box": [6.34, 8.35, 7.76, 10.90],
        "spawn": [7.05, 1.68, 9.60, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "suite_master",
        "name": "Suíte Master",
        "area": 13.7,
        # Composta pelo dormitório e pelo closet/hall de entrada
        "box": [0.94, 6.77, 4.45, 10.90],
        "spawn": [2.60, 1.68, 8.80, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "suite_master_closet",
        "name": "Closet Suíte Master",
        "area": 3.8,
        "box": [4.45, 6.77, 7.76, 8.35],
        "spawn": [6.10, 1.68, 7.50, -1.57],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho_master",
        "name": "Banho Master (Cuba Dupla)",
        "area": 4.8,
        "box": [4.45, 8.35, 6.34, 10.90],
        "spawn": [5.39, 1.68, 9.60, 0.0],
        "floor": "tile_light",
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

print(f"Generated revised apartment_geometry.js with {len(walls)} walls and {len(rooms_data)} rooms!")
