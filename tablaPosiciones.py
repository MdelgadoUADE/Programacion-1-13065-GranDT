import os
def crear_matriz_posiciones(equipos):
    
    """
    Crea una matriz de posiciones para los equipos proporcionados.

    Cada equipo en la lista de entrada se representa como una fila en la matriz
    con el formato [equipo, ganados, empatados, perdidos, puntos].

    Args:
        equipos (list): Lista de nombres de equipos.

    Returns:
        list: Matriz de posiciones inicializada con 0 en "ganados", "empatados",
        "perdidos" y "puntos" para cada equipo.
    """

    matriz = []
    for equipo in equipos:
        matriz.append([equipo, 0, 0, 0, 0])  # [equipo, ganados, empatados, perdidos, puntos]
    return matriz

def actualizar_posiciones(matriz_posiciones):
    """
    Actualiza la tabla de posiciones del torneo.

    Primero ordena la matriz de posiciones de manera descendente segun los puntos
    de cada equipo. Luego actualiza el archivo HTML de la tabla de posiciones con
    los datos de la matriz ordenada.

    Args:
        matriz_posiciones (list): Matriz de posiciones del torneo.
    """
    # 2. Ordenar la matriz
    matriz_posiciones = ordenar_matriz(matriz_posiciones)

    # 3. Actualizar la tabla HTML
    nombre_archivo = "html_y_css/tabla_posiciones.html"
    actualizar_tabla_posiciones_html(matriz_posiciones, nombre_archivo)

def actualizar_matriz_posiciones(matriz_posiciones, resultados_partido):
    """
    Actualiza la matriz de posiciones segun los resultados de un partido

    Args:
    matriz_posiciones (list): matriz de posiciones
    resultados_partido (dict): diccionario con los resultados del partido. Las claves son los nombres de los equipos y los valores son "gana", "pierde" o "empata"

    Returns:
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

def ordenar_matriz(matriz):
    """
    Ordena la matriz de posiciones de manera descendente segun los puntos de cada equipo, Luego partidos ganados, luego por empatados, y por ultimo por derrotas.

    Args:
        matriz (list): Matriz de posiciones del torneo.

    Returns:
        list: Matriz ordenada de posiciones.
    """
    return sorted(matriz, key=lambda x: (-x[4], -x[1], -x[2], x[3]))

def actualizar_tabla_posiciones_html(matriz_posiciones, nombre_archivo):
    """
    Actualiza la tabla de posiciones del torneo en el archivo HTML especificado.

    Reemplaza el contenido de la tabla existente con la matriz de posiciones
    actualizada.

    Args:
        matriz_posiciones : Matriz de posiciones del torneo.
        nombre_archivo (str): Ruta del archivo HTML de la tabla de posiciones.

    Raises:
        Exception: Si no se encuentra el archivo HTML o la estructura de la tabla
            no se puede encontrar.
    """
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__)) 
        ruta_archivo = os.path.join(directorio_actual, nombre_archivo) 
        
        if not os.path.exists(ruta_archivo):
            print(f"Error: No se encontró el archivo {nombre_archivo} en {directorio_actual}")
            return
        
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        
        inicio_tabla = contenido.find("<tr><td>")
        fin_tabla = contenido.find("</table>")
        
        if inicio_tabla == -1 or fin_tabla == -1:
            raise Exception("No se pudo encontrar la estructura de la tabla en el archivo HTML")
        
        nueva_tabla = ""
        for posicion, equipo in enumerate(matriz_posiciones, 1):
            nueva_tabla += f"<tr><td>{posicion}. {equipo[0]}</td><td>{equipo[1]}</td><td>{equipo[2]}</td><td>{equipo[3]}</td><td>{equipo[4]}</td></tr>"
        
        # Reemplazar el contenido antiguo con el nuevo
        nuevo_contenido = contenido[:inicio_tabla] + nueva_tabla + contenido[fin_tabla:]
        
        # Guardar el archivo actualizado
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(nuevo_contenido)
            
        print()   
        print(f"Tabla actualizada en: {ruta_archivo}")
        print("Puedes abrir el archivo manualmente en tu navegador para ver la tabla de posiciones.")
        
    except Exception as e:
        print(f"Error al actualizar la tabla: {e}")

def generar_fixture_ida_vuelta(equipos):
    """
    Genera un fixture de ida y vuelta para una lista de equipos.

    Para cada ronda, se generan encuentros alternando la localía de los equipos.
    La segunda vuelta invierte los encuentros de la primera vuelta.

    Args:
        equipos (list): Lista de nombres de equipos.

    Returns:
        list: Fixture completo con los partidos de ida y vuelta.
    """

    cantidad_equipos = len(equipos)
    mitad = cantidad_equipos // 2 
    fechas_ida = []

    for ronda in range(cantidad_equipos - 1):
        fecha = []
        for i in range(mitad):
            local = equipos[i]
            visitante = equipos[-i-1] 
            if ronda % 2 == 0:
                partido = (local, visitante)
            else:
                partido = (visitante, local)
            fecha.append(partido)
        fechas_ida.append(fecha)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    # Usamos lambda + map para invertir local/visitante en cada partido de la fechas de vuelta
    fechas_vuelta = list(map(lambda fecha: list(map(lambda p: (p[1], p[0]), fecha)), fechas_ida))

    fixture_completo = fechas_ida + fechas_vuelta
    return fixture_completo