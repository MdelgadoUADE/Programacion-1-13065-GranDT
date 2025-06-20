import json

ACENTOS = {
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}


def normalizar_acentos(string):
    string = string.lower()
    return ''.join([ACENTOS.get(c, c) for c in string])


def confirmar_seleccion(mensaje):
    """Codigo basico de validacion para confirmar una seleccion

    Args:
        mensaje (str): Mensaje a mostrar, ingresar None para mostrar mensaje defecto

    Returns:
        bool: True o False"""
    if mensaje == None:
        print("Desea continuar? (S/N)")
    else:
        print(f"{mensaje} (S/N)")
    seleccion = input("> ").lower()
    while seleccion != "s" and seleccion != "n":
        print("Opcion no valida")
        seleccion = input("> ").lower()
    if seleccion == "s":
        return True
    elif seleccion == "n":
        return False


def registrar_excepciones(e):
    """Generador de log de errores para depuracion de codigo, genera un archivo log bajo la carpeta log, nombre error_log.txt

    Args: 
        e (Exception): Excepcion a registrar
    """
    try:
        archivo = open('log/error_log.txt', 'a')
        try:
            error = f"Tipo: {type(e)} - Mensaje: {str(e)}\n"
            print(f"Ocurrio un error: {error}")
            archivo.write(error)
        finally:
            archivo.close()
    except Exception as logError:
        print(f"Error al escribir el log: {logError}")


def abrir_archivo_json(nombre_archivo, modo):
    try:
        archivo = open(nombre_archivo, modo)
        lineas = archivo.read()
        archivo.close()

        contenido = json.loads(lineas)
        return contenido

    except FileNotFoundError:
        print("No se pudo encontrar el archivo")

    except json.decoder.JSONDecodeError:
        print("No se pudo decodificar el archivo")

    except Exception as e:
        registrar_excepciones(e)


def cargar_evento(listaEvento, nroFecha):
    """
    Recibe cada lista de eventos, ya asignados, por categoria y los escribe en un archivo de salida.

    Args:
        listaEvento (list): Lista del tipo de evento para agregar al archivo.
        nroFecha (list): Numero de fecha que se va a escribir.
    """

    eventos2json = []

    for evento in listaEvento:
        eventos2json.append({
            "evento": evento[-2],
            "equipo": evento[1],
            "id_jugador": evento[0],
            "nombre": evento[2],
            "apellido": evento[3],
            "posicion": evento[4],
            "puntaje_asociado": evento[-1]
        })

    if nroFecha != 0:
        data_path = f"data/eventos{nroFecha}.txt"

    data_path = "data/eventos.txt"
    data = []

    if os.path.exists(data_path):
        try:
            with open(data_path, mode="r", encoding="UTF-8") as archivo:
                data = json.load(archivo)
        except FileNotFoundError:
            print("No se encontró el archivo.")

    data.extend(eventos2json)

    with open(data_path, mode='w', encoding='utf-8') as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)
