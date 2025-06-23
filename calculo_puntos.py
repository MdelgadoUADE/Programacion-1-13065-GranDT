import json
from main import abrir_archivo_json
def calcular_puntos_fecha(fecha_actual):

    """
    Actualiza los puntos de los usuarios en base a la fecha actual y los eventos ocurridos hasta la fecha.

    Args:
        fecha_actual (int): número de la fecha actual en el torneo

    Returns:
        None
    """
    
    print()
    print("----Puntaje de Usuarios----".center(160))

    usuarios_core = abrir_archivo_json("data/usuarios.json", "r")
    eventos_json = formato_json("data/eventos.txt")
    usuarios_core = actualizar_puntos_usuarios(usuarios_core, eventos_json, fecha_actual)
    print()

    if usuarios_core:
        with open("data/usuarios.json", "w", encoding="utf-8") as f:
            json.dump(usuarios_core, f, indent=4)
    else:
        print("Error: USUARIOS está vacío, no se guardará el archivo.")

def formato_json(path_eventos):
    """
    Lee un archivo y devuelve su contenido en formato json
    (diccionario en python).

    Args:
        path_eventos (str): ruta del archivo json a leer

    Returns:
        dict: contenido del archivo json en formato diccionario
    """
    with open(path_eventos, "r", encoding="utf-8") as f:
        eventos = json.loads(f.read().replace("'", '"')) 
    return eventos


def calcular_puntos_usuario(titulares, dic_titulares, eventos, fecha_actual):
    """
    Calcula y actualiza los puntos de los jugadores titulares de un usuario
    basándose en los eventos ocurridos durante la fecha actual.

    Args:
        titulares (list): Lista de IDs de los jugadores titulares del usuario.
        dic_titulares (dict): Diccionario con los jugadores titulares y sus puntos actuales.
        eventos (list): Lista de eventos que han ocurrido, cada uno representado como un diccionario.
        fecha_actual (int): Número de la fecha actual en el torneo.

    Returns:
        tuple: Una tupla que contiene los puntos totales acumulados por los titulares y
               el diccionario actualizado de titulares con sus nuevos puntajes.
    """

    puntos = 0
    for evento in eventos:
        # Solo eventos de la fecha actual y con id_jugador válido
        id_jugador = str(evento.get("id_jugador"))
        if evento.get("fecha") == fecha_actual and id_jugador in titulares:
            puntaje = evento.get("puntaje_asociado", 0)
            puntos += puntaje
            # Sumar el puntaje al jugador titular
            dic_titulares[id_jugador] += puntaje
    return puntos, dic_titulares

def imprimir_puntos_usuario(puntos, nombre):
    """
    Imprime en pantalla los puntos de un usuario en formato centrado

    Args:
        puntos (int): Puntos actuales del usuario
        nombre (str): Nombre del usuario
    """
    print(f"Usuario: {nombre}, Puntos: {puntos}".center(160))



def actualizar_puntos_usuarios(usuarios_core, eventos, fecha_actual):
    """
    Actualiza los puntos de los usuarios en base a la fecha actual y eventos ocurridos en la fecha.

    Args:
        usuarios_core (dict): diccionario con la información de cada usuario
        eventos (dict): diccionario con la información de los eventos ocurridos
        fecha_actual (int): número de la fecha actual en el torneo

    Returns:
        dict: diccionario actualizado con la información de cada usuario
    """
    for nombre, usuario in usuarios_core.items():
        titulares = list(usuario["titulares"].keys()) # Lista de IDs de los jugadores titulares
        dic_titulares = usuario["titulares"] # Diccionario con los jugadores titulares y sus puntos
        puntos, dic_titulares = calcular_puntos_usuario(titulares, dic_titulares, eventos, fecha_actual)
        usuario["puntos"] += puntos
        imprimir_puntos_usuario(usuario["puntos"], nombre)
    return usuarios_core
