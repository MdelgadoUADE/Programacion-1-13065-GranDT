def crear_matriz_posiciones(equipos):
    """
    Crea una matriz para almacenar las posiciones de los equipos en una tabla de liga.

    Parametros:
    equipos (list): Lista de nombres de equipos.

    Retorna:
    list: Matriz de dimensiones n x 5, donde n es el número de equipos. 
          Las columnas representan: equipo, ganados, empatados, perdidos, puntos totales.
    """

    filas=(len(equipos))
    columnas = 5 #equipo ganados empatados perdidos puntosTotales
    matriz = [[0]*columnas for i in range(filas)]
    return matriz

def rellenar_equipos_matriz(lista_equipos,matriz_posiciones):
    """
    Rellena la primera columna de la matriz con los nombres de los equipos en la lista_equipos
    
    Parametros:
    lista_equipos (list): lista de nombres de equipos
    matriz_posiciones (list): matriz de posiciones
    
    Retorna:
    list: matriz de posiciones con la primera columna rellenada con los nombres de los equipos
    """
    filas = len(matriz_posiciones)
    columnas = len(matriz_posiciones[0])
    for f in range(filas):
        for c in range(columnas):
            matriz_posiciones[f][0] = lista_equipos[f]
    return matriz_posiciones

def actualizar_matriz_posiciones(matriz_posiciones, resultados_partido):
    """
    Actualiza la matriz de posiciones segun los resultados de un partido

    Parametros:
    matriz_posiciones (list): matriz de posiciones
    resultados_partido (dict): diccionario con los resultados del partido. Las claves son los nombres de los equipos y los valores son "gana", "pierde" o "empata"

    Retorna:
    list: matriz de posiciones actualizada
    """
    for equipo, resultado in resultados_partido.values():
        for fila in matriz_posiciones:
            if fila[0] == equipo:
                if resultado == "gana":
                    fila[1] += 1  
                    fila[4] += 3  
                elif resultado == "pierde":
                    fila[3] += 1  
                elif resultado == "empata":
                    fila[4] += 1
                    fila[2] += 1 
                break
    return matriz_posiciones
def generar_html_tabla_posiciones(matriz_posiciones):
    """
    Genera una representación HTML de la tabla de posiciones.

    Parámetros:
    matriz_posiciones (list): Una matriz donde cada fila representa un equipo y las columnas
                              contienen el nombre del equipo, la cantidad de partidos ganados,
                              empatados, perdidos, y los puntos totales.

    Retorna:
    str: Una cadena que contiene el código HTML para la tabla de posiciones.
    """

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tabla de Posiciones</title>
        <link rel="stylesheet" href="stylesheet.css">
    </head>
    <body>
        <h2>Tabla de Posiciones</h2>
        <table>
            <tr>
                <th>Equipo</th>
                <th>Ganados</th>
                <th>Empatados</th>
                <th>Perdidos</th>
                <th>Puntos Totales</th>
            </tr>
    """
    for fila in matriz_posiciones:
        html += "<tr>"
        for celda in fila:
            html += f"<td>{celda}</td>"
        html += "</tr>"
    
    html += """
        </table>
    </body>
    </html>
    """
    return html

def guardar_tabla_posiciones_html(matriz_posiciones, nombre_archivo="tabla_posiciones.html"):
    """
    Guarda la tabla de posiciones en un archivo HTML.

    Parámetros:
    matriz_posiciones (list): Una matriz donde cada fila representa un equipo y las columnas
                              contienen el nombre del equipo, la cantidad de partidos ganados,
                              empatados, perdidos, y los puntos totales.
    nombre_archivo (str, opcional): El nombre del archivo que se creará. Por defecto es
                                    "tabla_posiciones.html".

    Retorna:
    None
    """
    
    html = generar_html_tabla_posiciones(matriz_posiciones)
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)
        print(f"Tabla guardada como '{nombre_archivo}'. Podés abrirlo en tu navegador.")
    except Exception as e:
        print("Error al guardar el archivo:", e)

def actualizar_y_guardar_tabla_posiciones(matriz_posiciones, resultados, nombre_archivo="tabla_posiciones.html"):
    """
    Actualiza la matriz de posiciones según los resultados proporcionados y guarda la tabla de posiciones actualizada en un archivo HTML.

    Parámetros:
    matriz_posiciones (list): Matriz actual de posiciones, donde cada fila representa un equipo y las columnas contienen el nombre del equipo, la cantidad de partidos ganados, empatados, perdidos y los puntos totales.
    resultados (dict): Diccionario con los resultados del partido. Las claves son los nombres de los equipos y los valores son "gana", "pierde" o "empata".
    nombre_archivo (str, opcional): El nombre del archivo HTML a crear. Por defecto es "tabla_posiciones.html".

    Retorna:
    None
    """
    # 1. Actualizar la matriz
    matriz_actualizada = actualizar_matriz_posiciones(matriz_posiciones,resultados)
    
    # 2. Generar y guardar HTML
    guardar_tabla_posiciones_html(matriz_actualizada, nombre_archivo)

def generar_fixture_ida_vuelta(equipos):
    """
    Genera un fixture para una competencia de ida y vuelta con los equipos dados
    
    Parametros:
    equipos (list): lista de nombres de equipos
    """

    cantidad_equipos = len(equipos)
    mitad = cantidad_equipos // 2
    fechas_ida = []

    for ronda in range(cantidad_equipos - 1):
        fecha = []
        for i in range(mitad):
            local = equipos[i]
            visitante = equipos[-i-1]
            # Alternar localía cada ronda para mejor distribución
            if ronda % 2 == 0:
                partido = (local, visitante)
            else:
                partido = (visitante, local)
            fecha.append(partido)
        fechas_ida.append(fecha)
        # Rotar los equipos (excepto el primero)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    # Usamos lambda + map para invertir local/visitante en cada partido de la fecha
    fechas_vuelta = list(map(lambda fecha: list(map(lambda p: (p[1], p[0]), fecha)), fechas_ida))

    fixture_completo = fechas_ida + fechas_vuelta
    return fixture_completo