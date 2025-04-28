# IMPORTACIONES
import random

# DEFINICIONES
BBDD_JUGADORES = {
    1: {'id_equipo': "Boca Juniors", 'nombre': 'Sergio', 'apellido': 'Romero', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False},
    2: {'id_equipo': "Boca Juniors", 'nombre': 'Luis', 'apellido': 'Advíncula', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    3: {'id_equipo': "Boca Juniors", 'nombre': 'Cristian', 'apellido': 'Lema', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    4: {'id_equipo': "Boca Juniors", 'nombre': 'Marcos', 'apellido': 'Rojo', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    5: {'id_equipo': "Boca Juniors", 'nombre': 'Frank', 'apellido': 'Fabra', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    6: {'id_equipo': "Boca Juniors", 'nombre': 'Guillermo', 'apellido': 'Fernández', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    7: {'id_equipo': "Boca Juniors", 'nombre': 'Ezequiel', 'apellido': 'Fernández', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    8: {'id_equipo': "Boca Juniors", 'nombre': 'Kevin', 'apellido': 'Zenón', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    9: {'id_equipo': "Boca Juniors", 'nombre': 'Luca', 'apellido': 'Langoni', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    10: {'id_equipo': "Boca Juniors", 'nombre': 'Miguel', 'apellido': 'Merentiel', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    11: {'id_equipo': "Boca Juniors", 'nombre': 'Edinson', 'apellido': 'Cavani', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    12: {'id_equipo': "River Plate", 'nombre': 'Franco', 'apellido': 'Armani', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False},
    13: {'id_equipo': "River Plate", 'nombre': 'Andrés', 'apellido': 'Herrera', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    14: {'id_equipo': "River Plate", 'nombre': 'Leandro', 'apellido': 'González Pirez', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    15: {'id_equipo': "River Plate", 'nombre': 'Paulo', 'apellido': 'Díaz', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    16: {'id_equipo': "River Plate", 'nombre': 'Milton', 'apellido': 'Casco', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    17: {'id_equipo': "River Plate", 'nombre': 'Rodrigo', 'apellido': 'Aliendro', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    18: {'id_equipo': "River Plate", 'nombre': 'Nicolás', 'apellido': 'De la Cruz', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    19: {'id_equipo': "River Plate", 'nombre': 'Ignacio', 'apellido': 'Fernández', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    20: {'id_equipo': "River Plate", 'nombre': 'Esequiel', 'apellido': 'Barco', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    21: {'id_equipo': "River Plate", 'nombre': 'Miguel', 'apellido': 'Borja', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    22: {'id_equipo': "River Plate", 'nombre': 'Facundo', 'apellido': 'Colidio', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    23: {'id_equipo': "Racing Club", 'nombre': 'Gabriel', 'apellido': 'Arias', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False},
    24: {'id_equipo': "Racing Club", 'nombre': 'Facundo', 'apellido': 'Mura', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    25: {'id_equipo': "Racing Club", 'nombre': 'Leonardo', 'apellido': 'Sigali', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    26: {'id_equipo': "Racing Club", 'nombre': 'Nazareno', 'apellido': 'Colombo', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    27: {'id_equipo': "Racing Club", 'nombre': 'Gabriel', 'apellido': 'Rojas', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    28: {'id_equipo': "Racing Club", 'nombre': 'Aníbal', 'apellido': 'Moreno', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    29: {'id_equipo': "Racing Club", 'nombre': 'Juan', 'apellido': 'Nardoni', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    30: {'id_equipo': "Racing Club", 'nombre': 'Agustín', 'apellido': 'Almendra', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    31: {'id_equipo': "Racing Club", 'nombre': 'Roger', 'apellido': 'Martínez', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    32: {'id_equipo': "Racing Club", 'nombre': 'Johan', 'apellido': 'Carbonero', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    33: {'id_equipo': "Racing Club", 'nombre': 'Maximiliano', 'apellido': 'Romero', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    34: {'id_equipo': "Independiente", 'nombre': 'Rodrigo', 'apellido': 'Rey', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False},
    35: {'id_equipo': "Independiente", 'nombre': 'Mauricio', 'apellido': 'Isla', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    36: {'id_equipo': "Independiente", 'nombre': 'Joaquín', 'apellido': 'Laso', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    37: {'id_equipo': "Independiente", 'nombre': 'Ayrton', 'apellido': 'Costa', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    38: {'id_equipo': "Independiente", 'nombre': 'Damián', 'apellido': 'Pérez', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False},
    39: {'id_equipo': "Independiente", 'nombre': 'Federico', 'apellido': 'Mancuello', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    40: {'id_equipo': "Independiente", 'nombre': 'Iván', 'apellido': 'Marcone', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    41: {'id_equipo': "Independiente", 'nombre': 'Lucas', 'apellido': 'González', 'posicion': 'Mediocampista', 'costo': 1000000, 'flag_capitan': False},
    42: {'id_equipo': "Independiente", 'nombre': 'Matías', 'apellido': 'Giménez', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    43: {'id_equipo': "Independiente", 'nombre': 'Alex', 'apellido': 'Luna', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    44: {'id_equipo': "Independiente", 'nombre': 'Gabriel', 'apellido': 'Ávalos', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    45: {'id_equipo': "San Lorenzo", 'nombre': 'Facundo', 'apellido': 'Altamirano', 'posicion': 'Arquero', 'costo': 1200000, 'flag_capitan': False}, 
    46: {'id_equipo': "San Lorenzo", 'nombre': 'Agustín', 'apellido': 'Giay', 'posicion': 'Defensor', 'costo': 7000000, 'flag_capitan': False}, 
    47: {'id_equipo': "San Lorenzo", 'nombre': 'Federico', 'apellido': 'Gattoni', 'posicion': 'Defensor', 'costo': 2500000, 'flag_capitan': False}, 
    48: {'id_equipo': "San Lorenzo", 'nombre': 'Gastón', 'apellido': 'Hernández', 'posicion': 'Defensor', 'costo': 3500000, 'flag_capitan': False}, 
    49: {'id_equipo': "San Lorenzo", 'nombre': 'Malcom', 'apellido': 'Braida', 'posicion': 'Defensor', 'costo': 4000000, 'flag_capitan': False}, 
    50: {'id_equipo': "San Lorenzo", 'nombre': 'Jalil', 'apellido': 'Elías', 'posicion': 'Mediocampista', 'costo': 2500000, 'flag_capitan': False}, 
    51: {'id_equipo': "San Lorenzo", 'nombre': 'Elías', 'apellido': 'Pérez', 'posicion': 'Mediocampista', 'costo': 2000000, 'flag_capitan': False}, 
    52: {'id_equipo': "San Lorenzo", 'nombre': 'Nahuel', 'apellido': 'Barrios', 'posicion': 'Delantero', 'costo': 2200000, 'flag_capitan': False}, 
    53: {'id_equipo': "San Lorenzo", 'nombre': 'Iván', 'apellido': 'Leguizamón', 'posicion': 'Delantero', 'costo': 2500000, 'flag_capitan': False}, 
    54: {'id_equipo': "San Lorenzo", 'nombre': 'Adam', 'apellido': 'Bareiro', 'posicion': 'Delantero', 'costo': 4500000, 'flag_capitan': False}, 
    55: {'id_equipo': "San Lorenzo", 'nombre': 'Nicolás', 'apellido': 'Blandi', 'posicion': 'Delantero', 'costo': 800000, 'flag_capitan': False}, 
    56: {'id_equipo': "Huracán", 'nombre': 'Lucas', 'apellido': 'Chaves', 'posicion': 'Arquero', 'costo': 1200000, 'flag_capitan': False}, 
    57: {'id_equipo': "Huracán", 'nombre': 'Guillermo', 'apellido': 'Soto', 'posicion': 'Defensor', 'costo': 600000, 'flag_capitan': False}, 
    58: {'id_equipo': "Huracán", 'nombre': 'Fernando', 'apellido': 'Tobio', 'posicion': 'Defensor', 'costo': 300000, 'flag_capitan': False},
    59: {'id_equipo': "Huracán", 'nombre': 'Lucas', 'apellido': 'Souto', 'posicion': 'Defensor', 'costo': 800000, 'flag_capitan': False}, 
    60: {'id_equipo': "Huracán", 'nombre': 'César', 'apellido': 'Ibáñez', 'posicion': 'Defensor', 'costo': 1200000, 'flag_capitan': False}, 
    61: {'id_equipo': "Huracán", 'nombre': 'Héctor', 'apellido': 'Fértoli', 'posicion': 'Mediocampista', 'costo': 800000, 'flag_capitan': False}, 
    62: {'id_equipo': "Huracán", 'nombre': 'Federico', 'apellido': 'Fattori', 'posicion': 'Mediocampista', 'costo': 700000, 'flag_capitan': False}, 
    63: {'id_equipo': "Huracán", 'nombre': 'Santiago', 'apellido': 'Hezze', 'posicion': 'Mediocampista', 'costo': 8000000, 'flag_capitan': False}, 
    64: {'id_equipo': "Huracán", 'nombre': 'Juan', 'apellido': 'Gauto', 'posicion': 'Delantero', 'costo': 1200000, 'flag_capitan': False}, 
    65: {'id_equipo': "Huracán", 'nombre': 'Ignacio', 'apellido': 'Pussetto', 'posicion': 'Delantero', 'costo': 2200000, 'flag_capitan': False}, 
    66: {'id_equipo': "Huracán", 'nombre': 'Matías', 'apellido': 'Cóccaro', 'posicion': 'Delantero', 'costo': 3000000, 'flag_capitan': False}, 
    67: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Tomás', 'apellido': 'Marchiori', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    68: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Leonardo', 'apellido': 'Jara', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    69: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Diego', 'apellido': 'Godín', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    70: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Valentín', 'apellido': 'Gómez', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    71: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Francisco', 'apellido': 'Ortega', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    72: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Máximo', 'apellido': 'Perrone', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    73: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Nicolás', 'apellido': 'Garayalde', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    74: {'id_equipo': "Vélez Sarsfield", 'nombre': 'José', 'apellido': 'Florentín', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    75: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Lucas', 'apellido': 'Janson', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    76: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Abiel', 'apellido': 'Osorio', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    77: {'id_equipo': "Vélez Sarsfield", 'nombre': 'Walter', 'apellido': 'Bou', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    78: {'id_equipo': "Estudiantes", 'nombre': 'Mariano', 'apellido': 'Andújar', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    79: {'id_equipo': "Estudiantes", 'nombre': 'Leonardo', 'apellido': 'Godoy', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    80: {'id_equipo': "Estudiantes", 'nombre': 'Zaid', 'apellido': 'Romero', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    81: {'id_equipo': "Estudiantes", 'nombre': 'Luciano', 'apellido': 'Lollo', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    82: {'id_equipo': "Estudiantes", 'nombre': 'Emmanuel', 'apellido': 'Más', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    83: {'id_equipo': "Estudiantes", 'nombre': 'Jorge', 'apellido': 'Rodríguez', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    84: {'id_equipo': "Estudiantes", 'nombre': 'Fernando', 'apellido': 'Zuqui', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    85: {'id_equipo': "Estudiantes", 'nombre': 'Benjamín', 'apellido': 'Rollheiser', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    86: {'id_equipo': "Estudiantes", 'nombre': 'José', 'apellido': 'Sosa', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    87: {'id_equipo': "Estudiantes", 'nombre': 'Guido', 'apellido': 'Carrillo', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    88: {'id_equipo': "Estudiantes", 'nombre': 'Mauro', 'apellido': 'Boselli', 'posicion': 'sin definir', 'costo': 1000000, 'flag_capitan': False}, 
    89: {'id_equipo': "Gimnasia", 'nombre': 'Tomás', 'apellido': 'Durso', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False}, 
    90: {'id_equipo': "Gimnasia", 'nombre': 'Bautista', 'apellido': 'Barros Schelotto', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    91: {'id_equipo': "Gimnasia", 'nombre': 'Felipe', 'apellido': 'Sánchez', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    92: {'id_equipo': "Gimnasia", 'nombre': 'Leonardo', 'apellido': 'Morales', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    93: {'id_equipo': "Gimnasia", 'nombre': 'Nicolás', 'apellido': 'Colazo', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    94: {'id_equipo': "Gimnasia", 'nombre': 'Rodrigo', 'apellido': 'Saravia', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    95: {'id_equipo': "Gimnasia", 'nombre': 'Brahian', 'apellido': 'Alemán', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    96: {'id_equipo': "Gimnasia", 'nombre': 'Alan', 'apellido': 'Lescano', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    97: {'id_equipo': "Gimnasia", 'nombre': 'Matías', 'apellido': 'Abaldo', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    98: {'id_equipo': "Gimnasia", 'nombre': 'Cristian', 'apellido': 'Tarragona', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    99: {'id_equipo': "Gimnasia", 'nombre': 'Rodrigo', 'apellido': 'Castillo', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    100: {'id_equipo': "Lanús", 'nombre': 'Lucas', 'apellido': 'Acosta', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False}, 
    101: {'id_equipo': "Lanús", 'nombre': 'Braian', 'apellido': 'Aguirre', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    102: {'id_equipo': "Lanús", 'nombre': 'Matías', 'apellido': 'Pérez', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    103: {'id_equipo': "Lanús", 'nombre': 'Yonathan', 'apellido': 'Cabral', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    104: {'id_equipo': "Lanús", 'nombre': 'Julian', 'apellido': 'Aude', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    105: {'id_equipo': "Lanús", 'nombre': 'Tomas', 'apellido': 'Belmonte', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    106: {'id_equipo': "Lanús", 'nombre': 'Luciano', 'apellido': 'Boggio', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    107: {'id_equipo': "Lanús", 'nombre': 'Pedro', 'apellido': 'De La Vega', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    108: {'id_equipo': "Lanús", 'nombre': 'Franco', 'apellido': 'Orozco', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    109: {'id_equipo': "Lanús", 'nombre': 'Leandro', 'apellido': 'Díaz', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    110: {'id_equipo': "Lanús", 'nombre': 'José', 'apellido': 'Sand', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    111: {'id_equipo': "Banfield", 'nombre': 'Marcelo', 'apellido': 'Barovero', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False}, 
    112: {'id_equipo': "Banfield", 'nombre': 'Emanuel', 'apellido': 'Coronel', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    113: {'id_equipo': "Banfield", 'nombre': 'Alejandro', 'apellido': 'Maciel', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    114: {'id_equipo': "Banfield", 'nombre': 'Luis', 'apellido': 'Del Pino Mago', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    115: {'id_equipo': "Banfield", 'nombre': 'Emanuel', 'apellido': 'Insúa', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    116: {'id_equipo': "Banfield", 'nombre': 'Alejandro', 'apellido': 'Cabrera', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    117: {'id_equipo': "Banfield", 'nombre': 'Ignacio', 'apellido': 'Rodríguez', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    118: {'id_equipo': "Banfield", 'nombre': 'Nicolás', 'apellido': 'Sosa Sánchez', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    119: {'id_equipo': "Banfield", 'nombre': 'Agustín', 'apellido': 'Urzi', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    120: {'id_equipo': "Banfield", 'nombre': 'Milton', 'apellido': 'Giménez', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    121: {'id_equipo': "Banfield", 'nombre': 'Juan', 'apellido': 'Bisanz', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    122: {'id_equipo': "Argentinos Juniors", 'nombre': 'Federico', 'apellido': 'Lanzillotta', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False}, 
    123: {'id_equipo': "Argentinos Juniors", 'nombre': 'Kevin', 'apellido': 'Mac Allister', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    124: {'id_equipo': "Argentinos Juniors", 'nombre': 'Miguel', 'apellido': 'Torrén', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    125: {'id_equipo': "Argentinos Juniors", 'nombre': 'Lucas', 'apellido': 'Villalba', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    126: {'id_equipo': "Argentinos Juniors", 'nombre': 'Román', 'apellido': 'Vega', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    127: {'id_equipo': "Argentinos Juniors", 'nombre': 'Franco', 'apellido': 'Moyano', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    128: {'id_equipo': "Argentinos Juniors", 'nombre': 'Fausto', 'apellido': 'Vera', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    129: {'id_equipo': "Argentinos Juniors", 'nombre': 'Alan', 'apellido': 'Rodríguez', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    130: {'id_equipo': "Argentinos Juniors", 'nombre': 'Thiago', 'apellido': 'Nuss', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    131: {'id_equipo': "Argentinos Juniors", 'nombre': 'Gabriel', 'apellido': 'Ávalos', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    132: {'id_equipo': "Argentinos Juniors", 'nombre': 'Francisco', 'apellido': 'González Metilli', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    133: {'id_equipo': "Defensa y Justicia", 'nombre': 'Ezequiel', 'apellido': 'Unsain', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False}, 
    134: {'id_equipo': "Defensa y Justicia", 'nombre': 'Nicolás', 'apellido': 'Tripichio', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    135: {'id_equipo': "Defensa y Justicia", 'nombre': 'Adonis', 'apellido': 'Frías', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    136: {'id_equipo': "Defensa y Justicia", 'nombre': 'Tomás', 'apellido': 'Cardona', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    137: {'id_equipo': "Defensa y Justicia", 'nombre': 'Alexis', 'apellido': 'Soto', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    138: {'id_equipo': "Defensa y Justicia", 'nombre': 'Kevin', 'apellido': 'Gutiérrez', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    139: {'id_equipo': "Defensa y Justicia", 'nombre': 'Gabriel', 'apellido': 'Alanís', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    140: {'id_equipo': "Defensa y Justicia", 'nombre': 'David', 'apellido': 'Barbona', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    141: {'id_equipo': "Defensa y Justicia", 'nombre': 'Gastón', 'apellido': 'Togni', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    142: {'id_equipo': "Defensa y Justicia", 'nombre': 'Uvita', 'apellido': 'Fernández', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    143: {'id_equipo': "Defensa y Justicia", 'nombre': 'Nicolás', 'apellido': 'Fernández', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    144: {'id_equipo': "Tigre", 'nombre': 'Gonzalo', 'apellido': 'Marinelli', 'posicion': 'Arquero', 'costo': 1000000, 'flag_capitan': False}, 
    145: {'id_equipo': "Tigre", 'nombre': 'Lucas', 'apellido': 'Blondel', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    146: {'id_equipo': "Tigre", 'nombre': 'Víctor', 'apellido': 'Cabrera', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    147: {'id_equipo': "Tigre", 'nombre': 'Abel', 'apellido': 'Luciatti', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    148: {'id_equipo': "Tigre", 'nombre': 'Sebastián', 'apellido': 'Prieto', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    149: {'id_equipo': "Tigre", 'nombre': 'Sebastián', 'apellido': 'Prediger', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    150: {'id_equipo': "Tigre", 'nombre': 'Lucas', 'apellido': 'Menossi', 'posicion': 'Centrocampista', 'costo': 1000000, 'flag_capitan': False}, 
    151: {'id_equipo': "Tigre", 'nombre': 'Alexis', 'apellido': 'Castro', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    152: {'id_equipo': "Tigre", 'nombre': 'Iñaki', 'apellido': 'Gutiérrez', 'posicion': 'Defensor', 'costo': 1000000, 'flag_capitan': False}, 
    153: {'id_equipo': "Tigre", 'nombre': 'Facundo', 'apellido': 'Colidio', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False}, 
    154: {'id_equipo': "Tigre", 'nombre': 'Mateo', 'apellido': 'Retegui', 'posicion': 'Delantero', 'costo': 1000000, 'flag_capitan': False},
    155: {'id_equipo': "Rosario Central", 'nombre': 'Jorge', 'apellido': 'Broun', 'posicion': 'arquero', 'costo': 1000000, 'flag_capitan': False}, 
    156: {'id_equipo': "Rosario Central", 'nombre': 'Damián', 'apellido': 'Martínez', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    157: {'id_equipo': "Rosario Central", 'nombre': 'Facundo', 'apellido': 'Mallo', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    158: {'id_equipo': "Rosario Central", 'nombre': 'Carlos', 'apellido': 'Quintana', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    159: {'id_equipo': "Rosario Central", 'nombre': 'Alan', 'apellido': 'Rodríguez', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    160: {'id_equipo': "Rosario Central", 'nombre': 'Kevin', 'apellido': 'Ortiz', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    161: {'id_equipo': "Rosario Central", 'nombre': 'Ignacio', 'apellido': 'Malcorra', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    162: {'id_equipo': "Rosario Central", 'nombre': 'Gino', 'apellido': 'Infantino', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    163: {'id_equipo': "Rosario Central", 'nombre': 'Jaminton', 'apellido': 'Campaz', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    164: {'id_equipo': "Rosario Central", 'nombre': 'Lautaro', 'apellido': 'Giaccone', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    165: {'id_equipo': "Rosario Central", 'nombre': 'Alejo', 'apellido': 'Véliz', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    166: {'id_equipo': "Newell's Old Boys", 'nombre': 'Lucas', 'apellido': 'Hoyos', 'posicion': 'arquero', 'costo': 1000000, 'flag_capitan': False}, 
    167: {'id_equipo': "Newell's Old Boys", 'nombre': 'Armando', 'apellido': 'Méndez', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    168: {'id_equipo': "Newell's Old Boys", 'nombre': 'Gustavo', 'apellido': 'Velázquez', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    169: {'id_equipo': "Newell's Old Boys", 'nombre': 'Willian', 'apellido': 'Tesillo', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    170: {'id_equipo': "Newell's Old Boys", 'nombre': 'Ángelo', 'apellido': 'Martino', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    171: {'id_equipo': "Newell's Old Boys", 'nombre': 'Juan', 'apellido': 'Sforza', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    172: {'id_equipo': "Newell's Old Boys", 'nombre': 'Iván', 'apellido': 'Gómez', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    173: {'id_equipo': "Newell's Old Boys", 'nombre': 'Éver', 'apellido': 'Banega', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    174: {'id_equipo': "Newell's Old Boys", 'nombre': 'Brian', 'apellido': 'Aguirre', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    175: {'id_equipo': "Newell's Old Boys", 'nombre': 'Francisco', 'apellido': 'González', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    176: {'id_equipo': "Newell's Old Boys", 'nombre': 'Ramiro', 'apellido': 'Sordo', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    177: {'id_equipo': "Atlético Tucumán", 'nombre': 'Tomás', 'apellido': 'Marchiori', 'posicion': 'arquero', 'costo': 1000000, 'flag_capitan': False}, 
    178: {'id_equipo': "Atlético Tucumán", 'nombre': 'Marcelo', 'apellido': 'Ortiz', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    179: {'id_equipo': "Atlético Tucumán", 'nombre': 'Bruno', 'apellido': 'Bianchi', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    180: {'id_equipo': "Atlético Tucumán", 'nombre': 'Matías', 'apellido': 'Orihuela', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    181: {'id_equipo': "Atlético Tucumán", 'nombre': 'Renzo', 'apellido': 'Tesuri', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    182: {'id_equipo': "Atlético Tucumán", 'nombre': 'Guillermo', 'apellido': 'Acosta', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    183: {'id_equipo': "Atlético Tucumán", 'nombre': 'Ramiro', 'apellido': 'Carrera', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    184: {'id_equipo': "Atlético Tucumán", 'nombre': 'Joaquín', 'apellido': 'Pereyra', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    185: {'id_equipo': "Atlético Tucumán", 'nombre': 'Marcelo', 'apellido': 'Estigarribia', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    186: {'id_equipo': "Atlético Tucumán", 'nombre': 'Cristian', 'apellido': 'Menéndez', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    187: {'id_equipo': "Atlético Tucumán", 'nombre': 'Mateo', 'apellido': 'Coronel', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    188: {'id_equipo': "Colón", 'nombre': 'Ignacio', 'apellido': 'Chicco', 'posicion': 'arquero', 'costo': 1000000, 'flag_capitan': False}, 
    189: {'id_equipo': "Colón", 'nombre': 'Eric', 'apellido': 'Meza', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    190: {'id_equipo': "Colón", 'nombre': 'Paolo', 'apellido': 'Goltz', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    191: {'id_equipo': "Colón", 'nombre': 'Facundo', 'apellido': 'Garcés', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    192: {'id_equipo': "Colón", 'nombre': 'Rafael', 'apellido': 'Delgado', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    193: {'id_equipo': "Colón", 'nombre': 'Federico', 'apellido': 'Lértora', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    194: {'id_equipo': "Colón", 'nombre': 'Cristian', 'apellido': 'Vega', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    195: {'id_equipo': "Colón", 'nombre': 'Santiago', 'apellido': 'Pierotti', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    196: {'id_equipo': "Colón", 'nombre': 'Luis', 'apellido': 'Rodríguez', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    197: {'id_equipo': "Colón", 'nombre': 'Tomás', 'apellido': 'Sandoval', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    198: {'id_equipo': "Colón", 'nombre': 'Wanchope', 'apellido': 'Ábila', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    199: {'id_equipo': "Unión", 'nombre': 'Sebastián', 'apellido': 'Moyano', 'posicion': 'arquero', 'costo': 1000000, 'flag_capitan': False}, 
    200: {'id_equipo': "Unión", 'nombre': 'Francisco', 'apellido': 'Gerometta', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    201: {'id_equipo': "Unión", 'nombre': 'Franco', 'apellido': 'Calderón', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    202: {'id_equipo': "Unión", 'nombre': 'Claudio', 'apellido': 'Corvalán', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    203: {'id_equipo': "Unión", 'nombre': 'Federico', 'apellido': 'Vera', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    204: {'id_equipo': "Unión", 'nombre': 'Enzo', 'apellido': 'Roldán', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    205: {'id_equipo': "Unión", 'nombre': 'Juan', 'apellido': 'Portillo', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    206: {'id_equipo': "Unión", 'nombre': 'Imanol', 'apellido': 'Machuca', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    207: {'id_equipo': "Unión", 'nombre': 'Lucas', 'apellido': 'Esquivel', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    208: {'id_equipo': "Unión", 'nombre': 'Mauro', 'apellido': 'Luna Diale', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    209: {'id_equipo': "Unión", 'nombre': 'Jerónimo', 'apellido': 'Domina', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    210: {'id_equipo': "Instituto", 'nombre': 'Jorge', 'apellido': 'Carranza', 'posicion': 'arquero', 'costo': 1000000, 'flag_capitan': False}, 
    211: {'id_equipo': "Instituto", 'nombre': 'Giuliano', 'apellido': 'Cerato', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    212: {'id_equipo': "Instituto", 'nombre': 'Fernando', 'apellido': 'Alarcón', 'posicion': 'defensor', 'costo': 1000000, 'flag_capitan': False}, 
    213: {'id_equipo': "Instituto", 'nombre': 'Ezequiel', 'apellido': 'Parnisari', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    214: {'id_equipo': "Instituto", 'nombre': 'Jonathan', 'apellido': 'Bay', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    215: {'id_equipo': "Instituto", 'nombre': 'Roberto', 'apellido': 'Bochi', 'posicion': 'mediocampista', 'costo': 1000000, 'flag_capitan': False}, 
    216: {'id_equipo': "Instituto", 'nombre': 'Gastón', 'apellido': 'Lodico', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    217: {'id_equipo': "Instituto", 'nombre': 'Joaquín', 'apellido': 'Varela', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    218: {'id_equipo': "Instituto", 'nombre': 'Brahian', 'apellido': 'Cuello', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    219: {'id_equipo': "Instituto", 'nombre': 'Adrián', 'apellido': 'Martínez', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}, 
    220: {'id_equipo': "Instituto", 'nombre': 'Santiago', 'apellido': 'Rodríguez', 'posicion': 'delantero', 'costo': 1000000, 'flag_capitan': False}
}

#equipo (nombre, equipo, puntos)
equipo_jugador1 = ["Matias",[1,5,99],0,10000000]

eventos = {
    0: {"titulo": "Partido Ganado", "puntaje_asociado": ""},
    1: {"titulo": "Partido Empatado", "puntaje_asociado": ""},
    2: {"titulo": "Partido Perdido", "puntaje_asociado": ""},
    3: {"titulo": "Gol", "puntaje_asociado": 6},
    4: {"titulo": "Penal", "puntaje_asociado": 6},
    5: {"titulo": "Asistencia", "puntaje_asociado": 3},
    6: {"titulo": "Tarjeta Amarilla", "puntaje_asociado": -2},
    7: {"titulo": "Tarjeta Roja", "puntaje_asociado": -4}   
}


# FUNCIONES
def print_menu_principal(nombre_usuario):
  print("\nGRAN DT\n" ,f"Bienvenido {nombre_usuario}\n")
  print("---------------\nMENU PRINCIPAL\n---------------")
  print("Por favor seleccione una opcion:\n",
  "A. Menu de Equipo\n",
  "B. Menu de Torneo\n",
  "C. Cambiar de Usuario\n",
  "D. Salir",
  )

def print_menu_equipo():
  print("---------------\nMENU EQUIPO\n---------------")
  print("Por favor selecciona una opcion:\n",
  "A. Ver Equipo\n",
  "B. Añadir Jugadores\n",
  "C. Remover Jugadores\n",
  "D. Asignar Capitan\n",
  "E. Menu anterior"
  )

def print_menu_torneo():
  print("---------------\nMENU TORNEO\n---------------")
  print("Por favor selecciona una opcion:\n",
  "A. Jugar proxima fecha\n",
  "B. Ver fixture\n",
  "C. Salir",
  )

def print_equipo(equipo_usuario):
  if len(equipo_usuario) == 0:
    print("Sin jugadores en equipo") 
  else:
    print()
    for jugador in equipo_usuario:
      datos_jugador = BBDD_JUGADORES.get(jugador)
      print(f"{datos_jugador['nombre']} {datos_jugador['apellido']} - Posicion: {datos_jugador['posicion']}")
    input("\nPresione enter para continuar")

def seleccion_jugadores_id(lista_jugadores):
  """
  Este codigo se ejecuta dentro de añadir jugadores, cuando hay varios con el mismo apellido se ejecuta y fuerza al jugador a seleccionar uno, devuelte una lista de longitud 1
  """
  print("Hay varios jugadores con el mismo apellido","\nPor favor indique el id del jugador a anadir:\n", end="")
  for jugador in lista_jugadores:
    print(f"{jugador} - {BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")

  while True:
    respuesta = int(input("> "))
    if respuesta in lista_jugadores:
      print(f"Jugador {BBDD_JUGADORES[respuesta]['nombre']} {BBDD_JUGADORES[respuesta]['apellido']} anadido al equipo")
      return [respuesta]
    else:
      print("Id incorrecto, intente nuevamente")

def añadir_jugadores(usuario):
  """
  Codigo que permite la funcionalidad de añadir jugadores al equipo
  """
  while True:
    lista_jugadores = []
    print("Porfavor indique el apellido del jugador a anadir:")
    apellido = input("> ").lower()
    for i in range(1, len(BBDD_JUGADORES)):
      if BBDD_JUGADORES.get(i)["apellido"].lower() == apellido:
        lista_jugadores.append(i)
      
    if len(lista_jugadores) == 0:
      print("Jugador no encontrado")

    elif len(lista_jugadores) > 1:
      lista_jugadores = seleccion_jugadores_id(lista_jugadores)
      usuario[1].append(lista_jugadores[0])

    else:
      print(f"Jugador {BBDD_JUGADORES[lista_jugadores[0]]['nombre']} {BBDD_JUGADORES[lista_jugadores[0]]['apellido']} anadido al equipo")
      usuario[1].append(lista_jugadores[0])

    print("Desea anadir otro jugador? (S/N)")
    respuesta = input("> ").lower()

    while respuesta != "s" and respuesta != "n":
      print("\nRespuesta no valida\n")
      print("Desea anadir otro jugador? (S/N)")
      respuesta = input("> ").lower()

    if respuesta == "n":
      return usuario
    
    elif respuesta == "s" and len(usuario[1]) == 11:
      print("Limite de jugadores alcanzado")
      return usuario
    
def eliminar_jugadores(usuario):
  while True:
    print("Por favor seleccione el jugador a eliminar usando el ID (primera parte):")
    for jugador in usuario[1]:
      print(f"{jugador} - {BBDD_JUGADORES[jugador]["nombre"]} {BBDD_JUGADORES[jugador]["apellido"]}")

    respuesta = int(input("> "))
    if respuesta in usuario[1]:
      usuario[1].remove(respuesta)
      print(f"Jugador {BBDD_JUGADORES[respuesta]['nombre']} {BBDD_JUGADORES[respuesta]['apellido']} eliminado del equipo")
    else:
      print("Id incorrecto")

    print("Desea eliminar otro jugador? (S/N)")
    respuesta = input("> ").lower()

    while respuesta != "s" and respuesta != "n":
      print("\nRespuesta no valida\n")
      print("Desea eliminar otro jugador? (S/N)")
      respuesta = input("> ").lower()

    if respuesta == "n":
      return usuario
    
    if respuesta == "s" and len(usuario[1]) == 0:
      print("Equipo sin jugadores")
      return usuario

def logica_menu_torneo(usuario):
  while True:
    print_menu_torneo()
    seleccion = input("> ").lower()
    if seleccion == "a":
      resultado = simular_partido(fixture[0][0], lista_jugadores)
      matriz_posiciones = crear_matriz_posiciones(lista_equipos)
      matriz_posiciones = rellenar_equipos_matriz(lista_equipos,matriz_posiciones)
      matriz_posiciones = actualizar_matriz_posiciones(matriz_posiciones,resultado)
      imprimir_matriz_posiciones(matriz_posiciones)
    elif seleccion == "b":
      ver_fixture(fixture)
    elif seleccion == "c":
      return usuario
    else:
      print("Opcion no valida")

def logica_menu_equipo(usuario):
  while True:
    print_menu_equipo()
    seleccion = input("> ").lower()
    if seleccion == "a":
      print_equipo(usuario[1])
    elif seleccion == "b":
      usuario = añadir_jugadores(usuario)
    elif seleccion == "c":
      eliminar_jugadores(usuario)
    elif seleccion == "e":
      return usuario
    else:
      print("Opcion no valida")

def logica_menu_principal(usuario):
  while True:
    print_menu_principal(usuario[0])
    seleccion = input("> ").lower()
    if seleccion == "a":
      logica_menu_equipo(usuario)
    elif seleccion == "b":
      logica_menu_torneo(usuario)
    elif seleccion == "c":
      print("Funcionalidad no añadida")
    elif seleccion == "d":
      return
    else:
      print("Opcion no valida")

def registro_de_equipos(jugadores):
  equipos=[]
  for jugador in jugadores:
    equipo = jugadores[jugador]['id_equipo']
    if equipo not in equipos:
        equipos.append(equipo)
  return equipos

def registro_de_jugadores(jugadores):       # Me devuelve los datos de los jugadores cargados en una tupla
  players=[]
  for clave,valor in jugadores.items():
    id_jugador = clave
    equipo = valor["id_equipo"]
    nombre = valor["nombre"]
    apellido = valor["apellido"]
    posicion = valor["posicion"]

    players.append((id_jugador, equipo, nombre, apellido, posicion))        # Datos de los jugadores
  return players

def generar_fixture_ida_vuelta(equipos):
    cantidad_equipos = len(equipos)
    mitad = cantidad_equipos // 2
    fechas_ida = []
    fechas_vuelta = []
    for ronda in range(cantidad_equipos - 1):
        fecha = []
        for i in range(mitad):
            local = equipos[i]
            visitante = equipos[-i-1]
            fecha.append((local, visitante))
        fechas_ida.append(fecha)
        # Vuelta: se invierten los roles de local y visitante
        fechas_vuelta.append([(v, l) for (l, v) in fecha])
        # Rotar los equipos (excepto el primero)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    fixture_completo = fechas_ida + fechas_vuelta
    return fixture_completo


def menu_torneo(fixture):
    while True:
        print("\n=== Menú de Torneo ===")
        print("1. Jugar próxima fecha")
        print("2. Ver fixture")
        print("3. Atras")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            menu_torneo()


        elif opcion == "2":
            ver_fixture(fixture)
        elif opcion == "3":
            print("Saliendo del torneo...")
            break 
        else:
            print("Opción inválida.")
            menu_torneo()


def ver_fixture(fixture):
    print("\n=== Menú del Fixture ===")
    print("1. Ver Fecha en Especifico") 
    print("2. Ver fixture completo")
    print("3. Atras") 
    opcion = input("Elegí una opción: ")
    if opcion == "1":
        fecha_especifica=int(input("Indique la fecha especifica: "))
        print()
        print(f"\nFecha {fecha_especifica}".upper())
        for partido in fixture[fecha_especifica]:
            print(f"{partido[0]} vs {partido[1]}")
        print()
    elif opcion=="2":
        for numero_fecha, fecha in enumerate(fixture, start=1):
            print(f"Fecha {numero_fecha}:".upper())
            for local, visitante in fecha:
                print(f"  {local} vs {visitante}")
            print("-" * 20)
    else:
        menu_torneo(fixture)

def simular_partido(fixture, jugadores):
  titulares_local = []
  titulares_visitante = []
  partido_final = []
  partido_local = []
  partido_visitante = []
  resultados_partidos = {}

  local, visitante = fixture

        # Simula resultado final
  casos = ["gana", "pierde", "empata"]
  resultado_local = random.choice(casos)
  if resultado_local == "gana":
      resultado_visitante = "pierde"
  elif resultado_local == "pierde":
      resultado_visitante = "gana"
  else:
      resultado_visitante = "empata"

  resultados_partidos["local"] = (local, resultado_local)
  resultados_partidos["visitante"] = (visitante, resultado_visitante)

  print(f"Equipo local, {local}, {resultado_local}")
  print(f"Equipo visitante, {visitante}, {resultado_visitante}")
              
        # Simula eventos de partido
  if resultado_local == "gana" or resultado_local == "pierde":       
      goles = random.randint(1, 4)
      if goles % 2 == 0:      # La idea es que sea random
          penales = 1     
      else:
          penales = 0
      asistencias = goles
  if resultado_local == "empata" or resultado_local == "empata":
      goles = random.randint(0, 2) * 2
      penales = random.randint(0, 1) * 2
      asistencias = goles
  t_amarillas = random.randint(0, 2)
  t_rojas = random.randint(0, 1)
  goles_totales = goles + penales
  
  print("\nGoles:",goles)
  print("Penales:",penales)
  print("Asistencias:",asistencias)
  print("Tarjetas Amarillas:",t_amarillas)
  print("Tarjetas Rojas:",t_rojas)
  print("Goles en el encuentro:", goles_totales)

              # De la base de jugadores me traigo los datos del equipo local y visitante
  for jugador in jugadores:
      id_jugador, equipo, nombre, apellido, posicion = jugador
      if equipo == local:
          titulares_local.append([id_jugador, equipo, nombre, apellido, posicion])
  #print(titulares_local)
  for jugador in jugadores:
      id_jugador, equipo, nombre, apellido, posicion = jugador
      if equipo == visitante:
          titulares_visitante.append([id_jugador, equipo, nombre, apellido, posicion])
  #print(titulares_visitante)
        
        # Asignacion random de eventos por posicion. Goles a Delanteros, Asistencias a Mediocampistas, etc...
  '''for jugador in titulares_local:
      if titulares_local[-1] == "Delantero": # Slice de listas?
          partido_local.append([])'''
  

  return resultados_partidos


def crear_matriz_posiciones(equipos):
    filas=(len(equipos))
    columnas = 4 #equipo ganados perdidos puntosTotales
    matriz = [[0]*columnas for i in range(filas)]
    return matriz

def rellenar_equipos_matriz(lista_equipos,matriz_posiciones):
    filas = len(matriz_posiciones)
    columnas = len(matriz_posiciones[0])
    for f in range(filas):
        for c in range(columnas):
            matriz_posiciones[f][0] = lista_equipos[f]
    return matriz_posiciones

def actualizar_matriz_posiciones(matriz_posiciones, resultados_partido):
    for equipo, resultado in resultados_partido.values():
        for fila in matriz_posiciones:
            if fila[0] == equipo:
                if resultado == "gana":
                    fila[1] += 1  # Ganados
                    fila[3] += 3  # Puntos totales
                elif resultado == "pierde":
                    fila[2] += 1  # Perdidos
                elif resultado == "empata":
                    fila[3] += 1 # (1 punto por empate)
                break
    return matriz_posiciones

def imprimir_matriz_posiciones(matriz_posiciones):
    filas = len(matriz_posiciones)
    columnas = len(matriz_posiciones[0])
    for f in range(filas):
        for c in range(columnas):
            print(str(matriz_posiciones[f][c]),end='  ')
        print()

def fecha_actual_partidos(fecha,fixture): # fecha deberia ser la fecha actual de la instancia del programa
    fecha_actual = fecha
    for partido in fixture[fecha_actual]:
        simular_partido(partido)
    fecha_actual= fecha_actual+1
    return fecha_actual

# PROGRAMA PRINCIPAL
lista_equipos = registro_de_equipos(BBDD_JUGADORES)
lista_jugadores = registro_de_jugadores(BBDD_JUGADORES)
fixture = generar_fixture_ida_vuelta(lista_equipos)

logica_menu_principal(equipo_jugador1)
