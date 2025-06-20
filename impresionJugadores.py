import os
from main import BBDD_JUGADORES
import json

try:
    # Encoding añadido debido a error extraño con json
    contenido = open("data/usuarios.json", "r", encoding="utf8")
    usuario = contenido.read()

    USUARIOS = json.loads(usuario)

except FileNotFoundError as error:
    print("No se pudo encontrar el archivo", error)

except Exception as error:
    print("Error: ", error)

finally:
    try:  # bloque protegido por si se intenta cerrar un archivo que no se consiguio abrir.
        contenido.close()
    except NameError:
        pass

def formacion_html(nombre_archivo, usuario, USUARIOS, BBDD_JUGADORES):
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            print(f"Error: No se encontró el archivo {nombre_archivo} en {directorio_actual}")
            return ""

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            html = archivo.read()
        
        # Buscar datos del usuario en USUARIOS
        datos_usuario = USUARIOS.get(usuario)
        if not datos_usuario:
            return "<p>Usuario no encontrado</p>"

        titulares = datos_usuario["titulares"]
        suplentes = datos_usuario["suplentes"]
        formacion = datos_usuario["formacion"]

        posiciones = (
            ["arquero"] * formacion["arquero"] +
            ["defensor"] * formacion["defensor"] +
            ["mediocampista"] * formacion["mediocampista"] +
            ["delantero"] * formacion["delantero"]
        )

        jugadores_por_posicion = {
            "arquero": [],
            "defensor": [],
            "mediocampista": [],
            "delantero": []
        }

        # Función recursiva para llenar titulares
        def llenar_titulares(index=0):
            if index >= len(titulares):
                return
            jugador_id = str(titulares[index])
            jugador = BBDD_JUGADORES.get(int(jugador_id))
            if jugador:
                posicion = posiciones[index]
                jugadores_por_posicion[posicion].append(
                    f"<li>{jugador['nombre']} {jugador['apellido']}</li>"
                )
            llenar_titulares(index + 1)

        llenar_titulares()

        # Armar HTML de suplentes
        suplentes_html = ""
        for s_id in suplentes:
            jugador = BBDD_JUGADORES.get(int(s_id))
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

# Llama la función con USUARIOS y BBDD_JUGADORES
html_render = formacion_html("htmlYCss/formacion.html", "Nicolas", USUARIOS, BBDD_JUGADORES)

with open("formacion.html", "w", encoding="utf-8") as f:
    f.write(html_render)

