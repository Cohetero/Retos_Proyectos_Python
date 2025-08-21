from .constantes import *

import os

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def pausar():
    input("\nEnter para continuar...\n")

def validar_entero(msg: str, r_min: int, r_max: int, validar_rango: bool) -> int:
    while True:
        try:
            opcion = int(input(f"{MAGENTA}{msg}:{RESET} ").strip())
            if validar_rango:
                if r_min <= opcion <= r_max:
                    return opcion
                else:
                    print(f"{ROJO}\nEl valor tiene que estar entre el rango {r_min} - {r_max}...{RESET}")
            else:
                return opcion
        except ValueError:
            print(f"{ROJO}\nIntroduzca un numero valido...{RESET}")