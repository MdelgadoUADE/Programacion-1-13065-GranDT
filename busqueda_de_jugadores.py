import re
from main import BBDD_JUGADORES
from utils import *
from impresionJugadores import *

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

def añadir_jugadores(usuario, listado_jugadores):
    """Comando que añade jugadores en base a un usuario dado y un listado de jugadores a agregar
    Calcula el costo y el presupuesto restante antes de una transaccion, pregunta si desea continuar
    
    Utiliza el comando de verificacion de formacion para realizar una validacion anterior

    Args:
        usuario (dict): Diccionario con la informacion del usuario
        listado_jugadores (set): Conjunto de jugadores a agregar
    """
    flag_repetidos = False
    try:
        if type(usuario) == dict and type(listado_jugadores) == set:
            if not verificacion_de_formacion(usuario, listado_jugadores):
                print("La formacion no permite añadir los jugadores seleccionados")
                return
    
            costo = 0
            for jugadores in listado_jugadores:
                costo += BBDD_JUGADORES[jugadores]["costo"]
            print(f"""El costo total de los jugadores es de: {costo}\nEl presupuesto disponible es de: {usuario['presupuesto']}\nEl presupuesto restante despues de la transacción es de: {usuario['presupuesto'] - costo}""")
            
            if costo <= usuario["presupuesto"]:
                if confirmar_seleccion("¿Desea realizar la transacción?"):
                    for jugador in listado_jugadores:
                        if str(jugador) not in usuario["titulares"] and str(jugador) not in usuario["suplentes"]:
                            usuario["titulares"][str(jugador)] = 0
                        else:
                            costo += BBDD_JUGADORES[jugador]["costo"]
                            flag_repetidos = True
                    usuario["presupuesto"] -= costo
                    print("Transacción realizada con exito")
                    if flag_repetidos:
                        print("Algunos jugadores ya estaban en el equipo y no se añadieron")
                    return usuario
            else:
                print("\nPresupuesto insuficiente para realizar la transacción")
                return
        elif usuario == "":
            return "anadir"
        else:
            raise TypeError

    except TypeError:
        registrar_excepciones(TypeError("El usuario debe ser un diccionario y la lista de jugadores debe ser un conjunto"))
    except Exception as e:
        registrar_excepciones(e)

def verificacion_de_formacion(usuario, jugadores_a_agregar):
    """Segun un usuario y un set de jugadores a agregar, verifica si la formacion de un usuario permite la adición de jugadores.
    Toma en cuenta las 4 posiciones y realiza restados en base a las posiciones de los jugadores a agregar

    Args:
        usuario (dict): Diccionario con la informacion del usuario
        jugadores_a_agregar (set): Conjunto de jugadores a agregar
    """
    try:
        if type(usuario) == dict and type(jugadores_a_agregar) == set:
            formacion = usuario["formacion"].copy()
            contador_suplentes = len(usuario["suplentes"])

            for jugador in usuario["titulares"]:
                formacion[BBDD_JUGADORES[int(jugador)]["posicion"]] -= 1

            for jugador in jugadores_a_agregar:
                if not formacion[BBDD_JUGADORES[int(jugador)]["posicion"]] <= 0:
                    formacion[BBDD_JUGADORES[int(jugador)]["posicion"]] -= 1
                elif contador_suplentes <= 4:
                    contador_suplentes += 1
                else:
                    raise AssertionError(f"No hay suficiente espacio en la formación para el jugador {BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")
            return True
    except AssertionError as e:
        return False
    except Exception as e:
        registrar_excepciones(e)

def eliminar_jugadores(usuario, jugadores_a_eliminar):
    jugadores_no_encontrados = []
    try:
        if usuario == "":
            return "eliminar"
        if len(jugadores_a_eliminar) <= 0:
            print("No hay jugadores para eliminar")
            return
        if type(usuario) == dict and type(jugadores_a_eliminar) == set: # Verifica que el usuario sea un diccionario y los jugadores a eliminar sean un set
            for int_jugador in jugadores_a_eliminar:
                jugador = str(int_jugador)
                if jugador in usuario["titulares"]:
                    del(usuario["titulares"][jugador])
                    usuario["presupuesto"] += BBDD_JUGADORES[int_jugador]["costo"]
                elif jugador in usuario["suplentes"]:
                    del(usuario["suplentes"][jugador])
                    usuario["presupuesto"] += BBDD_JUGADORES[int_jugador]["costo"]
                else:
                    jugadores_no_encontrados.append(int_jugador)
            if len(jugadores_no_encontrados) > 0:
                print(f"Los siguientes jugadores no fueron encontrados para eliminar:")
                for jugador in jugadores_no_encontrados:
                    print(f"{BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")
            return
        else:
            raise TypeError

    except TypeError:
        registrar_excepciones(TypeError("El usuario debe ser un diccionario y la lista de jugadores debe ser un conjunto o lista"))
    except Exception as e:
        registrar_excepciones(e)

LISTA_DE_COMANDOS = {
    "-e":filtro_por_equipo,
    "-c":filtro_por_costo,
    "-n":filtro_por_nombre,
    "-A":filtro_por_apellido,
    "-v": lambda valor: ver_jugadores("", valor, ""),
    "-a":lambda valor: añadir_jugadores("", valor),
    "-r":lambda valor: eliminar_jugadores("", valor),
    "salir":"salir",
    "exit":"salir",
    "clear": "borrar",
    "limpiar": "borrar"
}

comandos_compilados = re.compile('|'.join(LISTA_DE_COMANDOS.keys()))
regex_comandos = re.compile("(--[A-Z]+|-[a-zA-Z]{0,4}|[a-zA-Z]+) *([a-zA-Z0-9]+ ?[a-zA-Z0-9]*)*")
regex_help = re.compile("^(-h|help) *(-[a-zA-Z])*")

def ayuda(comando):
    if comandos_compilados.match(comando):
        pass
    elif comando == "-h" or comando == "-help":
        print("El comando ayuda permite ver las funciones de los comandos convocandola antes de ellos\npor ejemplo haciendo -h '--EQUIPO'\npodemos obtener la funcionalidad que cumple el comando '--EQUIPO'")    
    elif comando == "":
        print("Bienvenido al buscador de jugadores\npara buscar ayuda sobre alguna funcion puedes colocar -h despues de la misma\n\nej. --EQUIPO -h\n\npara ver todos los comandos puedes usar -h -h\n")

def ver_jugadores(set_jugadores,opciones,usuario):
    """Segun un set de jugadores, realiza una revision de la base de datos y genera una salida por pantalla con diferente
    Cantidad de datos segun las opciones utilizadas

    Argumentos:
    set_jugadores (set): Conjunto de jugadores seleccionados
    opciones (str): El comando utilizado con sus distintas opciones
    """
    print_jugador_long = lambda id_jugador : print(f"{BBDD_JUGADORES[id_jugador]['nombre']} {BBDD_JUGADORES[id_jugador]['apellido']} - Posicion: {BBDD_JUGADORES[id_jugador]['posicion']} - Equipo: {BBDD_JUGADORES[id_jugador]['id_equipo']} - Costo: {BBDD_JUGADORES[id_jugador]['costo']}")
    print_jugador_short = lambda id_jugador : print(f"{BBDD_JUGADORES[id_jugador]['nombre']} {BBDD_JUGADORES[id_jugador]['apellido']}")

    if type(set_jugadores) == set:
        if len(set_jugadores) == 0 and "u" not in opciones:
            print("No hay jugadores seleccionados todavia")
            return
        sumador_costos = 0
        
        if "u" in opciones:
            print(f"Equipo de usuario {usuario['nom_usuario']}")
            if "l" in opciones:
                print("Titulares:")
                for jugador in usuario["titulares"]:
                    jugador = int(jugador)
                    print_jugador_long(jugador)

                print("\nSuplentes:")
                for jugador in usuario["suplentes"]:
                    jugador = int(jugador)
                    print_jugador_long(jugador)
            else:
                print("Titulares:")
                for jugador in usuario["titulares"]:
                    jugador = int(jugador)
                    print_jugador_short(jugador)

                print("\nSuplentes:")
                for jugador in usuario["suplentes"]:
                    jugador = int(jugador)
                    print_jugador_short(jugador)

            if "c" in opciones:
                for jugador in usuario["titulares"]:
                    jugador = int(jugador)
                    sumador_costos += BBDD_JUGADORES[jugador]['costo']

                for jugador in usuario["suplentes"]:
                    jugador = int(jugador)
                    sumador_costos += BBDD_JUGADORES[jugador]['costo']
                print(f"El valor total de los jugadores en el equipo es de: {sumador_costos}")
        else:
            print("Los jugadores seleccionados son:")
            if "l" in opciones:
                for jugador in set_jugadores:
                    print_jugador_long(jugador)
            else:
                for jugador in set_jugadores:
                    print_jugador_short(jugador)
            if "c" in opciones:
                for jugador in set_jugadores:
                    sumador_costos += BBDD_JUGADORES[jugador]['costo']
                print(f"El costo total de los jugadores es de: {sumador_costos}")
    else:
        return ver_jugadores

def limpiar_comandos_duplicados(comandos):
    """Toma un listado de comandos y remueve los duplicados si existen (util para los RegEx en el codigo)
    
    Args:
        comandos (list): lista de comandos
    """
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

    Args:
        comandos (list): lista de comandos
    """
    #1. si el primer comando es "-v" se mueve al final
    if "-v" in comandos[0][0] or "-a" in comandos[0][0] or "-r" in comandos[0][0]:
       comandos.append(comandos.pop(0))
    return comandos

def procesar_comandos(input, listado_jugadores, usuario):
    """
    Procesa todos el string ingresado al programa y lo convierte una lista de comandos para procesar, luego itera cada uno y los ejecuta

    Args:
        input (str): un string que puede contener una x cantidad de comandos
        listado_jugadores (set): Conjunto de jugadores a agregar, se utiliza para no perder la informacion entre ejecuciones de la funcion
        usuario (dict): diccionario con la informacion del usuario para luego realizar modificaciones segun funcion
    """
    
    comando_help, comandos = regex_help.findall(input), regex_comandos.findall(input)

    print(comandos)
    if len(comandos) > 0:
        comandos = limpiar_comandos_duplicados(comandos)
        comandos = [(comando, valor.strip().lower()) for comando, valor in comandos]

        if len(comando_help) > 0:
            ayuda(comando_help[0][1])

        for comando in comandos:

            devolucion = ""
            if LISTA_DE_COMANDOS.get(comando[0]) == "salir":
                return True
            if comando[0] in LISTA_DE_COMANDOS or comando[0][:2] in LISTA_DE_COMANDOS:
                listado_jugadores = ejecutar_comando(comando, listado_jugadores, usuario)
        return listado_jugadores
                
def ejecutar_comando(comando, listado_jugadores, usuario):
    """Ejecuta un comando, utiliza una u otra funcion dependiendo del comando dado"""
    try:
        devolucion = LISTA_DE_COMANDOS[comando[0][:2]](comando[1])
    except KeyError:
        devolucion = LISTA_DE_COMANDOS[comando[0]]
    if type(devolucion) == set:
        if len(listado_jugadores) == 0:
            listado_jugadores.update(devolucion)
        else:
            listado_jugadores = listado_jugadores & devolucion
    if devolucion == "borrar":
        listado_jugadores = set()
    if devolucion == ver_jugadores:  
        ver_jugadores(listado_jugadores, comando[0], usuario)
    if devolucion == "anadir":
        añadir_jugadores(usuario, listado_jugadores)
        listado_jugadores = set()
    if devolucion == "eliminar":
        eliminar_jugadores(usuario, listado_jugadores)
        listado_jugadores = set()
    return listado_jugadores

def iniciar_busqueda(usuario):
    """Inicia la consola de busqueda de jugadores, requiere el usuario quien esta realizando las modificaciones
    
    args:
        usuario (dict): Diccionario con la informacion del usuario
    """
    print("Consola de busqueda\n\ningresar '-h' para ayuda\n")
    print("Comandos basicos:\n-a  (Añadir jugadores)\t-r  (Remover jugadores)\n-n  (Nombre de jugador [valor])\t-A  (Apellido de jugador [valor])\n-c  (Costo de jugador [valor])\t")
    listado_jugadores = set()
    while True:
        valor_buscado = input("> ")
        try:
            process = procesar_comandos(normalizar_acentos(valor_buscado),listado_jugadores, usuario)
            if type(process) == set:
                listado_jugadores = process
            elif process:
                print("Saliendo...")
                guardar_usuario(usuario)
                return

        except Exception as e:
            registrar_excepciones(e)

def guardar_usuario(usuario):
    try:
        listado_usuarios = abrir_archivo_json("data/usuarios.json", "r")
        listado_usuarios[usuario["nom_usuario"]] = usuario
        
        with open("data/usuarios.json", "w") as archivo:
            json.dump(listado_usuarios, archivo, indent=4)

    except Exception as e:
        registrar_excepciones(e)