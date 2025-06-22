import json
import os
import re

ACENTOS = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}


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
    maximo = max(
        (data for data in stats.values() if data["posicion"] == posicion),
        key=lambda d: d[evento], default={"nombre": "", "apellido": "", evento: 0})
    return maximo
