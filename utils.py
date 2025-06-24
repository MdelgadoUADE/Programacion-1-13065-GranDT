import json
import os
import re

ACENTOS = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}


def revisar_ruta(ruta_archivo, crear_carpeta):
    """Revisa una ruta de archivo y retorna True si existe, tambien permite crear la ruta en caso de que no exista.

    Args:
        ruta_archivo (str): Ruta de archivo a revisar.
        crear_carpeta (bool): Indica si se debe crear la carpeta en caso de que no exista.

    Returns:
        bool: True si la ruta existe, False en caso contrario.
    """
    try:
        ruta_archivo = os.path.dirname(os.path.abspath(__file__)) + f"\\{ruta_archivo}"
        if os.path.exists(ruta_archivo):
            return True
        else:
            if crear_carpeta:
                os.mkdir(ruta_archivo)
                print(f"Directorio {ruta_archivo} no existia, creado")
                return True
            else:
                return False
    except OSError as e:
        print("Error de sistema!, verificar de no estar accediendo a archivos mientas se ejecuta el programa")        
    
    except Exception as e:
        registrar_excepciones(e)

def normalizar_acentos(string):
    return ''.join([ACENTOS.get(c, c) for c in string])

def str_bool_literal(string):
    """El que hizo la funcion de bool de python no evalua si el string dice true o false asi que para solucionar cree mi propia funcion

    Args:
        string (str): Cadena de texto a evaluar

    Returns:
        bool: True o False
    """
    try:
        if string.lower() == "true":
            return True
        elif string.lower() == "false":
            return False
    except AttributeError:
        if string:
            return True
        else:
            return False
    except Exception as e:
        registrar_excepciones(e)


def registro_de_equipos(jugadores):
    """Registra los equipos de la base de jugadores en una lista.

    Dado un diccionario de jugadores, recorre cada jugador y agrega su equipo a una lista si no existe ya.

    Argumentos:
    jugadores (dict): Diccionario con los jugadores como claves y sus datos como valores.

    Return:
    list: Una lista de los equipos de los jugadores.
    """
    equipos = []
    for jugador in jugadores:
        equipo = jugadores[jugador]['id_equipo']
        if equipo not in equipos:
            equipos.append(equipo)
    return equipos

def convertir_str_a_matriz(matriz,convertir_casos_a_int):
    """Convierte una cadena de texto a una matriz, da la opcion si la matriz tiene integers de poder convertirlos (para uso de archivo config)

    Args: 
        matriz (str): Cadena de texto a convertir
        convertir_casos_a_int (bool): Si se desea convertir los casos a enteros"""
    subgrupos = re.findall(r'\[([^\[\]]+)\]', matriz)

    lista_final = []

    for grupo in subgrupos:
        elementos = grupo.split(',')
        sublista = []
        for item in elementos:
            item = item.strip()
            item = item.strip("''")
            # Si deseamos intentamos convertirlo a entero
            if convertir_casos_a_int:
                try:
                    sublista.append(int(item))
                except ValueError:
                    sublista.append(item)
            else:
                sublista.append(item)
        lista_final.append(sublista)

    return lista_final


def confirmar_seleccion(mensaje):
    """Codigo basico de validacion para confirmar una seleccion

    Args:
        mensaje (str): Mensaje a mostrar, ingresar None para mostrar mensaje defecto

    Returns:
        bool: True o False"""
    if mensaje == None:
        print("Desea continuar? (S/N)")
    else:
        print(f"{mensaje} (S/N)")
    seleccion = input("> ").lower()
    while seleccion != "s" and seleccion != "n":
        print("Opcion no valida")
        seleccion = input("> ").lower()
    if seleccion == "s":
        return True
    elif seleccion == "n":
        return False


def registrar_excepciones(e):
    """Generador de log de errores para depuracion de codigo, genera un archivo log bajo la carpeta log, nombre error_log.txt

    Args: 
        e (Exception): Excepcion a registrar
    """
    try:
        archivo = open('log/error_log.txt', 'a')
        try:
            error = f"Tipo: {type(e)} - Mensaje: {str(e)}\n"
            print(f"Ocurrio un error: {error}")
            archivo.write(error)
        finally:
            archivo.close()
    except Exception as logError:
        print(f"Error al escribir el log: {logError}")


def abrir_archivo_json(nombre_archivo, modo):
    """Abre un archivo json y lo devuelve como un diccionario

    Args:
        nombre_archivo (str): nombre del archivo a abrir
        modo (str): modo de apertura del archivo, ejemplo: 'r' o 'w'

    Returns:
        dict: contenido del archivo json
    """
    try:
        archivo = open(nombre_archivo, modo)
        lineas = archivo.read()
        archivo.close()

        contenido = json.loads(lineas)
        return contenido

    except FileNotFoundError:
        print("No se pudo encontrar el archivo")

    except json.decoder.JSONDecodeError:
        print("No se pudo decodificar el archivo")

    except Exception as e:
        registrar_excepciones(e)


def buscar_maximo_evento(posicion, evento, stats):
    """
    Busca el jugador con el máximo valor en un evento específico dado su posición.

    Args:
        posicion (str): La posición del jugador (e.g., "delantero", "mediocampista", "defensor").
        evento (str): El tipo de evento a considerar (e.g., "goles", "asis", "amarillas", "rojas").
        stats (dict): Un diccionario que contiene las estadísticas de los jugadores.

    Returns:
        dict: Un diccionario con los datos del jugador que tiene el máximo valor en el evento especificado. 
        Incluye el nombre, apellido y el valor del evento. Si no se encuentra ningún jugador, retorna un 
        diccionario con valores vacíos y el valor del evento como 0.
    """

    maximo = max(
        (data for data in stats.values() if data["posicion"] == posicion),
        key=lambda d: d[evento], default={"nombre": "", "apellido": "", evento: 0})
    return maximo
