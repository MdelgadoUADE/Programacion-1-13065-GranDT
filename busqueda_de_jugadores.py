import re
from main import BBDD_JUGADORES
from utils import *

def ayuda(valores_adyacentes):
    print("Bienvenido al buscador de jugadores\npara buscar ayuda sobre alguna funcion puedes colocar -h despues de la misma\n\nej. --EQUIPO -h\n\npara ver todos los comandos puedes usar -h -h\n")
    
    if valores_adyacentes in LISTA_DE_COMANDOS:
        func_shortcut = LISTA_DE_COMANDOS[valores_adyacentes]
        if func_shortcut == ayuda:
            print("La funcion ayuda permite ver los funciones de los comandos convocandola al lado de ellos\npor ejemplo haciendo --EQUIPO -h\npodemos obtener los datos del comando --EQUIPO")
        elif func_shortcut:
            pass

def ver_jugadores(set_jugadores):
    if type(set_jugadores) == set:
        pass
    else:
        return ver_jugadores


def filtrar_por(filtro, valor_pasado):

    if filtro == "costo": # Validacion a parte por costo para convertir datos a int y poder filtrar entre rangos de valores
        costos = valor_pasado.split()
        costos = [int(valor) for valor in costos]
        if len(costos) > 1:
            jugadores_menor_valor = set(filter(lambda jugador: BBDD_JUGADORES[jugador]["costo"] >= costos[0], BBDD_JUGADORES.keys()))
            jugadores_mayor_valor = set(filter(lambda jugador: BBDD_JUGADORES[jugador]["costo"] <= costos[1], BBDD_JUGADORES.keys()))
            return jugadores_menor_valor.intersection(jugadores_mayor_valor)
        else:
            return set(filter(lambda jugador: BBDD_JUGADORES[jugador][filtro] == costos[0], BBDD_JUGADORES.keys()))
    return set(filter(lambda jugador: normalizar_acentos(BBDD_JUGADORES[jugador][filtro].lower()) == valor_pasado, BBDD_JUGADORES.keys()))

LISTA_DE_COMANDOS = {
    "-h": ayuda,
    "help": ayuda,
    "-e":lambda valor: filtrar_por("id_equipo", valor),
    "--EQUIPO":lambda valor: filtrar_por("id_equipo", valor),
    "-p":lambda valor: filtrar_por("costo", valor),
    "--PRECIO":lambda valor: filtrar_por("costo", valor),
    "-n":lambda valor: filtrar_por("nombre", valor),
    "--NOMBRE":lambda valor: filtrar_por("nombre", valor),
    "-a":lambda valor: filtrar_por("apellido", valor),
    "--APELLIDO":lambda valor: filtrar_por("apellido", valor),
    "-v": ver_jugadores,
    "--VER": ver_jugadores,
    "salir":None,
    "exit":None,
    "clear": True,
    "limpiar": True
}
print("Consola de busqueda\ningresar '-h' para ayuda")
print("Comandos basicos:\n-a, --ANADIR\n-r, --REMOVER\n, --NOMBRE\n-a, --APELLIDO")

comandos_compilados = '|'.join(LISTA_DE_COMANDOS.keys())
regex_comandos_comunes = re.compile(f"({comandos_compilados}) +([a-zA-Z0-9]+ ?[a-zA-Z0-9]*)+")
regex_comandos_combinados = re.compile(f"({comandos_compilados}) ({comandos_compilados})")

def procesar_comandos(input):
    jugadores_seleccionados = set()
    comandos = regex_comandos_combinados.findall(input) + regex_comandos_comunes.findall(input)

    #esta lista por compresion remueve todos los espacios blancos adelante y atras de los comandos 
    comandos = [(comando, valor.strip()) for comando, valor in comandos]

    if comandos != None:
        for comando in comandos:
            print(comandos)
            if LISTA_DE_COMANDOS[comando[0]] == None:
                return True
            devolucion = LISTA_DE_COMANDOS[comando[0]](comando[1])
            if type(devolucion) == set:
                if len(jugadores_seleccionados) == 0:
                    jugadores_seleccionados.update(devolucion)
                else:
                    jugadores_seleccionados = jugadores_seleccionados & devolucion
            if devolucion == True:
                jugadores_seleccionados = set()
            if devolucion == ver_jugadores:  
                print(jugadores_seleccionados)

def iniciar_busqueda():
    while True:
        lista_devolucion = []
        valor_buscado = input("> ")
        if procesar_comandos(valor_buscado.lower()):
            return

#print(re.search(f"({shortcut}) ([a-zA-Z]+ ?[a-zA-Z]*)","-e Velez Sarsfield"))
        
iniciar_busqueda()
    