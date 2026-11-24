const APARTMENT_DATA = {
  "dimensions": {
    "width": 13.5,
    "depth": 11.38,
    "height": 2.7
  },
  "rooms": [
    {
      "id": "hall",
      "name": "Hall de Entrada",
      "area": 4.1,
      "box": [
        10.42,
        1.02,
        12.27,
        3.21
      ],
      "spawn": [
        11.35,
        1.6,
        2.05,
        3.14
      ],
      "floor": "porcelain",
      "color": "#e2ded6"
    },
    {
      "id": "lavabo",
      "name": "Lavabo Social",
      "area": 2.7,
      "box": [
        8.76,
        0.44,
        10.42,
        2.16
      ],
      "spawn": [
        9.55,
        1.6,
        1.4,
        0.0
      ],
      "floor": "tile_dark",
      "color": "#c8c4bc"
    },
    {
      "id": "cozinha",
      "name": "Cozinha",
      "area": 9.0,
      "box": [
        3.95,
        0.44,
        8.76,
        2.16
      ],
      "spawn": [
        6.35,
        1.6,
        1.35,
        3.14
      ],
      "floor": "porcelain",
      "color": "#ded9cf"
    },
    {
      "id": "servico",
      "name": "\u00c1rea de Servi\u00e7o",
      "area": 5.4,
      "box": [
        0.95,
        0.44,
        3.95,
        2.16
      ],
      "spawn": [
        2.45,
        1.6,
        1.35,
        0.0
      ],
      "floor": "tile_light",
      "color": "#d5d1c8"
    },
    {
      "id": "terraco",
      "name": "Terra\u00e7o Gourmet",
      "area": 16.0,
      "box": [
        0.4,
        2.16,
        3.95,
        6.77
      ],
      "spawn": [
        2.15,
        1.6,
        4.5,
        1.57
      ],
      "floor": "deck_or_tile",
      "color": "#cfc8ba"
    },
    {
      "id": "sala",
      "name": "Sala de Estar / Jantar",
      "area": 29.4,
      "box": [
        3.95,
        2.16,
        10.45,
        6.77
      ],
      "spawn": [
        7.2,
        1.6,
        4.5,
        -1.57
      ],
      "floor": "porcelain",
      "color": "#e8e5dc"
    },
    {
      "id": "circulacao",
      "name": "Circula\u00e7\u00e3o \u00cdntima",
      "area": 4.3,
      "box": [
        7.76,
        6.77,
        10.45,
        8.35
      ],
      "spawn": [
        8.8,
        1.6,
        7.5,
        3.14
      ],
      "floor": "wood",
      "color": "#ded4c3"
    },
    {
      "id": "suite1",
      "name": "Su\u00edte 1",
      "area": 8.4,
      "box": [
        10.45,
        4.84,
        13.33,
        7.75
      ],
      "spawn": [
        11.89,
        1.6,
        6.2,
        -1.57
      ],
      "floor": "wood",
      "color": "#d9ccb6"
    },
    {
      "id": "banho1",
      "name": "Banho 1",
      "area": 4.7,
      "box": [
        10.45,
        3.21,
        13.33,
        4.84
      ],
      "spawn": [
        11.45,
        1.6,
        4.2,
        0.0
      ],
      "floor": "tile_light",
      "color": "#ccc7bd"
    },
    {
      "id": "terraco_tecnico",
      "name": "Terra\u00e7o T\u00e9cnico (AC)",
      "area": 3.4,
      "box": [
        10.64,
        7.75,
        13.33,
        9.0
      ],
      "spawn": [
        11.95,
        1.6,
        8.35,
        0.0
      ],
      "floor": "concrete",
      "color": "#b8b4ab"
    },
    {
      "id": "suite2",
      "name": "Su\u00edte 2",
      "area": 6.4,
      "box": [
        7.76,
        8.35,
        10.25,
        10.9
      ],
      "spawn": [
        9.0,
        1.6,
        9.6,
        0.0
      ],
      "floor": "wood",
      "color": "#d9ccb6"
    },
    {
      "id": "banho2",
      "name": "Banho 2",
      "area": 3.6,
      "box": [
        6.34,
        8.35,
        7.76,
        10.9
      ],
      "spawn": [
        7.05,
        1.6,
        9.6,
        0.0
      ],
      "floor": "tile_light",
      "color": "#ccc7bd"
    },
    {
      "id": "suite_master",
      "name": "Su\u00edte Master",
      "area": 14.5,
      "box": [
        0.94,
        6.77,
        4.45,
        10.9
      ],
      "spawn": [
        2.6,
        1.6,
        8.8,
        0.0
      ],
      "floor": "wood",
      "color": "#d9ccb6"
    },
    {
      "id": "suite_master_closet",
      "name": "Closet Su\u00edte Master",
      "area": 5.2,
      "box": [
        4.45,
        6.77,
        7.76,
        8.35
      ],
      "spawn": [
        6.1,
        1.6,
        7.5,
        -1.57
      ],
      "floor": "wood",
      "color": "#d9ccb6"
    },
    {
      "id": "banho_master",
      "name": "Banho Master (Cuba Dupla)",
      "area": 4.8,
      "box": [
        4.45,
        8.35,
        6.34,
        10.9
      ],
      "spawn": [
        5.39,
        1.6,
        9.6,
        0.0
      ],
      "floor": "tile_light",
      "color": "#dedbd5"
    }
  ],
  "walls": [
    {
      "id": "ext_north_service",
      "x1": 0.95,
      "z1": 0.44,
      "x2": 3.95,
      "z2": 0.44,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "ventilation",
          "start": 0.45,
          "width": 1.2,
          "sill": 1.6,
          "height": 0.8,
          "label": "Ventila\u00e7\u00e3o Servi\u00e7o"
        }
      ]
    },
    {
      "id": "ext_north_kitchen_lavabo",
      "x1": 3.95,
      "z1": 0.44,
      "x2": 10.42,
      "z2": 0.44,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_north_hall_recess",
      "x1": 10.42,
      "z1": 0.44,
      "x2": 10.42,
      "z2": 1.02,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_north_hall_front",
      "x1": 10.42,
      "z1": 1.02,
      "x2": 12.27,
      "z2": 1.02,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "door",
          "start": 0.4,
          "width": 0.9,
          "height": 2.1,
          "label": "Entrada Social"
        }
      ]
    },
    {
      "id": "ext_east_hall",
      "x1": 12.27,
      "z1": 1.02,
      "x2": 12.27,
      "z2": 3.21,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_hall_to_bath1",
      "x1": 12.27,
      "z1": 3.21,
      "x2": 13.33,
      "z2": 3.21,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_east_bath1",
      "x1": 13.33,
      "z1": 3.21,
      "x2": 13.33,
      "z2": 4.84,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.5,
          "width": 0.6,
          "sill": 1.7,
          "height": 0.6,
          "label": "Janela Banho 1"
        }
      ]
    },
    {
      "id": "ext_east_suite1_solid_acoustic",
      "x1": 13.33,
      "z1": 4.84,
      "x2": 13.33,
      "z2": 7.75,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_east_tech_balcony",
      "x1": 13.33,
      "z1": 7.75,
      "x2": 13.33,
      "z2": 9.0,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_south_tech_balcony",
      "x1": 10.64,
      "z1": 9.0,
      "x2": 13.33,
      "z2": 9.0,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_west_tech_balcony",
      "x1": 10.64,
      "z1": 7.75,
      "x2": 10.64,
      "z2": 9.0,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_south_suite2",
      "x1": 7.76,
      "z1": 10.9,
      "x2": 10.25,
      "z2": 10.9,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.5,
          "width": 1.4,
          "sill": 0.9,
          "height": 1.3,
          "label": "Janela Su\u00edte 2"
        }
      ]
    },
    {
      "id": "ext_east_suite2_wall",
      "x1": 10.25,
      "z1": 8.35,
      "x2": 10.25,
      "z2": 10.9,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_south_bath2",
      "x1": 6.34,
      "z1": 10.9,
      "x2": 7.76,
      "z2": 10.9,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.4,
          "width": 0.6,
          "sill": 1.7,
          "height": 0.6,
          "label": "Janela Banho 2"
        }
      ]
    },
    {
      "id": "ext_south_bath_master",
      "x1": 4.45,
      "z1": 10.9,
      "x2": 6.34,
      "z2": 10.9,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.6,
          "width": 0.7,
          "sill": 1.7,
          "height": 0.6,
          "label": "Janela Banho Master"
        }
      ]
    },
    {
      "id": "ext_south_suite_master_solid",
      "x1": 0.94,
      "z1": 10.9,
      "x2": 4.45,
      "z2": 10.9,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_west_suite_master",
      "x1": 0.94,
      "z1": 6.77,
      "x2": 0.94,
      "z2": 10.9,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 1.2,
          "width": 1.6,
          "sill": 0.9,
          "height": 1.3,
          "label": "Janela Su\u00edte Master"
        }
      ]
    },
    {
      "id": "ext_west_terrace_balcony",
      "x1": 0.4,
      "z1": 2.16,
      "x2": 0.4,
      "z2": 6.77,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_west_service",
      "x1": 0.95,
      "z1": 0.44,
      "x2": 0.95,
      "z2": 2.16,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "terrace_recess_top",
      "x1": 0.4,
      "z1": 2.16,
      "x2": 0.95,
      "z2": 2.16,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "terrace_recess_bottom",
      "x1": 0.4,
      "z1": 6.77,
      "x2": 0.94,
      "z2": 6.77,
      "thick": 0.19,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "int_master_to_terrace_and_living",
      "x1": 0.94,
      "z1": 6.77,
      "x2": 7.76,
      "z2": 6.77,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_corridor_to_suite_master",
      "x1": 7.76,
      "z1": 6.77,
      "x2": 7.76,
      "z2": 8.35,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.6,
          "width": 0.8,
          "height": 2.1,
          "label": "Porta Su\u00edte Master"
        }
      ]
    },
    {
      "id": "int_master_to_bath_master_solid",
      "x1": 4.45,
      "z1": 8.35,
      "x2": 4.45,
      "z2": 10.9,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_bath_master_north_wall",
      "x1": 4.45,
      "z1": 8.35,
      "x2": 6.34,
      "z2": 8.35,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.85,
          "width": 0.7,
          "height": 2.1,
          "label": "Porta Banho Master"
        }
      ]
    },
    {
      "id": "int_bath_master_to_bath2_solid",
      "x1": 6.34,
      "z1": 8.35,
      "x2": 6.34,
      "z2": 10.9,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_bath2_north_wall_solid",
      "x1": 6.34,
      "z1": 8.35,
      "x2": 7.76,
      "z2": 8.35,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_bath2_to_suite2",
      "x1": 7.76,
      "z1": 8.35,
      "x2": 7.76,
      "z2": 10.9,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.12,
          "width": 0.7,
          "height": 2.1,
          "label": "Porta Banho 2"
        }
      ]
    },
    {
      "id": "int_corridor_to_suite2",
      "x1": 7.76,
      "z1": 8.35,
      "x2": 10.25,
      "z2": 8.35,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.2,
          "width": 0.8,
          "height": 2.1,
          "label": "Porta Su\u00edte 2"
        }
      ]
    },
    {
      "id": "int_suite1_to_living_corridor",
      "x1": 10.45,
      "z1": 4.84,
      "x2": 10.45,
      "z2": 7.75,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 1.95,
          "width": 0.8,
          "height": 2.1,
          "label": "Porta Su\u00edte 1"
        }
      ]
    },
    {
      "id": "int_bath1_to_suite1",
      "x1": 10.45,
      "z1": 4.84,
      "x2": 13.33,
      "z2": 4.84,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.2,
          "width": 0.7,
          "height": 2.1,
          "label": "Porta Banho 1"
        }
      ]
    },
    {
      "id": "int_bath1_to_hall",
      "x1": 10.45,
      "z1": 3.21,
      "x2": 12.27,
      "z2": 3.21,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_suite1_to_tech_balcony",
      "x1": 10.45,
      "z1": 7.75,
      "x2": 13.33,
      "z2": 7.75,
      "thick": 0.16,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.6,
          "width": 1.8,
          "sill": 0.9,
          "height": 1.3,
          "label": "Janela Su\u00edte 1"
        }
      ]
    },
    {
      "id": "int_terrace_to_living_glass",
      "x1": 3.95,
      "z1": 2.16,
      "x2": 3.95,
      "z2": 6.77,
      "thick": 0.1,
      "height": 2.7,
      "type": "sliding_glass_wall",
      "openings": [
        {
          "type": "sliding_glass",
          "start": 0.15,
          "width": 4.3,
          "height": 2.45,
          "label": "Esquadria de Vidro Terra\u00e7o"
        }
      ]
    },
    {
      "id": "int_terrace_to_service_solid",
      "x1": 0.95,
      "z1": 2.16,
      "x2": 3.95,
      "z2": 2.16,
      "thick": 0.16,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_kitchen_to_service",
      "x1": 3.95,
      "z1": 0.44,
      "x2": 3.95,
      "z2": 2.16,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.5,
          "width": 0.75,
          "height": 2.1,
          "label": "Porta Servi\u00e7o"
        }
      ]
    },
    {
      "id": "int_kitchen_to_terrace_door",
      "x1": 3.48,
      "z1": 2.16,
      "x2": 3.95,
      "z2": 2.16,
      "thick": 0.14,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_kitchen_div_wall",
      "x1": 3.95,
      "z1": 2.8,
      "x2": 7.6,
      "z2": 2.8,
      "thick": 0.15,
      "height": 0.95,
      "type": "countertop",
      "openings": []
    },
    {
      "id": "int_kitchen_div_lintel",
      "x1": 3.95,
      "z1": 2.8,
      "x2": 7.6,
      "z2": 2.8,
      "thick": 0.15,
      "height": 0.35,
      "type": "beam",
      "openings": []
    },
    {
      "id": "int_kitchen_open_pass",
      "x1": 7.6,
      "z1": 2.16,
      "x2": 8.76,
      "z2": 2.16,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "opening",
          "start": 0.0,
          "width": 1.16,
          "height": 2.4,
          "label": "Acesso Cozinha"
        }
      ]
    },
    {
      "id": "int_lavabo_to_kitchen",
      "x1": 8.76,
      "z1": 0.44,
      "x2": 8.76,
      "z2": 2.16,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_lavabo_to_living",
      "x1": 8.76,
      "z1": 2.16,
      "x2": 10.42,
      "z2": 2.16,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.25,
          "width": 0.7,
          "height": 2.1,
          "label": "Porta Lavabo"
        }
      ]
    },
    {
      "id": "int_hall_to_living",
      "x1": 10.42,
      "z1": 2.16,
      "x2": 10.42,
      "z2": 3.21,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "opening",
          "start": 0.0,
          "width": 1.05,
          "height": 2.4,
          "label": "Entrada Living"
        }
      ]
    }
  ],
  "pillars": [
    {
      "id": "pil_01",
      "name": "Pilar Servi\u00e7o Noroeste",
      "x": 0.95,
      "z": 0.44,
      "w": 0.28,
      "d": 0.28,
      "h": 2.7
    },
    {
      "id": "pil_02",
      "name": "Pilar Servi\u00e7o/Cozinha Norte",
      "x": 2.06,
      "z": 0.44,
      "w": 0.35,
      "d": 0.55,
      "h": 2.7
    },
    {
      "id": "pil_03",
      "name": "Pilar Cozinha/Lavabo Norte",
      "x": 8.76,
      "z": 0.44,
      "w": 0.35,
      "d": 0.6,
      "h": 2.7
    },
    {
      "id": "pil_04",
      "name": "Pilar Hall Entrada Leste",
      "x": 10.42,
      "z": 0.81,
      "w": 0.35,
      "d": 0.85,
      "h": 2.7
    },
    {
      "id": "pil_05",
      "name": "Pilar Hall/Banho 1",
      "x": 10.45,
      "z": 3.21,
      "w": 0.35,
      "d": 0.85,
      "h": 2.7
    },
    {
      "id": "pil_06",
      "name": "Pilar Cozinha/Terra\u00e7o",
      "x": 3.48,
      "z": 1.98,
      "w": 0.45,
      "d": 0.45,
      "h": 2.7
    },
    {
      "id": "pil_07",
      "name": "Pilar Terra\u00e7o/Master Oeste",
      "x": 0.94,
      "z": 6.77,
      "w": 0.35,
      "d": 0.85,
      "h": 2.7
    },
    {
      "id": "pil_08",
      "name": "Pilar Master Sudoeste",
      "x": 0.94,
      "z": 10.55,
      "w": 0.85,
      "d": 0.35,
      "h": 2.7
    },
    {
      "id": "pil_09",
      "name": "Pilar Circula\u00e7\u00e3o Central",
      "x": 8.76,
      "z": 6.77,
      "w": 0.35,
      "d": 0.85,
      "h": 2.7
    },
    {
      "id": "pil_10",
      "name": "Pilar Su\u00edte 1/T\u00e9cnico",
      "x": 10.45,
      "z": 7.75,
      "w": 0.35,
      "d": 0.6,
      "h": 2.7
    },
    {
      "id": "pil_11",
      "name": "Pilar T\u00e9cnico Sudeste",
      "x": 12.98,
      "z": 7.75,
      "w": 0.35,
      "d": 0.85,
      "h": 2.7
    }
  ],
  "shafts": [
    {
      "id": "sh_gourmet",
      "name": "Shaft Gourmet/Servi\u00e7o",
      "x": 2.3,
      "z": 2.16,
      "w": 0.87,
      "d": 0.55,
      "h": 2.7
    },
    {
      "id": "sh_master",
      "name": "Shaft Banho Master",
      "x": 4.06,
      "z": 10.04,
      "w": 0.45,
      "d": 0.86,
      "h": 2.7
    },
    {
      "id": "sh_banho2",
      "name": "Shaft Banho 2",
      "x": 5.94,
      "z": 10.04,
      "w": 0.4,
      "d": 0.86,
      "h": 2.7
    },
    {
      "id": "sh_banho1",
      "name": "Shaft Banho 1",
      "x": 11.8,
      "z": 3.21,
      "w": 0.85,
      "d": 0.6,
      "h": 2.7
    },
    {
      "id": "sh_lavabo",
      "name": "Shaft Lavabo",
      "x": 8.76,
      "z": 0.44,
      "w": 0.6,
      "d": 0.5,
      "h": 2.7
    },
    {
      "id": "sh_servico",
      "name": "Shaft \u00c1rea de Servi\u00e7o",
      "x": 1.25,
      "z": 0.44,
      "w": 0.8,
      "d": 0.5,
      "h": 2.7
    },
    {
      "id": "sh_tecnico",
      "name": "Shaft Terra\u00e7o T\u00e9cnico AC",
      "x": 12.42,
      "z": 8.25,
      "w": 0.35,
      "d": 0.65,
      "h": 2.7
    }
  ],
  "fixtures": [
    {
      "id": "bancada_cozinha",
      "type": "counter_sink",
      "room": "cozinha",
      "x": 4.1,
      "z": 0.46,
      "w": 4.5,
      "d": 0.6,
      "h": 0.88,
      "material": "granite_black",
      "has_sink": true,
      "sink_x": 6.0,
      "sink_type": "kitchen_rect"
    },
    {
      "id": "tanque_servico",
      "type": "laundry_tub",
      "room": "servico",
      "x": 2.25,
      "z": 0.46,
      "w": 0.7,
      "d": 0.55,
      "h": 0.86,
      "material": "ceramic_white",
      "has_sink": true,
      "sink_x": 2.6,
      "sink_type": "laundry_tub"
    },
    {
      "id": "bancada_gourmet",
      "type": "gourmet_counter",
      "room": "terraco",
      "x": 0.96,
      "z": 2.18,
      "w": 1.34,
      "d": 0.6,
      "h": 0.9,
      "material": "granite_black",
      "has_sink": true,
      "sink_x": 1.3,
      "sink_type": "round_sink",
      "has_barbecue": true,
      "bbq_x": 1.85,
      "bbq_w": 0.45
    },
    {
      "id": "bancada_banho_master",
      "type": "double_vanity",
      "room": "banho_master",
      "x": 4.47,
      "z": 8.4,
      "w": 0.55,
      "d": 1.5,
      "h": 0.85,
      "material": "marble_light",
      "has_sink": true,
      "sink_type": "double_sink",
      "sink_z1": 8.75,
      "sink_z2": 9.45
    },
    {
      "id": "vaso_banho_master",
      "type": "toilet",
      "room": "banho_master",
      "x": 5.85,
      "z": 9.15,
      "w": 0.42,
      "d": 0.65,
      "h": 0.78,
      "rotY": -1.57
    },
    {
      "id": "box_banho_master",
      "type": "shower_box",
      "room": "banho_master",
      "x": 4.45,
      "z": 9.9,
      "w": 1.89,
      "d": 1.0,
      "h": 1.95,
      "shower_pos": [
        5.4,
        2.2,
        10.75
      ]
    },
    {
      "id": "bancada_banho2",
      "type": "vanity",
      "room": "banho2",
      "x": 6.36,
      "z": 8.37,
      "w": 0.85,
      "d": 0.55,
      "h": 0.85,
      "material": "marble_light",
      "has_sink": true,
      "sink_x": 6.78,
      "sink_type": "single_sink"
    },
    {
      "id": "vaso_banho2",
      "type": "toilet",
      "room": "banho2",
      "x": 6.45,
      "z": 9.15,
      "w": 0.42,
      "d": 0.65,
      "h": 0.78,
      "rotY": 1.57
    },
    {
      "id": "box_banho2",
      "type": "shower_box",
      "room": "banho2",
      "x": 6.34,
      "z": 9.9,
      "w": 1.42,
      "d": 1.0,
      "h": 1.95,
      "shower_pos": [
        7.05,
        2.2,
        10.75
      ]
    },
    {
      "id": "bancada_banho1",
      "type": "vanity",
      "room": "banho1",
      "x": 10.47,
      "z": 3.25,
      "w": 0.55,
      "d": 0.85,
      "h": 0.85,
      "material": "marble_light",
      "has_sink": true,
      "sink_z": 3.65,
      "sink_type": "single_sink"
    },
    {
      "id": "vaso_banho1",
      "type": "toilet",
      "room": "banho1",
      "x": 11.45,
      "z": 3.3,
      "w": 0.42,
      "d": 0.65,
      "h": 0.78,
      "rotY": 0.0
    },
    {
      "id": "box_banho1",
      "type": "shower_box",
      "room": "banho1",
      "x": 12.05,
      "z": 3.21,
      "w": 1.28,
      "d": 1.63,
      "h": 1.95,
      "shower_pos": [
        12.7,
        2.2,
        4.0
      ]
    },
    {
      "id": "bancada_lavabo",
      "type": "vanity",
      "room": "lavabo",
      "x": 9.75,
      "z": 1.5,
      "w": 0.55,
      "d": 0.65,
      "h": 0.85,
      "material": "marble_light",
      "has_sink": true,
      "sink_z": 1.82,
      "sink_type": "single_sink"
    },
    {
      "id": "vaso_lavabo",
      "type": "toilet",
      "room": "lavabo",
      "x": 9.25,
      "z": 0.55,
      "w": 0.42,
      "d": 0.65,
      "h": 0.78,
      "rotY": 0.0
    }
  ]
};
