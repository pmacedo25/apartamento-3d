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
      "area": 4.4,
      "box": [
        10.45,
        0.85,
        12.3,
        3.25
      ],
      "spawn": [
        11.37,
        1.68,
        2.05,
        3.14
      ],
      "floor": "porcelain",
      "color": "#e2ded6"
    },
    {
      "id": "lavabo",
      "name": "Lavabo",
      "area": 2.7,
      "box": [
        8.95,
        0.44,
        10.45,
        2.25
      ],
      "spawn": [
        9.7,
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
      "area": 4.0,
      "box": [
        7.3,
        6.77,
        10.45,
        8.25
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
      "area": 8.5,
      "box": [
        10.45,
        4.8,
        13.35,
        7.75
      ],
      "spawn": [
        11.9,
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
      "area": 4.5,
      "box": [
        10.45,
        3.25,
        13.35,
        4.8
      ],
      "spawn": [
        11.9,
        1.68,
        4.0,
        0.0
      ],
      "floor": "tile_light",
      "color": "#ccc7bd"
    },
    {
      "id": "terraco_tecnico",
      "name": "Terra\u00e7o T\u00e9cnico (Ar Cond.)",
      "area": 4.2,
      "box": [
        10.45,
        7.75,
        13.35,
        9.2
      ],
      "spawn": [
        11.9,
        1.68,
        8.5,
        0.0
      ],
      "floor": "concrete",
      "color": "#b8b4ab"
    },
    {
      "id": "suite2",
      "name": "Su\u00edte 2",
      "area": 8.1,
      "box": [
        7.3,
        8.25,
        10.25,
        11.0
      ],
      "spawn": [
        8.8,
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
      "area": 4.1,
      "box": [
        5.75,
        8.35,
        7.3,
        11.0
      ],
      "spawn": [
        6.5,
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
      "area": 13.7,
      "box": [
        0.94,
        6.77,
        4.25,
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
      "id": "banho_master",
      "name": "Banho Master (Cuba Dupla)",
      "area": 3.8,
      "box": [
        4.25,
        8.35,
        5.75,
        10.9
      ],
      "spawn": [
        5.0,
        1.68,
        9.6,
        0.0
      ],
      "floor": "marble",
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
          "width": 1.2,
          "sill": 1.6,
          "height": 0.8
        }
      ]
    },
    {
      "id": "ext_north_kitchen",
      "x1": 3.95,
      "z1": 0.44,
      "x2": 8.95,
      "z2": 0.44,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_north_lavabo",
      "x1": 8.95,
      "z1": 0.44,
      "x2": 10.45,
      "z2": 0.44,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_north_hall_recess",
      "x1": 10.45,
      "z1": 0.44,
      "x2": 10.45,
      "z2": 0.85,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_north_hall_front",
      "x1": 10.45,
      "z1": 0.85,
      "x2": 12.3,
      "z2": 0.85,
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
      "x1": 12.3,
      "z1": 0.85,
      "x2": 12.3,
      "z2": 3.25,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_hall_to_bath1",
      "x1": 12.3,
      "z1": 3.25,
      "x2": 13.35,
      "z2": 3.25,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_east_bath1",
      "x1": 13.35,
      "z1": 3.25,
      "x2": 13.35,
      "z2": 4.8,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.5,
          "width": 0.6,
          "sill": 1.7,
          "height": 0.6
        }
      ]
    },
    {
      "id": "ext_east_suite1",
      "x1": 13.35,
      "z1": 4.8,
      "x2": 13.35,
      "z2": 7.75,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.8,
          "width": 1.4,
          "sill": 0.9,
          "height": 1.3,
          "label": "Janela Su\u00edte 1"
        }
      ]
    },
    {
      "id": "ext_east_tech_balcony",
      "x1": 13.35,
      "z1": 7.75,
      "x2": 13.35,
      "z2": 9.2,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_south_tech_balcony",
      "x1": 10.45,
      "z1": 9.2,
      "x2": 13.35,
      "z2": 9.2,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_west_tech_balcony",
      "x1": 10.45,
      "z1": 8.25,
      "x2": 10.45,
      "z2": 9.2,
      "thick": 0.15,
      "height": 1.2,
      "type": "railing",
      "openings": []
    },
    {
      "id": "ext_south_suite2",
      "x1": 7.3,
      "z1": 11.0,
      "x2": 10.25,
      "z2": 11.0,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.7,
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
      "z1": 8.25,
      "x2": 10.25,
      "z2": 11.0,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": []
    },
    {
      "id": "ext_south_bath2",
      "x1": 5.75,
      "z1": 11.0,
      "x2": 7.3,
      "z2": 11.0,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.4,
          "width": 0.6,
          "sill": 1.7,
          "height": 0.6
        }
      ]
    },
    {
      "id": "ext_south_bath_master",
      "x1": 4.25,
      "z1": 10.9,
      "x2": 5.75,
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
          "height": 0.6
        }
      ]
    },
    {
      "id": "ext_south_suite_master",
      "x1": 0.94,
      "z1": 10.9,
      "x2": 4.25,
      "z2": 10.9,
      "thick": 0.18,
      "height": 2.7,
      "type": "exterior",
      "openings": [
        {
          "type": "window",
          "start": 0.7,
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
      "id": "int_master_to_terrace",
      "x1": 0.94,
      "z1": 6.77,
      "x2": 3.95,
      "z2": 6.77,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_hallway_to_living",
      "x1": 3.95,
      "z1": 6.77,
      "x2": 7.76,
      "z2": 6.77,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_master_to_bath_master",
      "x1": 4.25,
      "z1": 8.35,
      "x2": 4.25,
      "z2": 10.9,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.35,
          "width": 0.7,
          "height": 2.1,
          "label": "Banho Master"
        }
      ]
    },
    {
      "id": "int_master_corridor_wall",
      "x1": 3.31,
      "z1": 8.35,
      "x2": 5.75,
      "z2": 8.35,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.15,
          "width": 0.8,
          "height": 2.1,
          "label": "Porta Su\u00edte Master"
        }
      ]
    },
    {
      "id": "int_bath_master_to_bath2",
      "x1": 5.75,
      "z1": 8.35,
      "x2": 5.75,
      "z2": 11.0,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_bath2_to_suite2",
      "x1": 7.3,
      "z1": 8.25,
      "x2": 7.3,
      "z2": 11.0,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.35,
          "width": 0.7,
          "height": 2.1,
          "label": "Banho 2"
        }
      ]
    },
    {
      "id": "int_suite2_to_corridor",
      "x1": 7.3,
      "z1": 8.25,
      "x2": 10.25,
      "z2": 8.25,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.5,
          "width": 0.8,
          "height": 2.1,
          "label": "Porta Su\u00edte 2"
        }
      ]
    },
    {
      "id": "int_suite1_to_living",
      "x1": 10.45,
      "z1": 4.8,
      "x2": 10.45,
      "z2": 7.75,
      "thick": 0.12,
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
      "z1": 4.8,
      "x2": 13.35,
      "z2": 4.8,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.6,
          "width": 0.7,
          "height": 2.1,
          "label": "Banho 1"
        }
      ]
    },
    {
      "id": "int_bath1_to_hall",
      "x1": 10.45,
      "z1": 3.25,
      "x2": 12.3,
      "z2": 3.25,
      "thick": 0.15,
      "height": 2.7,
      "type": "interior",
      "openings": []
    },
    {
      "id": "int_suite1_to_tech_balcony",
      "x1": 10.45,
      "z1": 7.75,
      "x2": 13.35,
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
      "x2": 10.45,
      "z2": 2.25,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "door",
          "start": 0.4,
          "width": 0.7,
          "height": 2.1,
          "label": "Lavabo"
        }
      ]
    },
    {
      "id": "int_hall_to_living",
      "x1": 10.45,
      "z1": 2.25,
      "x2": 10.45,
      "z2": 3.25,
      "thick": 0.12,
      "height": 2.7,
      "type": "interior",
      "openings": [
        {
          "type": "opening",
          "start": 0.0,
          "width": 1.0,
          "height": 2.4,
          "label": "Entrada Living"
        }
      ]
    }
  ]
};
