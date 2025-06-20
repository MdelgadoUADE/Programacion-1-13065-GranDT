# SEGUNDA ENTREGA, EQUIPO GRANDT
# SEBASTIAN PENZA, MATIAS DELGADO, NICOLAS LOVERA

# IMPORTACIONES
import re
import random
import json
import os
from json.decoder import JSONDecodeError
from utils import *
from tablaPosiciones import *


try:
    # Encoding añadido debido a error extraño con json
    contenido = open("data/jugadores_actualizados.json", "r", encoding="utf8")
    jugadores = contenido.read()

    BBDD_JUGADORES = json.loads(jugadores)
    # conversion de numeros de string a enteros
    BBDD_JUGADORES = {int(k): v for k, v in BBDD_JUGADORES.items()}

except FileNotFoundError as error:
    print("No se pudo encontrar el archivo", error)

except Exception as error:
    print("Error: ", error)

finally:
    try:  # bloque protegido por si se intenta cerrar un archivo que no se consiguio abrir.
        contenido.close()
    except NameError:
        pass


# DEFINICIONES
"""
ARMADO DE JUGADORES
Matriz [
jugador [nombre, equipo, titulares, nro capitan, puntos, presupuesto]
]

"""
id_eventos = {
    0: {"titulo": "Partido Ganado", "puntaje_asociado": ""},
    1: {"titulo": "Partido Empatado", "puntaje_asociado": ""},
    2: {"titulo": "Partido Perdido", "puntaje_asociado": ""},
    3: {"titulo": "Gol", "puntaje_asociado": 6},
    4: {"titulo": "Asistencia", "puntaje_asociado": 3},
    5: {"titulo": "Tarjeta Amarilla", "puntaje_asociado": -2},
    6: {"titulo": "Tarjeta Roja", "puntaje_asociado": -4}
}

# ---------------------------------------------
# FUNCIONES
#   PRINTS


def print_menu_usuarios():
    print("""
  ____                        ____ _____ 
 / ___| _   _ _ __   ___ _ __|  _ \_   _|
 \___ \| | | | '_ \ / _ \ '__| | | || |  
  ___) | |_| | |_) |  __/ |  | |_| || |  
 |____/ \__,_| .__/ \___|_|  |____/ |_|  
             |_|                         
""")
    print("---------------\nMENU USUARIOS\n---------------")
    print("Por favor seleccione una opcion:\n",
          "A. Seleccionar usuario\n",
          "B. Agregar Usuario\n",
          "C. Eliminar Usuario\n",
          "D. Salir",
          )


def print_menu_principal(nombre_usuario):
    print()
    print(f"Bienvenido {nombre_usuario}!!\n")
    print("---------------\nMENU PRINCIPAL\n---------------")
    print("Por favor seleccione una opcion:\n",
          "A. Menu de Equipo\n",
          "B. Menu de Torneo\n",
          # "C. Cambiar de Usuario\n",
          "C. Salir",
          )


def print_menu_equipo():
    print("---------------\nMENU EQUIPO\n---------------")
    print("Por favor selecciona una opcion:\n",
          "A. Ver Equipo\n",
          "B. Añadir Jugadores\n",
          "C. Remover Jugadores\n",
          # "D. Asignar Capitan\n",
          "D. Regresar al menu principal"
          )


def print_menu_torneo():
    print("---------------\nMENU TORNEO\n---------------")
    print("Por favor selecciona una opcion:\n",
          "A. Jugar proxima fecha\n",
          "B. Ver fixture\n",
          "C. Regresar al menu principal",
          )


def print_equipo(equipo_usuario):
    if len(equipo_usuario) == 0:
        print("Sin jugadores en equipo")
    else:
        print()
        for jugador in equipo_usuario:
            datos_jugador = BBDD_JUGADORES.get(jugador)
            print(
                f"{datos_jugador['nombre']} {datos_jugador['apellido']} - Posicion: {datos_jugador['posicion']}")
        input("\nPresione enter para continuar")
# ---------------------------------------------
#   LOGICA


def main():
    """'Yo soy el alfa y el omega, el principio y el fin'.
    Esta funcion inicia el programa y se encarga de llamar a la primera funcion de menu usuarios. No tiene parametros o retornos"""
    try:

        contenido = open("data/usuarios.json", "r")
        lineas = contenido.read()
        contenido.close()

        usuarios = json.loads(lineas)

        logica_menu_usuarios(usuarios)

    except (FileNotFoundError, JSONDecodeError):
        print("No hay usuarios registrados, por favor cree uno\n")
        with open("data/usuarios.json", "w") as contenido:
            json.dump(registrar_usuario(), contenido, indent=4)

        main()

    except Exception as e:
        registrar_excepciones(e)


def registrar_usuario():
    print("Por favor ingrese el nombre de usuario a agregar:")
    nombre = input("> ")
    usuario = {
        nombre: {
            "nom_usuario": nombre,
            "formacion": {
                "arquero": 1,
                "defensor": 4,
                "centrocampista": 4,
                "delantero": 2
            },
            "equipo": [],
            "titulares": [],
            "nro_capitan": 0,
            "presupuesto": 42000000,
            "puntos": 0
        }
    }
    return usuario


def seleccionar_usuario():
    try:
        while True:
            usuarios = abrir_archivo_json("data/usuarios.json", 'r')

            if len(usuarios) < 1:
                raise UserWarning()

            print("Indicar con que usuario acceder: ")
            for usuario in usuarios:
                print(f"- {usuario}")
            print("- Salir")

            usuario_seleccionado = input("> ")
            if usuario_seleccionado.lower() == "salir":
                return
            try:
                return usuarios[usuario_seleccionado]
            except KeyError:
                print("No se pudo encontrar el usuario")
                if not confirmar_seleccion("Desea seguir intentando?"):
                    return
    except UserWarning:
        print("No hay usuarios registrados!\nPor favor cree uno\n")
        input("Presione enter para continuar")


def remover_usuario():
    while True:
        print("Por favor indique que usuario desea eliminar (con nombre):")

        contador = 0
        usuarios = abrir_archivo_json("data/usuarios.json", "r")
        for usuario in usuarios:
            print(f"{contador} - {usuario}")
            print(f"{contador + 1} Salir")
            contador += 1

        usuario_seleccionado = input("> ")
        if usuario_seleccionado.lower() == "salir":
            return
        try:
            usuarios.pop(usuario_seleccionado)
        except KeyError:
            print("No se pudo encontrar el usuario")
            if not confirmar_seleccion("Desea seguir intentando?"):
                return
        else:
            with open("data/usuarios.json", "w") as contenido:
                json.dump(usuarios, contenido, indent=4)
            print(f"Usuario {usuario_seleccionado} eliminado con exito")


def registro_de_equipos(jugadores):
    """Registra los equipos de la base de jugadores en una lista.

    Dado un diccionario de jugadores, recorre cada jugador y agrega su equipo a una lista si no existe ya.

    Argumentos:
    jugadores (dict): Diccionario con los jugadores como claves y sus datos como valores.

    Return:
    list: Una lista de los equipos de los jugadores.
    """
    equipos = []
    for jugador in jugadores:
        equipo = jugadores[jugador]['id_equipo']
        if equipo not in equipos:
            equipos.append(equipo)
    return equipos


def seleccion_jugadores_id(lista_jugadores):
    """Este codigo se ejecuta dentro de añadir jugadores, cuando hay varios con el mismo apellido se ejecuta y fuerza al jugador a seleccionar uno, devuelte una lista de longitud 1

    Args:
        lista_jugadores (list): [id_jugador]

    Returns:
        list: [id_jugador]
    """
    print("Hay varios jugadores con el mismo apellido",
          "\nPor favor indique el id del jugador a anadir:\n", end="")
    for jugador in lista_jugadores:
        print(
            f"{jugador} - {BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")

    while True:
        respuesta = int(input("> "))
        if respuesta in lista_jugadores:
            print(
                f"Jugador {BBDD_JUGADORES[respuesta]['nombre']} {BBDD_JUGADORES[respuesta]['apellido']} anadido al equipo")
            return [respuesta]
        else:
            print("Id incorrecto, intente nuevamente")


def añadir_jugadores(usuario):
    pass


def solicitar_dato_jugador(dato):
    print(f"Porfavor indique el {dato} del jugador a buscar:")
    return input("> ")


def buscar_jugador(dato):
    if dato == "nombre, apellido":
        pass
    else:
        pass


def logica_menu_usuarios(dic_usuarios):
    while True:
        print_menu_usuarios()
        seleccion = input("> ").lower()
        if seleccion == "a":
            usuario = seleccionar_usuario()
            if usuario != None:
                logica_menu_principal(usuario)
        elif seleccion == "b":
            with open("data/usuarios.json", "w") as contenido:
                dic_usuarios.update(registrar_usuario())
                json.dump(dic_usuarios, contenido, indent=4)
        elif seleccion == "c":
            remover_usuario()
        elif seleccion == "d":
            return
        else:
            print("Opcion no valida")


def logica_menu_torneo(usuario, fixture, matriz_posiciones):

    fecha_actual = 0
    while True:
        print_menu_torneo()
        seleccion = input("> ").lower()
        if seleccion == "a":
            if fecha_actual < len(fixture):
                matriz_posiciones = simular_fecha(fecha_actual, fixture, matriz_posiciones)
                fecha_actual += 1
            else:
                print("¡El torneo ha terminado!")
        elif seleccion == "b":
            ver_fixture(fixture, usuario)
        elif seleccion == "c":
            return usuario
        else:
            print("Opcion no valida")


def logica_menu_equipo(usuario):
    while True:
        print_menu_equipo()
        seleccion = input("> ").lower()
        if seleccion == "a":
            print_equipo(usuario["equipo"])
        elif seleccion == "b":
            usuario = añadir_jugadores(usuario)
        elif seleccion == "c":
            eliminar_jugadores(usuario)
        elif seleccion == "d":
            return usuario
        else:
            print("Opcion no valida")


def logica_menu_principal(usuario):
    """
    Muestra el menu principal y se encarga de llamar a las demas funciones segun la eleccion del usuario

    Parametros:
    usuario (list): [id_usuario, lista_jugadores, nro_capitan, puntos, presupuesto]
    """
    while True:
        print_menu_principal(usuario["nom_usuario"])
        seleccion = input("> ").lower()
        if seleccion == "a":
            logica_menu_equipo(usuario)
        elif seleccion == "b":
            logica_menu_torneo(usuario, fixture, matriz_posiciones)
        elif seleccion == "c":
            logica_menu_usuarios()
        elif seleccion == "c":
            return
        else:
            print("Opcion no valida")


# Me devuelve los datos de los jugadores cargados en una tupla
def registro_de_jugadores(jugadores):
    players = []
    for clave, valor in jugadores.items():
        id_jugador = clave
        equipo = valor["id_equipo"]
        nombre = valor["nombre"]
        apellido = valor["apellido"]
        posicion = valor["posicion"]

        # Datos de los jugadores
        players.append((id_jugador, equipo, nombre, apellido, posicion))
    return players


def ver_fixture(fixture, usuario):
    """
    Muestra el menú del fixture para ver fechas o ver el fixture completo

    Parametros:
    fixture (list): lista de listas, cada una con los partidos de una fecha
    """

    print("\n=== Menú del Fixture ===")
    print("A. Ver Fecha en Especifico")
    print("B. Ver fixture completo")
    print("C. Atras")
    opcion = input("Elegí una opción: ")
    if opcion == "A":
        fecha_especifica = int(input("Indique la fecha especifica: "))
        while fecha_especifica > len(fixture) or fecha_especifica < 1:
            print("Fecha no válida")
            fecha_especifica=int(input("Indique la fecha especifica: "))
        print()
        print(f"\nFecha {fecha_especifica}".upper())
        for partido in fixture[fecha_especifica-1]:
            print(f"{partido[0]} vs {partido[1]}")
        print()
    elif opcion == "B":
        for numero_fecha, fecha in enumerate(fixture, start=1):
            print(f"Fecha {numero_fecha}:".upper())
            for local, visitante in fecha:
                print(f"  {local} vs {visitante}")
            print("-" * 20)
    else:
        logica_menu_torneo(usuario, fixture, matriz_posiciones)


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


def simular_eventos(fixture, resultado_local):
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

    eventos.append(local)
    eventos.append(resultado_local)
    eventos.append(visitante)

    if resultado_local == "gana":
        resultado_visitante = "pierde"
        eventos.append(resultado_visitante)
        while (goles_local <= goles_visitante):
            goles_local = random.randint(1, 5)
            goles_visitante = random.randint(0, 4)
            asis_local = goles_local
            asis_visitante = goles_visitante
    elif resultado_local == "pierde":
        resultado_visitante = "gana"
        eventos.append(resultado_visitante)
        while (goles_visitante <= goles_local):
            goles_visitante = random.randint(1, 5)
            goles_local = random.randint(0, 4)
            asis_local = goles_local
            asis_visitante = goles_visitante
    else:
        resultado_visitante = "empata"
        eventos.append(resultado_visitante)
        goles_local = random.randint(0, 5)
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
    print("Goles en el encuentro:", goles_totales)
    print("Asistencias equipo local:", asis_local)
    print("Asistencias equipo visitante:", asis_visitante)
    print("Tarjetas Amarillas Local:", t_amarilla_local)
    print("Tarjetas Amarillas Visita:", t_amarilla_visita)

    # [local, res_local, visi, res_visi, gol_total, gol_local, gol_visi, asis_local, asis_visitante, t_amarilla_local, t_amarilla_visita]
    return eventos


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

    print(f"Equipo local, {local}, {resultado_local}")
    print(f"Equipo visitante, {visitante}, {resultado_visitante}")
    print()
    return resultados_partidos


def simular_eventos(fixture, resultado_local):
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

    eventos.append(local)
    eventos.append(resultado_local)
    eventos.append(visitante)

    if resultado_local == "gana":
        resultado_visitante = "pierde"
        eventos.append(resultado_visitante)
        while (goles_local <= goles_visitante):
            goles_local = random.randint(1, 5)
            goles_visitante = random.randint(0, 4)
            asis_local = goles_local
            asis_visitante = goles_visitante
    elif resultado_local == "pierde":
        resultado_visitante = "gana"
        eventos.append(resultado_visitante)
        while (goles_visitante <= goles_local):
            goles_visitante = random.randint(1, 5)
            goles_local = random.randint(0, 4)
            asis_local = goles_local
            asis_visitante = goles_visitante
    else:
        resultado_visitante = "empata"
        eventos.append(resultado_visitante)
        goles_local = random.randint(0, 5)
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
    print("Goles en el encuentro:", goles_totales)
    print("Asistencias equipo local:", asis_local)
    print("Asistencias equipo visitante:", asis_visitante)
    print("Tarjetas Amarillas Local:", t_amarilla_local)
    print("Tarjetas Amarillas Visita:", t_amarilla_visita)

    # [local, res_local, visi, res_visi, gol_total, gol_local, gol_visi, asis_local, asis_visitante, t_amarilla_local, t_amarilla_visita]
    return eventos


def asignar_eventos(equipo_local, equipo_visitante, eventos, id_eventos):
    """
    Asigna aleatoriamente eventos a jugadores titulares de dos equipos. Pondera cada asignacion segun tipo de evento y posicion del jugador.

    Args:
        equipo_local (list): Titulares local.
        equipo_visitante (list): Titulares visitante.
        eventos (list): Eventos aleatorios del partido.
        id_eventos (dict): Datos asociados a cada evento.

    Returns:
        eventos_asignados (list): Eventos asignados a jugadores de ambos equipos.
    """

    # Probabilidad gol
    prob_gol = {"Arquero": 0.0, "Defensor": 0.1,
                "Mediocampista": 0.2, "Delantero": 0.7}
# Probabilidad asistencia
    prob_asis = {"Arquero": 0.1, "Defensor": 0.1,
                 "Mediocampista": 0.6, "Delantero": 0.2}
# Probabilidad tarjeta amarilla
    prob_ta = {"Arquero": 0.1, "Defensor": 0.3,
               "Mediocampista": 0.3, "Delantero": 0.3}

    id_eventos = {
        0: {"titulo": "Partido Ganado", "puntaje_asociado": ""},
        1: {"titulo": "Partido Empatado", "puntaje_asociado": ""},
        2: {"titulo": "Partido Perdido", "puntaje_asociado": ""},
        3: {"titulo": "Gol", "puntaje_asociado": 6},
        4: {"titulo": "Asistencia", "puntaje_asociado": 3},
        5: {"titulo": "Tarjeta Amarilla", "puntaje_asociado": -2},
        6: {"titulo": "Tarjeta Roja", "puntaje_asociado": -4}
    }

    eventos_asignados = []
    goles_local = []
    asistencias_local = []
    amarillas_local = []
    goles_visita = []
    asistencias_visita = []
    amarillas_visita = []
    aux = []

    # LOCAL
    # gol
    pesos_local = [prob_gol.get(jugador[4], 0.1)
                   for jugador in equipo_local]
    while (eventos[5] != 0):
        goleador = random.choices(
            equipo_local, weights=pesos_local, k=1)[0]
        aux.extend(goleador)
        aux.append(id_eventos[3]["titulo"])
        aux.append(id_eventos[3]["puntaje_asociado"])
        goles_local.append(aux)
        aux = []
        eventos[5] -= 1

    # asist
    pesos_local = [prob_asis.get(jugador[4], 0.1)
                   for jugador in equipo_local]
    while (eventos[-4] != 0):
        asistidor = random.choices(
            equipo_local, weights=pesos_local, k=1)[0]
        aux.extend(asistidor)
        aux.append(id_eventos[4]["titulo"])
        aux.append(id_eventos[4]["puntaje_asociado"])
        asistencias_local.append(aux)
        aux = []
        eventos[-4] -= 1

    # tarjetas
    pesos_local = [prob_ta.get(jugador[4], 0.1)
                   for jugador in equipo_local]
    while (eventos[-2] != 0):
        amonestado = random.choices(
            equipo_local, weights=pesos_local, k=1)[0]
        aux.extend(amonestado)
        aux.append(id_eventos[5]["titulo"])
        aux.append(id_eventos[5]["puntaje_asociado"])
        amarillas_local.append(aux)
        aux = []
        eventos[-2] -= 1

    # VISITA
    # gol
    pesos_visita = [prob_gol.get(jugador[4], 0.1)
                    for jugador in equipo_visitante]
    while (eventos[6] != 0):
        goleador = random.choices(
            equipo_visitante, weights=pesos_visita, k=1)[0]
        aux.extend(goleador)
        aux.append(id_eventos[3]["titulo"])
        aux.append(id_eventos[3]["puntaje_asociado"])
        goles_visita.append(aux)
        aux = []
        eventos[6] -= 1

    # asist
    pesos_visita = [prob_asis.get(jugador[4], 0.1)
                    for jugador in equipo_visitante]
    while (eventos[-3] != 0):
        asistidor = random.choices(
            equipo_visitante, weights=pesos_visita, k=1)[0]
        aux.extend(asistidor)
        aux.append(id_eventos[4]["titulo"])
        aux.append(id_eventos[4]["puntaje_asociado"])
        asistencias_visita.append(aux)
        aux = []
        eventos[-3] -= 1

    # tarjetas
    pesos_visita = [prob_ta.get(jugador[4], 0.1)
                    for jugador in equipo_visitante]
    while (eventos[-1] != 0):
        amonestado = random.choices(
            equipo_visitante, weights=pesos_visita, k=1)[0]
        aux.extend(amonestado)
        aux.append(id_eventos[5]["titulo"])
        aux.append(id_eventos[5]["puntaje_asociado"])
        amarillas_visita.append(aux)
        aux = []
        eventos[-1] -= 1

    # [evento, equipo, id_jugador, nombre, apellido, posicion, puntaje_asociado]
    eventos_asignados.append(goles_local)
    eventos_asignados.append(asistencias_local)
    eventos_asignados.append(amarillas_local)
    eventos_asignados.append(goles_visita)
    eventos_asignados.append(asistencias_visita)
    eventos_asignados.append(amarillas_visita)
    return eventos_asignados

def simular_fecha(fecha_actual, fixture, matriz_posiciones):
    print(f"\n=== FECHA {fecha_actual+1} ===")
    
    for partido in fixture[fecha_actual]:
        resultados_partido = simular_resultado_partido(partido)
        actualizar_matriz_posiciones(matriz_posiciones, resultados_partido)
    
    # 2. Ordenar la matriz
    matriz_posiciones = ordenar_matriz(matriz_posiciones)
    
    # 3. Actualizar la tabla HTML
    actualizar_tabla_posiciones_html(matriz_posiciones)
    
    return matriz_posiciones

""" LA DEJAMOS POR LAS DUDAS PERO NO ES LLAMADA
def fecha_actual_partidos(fecha,fixture): # fecha deberia ser la fecha actual de la instancia del programa
    fecha_actual = fecha
    for partido in fixture[fecha_actual]:
        simular_partido(partido)
    fecha_actual= fecha_actual+1
    return fecha_actual
"""
lista_equipos = registro_de_equipos(BBDD_JUGADORES)
fixture = generar_fixture_ida_vuelta(lista_equipos)
matriz_posiciones = crear_matriz_posiciones(lista_equipos)



# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    main()
