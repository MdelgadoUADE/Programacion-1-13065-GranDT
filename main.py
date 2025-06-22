# SEGUNDA ENTREGA, EQUIPO GRANDT
# SEBASTIAN PENZA, MATIAS DELGADO, NICOLAS LOVERA

# IMPORTACIONES
from busqueda_de_jugadores import *
import re
import random
import json
import os
from json.decoder import JSONDecodeError
from utils import *
from tablaPosiciones import *
from impresionJugadores import *
from calculo_puntos import *
from reportes_torneo import *
from logica import *
from config_manager import *

configuraciones = cargar_configuracion()

try:
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

id_eventos = {
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
          "D. Restaurar\n",
          "E. Salir",
          )


def print_menu_principal(nombre_usuario):
    print()
    print(f"Bienvenido {nombre_usuario}!!\n")
    print("---------------\nMENU PRINCIPAL\n---------------")
    print("Por favor seleccione una opcion:\n",
          "A. Consola de Equipo\n",
          "B. Imprimir equipo en HTML\n",
          "C. Menu de Torneo\n",
          "D. Cambiar de Usuario\n",
          "E. Salir",
          )


def print_menu_torneo():
    print("---------------\nMENU TORNEO\n---------------")
    print("Por favor selecciona una opcion:\n",
          "A. Jugar proxima fecha\n",
          "B. Ver fixture\n",
          "C. Regresar al menu principal",
          )

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

    except (FileNotFoundError, JSONDecodeError) as e:
        registrar_excepciones(e)
        print("No hay usuarios registrados, por favor cree uno\n")
        with open("data/usuarios.json", "w") as contenido:
            json.dump(registrar_usuario(), contenido, indent=4)

        main()

    except Exception as e:
        registrar_excepciones(e)


def registrar_usuario():
    print("Por favor ingrese el nombre de usuario a agregar:")
    nombre = input("> ")
    if len(nombre) <= 0:
        print("El nombre no puede estar vacio, por favor vuelva a intentarlo")
        while len(nombre) <= 0:
            nombre = input("> ")
    return definicion_usuario(nombre)


def seleccionar_usuario():
    try:
        while True:
            usuarios = abrir_archivo_json("data/usuarios.json", 'r')

            if len(usuarios) < 1:
                raise UserWarning()
            contador_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

            print("Indicar con que usuario acceder: ")
            i = 0
            for usuario in usuarios:
                print(f"{contador_letras[i].upper()} - {usuario}")
                i += 1
            print(f"{contador_letras[i].upper()} - Salir")

            usuario_seleccionado = input("> ")
            if usuario_seleccionado.lower() == "salir":
                return
            try:
                if usuario_seleccionado in contador_letras:
                    usuario_seleccionado = contador_letras.index(
                        usuario_seleccionado)
                    usuario_seleccionado = list(usuarios.keys())[
                        usuario_seleccionado]
                return usuarios[usuario_seleccionado]
            except KeyError:
                print("No se pudo encontrar el usuario")
                if not confirmar_seleccion("Desea seguir intentando?"):
                    return
            except IndexError:
                if usuario_seleccionado - len(usuarios) <= 0:
                    return
                print("No se pudo encontrar el usuario")
                if not confirmar_seleccion("Desea seguir intentando?"):
                    return
            
    except UserWarning:
        print("No hay usuarios registrados!\nPor favor cree uno\n")
        input("Presione enter para continuar")


def remover_usuario():
    while True:
        usuarios = abrir_archivo_json("data/usuarios.json", "r")
        contador_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        print("\nPor favor indique que usuario desea eliminar:")
        i = 0
        for usuario in usuarios:
            print(f"{contador_letras[i].upper()} - {usuario}")
            i += 1
        print(f"{contador_letras[i].upper()} - Salir")

        usuario_seleccionado = input("> ")
            
        try:
            if usuario_seleccionado.lower() == "salir":
                return
            if usuario_seleccionado in contador_letras:
                usuario_seleccionado = contador_letras.index(usuario_seleccionado)
                usuario_seleccionado = list(usuarios.keys())[usuario_seleccionado]
            del(usuarios[usuario_seleccionado])

        except KeyError:
            print("No se pudo encontrar el usuario")
            if not confirmar_seleccion("Desea seguir intentando?"):
                return
        except IndexError:
            if usuario_seleccionado - len(usuarios) <= 0: #como el usuario no puede ingresar una letra fuera de rango de la lista puedo usar el <
                return
            print("No se pudo encontrar el usuario")
            if not confirmar_seleccion("Desea seguir intentando?"):
                return
        else:
            with open("data/usuarios.json", "w") as contenido:
                json.dump(usuarios, contenido, indent=4)
            print(f"Usuario {usuario_seleccionado} eliminado con exito")
            input("Presione enter para continuar")

def logica_menu_usuarios(dic_usuarios):
    flag_comienzo_torneo = str_bool_literal(configuraciones["flag_comienzo_torneo"])

    while True:
        print_menu_usuarios()
        seleccion = input("> ").lower()
        if seleccion == "a":
            usuario = seleccionar_usuario()
            if usuario != None:
                logica_menu_principal(usuario)
        elif seleccion == "b":
            if flag_comienzo_torneo != True:
                with open("data/usuarios.json", "w") as contenido:
                    dic_usuarios.update(registrar_usuario())
                    json.dump(dic_usuarios, contenido, indent=4)
            else:
                print("El torneo ya ha comenzado, no sera posible registrar un nuevo usuario")
                input("Presione enter para continuar")
        elif seleccion == "c":
            remover_usuario()
        elif seleccion == "d":
            if confirmar_seleccion("Esta seguro de restaurar el juego? (esta accion no tiene marcha atras)"):
                restaurar_juego()
        elif seleccion == "e":
            guardar_configuraciones(configuraciones)
            return  # aca deberia cortar ejecucion
        else:
            print("Opcion no valida")


def logica_menu_torneo(usuario, fixture, matriz_posiciones):

    fecha_actual = int(configuraciones["fecha_actual"])

    while True:
        if fecha_actual >= len(fixture):
            configuraciones["flag_end_state"] = True

        fin_torneo = str_bool_literal(configuraciones["flag_end_state"])

        print_menu_torneo()
        seleccion = input("> ").lower()
        if seleccion == "a":
            if not fin_torneo:
                matriz_posiciones = simular_fecha(fecha_actual, fixture, matriz_posiciones, usuario)
                fecha_actual += 1
                configuraciones["flag_comienzo_torneo"] = True
            else:
                print("¡El torneo ha terminado!")
                reporte_final_usuarios()
                reporte_maximos_eventos()
                if confirmar_seleccion("Desea volver al menu principal?"):
                    return
        elif seleccion == "b":
            ver_fixture(fixture, usuario)
        elif seleccion == "c":
            configuraciones["fecha_actual"] = fecha_actual
            configuraciones["matriz_posiciones"] = matriz_posiciones
            return usuario
        else:
            print("Opcion no valida")


def logica_menu_principal(usuario):
    """
    Muestra el menu principal y se encarga de llamar a las demas funciones segun la eleccion del usuario

    Args:
        usuario (list): [id_usuario, lista_jugadores, nro_capitan, puntos, presupuesto]
    """
    while True:
        fin_torneo = str_bool_literal(configuraciones["flag_end_state"])
        inicio_torneo = str_bool_literal(configuraciones["flag_comienzo_torneo"])

        print_menu_principal(usuario["nom_usuario"])
        seleccion = input("> ").lower()
        if seleccion == "a" and not fin_torneo:
            if not fin_torneo and not inicio_torneo:
                iniciar_busqueda(usuario)
            elif inicio_torneo:
                print("El torneo ya ha comenzado, no sera posible acceder a la consola de equipo")
            else:
                print("El torneo ha terminado, no sera posible acceder a la consola de equipo")
        elif seleccion == "b":
            imprimir_equipo_platilla(usuario, BBDD_JUGADORES)
            input("Presione enter para continuar")
        elif seleccion == "c":
            logica_menu_torneo(usuario, fixture, matriz_posiciones)
        elif seleccion == "d":
            return
        elif seleccion == "e":
            guardar_configuraciones(configuraciones)
            exit()
        else:
            print("Opcion no valida")


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

    Args:
        fixture (list): lista de listas, cada una con los partidos de una fecha
    """

    print("\n=== Menú del Fixture ===")
    print("A. Ver Fecha en Especifico")
    print("B. Ver fixture completo")
    print("C. Atras")
    opcion = input("Elegí una opción: ")
    if opcion.lower() == "a":
        fecha_especifica = int(input("Indique la fecha especifica: "))
        while fecha_especifica > len(fixture) or fecha_especifica < 1:
            print("Fecha no válida")
            fecha_especifica = int(input("Indique la fecha especifica: "))
        print()
        print(f"\nFecha {fecha_especifica}".upper())
        for partido in fixture[fecha_especifica-1]:
            print(f"{partido[0]} vs {partido[1]}")
        print()
    elif opcion.lower() == "b":
        for numero_fecha, fecha in enumerate(fixture, start=1):
            print(f"Fecha {numero_fecha}:".upper())
            for local, visitante in fecha:
                print(f"  {local} vs {visitante}")
            print("-" * 20)
    elif opcion.lower() == "c":
        return
    else:
        print("Opcion no valida")


def simular_fecha(fecha_actual, fixture, matriz_posiciones, usuario):

    """
    Simula los eventos de una fecha de torneo, actualizando las posiciones y generando reportes.

    Args:
        fecha_actual (int): Número de la fecha actual en el torneo.
        fixture (list): Lista de listas, cada una con los partidos programados para una fecha.
        matriz_posiciones (list): Matriz de posiciones del torneo.
        usuario (dict): Información del usuario actual.

    Returns:
        list: Matriz de posiciones actualizada tras la simulación de la fecha.
    """

    print(f"\n=== FECHA {fecha_actual+1} ===")

    eventos = []
    titulares_local = []
    titulares_visitante = []

    i = 0
    for partido in fixture[fecha_actual]:
        resultados_partido = simular_resultado_partido(partido)
        actualizar_matriz_posiciones(matriz_posiciones, resultados_partido)
        eventos = simular_eventos(
            fixture[fecha_actual][i], fecha_actual+1, resultados_partido["local"][1])
        titulares_local, titulares_visitante = procesar_equipos(
            fixture[fecha_actual][i], BBDD_JUGADORES)
        asignar_eventos(titulares_local, titulares_visitante,
                        eventos, id_eventos, fecha_actual+1)
        i += 1

    reporte_maximos_eventos()

    calcular_puntos_fecha(fecha_actual+1)

    imprimir_equipo_platilla(usuario, BBDD_JUGADORES)
    # 1. Actualizar posiciones
    actualizar_posiciones(matriz_posiciones)

    return matriz_posiciones


lista_equipos = registro_de_equipos(BBDD_JUGADORES)
fixture = generar_fixture_ida_vuelta(lista_equipos)

matriz_posiciones = configuraciones.get("matriz_posiciones")
if matriz_posiciones is None or len(matriz_posiciones) == 0:
    matriz_posiciones = crear_matriz_posiciones(lista_equipos)
    configuraciones["matriz_posiciones"] = matriz_posiciones
else:
    matriz_posiciones = convertir_str_a_matriz(
        configuraciones["matriz_posiciones"], True)

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    main()
