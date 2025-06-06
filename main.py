#SEGUNDA ENTREGA, EQUIPO GRANDT
#SEBASTIAN PENZA, MATIAS DELGADO, NICOLAS LOVERA

# IMPORTACIONES
import re
import random
import json
from json.decoder import JSONDecodeError
from utils import *
from tablaPosiciones import *


try:
  contenido = open("data/jugadores_actualizados.json", "r", encoding="utf8") #Encoding añadido debido a error extraño con json
  jugadores = contenido.read()

  BBDD_JUGADORES = json.loads(jugadores)
  BBDD_JUGADORES = {int(k): v for k, v in BBDD_JUGADORES.items()} #conversion de numeros de string a enteros

except FileNotFoundError as error:
      print("No se pudo encontrar el archivo", error)
    
except Exception as error:
        print("Error: ", error)
    
finally:
    try: #bloque protegido por si se intenta cerrar un archivo que no se consiguio abrir.
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
eventos = {
    0: {"titulo": "Partido Ganado", "puntaje_asociado": ""},
    1: {"titulo": "Partido Empatado", "puntaje_asociado": ""},
    2: {"titulo": "Partido Perdido", "puntaje_asociado": ""},
    3: {"titulo": "Gol", "puntaje_asociado": 6},
    4: {"titulo": "Penal", "puntaje_asociado": 6},
    5: {"titulo": "Asistencia", "puntaje_asociado": 3},
    6: {"titulo": "Tarjeta Amarilla", "puntaje_asociado": -2},
    7: {"titulo": "Tarjeta Roja", "puntaje_asociado": -4}   
}

#---------------------------------------------
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
  print(f"Bienvenido {nombre_usuario}\n")
  print("---------------\nMENU PRINCIPAL\n---------------")
  print("Por favor seleccione una opcion:\n",
  "A. Menu de Equipo\n",
  "B. Menu de Torneo\n",
  #"C. Cambiar de Usuario\n",
  "C. Salir",
  )

def print_menu_equipo():
  print("---------------\nMENU EQUIPO\n---------------")
  print("Por favor selecciona una opcion:\n",
  "A. Ver Equipo\n",
  "B. Añadir Jugadores\n",
  "C. Remover Jugadores\n",
  #"D. Asignar Capitan\n",
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
      print(f"{datos_jugador['nombre']} {datos_jugador['apellido']} - Posicion: {datos_jugador['posicion']}")
    input("\nPresione enter para continuar")
#---------------------------------------------
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
    with open ("data/usuarios.json", "w") as contenido:
      json.dump(registrar_usuario(), contenido, indent=4)

    main()

  except Exception as e:
    registrar_excepciones(e)
        
   
def registrar_usuario():
  print("Por favor ingrese el nombre de usuario a agregar:")
  nombre = input("> ")
  usuario = {
     nombre:{
        "nom_usuario":nombre,
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
      with open ("data/usuarios.json", "w") as contenido:
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
  equipos=[]
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
  print("Hay varios jugadores con el mismo apellido","\nPor favor indique el id del jugador a anadir:\n", end="")
  for jugador in lista_jugadores:
    print(f"{jugador} - {BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")

  while True:
    respuesta = int(input("> "))
    if respuesta in lista_jugadores:
      print(f"Jugador {BBDD_JUGADORES[respuesta]['nombre']} {BBDD_JUGADORES[respuesta]['apellido']} anadido al equipo")
      return [respuesta]
    else:
      print("Id incorrecto, intente nuevamente")

def añadir_jugadores(usuario):
  pass

def seleccion_de_busqueda():
  #nombre apellido
  #posicion
  #equipo
  #costo

#def busqueda_nom_apellido(nom_buscado):
#  for jugador in BBDD_JUGADORES:
#    pass

# def añadir_jugadores(usuario):
  """Codigo que permite la funcionalidad de añadir jugadores al equipo

  Args:
      usuario (list): [id_equipo, lista_jugadores, nro_capitan, puntos, presupuesto]

  Returns:
      usuario (list): [id_equipo, lista_jugadores, nro_capitan, puntos, presupuesto]
  """
  """presupuesto_disponible = usuario["presupuesto"] #variable auxiliar
  jugadores_seleccionados = set()

  # lambdas para obtener datos especificos de la BBDD
  nom_jugador = lambda id_jugador : f"{BBDD_JUGADORES[id_jugador]['nombre']} {BBDD_JUGADORES[id_jugador]['apellido']}"
  precio_jugador = lambda id_jugador : BBDD_JUGADORES[id_jugador]['costo']

  while True:
    
    lista_jugadores = []
    # anadir seleccion de jugadores por tipo especificado (apellido, nombre, posicion, equipo)
    print("Porfavor indique el apellido del jugador a anadir:")
    apellido = input("> ").lower()
    for i in range(1, len(BBDD_JUGADORES)): #Revisa todos los jugadores y anade todos los que tengan el apellido indicado
      if BBDD_JUGADORES.get(i)['apellido'].lower() == apellido and i not in usuario["equipo"]:
        lista_jugadores.append(i)
      
    if len(lista_jugadores) == 0:
      print("Jugador no encontrado")

    elif len(lista_jugadores) > 1: #Si hay mas de un jugador con el mismo apellido activa la funcion selecion_jugadores_id
      lista_jugadores = seleccion_jugadores_id(lista_jugadores)
      usuario["equipo"].add(lista_jugadores[0])

    else:
      if presupuesto_disponible - precio_jugador(lista_jugadores[0]) < 0: #Si hay suficiente presupuesto pregunta si desea anadir el jugador
        print(f"\nEl jugador {nom_jugador(lista_jugadores[0])} cuesta {precio_jugador(lista_jugadores[0])}")
        print("Presupuesto actual:", presupuesto_disponible)
        print("Presupuesto futuro:", presupuesto_disponible - precio_jugador(lista_jugadores[0]))
        
        if confirmar_seleccion(None):
          print(f"Jugador {nom_jugador(lista_jugadores[0])} añadido al equipo")
          jugadores_seleccionados.add(lista_jugadores[0])
          presupuesto_disponible -= precio_jugador(lista_jugadores[0]) 
      else:
         print("\nNo hay suficiente presupuesto para anadir el jugador")
         input("Presione enter para continuar")

    if confirmar_seleccion("\nDesea anadir otro jugador?"):
      if len(jugadores_seleccionados) + len(usuario[1]) >= 15:
        print("\nEquipo lleno")
        input("Presione enter para continuar")
        usuario["equipo"] = jugadores_seleccionados | usuario[1]
        usuario["presupuesto3" \
        ""] = presupuesto_disponible
        return usuario
    else:
      usuario[1] = jugadores_seleccionados | usuario[1]
      usuario[5] = presupuesto_disponible
      return usuario
    
    print("Jugadores actualmente seleccionados:")
    for jugador in jugadores_seleccionados:
       print(f"")"""

"""def eliminar_jugadores(usuario):
  while True:
    if len(usuario[1]) == 0:
      print("\nEquipo sin jugadores")
      input("Presione enter para continuar")
      return usuario
    
    print("Por favor seleccione el jugador a eliminar usando el ID (primera parte):")
    for jugador in usuario[1]:
      print(f"{jugador} - {BBDD_JUGADORES[jugador]['nombre']} {BBDD_JUGADORES[jugador]['apellido']}")

    respuesta = int(input("> "))
    if respuesta in usuario[1]:
      usuario[1].remove(respuesta)
      print(f"Jugador {BBDD_JUGADORES[respuesta]['nombre']} {BBDD_JUGADORES[respuesta]['apellido']} eliminado del equipo")
    else:
      print("Id incorrecto")

    print("Desea eliminar otro jugador? (S/N)")
    respuesta = input("> ").lower()

    while respuesta != "s" and respuesta != "n":
      print("\nRespuesta no valida\n")
      print("Desea eliminar otro jugador? (S/N)")
      respuesta = input("> ").lower()

    if respuesta == "n":
      return usuario
    
    if respuesta == "s" and len(usuario[1]) == 0:
      print("Equipo sin jugadores")
      return usuario"""

def logica_menu_usuarios(dic_usuarios):
  while True:
    print_menu_usuarios()
    seleccion = input("> ").lower()
    if seleccion == "a":
      usuario = seleccionar_usuario()
      if usuario != None:
        logica_menu_principal()
    elif seleccion == "b":
      with open ("data/usuarios.json", "w") as contenido:
        dic_usuarios.update(registrar_usuario())
        json.dump(dic_usuarios, contenido, indent=4)
    elif seleccion == "c":
      remover_usuario()
    elif seleccion == "d":
      return
    else:
      print("Opcion no valida")

def logica_menu_torneo(usuario,fixture):
  while True:
    print_menu_torneo()
    seleccion = input("> ").lower()
    if seleccion == "a":
      resultado = simular_partido(fixture[0][0], lista_jugadores)
      actualizar_y_guardar_tabla_posiciones(matriz_posiciones,resultado)
    elif seleccion == "b":
      ver_fixture(fixture,usuario)
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
      logica_menu_torneo(usuario,fixture)
    #elif seleccion == "c":
      logica_menu_usuarios()
    elif seleccion == "c":
      return
    else:
      print("Opcion no valida")

def registro_de_jugadores(jugadores):       # Me devuelve los datos de los jugadores cargados en una tupla
  players=[]
  for clave,valor in jugadores.items():
    id_jugador = clave
    equipo = valor["id_equipo"]
    nombre = valor["nombre"]
    apellido = valor["apellido"]
    posicion = valor["posicion"]

    players.append((id_jugador, equipo, nombre, apellido, posicion))        # Datos de los jugadores
  return players

def ver_fixture(fixture,usuario):
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
        fecha_especifica=int(input("Indique la fecha especifica: "))
        while fecha_especifica < 1 or fecha_especifica > 37:
           print("Error, fecha inexistente, intente nuevamente")
           fecha_especifica=int(input("Indique la fecha especifica: "))
        print()
        print(f"\nFecha {fecha_especifica}".upper())
        for partido in fixture[fecha_especifica]:
            print(f"{partido[0]} vs {partido[1]}")
        print()
    elif opcion=="B":
        for numero_fecha, fecha in enumerate(fixture, start=1):
            print(f"Fecha {numero_fecha}:".upper())
            for local, visitante in fecha:
                print(f"  {local} vs {visitante}")
            print("-" * 20)
    else:
        logica_menu_torneo(usuario,fixture)

        
def simular_eventos(local, visitante, resultado_local):
    # Simula eventos de partido. Devuelve una lista con valores para cada evento.
  eventos = []

  goles_local = 0
  goles_visitante = 0
  if resultado_local == "gana":
      goles = random.randint(1, 4) 
      if goles % 2 == 0:
          penales = 1
          goles_totales = goles + penales
      else:
          penales = 0
      asistencias = goles
      goles_local = goles_totales - 1
      goles_visitante = 1
      eventos.append(resultado_local)
      eventos.append(goles)
      eventos.append(penales)
      eventos.append(goles_totales)
      eventos.append(asistencias)

  elif resultado_local == "empata":
      goles = random.randint(0, 2) * 2
      penales = random.randint(0, 1) * 2
      asistencias = goles
      goles_totales = goles + penales
      goles_local = goles_totales // 2
      goles_visitante = goles_totales // 2
      eventos.append(resultado_local)
      eventos.append(goles)
      eventos.append(penales)
      eventos.append(goles_totales)
      eventos.append(asistencias)

  else:
      eventos.append(resultado_local)
      eventos.append(goles)
      eventos.append(penales)
      eventos.append(goles_totales)
      eventos.append(asistencias)

  t_amarillas = random.randint(0, 2)
  #t_rojas = random.randint(0, 1)
  eventos.append(t_amarillas)
  #eventos.append(t_rojas)

  print(f"{local} {goles_local} - {visitante} {goles_visitante}")
  print("Goles:",goles)
  print("Penales:",penales)
  print("Goles en el encuentro:", goles_totales)
  print("Asistencias:",asistencias)
  print("Tarjetas Amarillas:",t_amarillas)
  #print("Tarjetas Rojas:",t_rojas)

  return eventos      # [resultado_local, goles, penales, goles_totales, asistencias, t_amarillas]

def simular_resultado_partido(local, visitante):
                  # Simula resultado final
  resultados_partidos = {}

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
  return resultados_partidos

def asignar_eventos(equipo_local, plantel_local, equipo_visitante, plantel_visitante, eventos):
# Probabilidad gol
    prob_gol = {"Defensor": 0.1, "Mediocampista": 0.2, "Delantero": 0.7}
# Probabilidad asistencia
    prob_asis = {"Defensor": 0.1, "Mediocampista": 0.7, "Delantero": 0.2}
# Probabilidad tarjeta amarilla
    prob_ta = {"Defensor": 0.6, "Mediocampista": 0.3, "Delantero": 0.1}
# Lesion es completamente random
    goles_local = 0
    goles_visitante = 0
    if eventos[0] == 'gana':
        goles_local = eventos[3] - 1
        goles_visitante = 1
    elif eventos[0] == 'pierde':
        goles_visitante = eventos[3] - 1
        goles_local = 1
    else:
        goles_visitante = eventos[3] // 2
        goles_local = eventos[3] // 2
    while goles_local != 0:
        pesos_gol = list(prob_gol.values())
        jugador = random.choices(equipo_local, weights=pesos_gol, k=1)[0]

def procesar_equipos_eventos(fixture, jugadores, eventos):
# Segmenta los equipos e invoca a la asignacion a los jugadores
  titulares_local = []
  titulares_visitante = []
  #partido_final = []
  delanteros_local = []
  medios_local = []
  defensores_local = []
  delanteros_visitante = []
  medios_visitante = []
  defensores_visitante = []
  local, visitante = fixture

# De la base de jugadores me traigo los datos del equipo local y visitante
  for jugador in jugadores:
      id_jugador, equipo, nombre, apellido, posicion = jugador
      if equipo == local:
          titulares_local.append([id_jugador, equipo, nombre, apellido, posicion])
  #print(titulares_local)
  for jugador in jugadores:
      id_jugador, equipo, nombre, apellido, posicion = jugador
      if equipo == visitante:
          titulares_visitante.append([id_jugador, equipo, nombre, apellido, posicion])
  #print(titulares_visitante)
  asignar_eventos(local, titulares_local, visitante, titulares_visitante, eventos)

# equipo local por posicion
  for jugador in titulares_local:
      if jugador[-1] == "Delantero":
          delanteros_local.append(jugador)
  #print(delanteros_local)
  for jugador in titulares_local:
      if jugador[-1] == "Mediocampista":
          medios_local.append(jugador)
  #print(medios_local)
  for jugador in titulares_local:
      if jugador[-1] == "Defensor":
          defensores_local.append(jugador)
  #print(defensores_local)

# equipo visitante por posicion
  for jugador in titulares_visitante:
      if jugador[-1] == "Delantero":
          delanteros_visitante.append(jugador)
  #print(delanteros_visitante)
  for jugador in titulares_visitante:
      if jugador[-1] == "Mediocampista":
          medios_visitante.append(jugador)
  #print(medios_visitante)
  for jugador in titulares_visitante:
      if jugador[-1] == "Defensor":
          defensores_visitante.append(jugador)
  #print(defensores_visitante)

def seleccion_de_jugadores(lista_jugadores):
  lista_de_jugadores = []
  while True:
    jugador_seleccionado = seleccionar_jugador_de_lista(ingreso_nombre(), lista_jugadores)
    if not jugador_seleccionado == None:
      if validar_seleccion(f"Desea añadir a {jugador_seleccionado[0]}?"):
        lista_de_jugadores.append(jugador_seleccionado)
      if not validar_seleccion("Desea seguir añadiendo jugadores?"):
        imprimir_equipo(lista_de_jugadores)
        return lista_de_jugadores

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
matriz_posiciones = rellenar_equipos_matriz(lista_equipos,matriz_posiciones)


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
  main()
