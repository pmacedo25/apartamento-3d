# -*- coding: utf-8 -*-
"""
PERFECT BLUEPRINT GEOMETRY GENERATOR
Derived directly from CAD lines, curves and cotas in
CONSTRUCOMPANY_HI VIEW_FINAIS 1 E 6_REV02.pdf (125.79 m²).
"""

import json

walls = [
    # ==========================================
    # --- EXTERIOR WALLS NORTH (Z = 0.44 a 1.01) ---
    # ==========================================
    {
        "id": "ext_north_service",
        "x1": 0.95, "z1": 0.44, "x2": 3.48, "z2": 0.44,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "ventilation", "start": 0.50, "width": 1.20, "sill": 1.60, "height": 0.80, "label": "Ventilação Serviço"}]
    },
    {
        "id": "ext_north_kitchen",
        "x1": 3.48, "z1": 0.44, "x2": 8.60, "z2": 0.44,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_lavabo",
        "x1": 8.60, "z1": 0.44, "x2": 9.95, "z2": 0.44,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_recess",
        "x1": 9.95, "z1": 0.44, "x2": 9.95, "z2": 1.01,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_north_hall_front",
        "x1": 9.95, "z1": 1.01, "x2": 11.80, "z2": 1.01,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "door", "start": 0.45, "width": 0.90, "height": 2.10, "label": "Entrada Social"}]
    },
    {
        "id": "ext_east_hall",
        "x1": 11.80, "z1": 1.01, "x2": 11.80, "z2": 3.18,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_hall_to_bath1",
        "x1": 11.80, "z1": 3.18, "x2": 12.86, "z2": 3.18,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS EAST (X = 12.86) ---
    # ==========================================
    {
        "id": "ext_east_bath1",
        "x1": 12.86, "z1": 3.18, "x2": 12.86, "z2": 4.81,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.50, "width": 0.60, "sill": 1.70, "height": 0.60, "label": "Janela Banho 1"}]
    },
    {
        "id": "ext_east_suite1_solid_acoustic",
        "x1": 12.86, "z1": 4.81, "x2": 12.86, "z2": 7.65,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_east_tech_balcony",
        "x1": 12.63, "z1": 7.79, "x2": 12.63, "z2": 8.98,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_south_tech_balcony",
        "x1": 10.17, "z1": 8.98, "x2": 12.63, "z2": 8.98,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_west_tech_balcony",
        "x1": 10.17, "z1": 7.79, "x2": 10.17, "z2": 8.98,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS SOUTH (Z = 10.88) ---
    # ==========================================
    {
        "id": "ext_south_suite2",
        "x1": 7.28, "z1": 10.88, "x2": 10.15, "z2": 10.88,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.70, "width": 1.40, "sill": 0.90, "height": 1.30, "label": "Janela Suíte 2"}]
    },
    {
        "id": "ext_east_suite2_wall",
        "x1": 10.15, "z1": 7.79, "x2": 10.15, "z2": 10.88,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "ext_south_bath2",
        "x1": 5.80, "z1": 10.88, "x2": 7.28, "z2": 10.88,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.45, "width": 0.60, "sill": 1.70, "height": 0.60, "label": "Janela Banho 2"}]
    },
    {
        "id": "ext_south_bath_master",
        "x1": 4.05, "z1": 10.88, "x2": 5.80, "z2": 10.88,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 0.55, "width": 0.65, "sill": 1.70, "height": 0.60, "label": "Janela Banho Master"}]
    },
    {
        "id": "ext_south_suite_master_solid",
        "x1": 0.94, "z1": 10.88, "x2": 4.05, "z2": 10.88,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- EXTERIOR WALLS WEST (X = 0.40 a 0.95) ---
    # ==========================================
    {
        "id": "ext_west_suite_master",
        "x1": 0.94, "z1": 6.75, "x2": 0.94, "z2": 10.88,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [{"type": "window", "start": 1.20, "width": 1.60, "sill": 0.90, "height": 1.30, "label": "Janela Suíte Master"}]
    },
    {
        "id": "ext_west_terrace_balcony",
        "x1": 0.40, "z1": 2.18, "x2": 0.40, "z2": 6.75,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "ext_west_service",
        "x1": 0.95, "z1": 0.44, "x2": 0.95, "z2": 2.18,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },
    {
        "id": "terrace_recess_top",
        "x1": 0.40, "z1": 2.18, "x2": 0.95, "z2": 2.18,
        "thick": 0.15, "height": 1.20, "type": "railing",
        "openings": []
    },
    {
        "id": "terrace_recess_bottom",
        "x1": 0.40, "z1": 6.75, "x2": 0.94, "z2": 6.75,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": []
    },

    # ==========================================
    # --- COZINHA & ÁREA DE SERVIÇO ---
    # ==========================================
    {
        "id": "int_service_kitchen_div",
        "x1": 3.48, "z1": 0.44, "x2": 3.48, "z2": 2.18,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.45, "width": 0.80, "height": 2.10, "label": "Porta Serviço"}
        ]
    },
    {
        "id": "int_kitchen_terrace_wall",
        "x1": 0.95, "z1": 2.18, "x2": 3.48, "z2": 2.18,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 1.65, "width": 0.80, "height": 2.10, "label": "Acesso Cozinha/Terraço"}
        ]
    },
    {
        "id": "int_kitchen_living_wall",
        "x1": 4.70, "z1": 2.13, "x2": 7.61, "z2": 2.13,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },

    # ==========================================
    # --- LAVABO & HALL SOCIAL ---
    # ==========================================
    {
        "id": "int_lavabo_west_wall",
        "x1": 8.60, "z1": 0.44, "x2": 8.60, "z2": 1.98,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_lavabo_south_wall",
        "x1": 8.60, "z1": 1.98, "x2": 9.95, "z2": 1.98,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.35, "width": 0.70, "height": 2.10, "label": "Porta Lavabo"}
        ]
    },
    {
        "id": "int_hall_living_div",
        "x1": 9.95, "z1": 1.98, "x2": 9.95, "z2": 3.18,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.15, "width": 0.95, "height": 2.10, "label": "Acesso Living"}
        ]
    },

    # ==========================================
    # --- LIVING & TERRAÇO GOURMET (ESQUADRIA) ---
    # ==========================================
    {
        "id": "esquadria_living_terraco",
        "x1": 4.70, "z1": 2.18, "x2": 4.70, "z2": 6.75,
        "thick": 0.10, "height": 2.70, "type": "glass_slider",
        "openings": [
            {"type": "sliding_door", "start": 0.30, "width": 3.90, "height": 2.40, "label": "Esquadria Living/Terraço"}
        ]
    },

    # ==========================================
    # --- DIVISÓRIA LIVING / CIRCULAÇÃO ÍNTIMA ---
    # ==========================================
    {
        "id": "int_living_to_corridor",
        "x1": 4.70, "z1": 6.60, "x2": 8.42, "z2": 6.60,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "passage", "start": 2.40, "width": 1.10, "height": 2.40, "label": "Acesso Circulação Íntima"}
        ]
    },

    # ==========================================
    # --- SUÍTE 1, BANHO 1 & TERRAÇO TÉCNICO ---
    # ==========================================
    {
        "id": "int_bath1_suite1_div",
        "x1": 10.15, "z1": 4.81, "x2": 12.86, "z2": 4.81,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_suite1_west_wall",
        "x1": 10.15, "z1": 3.18, "x2": 10.15, "z2": 7.65,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.40, "width": 0.70, "height": 2.10, "label": "Porta Banho 1"},
            {"type": "door", "start": 3.50, "width": 0.80, "height": 2.10, "label": "Porta Suíte 1"}
        ]
    },
    {
        "id": "int_suite1_south_facade_window",
        "x1": 10.15, "z1": 7.65, "x2": 12.86, "z2": 7.65,
        "thick": 0.19, "height": 2.70, "type": "exterior",
        "openings": [
            {"type": "sliding_window", "start": 0.40, "width": 1.80, "sill": 0.85, "height": 1.40, "label": "Janela Suíte 1 (Varanda Técnica)"}
        ]
    },

    # ==========================================
    # --- ROUPEIRO / CIRCULAÇÃO ÍNTIMA ---
    # ==========================================
    {
        "id": "int_roupeiro_niche",
        "x1": 8.34, "z1": 7.65, "x2": 9.95, "z2": 7.65,
        "thick": 0.12, "height": 2.70, "type": "interior",
        "openings": []
    },

    # ==========================================
    # --- SUÍTE 2 & BANHO 2 (EXATAS COORDENADAS) ---
    # ==========================================
    {
        "id": "int_suite2_north_wall",
        "x1": 7.28, "z1": 8.35, "x2": 10.15, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.20, "width": 0.80, "height": 2.10, "label": "Porta Suíte 2"}
        ]
    },
    {
        "id": "int_bath2_to_suite2",
        "x1": 7.28, "z1": 8.35, "x2": 7.28, "z2": 10.88,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_bath2_north_wall",
        "x1": 5.80, "z1": 8.40, "x2": 7.28, "z2": 8.40,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.70, "width": 0.70, "height": 2.10, "label": "Porta Banho 2"}
        ]
    },
    {
        "id": "int_bath_master_to_bath2",
        "x1": 5.80, "z1": 8.40, "x2": 5.80, "z2": 10.88,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },

    # ==========================================
    # --- SUÍTE MASTER, CLOSET & BANHO MASTER ---
    # ==========================================
    {
        "id": "int_master_to_terrace",
        "x1": 0.94, "z1": 6.75, "x2": 4.70, "z2": 6.75,
        "thick": 0.15, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_corridor_to_suite_master",
        "x1": 7.28, "z1": 6.60, "x2": 7.28, "z2": 8.35,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.75, "width": 0.80, "height": 2.10, "label": "Porta Suíte Master"}
        ]
    },
    {
        "id": "int_master_to_bath_master_solid",
        "x1": 4.05, "z1": 8.40, "x2": 4.05, "z2": 10.88,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": []
    },
    {
        "id": "int_bath_master_north_wall",
        "x1": 4.05, "z1": 8.40, "x2": 5.80, "z2": 8.40,
        "thick": 0.14, "height": 2.70, "type": "interior",
        "openings": [
            {"type": "door", "start": 0.70, "width": 0.70, "height": 2.10, "label": "Porta Banho Master"}
        ]
    }
]

# 11 PILARES DE CONCRETO (Extraídos com precisão métrica)
pillars = [
    {"id": "P1", "name": "Pilar Varanda Noroeste", "x": 0.40, "z": 2.18, "w": 0.25, "d": 0.60, "h": 2.70},
    {"id": "P2", "name": "Pilar Divisa Serviço/Cozinha", "x": 3.48, "z": 2.18, "w": 0.25, "d": 0.55, "h": 2.70},
    {"id": "P3", "name": "Pilar Varanda Sudoeste", "x": 0.40, "z": 6.75, "w": 0.25, "d": 0.60, "h": 2.70},
    {"id": "P4", "name": "Pilar Esquadria Terraço/Living Sul", "x": 4.70, "z": 6.75, "w": 0.25, "d": 0.70, "h": 2.70},
    {"id": "P5", "name": "Pilar Hall / Lavabo", "x": 9.95, "z": 1.01, "w": 0.30, "d": 0.50, "h": 2.70},
    {"id": "P6", "name": "Pilar Hall / Banho 1", "x": 11.80, "z": 3.18, "w": 0.25, "d": 0.50, "h": 2.70},
    {"id": "P7", "name": "Pilar Fachada Banho 1 / Suíte 1", "x": 12.86, "z": 4.81, "w": 0.25, "d": 0.60, "h": 2.70},
    {"id": "P8", "name": "Pilar Terraço Técnico", "x": 12.63, "z": 7.79, "w": 0.25, "d": 0.50, "h": 2.70},
    {"id": "P9", "name": "Pilar Sul Suíte 2 / Técnico", "x": 10.15, "z": 10.88, "w": 0.25, "d": 0.60, "h": 2.70},
    {"id": "P10", "name": "Pilar Sul Divisa Banhos", "x": 5.80, "z": 10.88, "w": 0.25, "d": 0.60, "h": 2.70},
    {"id": "P11", "name": "Pilar Sul Canto Master", "x": 0.94, "z": 10.88, "w": 0.25, "d": 0.60, "h": 2.70}
]

# 7 SHAFTS HIDRÁULICOS E DE VENTILAÇÃO
shafts = [
    {"id": "S1", "name": "Shaft Churrasqueira / Gourmet", "x": 1.25, "z": 2.45, "w": 0.45, "d": 0.45, "h": 2.70},
    {"id": "S2", "name": "Shaft Cozinha / Prumada Norte", "x": 5.40, "z": 0.60, "w": 0.40, "d": 0.30, "h": 2.70},
    {"id": "S3", "name": "Shaft Lavabo", "x": 9.75, "z": 0.60, "w": 0.35, "d": 0.30, "h": 2.70},
    {"id": "S4", "name": "Shaft Banho 1", "x": 12.60, "z": 3.40, "w": 0.45, "d": 0.40, "h": 2.70},
    {"id": "S5", "name": "Shaft Banho Master", "x": 4.25, "z": 8.65, "w": 0.38, "d": 0.45, "h": 2.70},
    {"id": "S6", "name": "Shaft Banho 2", "x": 7.05, "z": 8.65, "w": 0.38, "d": 0.45, "h": 2.70},
    {"id": "S7", "name": "Shaft Terraço Técnico AC", "x": 10.45, "z": 8.00, "w": 0.45, "d": 0.40, "h": 2.70}
]

# BANCADAS E LOUÇAS FIXAS DE ENTREGA
fixtures = [
    # Cozinha
    {"id": "fix_kitchen_counter", "type": "countertop", "room": "Cozinha", "x": 6.00, "z": 0.74, "w": 4.50, "d": 0.60, "h": 0.90, "material": "granite_black", "has_sink": True, "sink_x": 6.00, "sink_type": "kitchen_single"},
    # Área de Serviço
    {"id": "fix_service_tub", "type": "laundry_tub", "room": "Área de Serviço", "x": 1.70, "z": 0.70, "w": 0.60, "d": 0.55, "h": 0.85, "material": "ceramic_white", "has_sink": True, "sink_x": 1.70, "sink_type": "laundry"},
    # Terraço Gourmet
    {"id": "fix_gourmet_counter", "type": "countertop", "room": "Terraço Gourmet", "x": 2.20, "z": 2.45, "w": 1.80, "d": 0.65, "h": 0.90, "material": "granite_black", "has_sink": True, "sink_x": 2.60, "sink_type": "round_prep"},
    {"id": "fix_gourmet_bbq", "type": "barbecue", "room": "Terraço Gourmet", "x": 1.60, "z": 2.45, "w": 0.80, "d": 0.65, "h": 1.10, "material": "masonry_dark", "has_sink": False, "sink_x": None, "sink_type": None},
    
    # Banho Master: BANCADA COM CUBA DUPLA!
    {"id": "fix_bath_master_vanity", "type": "vanity_double", "room": "Banho Master", "x": 4.92, "z": 8.68, "w": 1.50, "d": 0.55, "h": 0.85, "material": "marble_white", "has_sink": True, "sink_x": 4.92, "sink_type": "double_cuba"},
    {"id": "fix_bath_master_toilet", "type": "toilet", "room": "Banho Master", "x": 5.45, "z": 9.40, "w": 0.45, "d": 0.65, "h": 0.80, "material": "ceramic_white", "has_sink": False, "sink_x": None, "sink_type": None},
    {"id": "fix_bath_master_glass_box", "type": "shower_box", "room": "Banho Master", "x": 4.92, "z": 10.30, "w": 1.50, "d": 0.90, "h": 2.10, "material": "glass_screen", "has_sink": False, "sink_x": None, "sink_type": None},

    # Banho 2
    {"id": "fix_bath2_vanity", "type": "vanity", "room": "Banho 2", "x": 6.54, "z": 8.68, "w": 1.20, "d": 0.55, "h": 0.85, "material": "marble_white", "has_sink": True, "sink_x": 6.54, "sink_type": "single_cuba"},
    {"id": "fix_bath2_toilet", "type": "toilet", "room": "Banho 2", "x": 6.00, "z": 9.40, "w": 0.45, "d": 0.65, "h": 0.80, "material": "ceramic_white", "has_sink": False, "sink_x": None, "sink_type": None},
    {"id": "fix_bath2_glass_box", "type": "shower_box", "room": "Banho 2", "x": 6.54, "z": 10.30, "w": 1.20, "d": 0.90, "h": 2.10, "material": "glass_screen", "has_sink": False, "sink_x": None, "sink_type": None},

    # Banho 1
    {"id": "fix_bath1_vanity", "type": "vanity", "room": "Banho 1", "x": 11.50, "z": 3.48, "w": 1.20, "d": 0.55, "h": 0.85, "material": "marble_white", "has_sink": True, "sink_x": 11.50, "sink_type": "single_cuba"},
    {"id": "fix_bath1_toilet", "type": "toilet", "room": "Banho 1", "x": 12.40, "z": 4.10, "w": 0.45, "d": 0.65, "h": 0.80, "material": "ceramic_white", "has_sink": False, "sink_x": None, "sink_type": None},
    {"id": "fix_bath1_glass_box", "type": "shower_box", "room": "Banho 1", "x": 10.60, "z": 4.10, "w": 0.85, "d": 1.20, "h": 2.10, "material": "glass_screen", "has_sink": False, "sink_x": None, "sink_type": None},

    # Lavabo
    {"id": "fix_lavabo_vanity", "type": "vanity", "room": "Lavabo", "x": 9.30, "z": 0.75, "w": 1.00, "d": 0.50, "h": 0.85, "material": "marble_white", "has_sink": True, "sink_x": 9.30, "sink_type": "single_cuba"},
    {"id": "fix_lavabo_toilet", "type": "toilet", "room": "Lavabo", "x": 8.90, "z": 1.40, "w": 0.45, "d": 0.65, "h": 0.80, "material": "ceramic_white", "has_sink": False, "sink_x": None, "sink_type": None}
]

# CÔMODOS
rooms = [
    {
        "id": "living",
        "name": "Living & Estar",
        "area": 24.5,
        "box": [4.70, 2.13, 9.95, 6.60],
        "floor": "tile_light",
        "spawn": [7.00, 1.60, 4.50, -1.57]
    },
    {
        "id": "terraco",
        "name": "Terraço Gourmet",
        "area": 19.8,
        "box": [0.40, 2.18, 4.70, 6.75],
        "floor": "deck_or_tile",
        "spawn": [2.50, 1.60, 4.50, 1.57]
    },
    {
        "id": "cozinha",
        "name": "Cozinha",
        "area": 9.8,
        "box": [3.48, 0.44, 8.60, 2.13],
        "floor": "tile_light",
        "spawn": [6.00, 1.60, 1.30, 3.14]
    },
    {
        "id": "servico",
        "name": "Área de Serviço",
        "area": 4.6,
        "box": [0.95, 0.44, 3.48, 2.18],
        "floor": "tile_light",
        "spawn": [2.20, 1.60, 1.30, 0]
    },
    {
        "id": "hall",
        "name": "Hall Social Privativo",
        "area": 3.8,
        "box": [9.95, 0.80, 11.80, 3.18],
        "floor": "tile_light",
        "spawn": [10.80, 1.60, 1.80, 1.57]
    },
    {
        "id": "lavabo",
        "name": "Lavabo",
        "area": 2.1,
        "box": [8.60, 0.44, 9.95, 1.98],
        "floor": "tile_light",
        "spawn": [9.25, 1.60, 1.20, 0]
    },
    {
        "id": "circulacao",
        "name": "Circulação Íntima & Roupeiro",
        "area": 4.5,
        "box": [7.28, 6.60, 10.15, 8.35],
        "floor": "wood",
        "spawn": [8.50, 1.60, 7.20, 1.57]
    },
    {
        "id": "suite_master",
        "name": "Suíte Master",
        "area": 15.2,
        "box": [0.94, 6.75, 4.05, 10.88],
        "floor": "wood",
        "spawn": [2.50, 1.60, 8.80, -1.57]
    },
    {
        "id": "closet_master",
        "name": "Closet Master",
        "area": 4.2,
        "box": [4.05, 6.75, 7.28, 8.40],
        "floor": "wood",
        "spawn": [5.60, 1.60, 7.50, 0]
    },
    {
        "id": "banho_master",
        "name": "Banho Master (Cuba Dupla)",
        "area": 4.3,
        "box": [4.05, 8.40, 5.80, 10.88],
        "floor": "tile_light",
        "spawn": [4.92, 1.60, 9.40, 0]
    },
    {
        "id": "suite2",
        "name": "Suíte 2",
        "area": 10.8,
        "box": [7.28, 8.35, 10.15, 10.88],
        "floor": "wood",
        "spawn": [8.70, 1.60, 9.60, 0]
    },
    {
        "id": "banho2",
        "name": "Banho 2",
        "area": 3.7,
        "box": [5.80, 8.40, 7.28, 10.88],
        "floor": "tile_light",
        "spawn": [6.54, 1.60, 9.40, 0]
    },
    {
        "id": "suite1",
        "name": "Suíte 1",
        "area": 10.5,
        "box": [10.15, 4.81, 12.86, 7.65],
        "floor": "wood",
        "spawn": [11.50, 1.60, 6.20, 0]
    },
    {
        "id": "banho1",
        "name": "Banho 1",
        "area": 3.6,
        "box": [10.15, 3.18, 12.86, 4.81],
        "floor": "tile_light",
        "spawn": [11.50, 1.60, 4.00, 0]
    },
    {
        "id": "terraco_tecnico",
        "name": "Terraço Técnico (AC)",
        "area": 2.8,
        "box": [10.17, 7.65, 12.63, 8.98],
        "floor": "deck_or_tile",
        "spawn": [11.40, 1.60, 8.30, 0]
    }
]

# Write directly to apartment_geometry.js
geometry_export = {
    "scale": "1:75",
    "private_area_m2": 125.79,
    "walls": walls,
    "pillars": pillars,
    "shafts": shafts,
    "fixtures": fixtures,
    "rooms": rooms
}

with open("apartment_geometry.js", "w", encoding="utf-8") as out_f:
    out_f.write("window.APARTMENT_GEOMETRY = " + json.dumps(geometry_export, indent=2, ensure_ascii=False) + ";\n")

print(f"Generated meticulous CAD geometry in apartment_geometry.js: {len(walls)} walls, {len(pillars)} pillars, {len(shafts)} shafts, {len(fixtures)} fixed fixtures, {len(rooms)} rooms!")

# Also write valid python build_geometry.py
import pprint
with open("build_geometry.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nHI VIEW ALTO DA BOA VISTA - FINAIS 1 E 6 (125.79 m²)\nMETICULOUS CAD REVISION & ARCHITECTURAL DATA GENERATOR\n"""\n\n')
    f.write("import json\n\n")
    f.write("walls = " + pprint.pformat(walls, indent=4) + "\n\n")
    f.write("pillars = " + pprint.pformat(pillars, indent=4) + "\n\n")
    f.write("shafts = " + pprint.pformat(shafts, indent=4) + "\n\n")
    f.write("fixtures = " + pprint.pformat(fixtures, indent=4) + "\n\n")
    f.write("rooms = " + pprint.pformat(rooms, indent=4) + "\n\n")
    f.write("""
geometry_export = {
    "scale": "1:75",
    "private_area_m2": 125.79,
    "walls": walls,
    "pillars": pillars,
    "shafts": shafts,
    "fixtures": fixtures,
    "rooms": rooms
}

with open("apartment_geometry.js", "w", encoding="utf-8") as out_f:
    out_f.write("window.APARTMENT_GEOMETRY = " + json.dumps(geometry_export, indent=2, ensure_ascii=False) + ";\\n")

print(f"Generated meticulous CAD geometry: {len(walls)} walls, {len(pillars)} pillars, {len(shafts)} shafts, {len(fixtures)} fixed fixtures, {len(rooms)} rooms!")
""")


print("Successfully wrote updated build_geometry.py")
