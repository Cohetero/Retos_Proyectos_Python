from .errores import CampoVacioError, FechaInvalidaError
from .constantes import *

from datetime import datetime

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

def validar_fecha(formato: str) -> datetime:
    while True:
        try:
            fecha = input(f"{MAGENTA}Fecha{RESET} {AMARILLO}({formato}): {RESET}").strip()
            fecha_conversion = datetime.strptime(fecha, formato)
            try:
                if datetime.now() < fecha_conversion:
                    return fecha_conversion
                else:
                    raise FechaInvalidaError(fecha_conversion)
            except FechaInvalidaError as e:
                print(f"{ROJO}{e}{RESET}")
        except ValueError:
            print(f"{ROJO}ERROR: Formato de cadena invalido{RESET}")

def validar_si_no(msg: str) -> bool:
    while True:
        busqueda = input(f"{MAGENTA}{msg}{RESET} (Si/No): ").strip().lower()
        if busqueda in ("si", "no"):
            return True if busqueda == "si" else False
        else:
            print(f"{AMARILLO}Solo se aceptan respuesta si o no...{RESET}")
