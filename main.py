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

def imprimir_equipo():
	for jugador in lista_jugadores:
		print(f"{jugador[0]}")

def validar_seleccion(mensaje):
	while True:
		validacion = str(input(mensaje + " [Y/N]: "))
		if validacion == "Y" or validacion == "y":
			return True
		elif validacion == "N" or validacion == "n":
			return False
		else:
			print("Valor ingresado no correcto, por favor intente nuevamente")
		

def seleccion_de_jugadores(lista_jugadores):
	lista_de_jugadores = []
	while True:
		jugador_seleccionado = seleccionar_jugador_de_lista(ingreso_nombre(), lista_jugadores)
		if not jugador_seleccionado == None:
			if validar_seleccion(f"Desea añadir a {jugador_seleccionado[0]}?"):
				lista_de_jugadores.append(jugador_seleccionado)
			if not validar_seleccion("Desea seguir añadiendo jugadores?"):
				return lista_de_jugadores
				
			

mis_jugadores = [
("Borja", "Delantero"),
("Lautaro", "Delantero"),
("Messi", "Mediocampista")
]

#print(seleccionar_jugador_de_lista(ingreso_nombre(), mis_jugadores))
seleccion_de_jugadores(mis_jugadores)