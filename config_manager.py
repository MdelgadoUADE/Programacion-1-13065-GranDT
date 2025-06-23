#Manejador de archivos de configuracion
import json
from json.decoder import JSONDecodeError
from utils import *

def definicion_usuario(nombre):
    return { nombre: {
        "nom_usuario": nombre,
        "formacion": {
            "arquero": 1,
            "defensor": 4,
            "mediocampista": 4,
            "delantero": 2
        },
        "titulares": {},
        "suplentes": {},
        "nro_capitan": 0,
        "presupuesto": 42000000,
        "puntos": 0
        }
    }

def cargar_configuracion():
    try:
        contenido = open("data/config.txt","r",encoding="utf8")
        lineas = contenido.read()
        contenido.close()
        return(procesar_configuraciones(lineas))        
    except FileNotFoundError:
        print("No se pudo encontrar el archivo")
    except Exception as e:
        registrar_excepciones(e)

def procesar_configuraciones(texto_configuraciones):
    configuraciones = texto_configuraciones.split("\n")
    for i in range(configuraciones.count("")):
        configuraciones.remove("")
    
    diccionario_configuraciones = {}
    for configuracion in configuraciones:
        configuracion = configuracion.split(":")
        diccionario_configuraciones[configuracion[0].strip()] = configuracion[1].strip()
    return diccionario_configuraciones

def guardar_configuraciones(configuraciones):

    try:
        archivo = open("data/config.txt","w",encoding="utf8")
        for configuracion in configuraciones:
            archivo.write(f"{configuracion}: {configuraciones[configuracion]}\n")
        archivo.close()
    except Exception as e:
        registrar_excepciones(e)

def restaurar_juego():
    """
    Restaura el juego a su estado inicial
    
    Incluye el archivo de configuraciones, del archivo de usuarios y el archivo de eventos
    """
    try:
        with open("data/config.txt", "w") as contenido:
            contenido.write("\n".join(["flag_end_state: False\n","flag_comienzo_torneo: False\n","fecha_actual: 0\n"]))
        usuarios = abrir_archivo_json("data/usuarios.json", "r")
        restaurar_usuarios = {}
        for usuario in usuarios:
            restaurar_usuario = definicion_usuario(usuario)
            restaurar_usuarios.update(restaurar_usuario)
        with open("data/usuarios.json", "w") as contenido:
            json.dump(restaurar_usuarios, contenido, indent=4)

        try:
            archivo_eventos = open("data/eventos.txt","r",encoding="utf8")
        except FileNotFoundError:
            pass
        else:
            with open("exports/eventos_temporada_anterior.txt", "w") as contenido:
                for linea in archivo_eventos:
                    contenido.write(linea)
            archivo_eventos.close()
            os.remove("data/eventos.txt")
        

    except FileNotFoundError as e:
        registrar_excepciones(e)
        print("No se pudo encontrar el archivo")

    except JSONDecodeError as e:
        registrar_excepciones(e)
        print("Hubo un error descodificando el JSON")

    except Exception as e:
        registrar_excepciones(e)