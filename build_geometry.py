# -*- coding: utf-8 -*-
"""
HI VIEW ALTO DA BOA VISTA - FINAIS 1 E 6 (125.79 m²)
METICULOUS CAD REVISION & ARCHITECTURAL DATA GENERATOR
Compiles:
1. Exact Wall Segments with verified openings (Suíte Master window WEST, Suíte 1 window SOUTH, etc.)
2. Structural Concrete Columns (Pilares de concreto)
3. Technical Plumbing & Vent Shafts (Shafts hidráulicos com requadração)
4. Fixed Architectural Fixtures delivered with the apartment:
   - Kitchen Stone Countertop with Sink & Mixer Faucet
   - Service Area Laundry Tub (Tanque) & Gas Heater area
   - Terraço Gourmet Countertop with Round Sink & Built-in Barbecue Grill
   - Master Bathroom Stone Vanity with DOUBLE SINKS (Cuba Dupla)
   - Bathrooms 1, 2 and Lavabo Stone Vanities with Sinks & Faucets
   - Toilets (Vasos Sanitários com caixa acoplada) in all 4 bathrooms
   - Tempered Glass Shower Screens (Boxes) & Showers in all 3 en-suites
5. Interactive Doors with exact swing directions and hinges
"""

import json

# Scale factor: 1m = 37.777 pt (Scale 1:75, 125.79 m²)
# Bounds: X from 0.0 to 13.50 m, Z from 0.0 to 11.38 m, Y (height) = 2.70 m

walls = [
    # ==========================================
    # --- EXTERIOR WALLS NORTH (Z = 0.44 a 1.02) ---
    # ==========================================
    {
        "id": "ext_north_service",
        "x1": 0.95, "z1": 0.44, "x2": 3.95, "z2": 0.44,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "ventilation", "start": 0.45, "width": 1.20, "sill": 1.60, "height": 0.80, "label": "Ventilação Serviço"}]
    },
    {
        "id": "ext_north_kitchen_lavabo",
        "x1": 3.95, "z1": 0.44, "x2": 10.42, "z2": 0.44,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_recess",
        "x1": 10.42, "z1": 0.44, "x2": 10.42, "z2": 1.02,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_front",
        "x1": 10.42, "z1": 1.02, "x2": 12.27, "z2": 1.02,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "door", "start": 0.40, "width": 0.90, "height": 2.10, "label": "Entrada Social"}]
    },
    {
        "id": "ext_east_hall",
        "x1": 12.27, "z1": 1.02, "x2": 12.27, "z2": 3.21,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_hall_to_bath1",
        "x1": 12.27, "z1": 3.21, "x2": 13.33, "z2": 3.21,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS EAST (X = 13.33) ---
    # ==========================================
    {
        "id": "ext_east_bath1",
        "x1": 13.33, "z1": 3.21, "x2": 13.33, "z2": 4.84,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.50, "width": 0.60, "sill": 1.70, "height": 0.60, "label": "Janela Banho 1"}]
    },
    {
        "id": "ext_east_suite1_solid_acoustic",
        # Alvenaria em bloco acústico contínua (Page 0 Legenda: laranja claro)
        "x1": 13.33, "z1": 4.84, "x2": 13.33, "z2": 7.75,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
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
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.50, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 2"}]
    },
    {
        "id": "ext_east_suite2_wall",
        "x1": 10.25, "z1": 8.35, "x2": 10.25, "z2": 10.90,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_south_bath2",
        "x1": 6.34, "z1": 10.90, "x2": 7.76, "z2": 10.90,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.40, "width": 0.60, "sill": 1.70, "height": 0.60, "label": "Janela Banho 2"}]
    },
    {
        "id": "ext_south_bath_master",
        "x1": 4.45, "z1": 10.90, "x2": 6.34, "z2": 10.90,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.60, "width": 0.70, "sill": 1.70, "height": 0.60, "label": "Janela Banho Master"}]
    },
    {
        "id": "ext_south_suite_master_solid",
        # Parede sul da Suíte Master é contínua e sólida (a janela fica na fachada OESTE!)
        "x1": 0.94, "z1": 10.90, "x2": 4.45, "z2": 10.90,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS WEST (X = 0.40 a 0.97) ---
    # ==========================================
    {
        "id": "ext_west_suite_master",
        # JANELA DA SUÍTE MASTER NA FACHADA OESTE! (Conforme CAD zone_suite_master.png)
        "x1": 0.94, "z1": 6.77, "x2": 0.94, "z2": 10.90,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 1.20, "width": 1.60, "sill": 0.90, "height": 1.30, "label": "Janela Suíte Master"}]
    },
    {
        "id": "ext_west_terrace_balcony",
        "x1": 0.40, "z1": 2.16, "x2": 0.40, "z2": 6.77,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_west_service",
        "x1": 0.95, "z1": 0.44, "x2": 0.95, "z2": 2.16,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "terrace_recess_top",
        "x1": 0.40, "z1": 2.16, "x2": 0.95, "z2": 2.16,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "terrace_recess_bottom",
        "x1": 0.40, "z1": 6.77, "x2": 0.94, "z2": 6.77,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- SUÍTE MASTER, CLOSET E BANHO MASTER ---
    # ==========================================
    {
        "id": "int_master_to_terrace_and_living",
        "x1": 0.94, "z1": 6.77, "x2": 7.76, "z2": 6.77,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_corridor_to_suite_master",
        "x1": 7.76, "z1": 6.77, "x2": 7.76, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.60, "width": 0.80, "height": 2.10, "label": "Porta Suíte Master"}
        ]
    },
    {
        "id": "int_master_to_bath_master_solid",
        # Divisória Dormitório / Banho Master: 100% FECHADA/SÓLIDA
        "x1": 4.45, "z1": 8.35, "x2": 4.45, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_bath_master_north_wall",
        # Parede Norte do Banho Master com porta de 0.70m abrindo para dentro
        "x1": 4.45, "z1": 8.35, "x2": 6.34, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.85, "width": 0.70, "height": 2.10, "label": "Porta Banho Master"}
        ]
    },
    {
        "id": "int_bath_master_to_bath2_solid",
        "x1": 6.34, "z1": 8.35, "x2": 6.34, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },

    # ==========================================
    # --- SUÍTE 2 E BANHO 2 ---
    # ==========================================
    {
        "id": "int_bath2_north_wall_solid",
        "x1": 6.34, "z1": 8.35, "x2": 7.76, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_bath2_to_suite2",
        "x1": 7.76, "z1": 8.35, "x2": 7.76, "z2": 10.90,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.12, "width": 0.70, "height": 2.10, "label": "Porta Banho 2"}
        ]
    },
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
    {
        "id": "int_suite1_to_living_corridor",
        "x1": 10.45, "z1": 4.84, "x2": 10.45, "z2": 7.75,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 1.95, "width": 0.80, "height": 2.10, "label": "Porta Suíte 1"}
        ]
    },
    {
        "id": "int_bath1_to_suite1",
        "x1": 10.45, "z1": 4.84, "x2": 13.33, "z2": 4.84,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.20, "width": 0.70, "height": 2.10, "label": "Porta Banho 1"}
        ]
    },
    {
        "id": "int_bath1_to_hall",
        "x1": 10.45, "z1": 3.21, "x2": 12.27, "z2": 3.21,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_suite1_to_tech_balcony",
        # JANELA / ESQUADRIA DE CORRER DA SUÍTE 1 VOLTADA PARA O TERRAÇO TÉCNICO!
        "x1": 10.45, "z1": 7.75, "x2": 13.33, "z2": 7.75,
        "thick": 0.16, "height": 2.70, "type": "exterior",
        "openings": [
            {"type": "window", "start": 0.60, "width": 1.80, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 1"}
        ]
    },

    # ==========================================
    # --- ÁREA SOCIAL: SALA, TERRAÇO, COZINHA, LAVABO, SERVIÇO ---
    # ==========================================
    {
        "id": "int_terrace_to_living_glass",
        "x1": 3.95, "z1": 2.16, "x2": 3.95, "z2": 6.77,
        "thick": 0.10, "height": 2.70, "type": "sliding_glass_wall",
        "openings": [{"type": "sliding_glass", "start": 0.15, "width": 4.30, "height": 2.45, "label": "Esquadria de Vidro Terraço"}]
    },
    {
        "id": "int_terrace_to_service_solid",
        # Parede sólida entre Terraço e Serviço com shaft e bancada gourmet
        "x1": 0.95, "z1": 2.16, "x2": 3.95, "z2": 2.16,
        "thick": 0.16, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_kitchen_to_service",
        # Parede Cozinha / Área de Serviço: contém porta de serviço
        "x1": 3.95, "z1": 0.44, "x2": 3.95, "z2": 2.16,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.50, "width": 0.75, "height": 2.10, "label": "Porta Serviço"}]
    },
    {
        "id": "int_kitchen_to_terrace_door",
        # Passagem / porta da Cozinha para o Terraço Gourmet
        "x1": 3.48, "z1": 2.16, "x2": 3.95, "z2": 2.16,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_kitchen_div_wall",
        # Parede L da Cozinha com balcão de refeições e vão aberto para o living
        "x1": 3.95, "z1": 2.80, "x2": 7.60, "z2": 2.80,
        "thick": 0.15, "height": 0.95, "type": "countertop",
        "openings": []
    },
    {
        "id": "int_kitchen_div_lintel",
        # Viga de teto sobre o balcão da cozinha
        "x1": 3.95, "z1": 2.80, "x2": 7.60, "z2": 2.80,
        "thick": 0.15, "height": 0.35, "type": "beam",
        "openings": []
    },
    {
        "id": "int_kitchen_open_pass",
        # Vão de passagem da Cozinha para o Living
        "x1": 7.60, "z1": 2.16, "x2": 8.76, "z2": 2.16,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.0, "width": 1.16, "height": 2.40, "label": "Acesso Cozinha"}]
    },
    {
        "id": "int_lavabo_to_kitchen",
        "x1": 8.76, "z1": 0.44, "x2": 8.76, "z2": 2.16,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_lavabo_to_living",
        # Porta do Lavabo Social
        "x1": 8.76, "z1": 2.16, "x2": 10.42, "z2": 2.16,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "door", "start": 0.25, "width": 0.70, "height": 2.10, "label": "Porta Lavabo"}]
    },
    {
        "id": "int_hall_to_living",
        # Entrada do Hall Social para a Sala de Estar
        "x1": 10.42, "z1": 2.16, "x2": 10.42, "z2": 3.21,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": [{"type": "opening", "start": 0.0, "width": 1.05, "height": 2.40, "label": "Entrada Living"}]
    }
]

# =========================================================================
# --- PILARES ESTRUTURAIS DE CONCRETO (CAD Hatch Page 0) ---
# =========================================================================
pillars = [
    {"id": "pil_01", "name": "Pilar Serviço Noroeste", "x": 0.95, "z": 0.44, "w": 0.28, "d": 0.28, "h": 2.70},
    {"id": "pil_02", "name": "Pilar Serviço/Cozinha Norte", "x": 2.06, "z": 0.44, "w": 0.35, "d": 0.55, "h": 2.70},
    {"id": "pil_03", "name": "Pilar Cozinha/Lavabo Norte", "x": 8.76, "z": 0.44, "w": 0.35, "d": 0.60, "h": 2.70},
    {"id": "pil_04", "name": "Pilar Hall Entrada Leste", "x": 10.42, "z": 0.81, "w": 0.35, "d": 0.85, "h": 2.70},
    {"id": "pil_05", "name": "Pilar Hall/Banho 1", "x": 10.45, "z": 3.21, "w": 0.35, "d": 0.85, "h": 2.70},
    {"id": "pil_06", "name": "Pilar Cozinha/Terraço", "x": 3.48, "z": 1.98, "w": 0.45, "d": 0.45, "h": 2.70},
    {"id": "pil_07", "name": "Pilar Terraço/Master Oeste", "x": 0.94, "z": 6.77, "w": 0.35, "d": 0.85, "h": 2.70},
    {"id": "pil_08", "name": "Pilar Master Sudoeste", "x": 0.94, "z": 10.55, "w": 0.85, "d": 0.35, "h": 2.70},
    {"id": "pil_09", "name": "Pilar Circulação Central", "x": 8.76, "z": 6.77, "w": 0.35, "d": 0.85, "h": 2.70},
    {"id": "pil_10", "name": "Pilar Suíte 1/Técnico", "x": 10.45, "z": 7.75, "w": 0.35, "d": 0.60, "h": 2.70},
    {"id": "pil_11", "name": "Pilar Técnico Sudeste", "x": 12.98, "z": 7.75, "w": 0.35, "d": 0.85, "h": 2.70}
]

# =========================================================================
# --- SHAFTS HIDRÁULICOS E DE VENTILAÇÃO (CAD Page 0) ---
# =========================================================================
shafts = [
    {"id": "sh_gourmet", "name": "Shaft Gourmet/Serviço", "x": 2.30, "z": 2.16, "w": 0.87, "d": 0.55, "h": 2.70},
    {"id": "sh_master", "name": "Shaft Banho Master", "x": 4.06, "z": 10.04, "w": 0.45, "d": 0.86, "h": 2.70},
    {"id": "sh_banho2", "name": "Shaft Banho 2", "x": 5.94, "z": 10.04, "w": 0.40, "d": 0.86, "h": 2.70},
    {"id": "sh_banho1", "name": "Shaft Banho 1", "x": 11.80, "z": 3.21, "w": 0.85, "d": 0.60, "h": 2.70},
    {"id": "sh_lavabo", "name": "Shaft Lavabo", "x": 8.76, "z": 0.44, "w": 0.60, "d": 0.50, "h": 2.70},
    {"id": "sh_servico", "name": "Shaft Área de Serviço", "x": 1.25, "z": 0.44, "w": 0.80, "d": 0.50, "h": 2.70},
    {"id": "sh_tecnico", "name": "Shaft Terraço Técnico AC", "x": 12.42, "z": 8.25, "w": 0.35, "d": 0.65, "h": 2.70}
]

# =========================================================================
# --- MOBILIÁRIO FIXO E ELEMENTOS ARQUITETÔNICOS ENTREGUES PELA CONSTRUTORA ---
# =========================================================================
fixtures = [
    # 1. Cozinha: Bancada em granito na parede norte com cuba de inox e torneira
    {
        "id": "bancada_cozinha", "type": "counter_sink", "room": "cozinha",
        "x": 4.10, "z": 0.46, "w": 4.50, "d": 0.60, "h": 0.88,
        "material": "granite_black", "has_sink": True, "sink_x": 6.00, "sink_type": "kitchen_rect"
    },
    # 2. Área de Serviço: Tanque de lavar roupas com cuba funda e torneira
    {
        "id": "tanque_servico", "type": "laundry_tub", "room": "servico",
        "x": 2.25, "z": 0.46, "w": 0.70, "d": 0.55, "h": 0.86,
        "material": "ceramic_white", "has_sink": True, "sink_x": 2.60, "sink_type": "laundry_tub"
    },
    # 3. Terraço Gourmet: Bancada em granito com cuba redonda e nicho de churrasqueira
    {
        "id": "bancada_gourmet", "type": "gourmet_counter", "room": "terraco",
        "x": 0.96, "z": 2.18, "w": 1.34, "d": 0.60, "h": 0.90,
        "material": "granite_black", "has_sink": True, "sink_x": 1.30, "sink_type": "round_sink",
        "has_barbecue": True, "bbq_x": 1.85, "bbq_w": 0.45
    },
    # 4. Banho Master: Bancada de mármore/granito com CUBA DUPLA (duas cubas e torneiras!)
    {
        "id": "bancada_banho_master", "type": "double_vanity", "room": "banho_master",
        "x": 4.47, "z": 8.40, "w": 0.55, "d": 1.50, "h": 0.85,
        "material": "marble_light", "has_sink": True, "sink_type": "double_sink",
        "sink_z1": 8.75, "sink_z2": 9.45
    },
    # 5. Banho Master: Vaso sanitário com caixa acoplada
    {
        "id": "vaso_banho_master", "type": "toilet", "room": "banho_master",
        "x": 5.85, "z": 9.15, "w": 0.42, "d": 0.65, "h": 0.78, "rotY": -1.57
    },
    # 6. Banho Master: Box de vidro temperado e ducha
    {
        "id": "box_banho_master", "type": "shower_box", "room": "banho_master",
        "x": 4.45, "z": 9.90, "w": 1.89, "d": 1.00, "h": 1.95, "shower_pos": [5.40, 2.20, 10.75]
    },

    # 7. Banho 2: Bancada com cuba de semi-encaixe
    {
        "id": "bancada_banho2", "type": "vanity", "room": "banho2",
        "x": 6.36, "z": 8.37, "w": 0.85, "d": 0.55, "h": 0.85,
        "material": "marble_light", "has_sink": True, "sink_x": 6.78, "sink_type": "single_sink"
    },
    # 8. Banho 2: Vaso sanitário
    {
        "id": "vaso_banho2", "type": "toilet", "room": "banho2",
        "x": 6.45, "z": 9.15, "w": 0.42, "d": 0.65, "h": 0.78, "rotY": 1.57
    },
    # 9. Banho 2: Box de chuveiro
    {
        "id": "box_banho2", "type": "shower_box", "room": "banho2",
        "x": 6.34, "z": 9.90, "w": 1.42, "d": 1.00, "h": 1.95, "shower_pos": [7.05, 2.20, 10.75]
    },

    # 10. Banho 1: Bancada com cuba
    {
        "id": "bancada_banho1", "type": "vanity", "room": "banho1",
        "x": 10.47, "z": 3.25, "w": 0.55, "d": 0.85, "h": 0.85,
        "material": "marble_light", "has_sink": True, "sink_z": 3.65, "sink_type": "single_sink"
    },
    # 11. Banho 1: Vaso sanitário
    {
        "id": "vaso_banho1", "type": "toilet", "room": "banho1",
        "x": 11.45, "z": 3.30, "w": 0.42, "d": 0.65, "h": 0.78, "rotY": 0.0
    },
    # 12. Banho 1: Box de chuveiro
    {
        "id": "box_banho1", "type": "shower_box", "room": "banho1",
        "x": 12.05, "z": 3.21, "w": 1.28, "d": 1.63, "h": 1.95, "shower_pos": [12.70, 2.20, 4.00]
    },

    # 13. Lavabo: Bancada em mármore esculpido
    {
        "id": "bancada_lavabo", "type": "vanity", "room": "lavabo",
        "x": 9.75, "z": 1.50, "w": 0.55, "d": 0.65, "h": 0.85,
        "material": "marble_light", "has_sink": True, "sink_z": 1.82, "sink_type": "single_sink"
    },
    # 14. Lavabo: Vaso sanitário
    {
        "id": "vaso_lavabo", "type": "toilet", "room": "lavabo",
        "x": 9.25, "z": 0.55, "w": 0.42, "d": 0.65, "h": 0.78, "rotY": 0.0
    }
]

# =========================================================================
# --- ROOMS DEFINITION WITH PRECISE CONTRACT AREAS (125.79 m²) ---
# =========================================================================
rooms_data = [
    {
        "id": "hall",
        "name": "Hall de Entrada",
        "area": 4.1,
        "box": [10.42, 1.02, 12.27, 3.21],
        "spawn": [11.35, 1.60, 2.05, 3.14],
        "floor": "porcelain",
        "color": "#e2ded6"
    },
    {
        "id": "lavabo",
        "name": "Lavabo Social",
        "area": 2.7,
        "box": [8.76, 0.44, 10.42, 2.16],
        "spawn": [9.55, 1.60, 1.40, 0.0],
        "floor": "tile_dark",
        "color": "#c8c4bc"
    },
    {
        "id": "cozinha",
        "name": "Cozinha",
        "area": 9.0,
        "box": [3.95, 0.44, 8.76, 2.16],
        "spawn": [6.35, 1.60, 1.35, 3.14],
        "floor": "porcelain",
        "color": "#ded9cf"
    },
    {
        "id": "servico",
        "name": "Área de Serviço",
        "area": 5.4,
        "box": [0.95, 0.44, 3.95, 2.16],
        "spawn": [2.45, 1.60, 1.35, 0.0],
        "floor": "tile_light",
        "color": "#d5d1c8"
    },
    {
        "id": "terraco",
        "name": "Terraço Gourmet",
        "area": 16.0,
        "box": [0.40, 2.16, 3.95, 6.77],
        "spawn": [2.15, 1.60, 4.50, 1.57],
        "floor": "deck_or_tile",
        "color": "#cfc8ba"
    },
    {
        "id": "sala",
        "name": "Sala de Estar / Jantar",
        "area": 29.4,
        "box": [3.95, 2.16, 10.45, 6.77],
        "spawn": [7.20, 1.60, 4.50, -1.57],
        "floor": "porcelain",
        "color": "#e8e5dc"
    },
    {
        "id": "circulacao",
        "name": "Circulação Íntima",
        "area": 4.3,
        "box": [7.76, 6.77, 10.45, 8.35],
        "spawn": [8.80, 1.60, 7.50, 3.14],
        "floor": "wood",
        "color": "#ded4c3"
    },
    {
        "id": "suite1",
        "name": "Suíte 1",
        "area": 8.4,
        "box": [10.45, 4.84, 13.33, 7.75],
        "spawn": [11.89, 1.60, 6.20, -1.57],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho1",
        "name": "Banho 1",
        "area": 4.7,
        "box": [10.45, 3.21, 13.33, 4.84],
        "spawn": [11.45, 1.60, 4.20, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "terraco_tecnico",
        "name": "Terraço Técnico (AC)",
        "area": 3.4,
        "box": [10.64, 7.75, 13.33, 9.00],
        "spawn": [11.95, 1.60, 8.35, 0.0],
        "floor": "concrete",
        "color": "#b8b4ab"
    },
    {
        "id": "suite2",
        "name": "Suíte 2",
        "area": 6.4,
        "box": [7.76, 8.35, 10.25, 10.90],
        "spawn": [9.00, 1.60, 9.60, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho2",
        "name": "Banho 2",
        "area": 3.6,
        "box": [6.34, 8.35, 7.76, 10.90],
        "spawn": [7.05, 1.60, 9.60, 0.0],
        "floor": "tile_light",
        "color": "#ccc7bd"
    },
    {
        "id": "suite_master",
        "name": "Suíte Master",
        "area": 14.5,
        "box": [0.94, 6.77, 4.45, 10.90],
        "spawn": [2.60, 1.60, 8.80, 0.0],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "suite_master_closet",
        "name": "Closet Suíte Master",
        "area": 5.2,
        "box": [4.45, 6.77, 7.76, 8.35],
        "spawn": [6.10, 1.60, 7.50, -1.57],
        "floor": "wood",
        "color": "#d9ccb6"
    },
    {
        "id": "banho_master",
        "name": "Banho Master (Cuba Dupla)",
        "area": 4.8,
        "box": [4.45, 8.35, 6.34, 10.90],
        "spawn": [5.39, 1.60, 9.60, 0.0],
        "floor": "tile_light",
        "color": "#dedbd5"
    }
]

model_data = {
    "dimensions": {"width": 13.50, "depth": 11.38, "height": 2.70},
    "rooms": rooms_data,
    "walls": walls,
    "pillars": pillars,
    "shafts": shafts,
    "fixtures": fixtures
}

js_content = "const APARTMENT_DATA = " + json.dumps(model_data, indent=2) + ";\n"

with open(r'c:\Users\sport\Documents\apartamento\apartment_geometry.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated meticulous CAD geometry: {len(walls)} walls, {len(pillars)} pillars, {len(shafts)} shafts, {len(fixtures)} fixed fixtures, {len(rooms_data)} rooms!")
