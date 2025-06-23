import json
from functools import reduce
from utils import buscar_maximo_evento


def reporte_final_usuarios(path_usuarios="data/usuarios.json"):
    """
    Genera el reporte final del torneo, mostrando el ranking de los usuarios
    por puntos y el usuario ganador.

    args:
        path_usuarios : str
            Path archivo JSON de usuarios.

    """
    with open(path_usuarios, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    # Ordenar usuarios por puntos (descendente)
    ranking = sorted(usuarios.items(),
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
        asistencias. Incluye el nombre, apellido y el valor del evento. Si no se
        encuentra ningún jugador, retorna un diccionario con valores vacíos y el
        valor del evento como 0.
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
        tarjetas amarillas. Incluye el nombre, apellido y el valor del evento. Si no se
        encuentra ningún jugador, retorna un diccionario con valores vacíos y el
        valor del evento como 0.
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
        tarjetas rojas. Incluye el nombre, apellido y el valor del evento. Si no se
        encuentra ningún jugador, retorna un diccionario con valores vacíos y el
        valor del evento como 0.
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
    # 1. Cargar los titulares de todos los usuarios (solo los IDs)
    with open(usuarios_path, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    titulares_ids = set()
    for usuario in usuarios.values():
        titulares_ids.update(str(jid) for jid in usuario["titulares"].keys())

    # 2. Acumuladores por jugador
    stats = {}  # id_jugador: {"nombre":..., "apellido":..., "posicion":..., "goles":0, "asis":0, "amarillas":0, "rojas":0}

    # 3. Leer eventos.txt línea por línea (asumiendo formato JSON por línea o lista de dicts)
    with open(eventos_path, "r", encoding="utf-8") as f:
        try:
            eventos = json.load(f)
        except Exception:
            # Si no es un JSON válido, Error
            print("Error: eventos.txt no es un formato JSON válido.")
            return

        for evento in eventos:
            id_jugador = str(evento.get("id_jugador"))
            if id_jugador not in titulares_ids:
                continue  # Solo titulares de usuarios

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

    # 4. Usar reduce para encontrar los máximos
    # Máximo goleador (delantero)
    max_goleador = reduce(
        lambda a, b: a if a["goles"] >= b["goles"] else b,
        (data for data in stats.values() if data["posicion"] == "delantero"),
        {"nombre": "", "apellido": "", "goles": -1}
    )
    # 5. Busca el jugador que mas asistencias hizo
    # Máximo asistidor (mediocampista)
    max_asistidor = buscar_maximo_asistidor(stats)

    # 5. Busca el jugador que mas tarjetas amarillas tiene
    # Más amarillas (defensor)
    max_amarillas = buscar_maximo_tarjetas_amarillas(stats)

    # 6. Busca el jugador que mas tarjetas rojas tiene
    # Mas rojas (defensor)
    max_rojas = buscar_maximo_tarjetas_rojas(stats)

    print("\n--- 📊 Estadísticas individuales (solo titulares de usuarios) ---\n".center(10))
    print(
        f"Rompe redes (Maximo Goleador): {max_goleador['nombre']} {max_goleador['apellido']} con {max_goleador['goles']} goles".center(160))
    print(
        f"El Mago (Maximo Asistidor): {max_asistidor['nombre']} {max_asistidor['apellido']} con {max_asistidor['asis']} asistencias".center(160))
    print(
        f"El Tosco (Mas tarjetas amarillas): {max_amarillas['nombre']} {max_amarillas['apellido']} con {max_amarillas['amarillas']} amarillas".center(160))
    if max_rojas['rojas'] == 0:
        print("No hubo tarjetas rojas entre los defensores titulares de los usuarios.".center(160))
    else:
        print(
            f"El mas Bostero (Mas tarjetas Rojas): {max_rojas['nombre']} {max_rojas['apellido']} con {max_rojas['rojas']} rojas".center(160))
