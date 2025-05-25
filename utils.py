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