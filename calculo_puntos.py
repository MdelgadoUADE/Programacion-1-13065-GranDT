import json

def cargar_eventos(path_eventos):
    with open(path_eventos, "r", encoding="utf-8") as f:
        eventos = json.loads(f.read().replace("'", '"'))
    return eventos

def calcular_puntos_usuario(usuario, eventos, fecha_actual):
    puntos = 0
    titulares = usuario["titulares"]  # Es un dict: {id_jugador: puntaje_actual}
    for evento in eventos:
        # Solo eventos de la fecha actual y con id_jugador válido
        id_jugador = str(evento.get("id_jugador"))
        if evento.get("fecha") == fecha_actual and id_jugador in titulares:
            puntaje = evento.get("puntaje_asociado", 0)
            puntos += puntaje
            # Sumar el puntaje al jugador titular
            titulares[id_jugador] += puntaje
    return puntos

def actualizar_puntos_usuarios(usuarios, eventos, fecha_actual):
    for usuario in usuarios.values():
        usuario["puntos"] = calcular_puntos_usuario(usuario, eventos, fecha_actual)
        
    return usuarios