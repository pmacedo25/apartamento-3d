import json

walls = [
    # ==========================================
    # --- EXTERIOR WALLS NORTH (Z = 0.44 a 1.02) ---
    # ==========================================
    {
        "id": "ext_north_service",
        "x1": 0.95, "z1": 0.44, "x2": 3.95, "z2": 0.44,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "ventilation", "start": 0.50, "width": 1.40, "sill": 1.60, "height": 0.80, "label": "Ventilação Serviço"}]
    },
    {
        "id": "ext_north_kitchen_lavabo",
        "x1": 3.95, "z1": 0.44, "x2": 10.42, "z2": 0.44,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_recess",
        "x1": 10.42, "z1": 0.44, "x2": 10.42, "z2": 1.02,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_front",
        "x1": 10.42, "z1": 1.02, "x2": 12.27, "z2": 1.02,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "door", "start": 0.45, "width": 0.90, "height": 2.10, "label": "Entrada Social"}]
    },
    {
        "id": "ext_east_hall",
        "x1": 12.27, "z1": 1.02, "x2": 12.27, "z2": 3.21,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_hall_to_bath1",
        "x1": 12.27, "z1": 3.21, "x2": 13.33, "z2": 3.21,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS EAST (X = 13.33) ---
    # ==========================================
    {
        "id": "ext_east_bath1",
        "x1": 13.33, "z1": 3.21, "x2": 13.33, "z2": 4.84,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.50, "width": 0.60, "sill": 1.70, "height": 0.60, "label": "Janela Banho 1"}]
    },
    {
        "id": "ext_east_suite1",
        "x1": 13.33, "z1": 4.84, "x2": 13.33, "z2": 7.75,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.75, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 1"}]
    },
    {
        "id": "ext_east_tech_balcony",
        "x1": 13.33, "z1": 7.75, "x2": 13.33, "z2": 9.00,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_south_tech_balcony",
        "x1": 10.64, "z1": 9.00, "x2": 13.33, "z2": 9.00,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_west_tech_balcony",
        "x1": 10.64, "z1": 7.75, "x2": 10.64, "z2": 9.00,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS SOUTH (Z = 10.90) ---
    # ==========================================
    {
        "id": "ext_south_suite2",
        "x1": 7.76, "z1": 10.90, "x2": 10.25, "z2": 10.90,
        "thick": 0.18, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.50, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 2"}]
    },
    {
        "id": "ext_east_suite2",
        "x1": 10.25, "z1": 8.35, "x2": 10.25, "z2": 10.90,
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
        "openings": [{"type": "window", "start": 0.85, "width": 1.80, "sill": 0.90, "height": 1.30, "label": "Janela Suíte Master"}]
    },

    # ==========================================
    # --- EXTERIOR WALLS WEST (X = 0.40 a 0.95) ---
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
    # --- SUÍTE MASTER, CLOSET E BANHO MASTER ---
    # ==========================================
    # Parede Norte da Suíte Master / Closet (divisória contínua com Terraço e Sala de Estar em Z=6.77)
    {
        "id": "int_master_to_terrace_and_living",
        "x1": 0.94, "z1": 6.77, "x2": 7.76, "z2": 6.77,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Parede Leste da Suíte Master (Divisória com Circulação Íntima em X=7.76)
    # Contém a porta de entrada da Suíte Master
    {
        "id": "int_corridor_to_suite_master",
        "x1": 7.76, "z1": 6.77, "x2": 7.76, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.62, "width": 0.80, "height": 2.10, "label": "Porta Suíte Master"}
        ]
    },

    # Parede Oeste do Banho Master (Divisória com Dormitório Master em X=4.45)
    # 100% FECHADA/SÓLIDA (Sem porta)
    {
        "id": "int_master_to_bath_master_solid",
        "x1": 4.45, "z1": 8.35, "x2": 4.45, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Parede Norte do Banho Master (em Z=8.35, de X=4.45 a 6.34)
    # Contém a porta de 0.70m abrindo para dentro do Banho Master de frente para a cuba dupla
    {
        "id": "int_bath_master_north_wall",
        "x1": 4.45, "z1": 8.35, "x2": 6.34, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.77, "width": 0.70, "height": 2.10, "label": "Porta Banho Master"}
        ]
    },

    # Parede Divisória entre Banho Master e Banho 2 (em X=6.34, de Z=8.35 a 10.90)
    # 100% FECHADA/SÓLIDA com shaft hidráulico
    {
        "id": "int_bath_master_to_bath2_solid",
        "x1": 6.34, "z1": 8.35, "x2": 6.34, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },

    # ==========================================
    # --- SUÍTE 2 E BANHO 2 ---
    # ==========================================
    # Parede Norte do Banho 2 (em Z=8.35, de X=6.34 a 7.76)
    # 100% FECHADA/SÓLIDA (divisória com o corredor íntimo)
    {
        "id": "int_bath2_north_wall_solid",
        "x1": 6.34, "z1": 8.35, "x2": 7.76, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Parede Divisória entre Banho 2 e Suíte 2 (em X=7.76, de Z=8.35 a 10.90)
    # Contém a porta do Banho 2 (0.70m) abrindo para a Suíte 2
    {
        "id": "int_bath2_to_suite2",
        "x1": 7.76, "z1": 8.35, "x2": 7.76, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.13, "width": 0.70, "height": 2.10, "label": "Porta Banho 2"}
        ]
    },

    # Parede Norte da Suíte 2 (em Z=8.35, de X=7.76 a 10.25)
    # Contém a porta de entrada da Suíte 2 vindo da circulação íntima
    {
        "id": "int_corridor_to_suite2",
        "x1": 7.76, "z1": 8.35, "x2": 10.25, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.20, "width": 0.80, "height": 2.10, "label": "Porta Suíte 2"}
        ]
    },

    # ==========================================
    # --- SUÍTE 1 E BANHO 1 ---
    # ==========================================
    # Parede Divisória Suíte 1 / Circulação & Sala (X = 10.45, de Z=4.84 a 7.75)
    # Contém a porta de entrada da Suíte 1
    {
        "id": "int_suite1_to_living_corridor",
        "x1": 10.45, "z1": 4.84, "x2": 10.45, "z2": 7.75,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 1.95, "width": 0.80, "height": 2.10, "label": "Porta Suíte 1"}
        ]
    },

    # Parede Divisória Banho 1 / Suíte 1 (Z = 4.84, de X=10.45 a 13.33)
    # Contém a porta do Banho 1 (0.70m) abrindo para a Suíte 1
    {
        "id": "int_bath1_to_suite1",
        "x1": 10.45, "z1": 4.84, "x2": 13.33, "z2": 4.84,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.25, "width": 0.70, "height": 2.10, "label": "Porta Banho 1"}
        ]
    },

    # Parede Divisória Banho 1 / Hall de Entrada (Z = 3.21, de X=10.45 a 12.27)
    # 100% FECHADA/SÓLIDA
    {
        "id": "int_bath1_to_hall",
        "x1": 10.45, "z1": 3.21, "x2": 12.27, "z2": 3.21,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Parede Suíte 1 / Terraço Técnico (Z = 7.75, de X=10.45 a 13.33)
    # Contém porta técnica de acesso aos condensadores de ar condicionado
    {
        "id": "int_suite1_to_tech_balcony",
        "x1": 10.45, "z1": 7.75, "x2": 13.33, "z2": 7.75,
        "thick": 0.15, "height": 2.70, "type": "exterior",
        "openings": [
            {"type": "door", "start": 1.80, "width": 0.75, "height": 2.10, "label": "Porta Técnica AC"}
        ]
    },

    # ==========================================
    # --- ÁREA SOCIAL: SALA, TERRAÇO, COZINHA, LAVABO, SERVIÇO ---
    # ==========================================
    # Grande esquadria de correr integrada de vidro Sala / Terraço Gourmet
    {
        "id": "int_terrace_to_living_glass",
        "x1": 3.95, "z1": 2.25, "x2": 3.95, "z2": 6.77,
        "thick": 0.10, "height": 2.70, "type": "sliding_glass_wall",
        "openings": [{"type": "sliding_glass", "start": 0.20, "width": 4.10, "height": 2.45, "label": "Esquadria de Vidro Terraço"}]
    },

    # Parede Divisória Terraço Gourmet / Área de Serviço (Z = 2.25, de X=0.95 a 3.95)
    # Contém porta de acesso Serviço / Terraço Gourmet
    {
        "id": "int_terrace_to_service",
        "x1": 0.95, "z1": 2.25, "x2": 3.95, "z2": 2.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 2.20, "width": 0.75, "height": 2.10, "label": "Porta Serviço/Terraço"}]
    },

    # Parede Cozinha / Área de Serviço (X = 3.95, de Z=0.44 a 2.25)
    # Passagem aberta de serviço
    {
        "id": "int_kitchen_to_service",
        "x1": 3.95, "z1": 0.44, "x2": 3.95, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.50, "width": 0.90, "height": 2.20, "label": "Passagem Cozinha/Serviço"}]
    },

    # Cozinha / Sala de Jantar (Z = 2.25, de X=3.95 a 7.80) - Bancada americana semi-aberta
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

    # Lavabo / Cozinha (X = 8.95, de Z=0.44 a 2.25)
    # 100% FECHADA/SÓLIDA
    {
        "id": "int_lavabo_to_kitchen",
        "x1": 8.95, "z1": 0.44, "x2": 8.95, "z2": 2.25,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },

    # Lavabo / Sala (Z = 2.25, de X=8.95 a 10.42)
    # Contém a porta do Lavabo Social
    {
        "id": "int_lavabo_to_living",
        "x1": 8.95, "z1": 2.25, "x2": 10.42, "z2": 2.25,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.35, "width": 0.70, "height": 2.10, "label": "Porta Lavabo"}]
    },

    # Hall / Sala (X = 10.42, de Z=2.25 a 3.21)
    # Vão aberto de entrada social para o living
    {
        "id": "int_hall_to_living",
        "x1": 10.42, "z1": 2.25, "x2": 10.42, "z2": 3.21,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.0, "width": 0.96, "height": 2.40, "label": "Entrada Living"}]
    }
]

rooms_data = [
    {
        "id": "hall",
        "name": "Hall de Entrada",
        "area": 4.1,
        "box": [10.42, 1.02, 12.27, 3.21],
        "spawn": [11.35, 1.68, 2.05, 3.14],
        "floor": "porcelain",
        "color": "#e2ded6"
    },
    {
        "id": "lavabo",
        "name": "Lavabo Social",
        "area": 2.7,
        "box": [8.95, 0.44, 10.42, 2.25],
        "spawn": [9.68, 1.68, 1.40, 0.0],
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
        "area": 4.3,
        "box": [7.76, 6.77, 10.45, 8.35],
        "spawn": [8.80, 1.68, 7.50, 3.14],
        "floor": "wood",
        "color": "#ded4c3"
    },
    {
        "id": "suite1",
        "name": "Suíte 1",
        "area": 8.4,
        "box": [10.45, 4.84, 13.33, 7.75],
        "spawn": [11.89, 1.68, 6.20, -1.57],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho1",
        "name": "Banho 1",
        "area": 4.7,
        "box": [10.45, 3.21, 13.33, 4.84],
        "spawn": [11.89, 1.68, 4.00, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "terraco_tecnico",
        "name": "Terraço Técnico (AC)",
        "area": 3.4,
        "box": [10.64, 7.75, 13.33, 9.00],
        "spawn": [11.95, 1.68, 8.35, 0.0],
        "floor": "concrete",
        "color": "#b8b4ab"
    },
    {
        "id": "suite2",
        "name": "Suíte 2",
        "area": 6.4,
        "box": [7.76, 8.35, 10.25, 10.90],
        "spawn": [9.00, 1.68, 9.60, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho2",
        "name": "Banho 2",
        "area": 3.6,
        "box": [6.34, 8.35, 7.76, 10.90],
        "spawn": [7.05, 1.68, 9.60, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "suite_master",
        "name": "Suíte Master",
        "area": 14.5,
        "box": [0.94, 6.77, 4.45, 10.90],
        "spawn": [2.60, 1.68, 8.80, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "suite_master_closet",
        "name": "Closet Suíte Master",
        "area": 5.2,
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

print(f"Audit completed: generated apartment_geometry.js with {len(walls)} audited walls and {len(rooms_data)} rooms!")
