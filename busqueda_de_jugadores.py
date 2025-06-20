import re
from main import BBDD_JUGADORES
from utils import *

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

filtro_por_equipo = lambda valor: filtrar_por("id_equipo", valor)
filtro_por_costo = lambda valor: filtrar_por("costo", valor)
filtro_por_nombre = lambda valor: filtrar_por("nombre", valor)
filtro_por_apellido = lambda valor: filtrar_por("apellido", valor)

LISTA_DE_COMANDOS = {
    "-e":filtro_por_equipo,
    "--EQUIPO":filtro_por_equipo,
    "-p":filtro_por_costo,
    "--PRECIO":filtro_por_costo,
    "-n":filtro_por_nombre,
    "--NOMBRE":filtro_por_nombre,
    "-ap":filtro_por_apellido,
    "--APELLIDO":filtro_por_apellido,
    "-v": lambda valor: ver_jugadores("", valor),
    "--VER": lambda valor: ver_jugadores("", valor),
    "-an":"",
    "--ANADIR":"",
    "-r":"",
    "--REMOVER":"",
    "salir":"salir",
    "exit":"salir",
    "clear": "borrar",
    "limpiar": "borrar"
}

comandos_compilados = re.compile('|'.join(LISTA_DE_COMANDOS.keys()))
regex_comandos = re.compile("(-[a-z]{0,4}|--[A-Z]+|[a-zA-Z]+) *([a-zA-Z0-9]+ ?[a-zA-Z0-9]*)*")
regex_help = re.compile("^(-h|help) *(-[a-zA-Z])*")

def ayuda(comando):
    if comandos_compilados.match(comando):
        pass
    elif comando == "-h" or comando == "-help":
        print("El comando ayuda permite ver las funciones de los comandos convocandola antes de ellos\npor ejemplo haciendo -h '--EQUIPO'\npodemos obtener la funcionalidad que cumple el comando '--EQUIPO'")    
    elif comando == "":
        print("Bienvenido al buscador de jugadores\npara buscar ayuda sobre alguna funcion puedes colocar -h despues de la misma\n\nej. --EQUIPO -h\n\npara ver todos los comandos puedes usar -h -h\n")

def ver_jugadores(set_jugadores,opciones):

    if type(set_jugadores) == set:
        if len(set_jugadores) == 0:
            print("No hay jugadores seleccionados todavia")
            return
        sumador_costos = 0
        print("Los jugadores seleccionados son:")
        if "l" in opciones:
            for jugador in set_jugadores:
                print(f"{BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']} - Posicion: {BBDD_JUGADORES[jugador]['posicion']} - Equipo: {BBDD_JUGADORES[jugador]['id_equipo']} - Costo: {BBDD_JUGADORES[jugador]['costo']}")
        else:
            for jugador in set_jugadores:
                print(f"{BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")
        if "c" in opciones:
            for jugador in set_jugadores:
                sumador_costos += BBDD_JUGADORES[jugador]['costo']
            print(f"El costo total de los jugadores es de: {sumador_costos}")
    else:
        return ver_jugadores

def limpiar_comandos_duplicados(comandos):
    """Toma un listado de comandos y remueve los duplicados si existen (util para los varios RegEx en el codigo)"""
    comandos_encontrados = []
    for comando in comandos:
        if comando[0] not in comandos_encontrados:
            comandos_encontrados.append(comando[0])
        else:
            del(comandos[comandos.index(comando)]) # eliminamos el comando duplicado
    comandos = reordenar_comandos(comandos)
    return comandos


def reordenar_comandos(comandos):
    """
    Reordena los comandos usando un set especifico de combinaciones para que se ejecuten de manera correcta
    """
    #1. si el primer comando es "-v" se mueve al final
    if "-v" in comandos[0][0]:
       comandos.append(comandos.pop(0))
    return comandos

def procesar_comandos(input, listado_jugadores, usuario):
    """
    Procesa todos el string ingresado al programa y lo convierte una lista de comandos para procesar, luego itera cada uno y los ejecuta
    """
    #aqui se otorga una prioridad de ejecucion a los comandos
    comando_help, comandos = regex_help.findall(input), regex_comandos.findall(input)
    #esta lista por compresion remueve todos los espacios blancos adelante y atras de los comandos 
    comandos = limpiar_comandos_duplicados(comandos)
    comandos = [(comando, valor.strip()) for comando, valor in comandos]

    if len(comando_help) > 0:
        ayuda(comando_help[0][1])

    if comandos != None:
        for comando in comandos:

            devolucion = ""
            if LISTA_DE_COMANDOS.get(comando[0]) == "salir":
                return True
            if comando[0] in LISTA_DE_COMANDOS:
                if type(LISTA_DE_COMANDOS[comando[0]]) != str:
                    devolucion = LISTA_DE_COMANDOS[comando[0]](comando[1])
                else:
                    devolucion = LISTA_DE_COMANDOS[comando[0]]
                if type(devolucion) == set:
                    if len(listado_jugadores) == 0:
                        listado_jugadores.update(devolucion)
                    else:
                        listado_jugadores = listado_jugadores & devolucion
                if devolucion == "borrar":
                    listado_jugadores = set()
                if devolucion == ver_jugadores:  
                    ver_jugadores(listado_jugadores, comando[0])

def iniciar_busqueda(usuario):
    jugadores_seleccionados = set()
    print("Consola de busqueda\ningresar '-h' para ayuda")
    print("Comandos basicos:\n-a  --AÑADIR\t-r  --REMOVER\n-n  --NOMBRE [valor]\t-a  --APELLIDO [valor]")
    while True:
        lista_devolucion = []
        valor_buscado = input("> ")
        if procesar_comandos(
            normalizar_acentos(
            valor_buscado.lower()), 
            jugadores_seleccionados,
            usuario
            ):
            return
        
iniciar_busqueda("")