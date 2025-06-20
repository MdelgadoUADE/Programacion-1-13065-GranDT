import os

def llenar_titulares(titulares, BBDD_JUGADORES, index=0, jugadores_por_posicion=None):
    if jugadores_por_posicion is None:
        jugadores_por_posicion = {
            "arquero": [],
            "defensor": [],
            "mediocampista": [],
            "delantero": []
        }
    if index >= len(titulares):
        return jugadores_por_posicion
    jugador_id = str(titulares[index])
    jugador = BBDD_JUGADORES.get(int(jugador_id))
    if jugador:
        posicion = jugador["posicion"].lower()
        if posicion in jugadores_por_posicion:
            jugadores_por_posicion[posicion].append(
                f"<li>{jugador['nombre']} {jugador['apellido']}</li>"
            )
    return llenar_titulares(titulares, BBDD_JUGADORES, index + 1, jugadores_por_posicion)

def formacion_html(nombre_archivo, usuario, USUARIOS, BBDD_JUGADORES):
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            print(f"Error: No se encontró el archivo {nombre_archivo} en {directorio_actual}")
            return ""

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            html = archivo.read()
        
        datos_usuario = USUARIOS.get(usuario)
        if not datos_usuario:
            return "<p>Usuario no encontrado</p>"

        titulares = datos_usuario["titulares"]
        suplentes = datos_usuario["suplentes"]

        # Llenar titulares y obtener el diccionario por posición
        jugadores_por_posicion = llenar_titulares(titulares, BBDD_JUGADORES)

        # Armar HTML de suplentes
        suplentes_html = ""
        for suplente in suplentes:
            jugador = BBDD_JUGADORES.get(int(suplente))
            if jugador:
                suplentes_html += f"<li>{jugador['nombre']} {jugador['apellido']}</li>\n"

        # Reemplazos en el HTML
        html = html.replace("{{usuario}}", usuario)
        for pos in jugadores_por_posicion:
            html = html.replace(f"{{{{{pos}}}}}", "\n".join(jugadores_por_posicion[pos]))
        html = html.replace("{{suplentes}}", suplentes_html)

        return html
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return ""


