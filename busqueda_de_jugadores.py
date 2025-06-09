import re

LISTA_DE_SHORTCUTS = {
    "-e":"id_equipo",
    "--EQUIPO":"id_equipo",
    "-p":"valor",
    "--PRECIO":"valor",
    "-n":"nombre",
    "--NOMBRE":"nombre",
    "-a":"apellido",
    "--APELLIDO":"apellido"
}
print("Consola de busqueda\ningresar '-h' para ayuda")

regex_shortcuts = re.compile(f"({'|'.join(LISTA_DE_SHORTCUTS.keys())}) ([a-zA-Z0-9]+ ?[a-zA-Z0-9]*)")

def shortcut_help(input):
    if re.search("[\-h|\-HELP]",input) != None:
        print("Bienvenido al buscador de jugadores")
        for shortcut in LISTA_DE_SHORTCUTS:
            print(f"{shortcut} \nconsigue el {LISTA_DE_SHORTCUTS[shortcut]}\n")

def shortcut_filtrado_valores(input):
    valor_encontrado = regex_shortcuts.findall(input)
    if valor_encontrado != None:
        print(valor_encontrado)
            #valores = set(filter(lambda jugador: jugador[LISTA_DE_SHORTCUTS[shortcut]] == re.search(""), BBDD_JUGADORES.values()))


while True:
    lista_devolucion = []
    valor_buscado = input("> ")
    shortcut_filtrado_valores(valor_buscado)
#print(re.search(f"({shortcut}) ([a-zA-Z]+ ?[a-zA-Z]*)","-e Velez Sarsfield"))
        

    

    