#SEGUNDA ENTREGA, EQUIPO GRANDT
#SEBASTIAN PENZA, MATIAS DELGADO, NICOLAS LOVERA

# IMPORTACIONES
import random
import json
from utils import *

try:
  contenido = open("data/jugadores_actualizados.json", "r", encoding="utf8") #Encoding añadido debido a error extraño con json
  jugadores = contenido.read()

  BBDD_JUGADORES = json.loads(jugadores)
  BBDD_JUGADORES = {int(k): v for k, v in BBDD_JUGADORES.items()}

except Exception as e:
  registrar_excepciones(e)

else:
  contenido.close()

# DEFINICIONES
"""
ARMADO DE JUGADORES
Matriz [
jugador [nombre, equipo, titulares, nro capitan, puntos, presupuesto]
]

"""
try:
  with open('data/usuarios.txt', 'w') as archivo:
     if len(archivo) == 0:
        pass # anadir funcion para agregar usuarios
     else:
        pass # anadir funcion de menu de usuarios
except Exception as e:
   registrar_excepciones(e)


diccionario_jugadores_test = {
   "matias delgado":{
      "equipo":set(),
      "titulares":set(),
      "nro_capitan":0,
      "puntos":0,
      "presupuesto":10000000
   }
}


matriz_jugadores = [
   ["Matias Delgado",set(),set(),0,0,10000000],
   ["Nicolas Lovera",set(),set(),0,0,10000000],
   ["Sebastian Penza",set(),set(),0,0,10000000],
   ["Ronaldinho",set(),set(),0,0,10000000]
]

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
def print_menu_principal(nombre_usuario):
  print("\nGRAN DT\n" ,f"Bienvenido {nombre_usuario}\n")
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
  "D. Menu anterior"
  )

def print_menu_torneo():
  print("---------------\nMENU TORNEO\n---------------")
  print("Por favor selecciona una opcion:\n",
  "A. Jugar proxima fecha\n",
  "B. Ver fixture\n",
  "C. Salir",
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
  """Yo soy el alfa y el omega, el principio y el fin"""
  try:
    with open('data/usuarios.txt', 'w') as archivo:
      if len(archivo) == 0:
        pass # anadir funcion para agregar usuarios
      else:
        pass # anadir funcion de menu de usuarios
  except Exception as e:
    registrar_excepciones(e)
   
def registro_de_equipos(jugadores):
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
  """Codigo que permite la funcionalidad de añadir jugadores al equipo

  Args:
      usuario (list): [id_equipo, lista_jugadores, nro_capitan, puntos, presupuesto]

  Returns:
      usuario (list): [id_equipo, lista_jugadores, nro_capitan, puntos, presupuesto]
  """
  presupuesto_disponible = usuario["presupuesto"] #variable auxiliar
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
       print(f"")

def eliminar_jugadores(usuario):
  while True:
    if len(usuario[1]) == 0:
      print("\nEquipo sin jugadores")
      input("Presione enter para continuar")
      return usuario
    
    print("Por favor seleccione el jugador a eliminar usando el ID (primera parte):")
    for jugador in usuario[1]:
      print(f"{jugador} - {BBDD_JUGADORES[jugador]["nombre"]} {BBDD_JUGADORES[jugador]["apellido"]}")

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
      return usuario

def logica_menu_torneo(usuario):
  while True:
    print_menu_torneo()
    seleccion = input("> ").lower()
    if seleccion == "a":
      resultado = simular_partido(fixture[0][0], lista_jugadores)
      matriz_posiciones = crear_matriz_posiciones(lista_equipos)
      matriz_posiciones = rellenar_equipos_matriz(lista_equipos,matriz_posiciones)
      matriz_posiciones = actualizar_matriz_posiciones(matriz_posiciones,resultado)
      imprimir_matriz_posiciones(matriz_posiciones)
    elif seleccion == "b":
      ver_fixture(fixture)
    elif seleccion == "c":
      return usuario
    else:
      print("Opcion no valida")

def logica_menu_equipo(usuario):
  while True:
    print_menu_equipo()
    seleccion = input("> ").lower()
    if seleccion == "a":
      print_equipo(usuario[1])
    elif seleccion == "b":
      usuario = añadir_jugadores(usuario)
    elif seleccion == "c":
      eliminar_jugadores(usuario)
    elif seleccion == "d":
      return usuario
    else:
      print("Opcion no valida")

def logica_menu_principal(usuario):
  while True:
    print_menu_principal(usuario[0])
    seleccion = input("> ").lower()
    if seleccion == "a":
      logica_menu_equipo(usuario)
    elif seleccion == "b":
      logica_menu_torneo(usuario)
    #elif seleccion == "c":
     # print("Funcionalidad no añadida")
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

def generar_fixture_ida_vuelta(equipos):
    cantidad_equipos = len(equipos)
    mitad = cantidad_equipos // 2
    fechas_ida = []
    fechas_vuelta = []
    for ronda in range(cantidad_equipos - 1):
        fecha = []
        for i in range(mitad):
            local = equipos[i]
            visitante = equipos[-i-1]
            fecha.append((local, visitante))
        fechas_ida.append(fecha)
        # Vuelta: se invierten los roles de local y visitante
        fechas_vuelta.append([(v, l) for (l, v) in fecha])
        # Rotar los equipos (excepto el primero)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    fixture_completo = fechas_ida + fechas_vuelta
    return fixture_completo


def menu_torneo(fixture):
    while True:
        print("\n=== Menú de Torneo ===")
        print("1. Jugar próxima fecha")
        print("2. Ver fixture")
        print("3. Atras")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            menu_torneo()


        elif opcion == "2":
            ver_fixture(fixture)
        elif opcion == "3":
            print("Saliendo del torneo...")
            break 
        else:
            print("Opción inválida.")
            menu_torneo()


def ver_fixture(fixture):
    print("\n=== Menú del Fixture ===")
    print("1. Ver Fecha en Especifico") 
    print("2. Ver fixture completo")
    print("3. Atras") 
    opcion = input("Elegí una opción: ")
    if opcion == "1":
        fecha_especifica=int(input("Indique la fecha especifica: "))
        while fecha_especifica < 1 or fecha_especifica > 37:
           print("Error, fecha inexistente, intente nuevamente")
           fecha_especifica=int(input("Indique la fecha especifica: "))
        print()
        print(f"\nFecha {fecha_especifica}".upper())
        for partido in fixture[fecha_especifica]:
            print(f"{partido[0]} vs {partido[1]}")
        print()
    elif opcion=="2":
        for numero_fecha, fecha in enumerate(fixture, start=1):
            print(f"Fecha {numero_fecha}:".upper())
            for local, visitante in fecha:
                print(f"  {local} vs {visitante}")
            print("-" * 20)
    else:
        menu_torneo(fixture)

def simular_partido(fixture, jugadores):
  titulares_local = []
  titulares_visitante = []
  partido_final = []
  partido_local = []
  partido_visitante = []
  resultados_partidos = {}

  local, visitante = fixture

        # Simula resultado final
  casos = ["gana", "pierde", "empata"]
  resultado_local = random.choice(casos)
  if resultado_local == "gana":
      resultado_visitante = "pierde"
  elif resultado_local == "pierde":
      resultado_visitante = "gana"
  else:
    return False



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

def calcular_eventos_partido(eventos):
  #eventos_x_partido = []
  goles = random.randint(0, 4)
  penales = random.randint(0, 2)
  asistencias = goles
  t_amarillas = random.randint(0, 2)
  t_rojas = random.randint(0, 1)
  goles_totales = goles + penales
  
  print("\nGoles:",goles)
  print("Penales:",penales)
  print("Asistencias:",asistencias)
  print("Tarjetas Amarillas:",t_amarillas)
  print("Tarjetas Rojas:",t_rojas)
  print("Goles en el encuentro:", goles_totales)
  input("\nPresione enter para continuar\n")

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
        
        # Asignacion random de eventos por posicion. Goles a Delanteros, Asistencias a Mediocampistas, etc...
  '''for jugador in titulares_local:
      if titulares_local[-1] == "Delantero": # Slice de listas?
          partido_local.append([])'''
  

  return resultados_partidos


def crear_matriz_posiciones(equipos):
    filas=(len(equipos))
    columnas = 4 #equipo ganados perdidos puntosTotales
    matriz = [[0]*columnas for i in range(filas)]
    return matriz

def rellenar_equipos_matriz(lista_equipos,matriz_posiciones):
    filas = len(matriz_posiciones)
    columnas = len(matriz_posiciones[0])
    for f in range(filas):
        for c in range(columnas):
            matriz_posiciones[f][0] = lista_equipos[f]
    return matriz_posiciones

def actualizar_matriz_posiciones(matriz_posiciones, resultados_partido):
    for equipo, resultado in resultados_partido.values():
        for fila in matriz_posiciones:
            if fila[0] == equipo:
                if resultado == "gana":
                    fila[1] += 1  # Ganados
                    fila[3] += 3  # Puntos totales
                elif resultado == "pierde":
                    fila[2] += 1  # Perdidos
                elif resultado == "empata":
                    fila[3] += 1 # (1 punto por empate)
                break
    return matriz_posiciones

def imprimir_matriz_posiciones(matriz_posiciones):
    print("----------TABLA DE POSICIONES----------")
    print("Equipo\tPG\tPP\tPts")
    filas = len(matriz_posiciones)
    columnas = len(matriz_posiciones[0])
    for f in range(filas):
        for c in range(columnas):
            print(str(matriz_posiciones[f][c]),end='   ')
        print()
    input("\nPresione enter para continuar\n")

def fecha_actual_partidos(fecha,fixture): # fecha deberia ser la fecha actual de la instancia del programa
    fecha_actual = fecha
    for partido in fixture[fecha_actual]:
        simular_partido(partido)
    fecha_actual= fecha_actual+1
    return fecha_actual

# PROGRAMA PRINCIPAL


lista_equipos = registro_de_equipos(BBDD_JUGADORES)
fixture = generar_fixture_ida_vuelta(lista_equipos)
logica_menu_principal(matriz_jugadores[0])

if __name__ == "__main__":
  main()