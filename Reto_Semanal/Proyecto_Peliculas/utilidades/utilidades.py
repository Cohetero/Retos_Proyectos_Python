import os

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# Constantes
RUTA_PELICULAS = "datos/peliculas.json"
RUTA_PELICULAS_CSV = "datos/peliculas.csv"

def validar_dato_entrada(msg: str, type: str) -> any:
    while True:
        try:
            opcion = input(f"{MAGENTA}{msg}{RESET}").strip().lower()
            if type == "int":
                return int(opcion)
            elif type == "float":
                return float(opcion)
            elif type == "char":
                return opcion
        except ValueError:
            print(f"{ROJO}\nIntroduzca un numero valido...{RESET}")

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def pausar():
    input("\nEnter para continuar...\n")