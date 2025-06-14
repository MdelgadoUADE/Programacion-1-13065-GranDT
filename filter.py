from main import BBDD_JUGADORES

#Esto va al main en un While y consume util donde va a haber una lista con los equipos y se hace una validacion con un IN si esta en la lista TRUE, pasa al filter
#Si es FALSE Pide de vuelta
posicionElegida = input("Ingrese la posicion en la que quiere buscar su jugador: ")
# Usar filter para filtrar jugadores por posición
listadoPosicion = set(filter(lambda jugador: BBDD_JUGADORES[jugador]['posicion'] == posicionElegida, BBDD_JUGADORES.keys()))






#Esto va al main en un While y consume util donde va a haber una lista con los equipos y se hace una validacion con un IN si esta en la lista TRUE, pasa al filter
#Si es FALSE Pide de vuelta
#equipoElegido = input("Ingrese el equipo en el que quiere buscar su jugador: ")
# Usar filter para filtrar jugadores por Equipo
#listadoEquipo = list(filter(lambda jugador: jugador['id_equipo'] == equipoElegido, BBDD_JUGADORES.values()))

#[7000000, 5000000, 1000000]
#costoElegido = int(input("Ingrese el costo por el que quiere buscar su jugador: "))
#listadoCosto = list(filter(lambda jugador: jugador['costo'] == costoElegido, BBDD_JUGADORES.values()))



for jugador in listadoPosicion:
    print(jugador)

print()

#for jugador in listadoEquipo:
#    print(jugador)

#print()

#for jugador in listadoCosto:
#    print(jugador)
