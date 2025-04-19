#TODO menu principal con opciones (menu de equipo, menu de torneo, (cambiar de usuario) mas adelante, salir) #MATIAS

#TODO menu de torneo (puntuacion actual, puntuacion otros jugadores, menu anterior) #NICOLAS

#TODO menu de equipo (añadir jugadores, remover jugadores, asignar capitan, asignar estrategia, menu anterior) #MATIAS

#TODO carga de datos de partido - mas adelante
#TODO datos de partido (equipos, quien gano, quien hizo gol, quien hizo asistencia, tarjetas(amarilla y roja), penales atajados, penales errados)
#TODO logica de puntaje

#TODO futuro logica de tarjetas (si es amarilla no puede jugar el proximo partido, si es roja no puede jugar, doble amarilla es roja)


diccionario_de_partidos={
	1: [   
	(1, 101, "gol"),
    (2, 102, "asistencia"),
    (3, 102, "amarilla"),
    (4, 101, "roja"),
    (5, 101, "penal atajado")
	]
}

jugadores = {
    1: {"id_equipo": 101, "nombre": "Lionel", "apellido": "Messi", "posicion": "delantero", "costo": 12000000, "flag_capitan": True},
    2: {"id_equipo": 102, "nombre": "Emiliano", "apellido": "Martínez", "posicion": "arquero", "costo": 6000000, "flag_capitan": False},
    3: {"id_equipo": 101, "nombre": "Ángel", "apellido": "Di María", "posicion": "mediocampista", "costo": 8000000, "flag_capitan": False},
    4: {"id_equipo": 103, "nombre": "Cristiano", "apellido": "Ronaldo", "posicion": "delantero", "costo": 11000000, "flag_capitan": True},
    5: {"id_equipo": 104, "nombre": "Manuel", "apellido": "Neuer", "posicion": "arquero", "costo": 5500000, "flag_capitan": False},
    6: {"id_equipo": 102, "nombre": "Nicolás", "apellido": "Otamendi", "posicion": "defensa", "costo": 7000000, "flag_capitan": False},
    7: {"id_equipo": 105, "nombre": "Kylian", "apellido": "Mbappé", "posicion": "delantero", "costo": 13000000, "flag_capitan": True},
    8: {"id_equipo": 106, "nombre": "Luka", "apellido": "Modric", "posicion": "mediocampista", "costo": 7500000, "flag_capitan": False},
    9: {"id_equipo": 107, "nombre": "Virgil", "apellido": "van Dijk", "posicion": "defensa", "costo": 9000000, "flag_capitan": True},
    10: {"id_equipo": 108, "nombre": "Harry", "apellido": "Kane", "posicion": "delantero", "costo": 9500000, "flag_capitan": False},
    11: {"id_equipo": 104, "nombre": "Joshua", "apellido": "Kimmich", "posicion": "mediocampista", "costo": 8200000, "flag_capitan": False},
    12: {"id_equipo": 106, "nombre": "Thibaut", "apellido": "Courtois", "posicion": "arquero", "costo": 6100000, "flag_capitan": False},
    13: {"id_equipo": 101, "nombre": "Rodrigo", "apellido": "De Paul", "posicion": "mediocampista", "costo": 7000000, "flag_capitan": False},
    14: {"id_equipo": 109, "nombre": "Erling", "apellido": "Haaland", "posicion": "delantero", "costo": 12500000, "flag_capitan": True},
    15: {"id_equipo": 107, "nombre": "Trent", "apellido": "Alexander-Arnold", "posicion": "defensa", "costo": 8800000, "flag_capitan": False},
    16: {"id_equipo": 110, "nombre": "Pedri", "apellido": "González", "posicion": "mediocampista", "costo": 7700000, "flag_capitan": False},
    17: {"id_equipo": 108, "nombre": "Jude", "apellido": "Bellingham", "posicion": "mediocampista", "costo": 9100000, "flag_capitan": False},
    18: {"id_equipo": 105, "nombre": "Antoine", "apellido": "Griezmann", "posicion": "delantero", "costo": 8700000, "flag_capitan": False},
    19: {"id_equipo": 110, "nombre": "Marc-André", "apellido": "ter Stegen", "posicion": "arquero", "costo": 5900000, "flag_capitan": False},
    20: {"id_equipo": 109, "nombre": "Martin", "apellido": "Ødegaard", "posicion": "mediocampista", "costo": 7600000, "flag_capitan": False}
}


#Programa Principal



#Datos jugador ("nombre", "posicion", numero, costo, flag_capitan)
#Ej
#("Enzo Perez", "Mediocampista", 24, 3000000, True)



#Datos Equipos ["Jugador", "nombre_equipo", puntos, presupuesto, [seleccion_titulares], [seleccion_suplentes]]
matrizEquipos = [
    ["Jugador1", "EquipoA", 25, 100000000, 
     [
         ("Enzo Perez", "Mediocampista", 24, 3000000, True),
     ],
     [
         
     ]
     ]
]





def seleccionar_jugador_de_lista(nombre_jugador, lista_jugadores):
  jugador_encontrado = False
  for jugador in lista_jugadores:
    if nombre_jugador in jugador:
      jugador_encontrado = True
      return jugador
  if not jugador_encontrado:
    print("Jugador no encontrado")
    return None



def ingreso_nombre():
  return str(input("Por favor ingrese el nombre del jugador: "))



def imprimir_equipo(lista_jugadores):
  if len(lista_jugadores) != 0:
    for jugador in lista_jugadores:
      print(f"{jugador[0]}, \t {jugador[1]}, \t Dorsal: {jugador[2]}")
  else:
    print("Sin jugadores en lista!")
  
def validar_seleccion(mensaje):
  while True:
    validacion = str(input(mensaje + " [Y/N]: "))
    if validacion == "Y" or validacion == "y":
      return True
    elif validacion == "N" or validacion == "n":
      return False
    else:
      print("Valor ingresado no correcto, por favor intente nuevamente")



def verificar_si_coincide_string(valor_a_verificar, valor_verificante):
  if valor_a_verificar == valor_verificante:
    return True
  else:
    return False



def seleccion_de_jugadores(lista_jugadores):
  lista_de_jugadores = []
  while True:
    jugador_seleccionado = seleccionar_jugador_de_lista(ingreso_nombre(), lista_jugadores)
    if not jugador_seleccionado == None:
      if validar_seleccion(f"Desea añadir a {jugador_seleccionado[0]}?"):
        lista_de_jugadores.append(jugador_seleccionado)
      if not validar_seleccion("Desea seguir añadiendo jugadores?"):
        imprimir_equipo(lista_de_jugadores)
        return lista_de_jugadores
        
def print_menu_principal(usuario):
      print("\nGRAN DT\n" ,f"Bienvenido {usuario}\n")
      print("Por favor seleccione una opcion:\n",
      "A. Ver equipo\n",
      "B. Ver puntos\n",
      "C. Jugadores disponible\n",
      "D. Mercado de cambios\n",
      "E. Salir del juego"
      )
      
def seleccion_menu_principal(usuario):
  print_menu_principal(usuario)
  
  
  

mis_jugadores = [
("Borja", "Delantero",9),
("Lautaro", "Delantero", 22),
("Messi", "Mediocampista", 10)
]

#print(seleccionar_jugador_de_lista(ingreso_nombre(), mis_jugadores))
print_menu_principal("Matias")
seleccion_de_jugadores(mis_jugadores)