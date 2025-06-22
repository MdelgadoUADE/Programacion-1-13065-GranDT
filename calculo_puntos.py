import json
from main import abrir_archivo_json
def calcular_puntos_fecha(fecha_actual):
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

def imprimir_puntos_usuario(puntos, nombre):
    print(f"Usuario: {nombre}, Puntos: {puntos}".center(160))



def actualizar_puntos_usuarios(usuarios_core, eventos, fecha_actual):
    for nombre, usuario in usuarios_core.items():
        titulares = list(usuario["titulares"].keys())
        dic_titulares = usuario["titulares"]
        puntos, dic_titulares = calcular_puntos_usuario(titulares, dic_titulares, eventos, fecha_actual)
        usuario["puntos"] += puntos
        imprimir_puntos_usuario(usuario["puntos"], nombre)
    return usuarios_core
