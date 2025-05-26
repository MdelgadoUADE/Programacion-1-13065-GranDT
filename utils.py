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