import random
import os
import json


def procesar_equipos(fixture, jugadores):
    """
    Extrae equipo local y visitante de la base de datos de jugadores.

    Args:
        fixture (tuple): Local vs. Visitante.
        jugadores (dict): Base de jugadores

    Returns:
        titulares (tuple): Local y visitante.
    """
    titulares_local = []
    titulares_visitante = []

    local, visitante = fixture

    for jugador, data in jugadores.items():
        if data["id_equipo"] == local:
            info_jugador = [jugador, data["id_equipo"],
                            data["nombre"], data["apellido"], data["posicion"]]
            titulares_local.append(info_jugador)

    for jugador, data in jugadores.items():
        if data["id_equipo"] == visitante:
            info_jugador = [jugador, data["id_equipo"],
                            data["nombre"], data["apellido"], data["posicion"]]
            titulares_visitante.append(info_jugador)

    # [id_jugador, equipo, nombre, apellido, posicion]
    return titulares_local, titulares_visitante


def simular_resultado_partido(fixture):
    """
    Randomiza el resultado de un partido.

    Args:
        fixture (tuple): Local vs. Visitante.

    Returns:
        resultados_partidos (dict): Resultado del partido.
    """

    resultados_partidos = {}
    local, visitante = fixture

    casos = ["gana", "pierde", "empata"]
    resultado_local = random.choice(casos)

    if resultado_local == "gana":
        resultado_visitante = "pierde"
    elif resultado_local == "pierde":
        resultado_visitante = "gana"
    else:
        resultado_visitante = "empata"

    resultados_partidos["local"] = (local, resultado_local)
    resultados_partidos["visitante"] = (visitante, resultado_visitante)

    return resultados_partidos


def simular_eventos(fixture, fecha, resultado_local):
    """
    Genera aleatoriamente los valores de los eventos de un partido.

    Args:
        fixture (tuple): Local vs. Visitante.
        resultado_local (str): Resultado del equipo local.

    Returns:
        Eventos (list): Una lista con todos los eventos del partido.
    """

    eventos = []
    local, visitante = fixture

    goles_local = 0
    goles_visitante = 0
    resultado_visitante = 0

    eventos.append(fecha)
    eventos.append(local)
    eventos.append(resultado_local)
    eventos.append(visitante)

    if resultado_local == "gana":
        resultado_visitante = "pierde"
        eventos.append(resultado_visitante)
        while (goles_local <= goles_visitante):
            goles_local = random.randint(1, 4)
            goles_visitante = random.randint(0, 3)
            asis_local = goles_local
            asis_visitante = goles_visitante
    elif resultado_local == "pierde":
        resultado_visitante = "gana"
        eventos.append(resultado_visitante)
        while (goles_visitante <= goles_local):
            goles_visitante = random.randint(1, 4)
            goles_local = random.randint(0, 3)
            asis_local = goles_local
            asis_visitante = goles_visitante
    else:
        resultado_visitante = "empata"
        eventos.append(resultado_visitante)
        goles_local = random.randint(0, 3)
        goles_local = goles_visitante

    goles_totales = goles_local + goles_visitante
    asis_local = goles_local
    asis_visitante = goles_visitante
    eventos.append(goles_totales)
    eventos.append(goles_local)
    eventos.append(goles_visitante)
    eventos.append(asis_local)
    eventos.append(asis_visitante)

    t_amarilla_local = random.randint(0, 2)
    t_amarilla_visita = random.randint(0, 2)
    eventos.append(t_amarilla_local)
    eventos.append(t_amarilla_visita)

    print(f"{local} {goles_local} - {visitante} {goles_visitante}")

    # [fecha, local, res_local, visi, res_visi, gol_total, gol_local, gol_visi, asis_local, asis_visitante, t_amarilla_local, t_amarilla_visita]
    return eventos


def asignar_eventos(equipo_local, equipo_visitante, eventos, id_eventos, nroFechaPartido):
    """
    Asigna aleatoriamente eventos a jugadores titulares de dos equipos. Pondera cada asignacion segun tipo de evento y posicion del jugador.

    Args:
        equipo_local (list): Titulares local.
        equipo_visitante (list): Titulares visitante.
        eventos (list): Eventos aleatorios del partido.
        id_eventos (dict): Datos asociados a cada evento.
        nroFecha (list): Fecha y Partido a simular.
    """

    # Probabilidades
    prob_gol = {"arquero": 0.0, "defensor": 0.1,
                "mediocampista": 0.2, "delantero": 0.7}
    prob_asis = {"arquero": 0.1, "defensor": 0.1,
                 "mediocampista": 0.6, "delantero": 0.2}
    prob_ta = {"arquero": 0.1, "defensor": 0.3,
               "mediocampista": 0.3, "delantero": 0.3}

    aux = []
    aux2 = []

    # LOCAL
    # gol
    pesos_local = [prob_gol.get(jugador[4], 0.1)
                   for jugador in equipo_local]
    while (eventos[6] != 0):
        goleador = random.choices(
            equipo_local, weights=pesos_local, k=1)[0]
        aux.extend(goleador)
        aux.append(id_eventos[3]["titulo"])
        aux.append(id_eventos[3]["puntaje_asociado"])
        aux2.append(aux)
        aux = []
        eventos[6] -= 1

    # asist
    pesos_local = [prob_asis.get(jugador[4], 0.1)
                   for jugador in equipo_local]
    while (eventos[-4] != 0):
        asistidor = random.choices(
            equipo_local, weights=pesos_local, k=1)[0]
        aux.extend(asistidor)
        aux.append(id_eventos[4]["titulo"])
        aux.append(id_eventos[4]["puntaje_asociado"])
        aux2.append(aux)
        aux = []
        eventos[-4] -= 1

    # tarjetas
    amonestadosLocal = {}
    pesos_local = [prob_ta.get(jugador[4], 0.1)
                   for jugador in equipo_local]
    while (eventos[-2] != 0):
        amonestado = random.choices(
            equipo_local, weights=pesos_local, k=1)[0]
        id_jugador = amonestado[0]
        if id_jugador in amonestadosLocal:
            aux3.extend(amonestado)
            aux3.append(id_eventos[5]["titulo"])
            aux3.append(id_eventos[5]["puntaje_asociado"])
            aux2.append(aux3)

            aux.extend(amonestado)
            aux.append(id_eventos[6]["titulo"])
            aux.append(id_eventos[6]["puntaje_asociado"])
            aux2.append(aux)
        else:
            aux.extend(amonestado)
            aux.append(id_eventos[5]["titulo"])
            aux.append(id_eventos[5]["puntaje_asociado"])
            aux2.append(aux)
        amonestadosLocal = amonestado
        aux = []
        aux3 = []
        eventos[-2] -= 1

    # VISITA
    # gol
    pesos_visita = [prob_gol.get(jugador[4], 0.1)
                    for jugador in equipo_visitante]
    while (eventos[7] != 0):
        goleador = random.choices(
            equipo_visitante, weights=pesos_visita, k=1)[0]
        aux.extend(goleador)
        aux.append(id_eventos[3]["titulo"])
        aux.append(id_eventos[3]["puntaje_asociado"])
        aux2.append(aux)
        aux = []
        eventos[7] -= 1

    # asist
    pesos_visita = [prob_asis.get(jugador[4], 0.1)
                    for jugador in equipo_visitante]
    while (eventos[-3] != 0):
        asistidor = random.choices(
            equipo_visitante, weights=pesos_visita, k=1)[0]
        aux.extend(asistidor)
        aux.append(id_eventos[4]["titulo"])
        aux.append(id_eventos[4]["puntaje_asociado"])
        aux2.append(aux)
        aux = []
        eventos[-3] -= 1

    # tarjetas
    amonestadosVisita = {}
    pesos_visita = [prob_ta.get(jugador[4], 0.1)
                    for jugador in equipo_visitante]
    while (eventos[-1] != 0):
        amonestado = random.choices(
            equipo_visitante, weights=pesos_visita, k=1)[0]
        id_jugador = amonestado[0]
        if id_jugador in amonestadosVisita:
            aux3.extend(amonestado)
            aux3.append(id_eventos[5]["titulo"])
            aux3.append(id_eventos[5]["puntaje_asociado"])
            aux2.append(aux3)

            aux.extend(amonestado)
            aux.append(id_eventos[6]["titulo"])
            aux.append(id_eventos[6]["puntaje_asociado"])
            aux2.append(aux)
        else:
            aux.extend(amonestado)
            aux.append(id_eventos[5]["titulo"])
            aux.append(id_eventos[5]["puntaje_asociado"])
            aux2.append(aux)
        amonestadosVisita = amonestado
        aux = []
        aux3 = []
        eventos[-1] -= 1

    cargar_evento(aux2, nroFechaPartido)
    aux2 = []


def cargar_evento(listaEvento, nroFecha):
    """
    Recibe cada lista de eventos individuales, ya asignados, por categoria y los escribe en un archivo de salida.

    Args:
        listaEvento (list): Lista del tipo de evento para agregar al archivo.
        nroFecha (list): Numero de fecha que se va a escribir.
    """

    eventos2json = []

    for evento in listaEvento:
        eventos2json.append({
            "fecha": nroFecha,
            "evento": evento[-2],
            "equipo": evento[1],
            "id_jugador": evento[0],
            "nombre": evento[2],
            "apellido": evento[3],
            "posicion": evento[4],
            "puntaje_asociado": evento[-1]
        })

    '''
    if nroFecha != 0:
        data_path = f"data/eventos{nroFecha}.txt"
    '''

    data = []

    if os.path.exists("data/eventos.txt"):
        try:
            with open("data/eventos.txt", mode="r", encoding="UTF-8") as archivo:
                data = json.load(archivo)
        except FileNotFoundError:
            print("No se encontró el archivo.")

    data.extend(eventos2json)

    with open("data/eventos.txt", mode='w', encoding='utf-8') as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)
