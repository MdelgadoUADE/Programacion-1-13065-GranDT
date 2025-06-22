import json


def formato_json(path_eventos):
    with open(path_eventos, "r", encoding="utf-8") as f:
        eventos = json.loads(f.read().replace("'", '"'))
    return eventos


def calcular_puntos_usuario(titulares, dic_titulares, eventos, fecha_actual):
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


def actualizar_puntos_usuarios(usuarios_core, eventos, fecha_actual):
    for usuario in usuarios_core.values():
        titulares = list(usuario["titulares"].keys())
        dic_titulares = usuario["titulares"]
        puntos, dic_titulares = calcular_puntos_usuario(titulares,dic_titulares, eventos, fecha_actual)
        usuario["puntos"] += puntos
        print(usuario["puntos"])
        print(dic_titulares)
    return usuarios_core
