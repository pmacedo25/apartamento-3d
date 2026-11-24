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
        1.68,
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
        8.95,
        0.44,
        10.42,
        2.25
      ],
      "spawn": [
        9.68,
        1.68,
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
        8.95,
        2.25
      ],
      "spawn": [
        6.45,
        1.68,
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
        2.25
      ],
      "spawn": [
        2.45,
        1.68,
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
        2.25,
        3.95,
        6.77
      ],
      "spawn": [
        2.15,
        1.68,
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
        2.25,
        10.45,
        6.77
      ],
      "spawn": [
        7.2,
        1.68,
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
        1.68,
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
        1.68,
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
        11.89,
        1.68,
        4.0,
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
        1.68,
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
        1.68,
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
        1.68,
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
        1.68,
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
        1.68,
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
        1.68,
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
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "ventilation",
          "start": 0.5,
          "width": 1.4,
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
      "thick": 0.18,
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
      "thick": 0.18,
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
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "door",
          "start": 0.45,
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
      "thick": 0.18,
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
      "thick": 0.18,
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
      "thick": 0.18,
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
      "id": "ext_east_suite1",
      "x1": 13.33,
      "z1": 4.84,
      "x2": 13.33,
      "z2": 7.75,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.75,
          "width": 1.4,
          "sill": 0.9,
          "height": 1.3,
          "label": "Janela Su\u00edte 1"
        }
      ]
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
      "thick": 0.18,
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
      "id": "ext_east_suite2",
      "x1": 10.25,
      "z1": 8.35,
      "x2": 10.25,
      "z2": 10.9,
      "thick": 0.18,
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
      "thick": 0.18,
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
      "thick": 0.18,
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
      "id": "ext_south_suite_master",
      "x1": 0.94,
      "z1": 10.9,
      "x2": 4.45,
      "z2": 10.9,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.85,
          "width": 1.8,
          "sill": 0.9,
          "height": 1.3,
          "label": "Janela Su\u00edte Master"
        }
      ]
    },
    {
      "id": "ext_west_suite_master",
      "x1": 0.94,
      "z1": 6.77,
      "x2": 0.94,
      "z2": 10.9,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_west_terrace_balcony",
      "x1": 0.4,
      "z1": 2.25,
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
      "z2": 2.25,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "terrace_recess_top",
      "x1": 0.4,
      "z1": 2.25,
      "x2": 0.95,
      "z2": 2.25,
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
      "thick": 0.18,
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
          "start": 0.62,
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
          "start": 0.77,
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
          "start": 0.13,
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
          "start": 0.25,
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
      "thick": 0.15,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "door",
          "start": 1.8,
          "width": 0.75,
          "height": 2.1,
          "label": "Porta T\u00e9cnica AC"
        }
      ]
    },
    {
      "id": "int_terrace_to_living_glass",
      "x1": 3.95,
      "z1": 2.25,
      "x2": 3.95,
      "z2": 6.77,
      "thick": 0.1,
      "height": 2.7,
      "type": "sliding_glass_wall",
      "openings": [
        {
          "type": "sliding_glass",
          "start": 0.2,
          "width": 4.1,
          "height": 2.45,
          "label": "Esquadria de Vidro Terra\u00e7o"
        }
      ]
    },
    {
      "id": "int_terrace_to_service",
      "x1": 0.95,
      "z1": 2.25,
      "x2": 3.95,
      "z2": 2.25,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 2.2,
          "width": 0.75,
          "height": 2.1,
          "label": "Porta Servi\u00e7o/Terra\u00e7o"
        }
      ]
    },
    {
      "id": "int_kitchen_to_service",
      "x1": 3.95,
      "z1": 0.44,
      "x2": 3.95,
      "z2": 2.25,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "opening",
          "start": 0.5,
          "width": 0.9,
          "height": 2.2,
          "label": "Passagem Cozinha/Servi\u00e7o"
        }
      ]
    },
    {
      "id": "int_kitchen_counter",
      "x1": 3.95,
      "z1": 2.25,
      "x2": 7.8,
      "z2": 2.25,
      "thick": 0.3,
      "height": 0.92,
      "type": "countertop",
      "openings": []
    },
    {
      "id": "int_kitchen_open_pass",
      "x1": 7.8,
      "z1": 2.25,
      "x2": 8.95,
      "z2": 2.25,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "opening",
          "start": 0.0,
          "width": 1.15,
          "height": 2.4,
          "label": "Acesso Cozinha"
        }
      ]
    },
    {
      "id": "int_lavabo_to_kitchen",
      "x1": 8.95,
      "z1": 0.44,
      "x2": 8.95,
      "z2": 2.25,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_lavabo_to_living",
      "x1": 8.95,
      "z1": 2.25,
      "x2": 10.42,
      "z2": 2.25,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.35,
          "width": 0.7,
          "height": 2.1,
          "label": "Porta Lavabo"
        }
      ]
    },
    {
      "id": "int_hall_to_living",
      "x1": 10.42,
      "z1": 2.25,
      "x2": 10.42,
      "z2": 3.21,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "opening",
          "start": 0.0,
          "width": 0.96,
          "height": 2.4,
          "label": "Entrada Living"
        }
      ]
    }
  ]
};
