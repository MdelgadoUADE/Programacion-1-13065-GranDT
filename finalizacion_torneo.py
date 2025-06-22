import json
from functools import reduce

def reporte_final_usuarios(path_usuarios="data/usuarios.json"):
    with open(path_usuarios, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    # Ordenar usuarios por puntos (descendente)
    ranking = sorted(usuarios.items(), key=lambda x: x[1]["puntos"], reverse=True)
    ganador, datos_ganador = ranking[0]
    print(f"\n El usuario ganador es: {ganador} con {datos_ganador['puntos']} puntos \n")
    print("Posiciones finales:")
    for i, (nombre, datos) in enumerate(ranking, 1):
        print(f"{i}. {nombre}: {datos['puntos']} puntos")

def reporte_maximos_eventos(eventos_path="data/eventos.txt", usuarios_path="data/usuarios.json"):
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
    # Máximo asistidor (mediocampista)
    max_asistidor = max(
        (data for data in stats.values() if data["posicion"] == "mediocampista"),
        key=lambda d: d["asis"], default={"nombre": "", "apellido": "", "asis": 0}
    )
    # Más amarillas (defensor)
    max_amarillas = max(
        (data for data in stats.values() if data["posicion"] == "defensor"),
        key=lambda d: d["amarillas"], default={"nombre": "", "apellido": "", "amarillas": 0}
    )
    # Más rojas (defensor)
    max_rojas = max(
        (data for data in stats.values() if data["posicion"] == "defensor"),
        key=lambda d: d["rojas"], default={"nombre": "", "apellido": "", "rojas": 0}
    )

    print("\n--- Estadísticas individuales (solo titulares de usuarios) ---")
    print(f"Rompe redes (Maximo Goleador): {max_goleador['nombre']} {max_goleador['apellido']} con {max_goleador['goles']} goles")
    print(f"El Mago (Maximo Asistidor): {max_asistidor['nombre']} {max_asistidor['apellido']} con {max_asistidor['asis']} asistencias")
    print(f"El Tosco (Mas tarjetas amarillas): {max_amarillas['nombre']} {max_amarillas['apellido']} con {max_amarillas['amarillas']} amarillas")
    print(f"El mas Bostero (Mas tarjetas Rojas): {max_rojas['nombre']} {max_rojas['apellido']} con {max_rojas['rojas']} rojas")
