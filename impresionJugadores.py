import os
from main import abrir_archivo_json

def imprimir_equipo_platilla(usuario, BBDD_JUGADORES):
    """
    Crea un archivo html que muestra la formación del equipo del usuario logueado.

    Args:
        usuario (dict): Diccionario con la información del usuario.
        BBDD_JUGADORES (dict): Diccionario con toda la información de los jugadores.
    """
    usuarios_core = abrir_archivo_json("data/usuarios.json", "r")
    html_render = formacion_html("html_y_css/formacion.html", usuario["nom_usuario"], usuarios_core, BBDD_JUGADORES)

    with open("equipo/formacion.html", "w", encoding="utf-8") as f:
        f.write(html_render)

def llenar_titulares(titulares, BBDD_JUGADORES, index=0):
    # Caso base: si procesó todos los titulares, retorna el diccionario vacío
    """
    Llena un diccionario con la posición y los nombres de los jugadores.
    
    Args:
        titulares (list): Lista de ids de los jugadores titulares.
        BBDD_JUGADORES (dict): Diccionario con toda la información de los jugadores.
        index (int): Indice del título actual en la lista de titulares.
    
    Returns:
        dict: Diccionario con la posición y los nombres de los jugadores.
    """
    if index >= len(titulares):
        return {
            "arquero": [],
            "defensor": [],
            "mediocampista": [],
            "delantero": []
        }
    # Llamada recursiva: obtener el diccionario ya procesado hasta ahora
    jugadores_por_posicion = llenar_titulares(titulares, BBDD_JUGADORES, index + 1)
    jugador_id = str(titulares[index])
    jugador = BBDD_JUGADORES.get(int(jugador_id))
    if jugador:
        posicion = jugador["posicion"]
        if posicion in jugadores_por_posicion:
            jugadores_por_posicion[posicion].insert(0, f"<li>{jugador['nombre']} {jugador['apellido']}</li>")
    return jugadores_por_posicion

def formacion_html(nombre_archivo, usuario, usuarios_core, BBDD_JUGADORES):
    """
    Lee un archivo HTML y reemplaza los placeholders para mostrar la formación del equipo del usuario.

    Args:
        nombre_archivo (str): Ruta del archivo HTML a leer.
        usuario (str): Nombre del usuario.
        usuarios_core (dict): Diccionario con toda la información de los usuarios.
        BBDD_JUGADORES (dict): Diccionario con toda la información de los jugadores.

    Returns:
        str: El HTML renderizado con la formación del equipo.
    """
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            print(f"Error: No se encontró el archivo {nombre_archivo} en {directorio_actual}")
            return ""

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            html = archivo.read()
        
        datos_usuario = usuarios_core.get(usuario)
        if not datos_usuario:
            return "<p>Usuario no encontrado</p>"

        titulares = list(datos_usuario["titulares"].keys())
        suplentes = list(datos_usuario["suplentes"].keys())

        jugadores_por_posicion = llenar_titulares(titulares, BBDD_JUGADORES)

        # Armar HTML de suplentes
        suplentes_html = ""
        for suplente in suplentes:
            jugador = BBDD_JUGADORES.get(int(suplente))
            if jugador:
                suplentes_html += f"<li>{jugador['nombre']} {jugador['apellido']}</li>\n"

        # Generar tabla de puntajes de titulares ORDENADA
        titulares_info = []
        for id_jugador in titulares:
            jugador = BBDD_JUGADORES.get(int(id_jugador))
            puntaje = datos_usuario["titulares"].get(id_jugador, 0)
            if jugador:
                titulares_info.append((jugador['nombre'], jugador['apellido'], puntaje))

        # Ordenar por puntaje descendente
        titulares_info.sort(key=lambda x: x[2], reverse=True)
        tabla_puntajes = "<table border='1'><tr><th>Nombre</th><th>Apellido</th><th>Puntaje</th></tr>"
        for nombre, apellido, puntaje in titulares_info:
            tabla_puntajes += f"<tr><td>{nombre}</td><td>{apellido}</td><td>{puntaje}</td></tr>"
        tabla_puntajes += "</table>"

        # Reemplazos en el HTML
        html = html.replace("{{usuario}}", usuario)
        for pos in jugadores_por_posicion:
            html = html.replace(f"{{{{{pos}}}}}", "\n".join(jugadores_por_posicion[pos]))
        html = html.replace("{{suplentes}}", suplentes_html)
        html = html.replace("{{tabla_puntajes}}", tabla_puntajes)

        print(f"La visualizacion del equipo esta lista, se puede ver en: {ruta_archivo}")

        return html
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return ""


