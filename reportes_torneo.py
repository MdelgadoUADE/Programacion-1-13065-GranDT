import json
from functools import reduce
from utils import *


def reporte_final_usuarios(path_usuarios="data/usuarios.json"):
    """
    Genera el reporte final del torneo, mostrando el ranking de los usuarios
    por puntos y el usuario ganador.

    args:
        path_usuarios : str
            Path archivo JSON de usuarios.

    """
    usuarios_final = abrir_archivo_json("data/usuarios.json", "r")

    # Ordenar usuarios por puntos (descendente)
    ranking = sorted(usuarios_final.items(),
                     key=lambda x: x[1]["puntos"], reverse=True)
    ganador, datos_ganador = ranking[0]
    print(
        f"\n El usuario ganador es: {ganador} con {datos_ganador['puntos']} puntos \n")
    print("Posiciones finales:")
    for i, (nombre, datos) in enumerate(ranking, 1):
        print(f"{i}. {nombre}: {datos['puntos']} puntos")


def buscar_maximo_asistidor(stats):
    """
    Busca el jugador con el máximo valor en asistencias en el torneo, entre los
    mediocampistas.

    Args:
        stats (dict): Un diccionario que contiene las estadísticas de los jugadores.

    Returns:
        dict: Un diccionario con los datos del jugador que tiene el máximo valor en
        asistencias. 
    """
    posicion = "mediocampista"
    evento = "asis"
    return buscar_maximo_evento(posicion, evento, stats)


def buscar_maximo_tarjetas_amarillas(stats):
    """
    Busca el jugador con el máximo valor en tarjetas amarillas en el torneo, entre los
    defensores.

    Args:
        stats (dict): Un diccionario que contiene las estadísticas de los jugadores.

    Returns:
        dict: Un diccionario con los datos del jugador que tiene el máximo valor en
        tarjetas amarillas.
    """

    posicion = "defensor"
    evento = "amarillas"
    return buscar_maximo_evento(posicion, evento, stats)


def buscar_maximo_tarjetas_rojas(stats):
    """
    Busca el jugador con el máximo valor en tarjetas rojas en el torneo, entre los
    defensores.

    Args:
        stats (dict): Un diccionario que contiene las estadísticas de los jugadores.

    Returns:
        dict: Un diccionario con los datos del jugador que tiene el máximo valor en
        tarjetas rojas.
    """
    posicion = "defensor"
    evento = "rojas"
    return buscar_maximo_evento(posicion, evento, stats)


def reporte_maximos_eventos(eventos_path="data/eventos.txt", usuarios_path="data/usuarios.json"):
    """
    Genera el reporte de los máximos eventos individuales en el torneo, entre los
    titulares de los usuarios. Los eventos son: Máximo Goleador (delantero),
    Máximo Asistidor (mediocampista), Más tarjetas amarillas (defensor) y Más tarjetas
    rojas (defensor).

    args:
        eventos_path : str
            Path archivo JSON de eventos.
        usuarios_path : str
            Path archivo JSON de usuarios.

    """

    with open(usuarios_path, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    titulares_ids = set()
    for usuario in usuarios.values():
        titulares_ids.update(str(jid) for jid in usuario["titulares"].keys())

    stats = {} 

    with open(eventos_path, "r", encoding="utf-8") as f:
        try:
            eventos = json.load(f)
        except Exception:
            print("Error: eventos.txt no es un formato JSON válido.")
            return

        for evento in eventos:
            id_jugador = str(evento.get("id_jugador"))
            if id_jugador not in titulares_ids:
                continue  

            nombre = evento.get("nombre", "")
            apellido = evento.get("apellido", "")
            posicion = evento.get("posicion", "")
            tipo = evento.get("evento", "")
            if id_jugador not in stats:
                stats[id_jugador] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "posicion": posicion,
                    "goles": 0,
                    "asis": 0,
                    "amarillas": 0,
                    "rojas": 0
                }
            if tipo == "Gol" and posicion == "delantero":
                stats[id_jugador]["goles"] += 1
            if tipo == "Asistencia" and posicion == "mediocampista":
                stats[id_jugador]["asis"] += 1
            if tipo == "Tarjeta Amarilla" and posicion == "defensor":
                stats[id_jugador]["amarillas"] += 1
            if tipo == "Tarjeta Roja" and posicion == "defensor":
                stats[id_jugador]["rojas"] += 1


    # Máximo goleador
    max_goleador = reduce(
        lambda a, b: a if a["goles"] >= b["goles"] else b,
        (data for data in stats.values() if data["posicion"] == "delantero"),
        {"nombre": "", "apellido": "", "goles": -1}
    )

    # Máximo asistidor
    max_asistidor = buscar_maximo_asistidor(stats)

    # Más amarillas
    max_amarillas = buscar_maximo_tarjetas_amarillas(stats)

    # Mas rojas 
    max_rojas = buscar_maximo_tarjetas_rojas(stats)

    print(f"=== 📊 Estadísticas individuales (Equipos Fantasia) ===".center(160))
    print()
    print(
        f"🎯 Rompe redes: {max_goleador['nombre']} {max_goleador['apellido']} con {max_goleador['goles']} goles".center(160))
    print(
        f"🧙 El Mago: {max_asistidor['nombre']} {max_asistidor['apellido']} con {max_asistidor['asis']} asistencias".center(160))
    print(
        f"🌲 El Tronco: {max_amarillas['nombre']} {max_amarillas['apellido']} con {max_amarillas['amarillas']} amarillas".center(160))
    if max_rojas['rojas'] == 0:
        print("No hubieron tarjetas rojas en la fecha.".center(160))
    else:
        print(
            f"🍖 El Carnicero: {max_rojas['nombre']} {max_rojas['apellido']} con {max_rojas['rojas']} rojas".center(160))
