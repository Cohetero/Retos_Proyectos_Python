from .errores import CampoVacioError, FechaInvalidaError
from .constantes import *

from datetime import datetime

import os

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def pausar():
    input("\nEnter para continuar...\n")

def validar_entero(msg: str) -> int:
    while True:
        try:
            opcion = int(input(f"{MAGENTA}{msg}:{RESET} ").strip())
            return opcion
        except ValueError:
            print(f"{ROJO}\nIntroduzca un numero valido...{RESET}")

def validar_texto(msg: str) -> str:
    while True:
        try:
            texto = input(f"{MAGENTA}{msg}:{RESET} ").strip()
            if texto:
                print("\n")
                return texto
            else:
                raise CampoVacioError("Error: no se puede dejar vacío el campo...")
        except CampoVacioError as e:
            print(f"{ROJO}{e}{RESET}")

def validar_fecha() -> datetime:
    while True:
        try:
            fecha = input(f"{MAGENTA}Fecha{RESET} {AMARILLO}(YYYY-MM-DD HH:MM): {RESET}").strip()
            fecha_conversion = datetime.strptime(fecha, FORMATO_FECHA)
            try:
                if datetime.now() < fecha_conversion:
                    return fecha_conversion
                else:
                    raise FechaInvalidaError(fecha_conversion)
            except FechaInvalidaError as e:
                print(f"{ROJO}{e}{RESET}")
        except ValueError:
            print(f"{ROJO}ERROR: Formato de cadena invalido{RESET}")