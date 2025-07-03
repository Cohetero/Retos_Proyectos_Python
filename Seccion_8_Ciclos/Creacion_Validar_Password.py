"""
Crear un programa para solicitar la validacion al momento de crear un valor de un password o contrseña
La contraseña debe tener al menos 6 caracteres.
En caso de no cumplir con esta condicion el programa debe volver a solicitar un nuevo valor
hasta que cumpla con la condicion
Si el valor proporcionado es valido, se debe imprimir: "Password valido" y debe terminar
la ejecucion del sistema
"""

import re

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# Constantes
MIN_LONGITUD = 6

def create_password() -> str:
    while True:
        password = input(f"{MAGENTA}Introduzca nuevo Password{RESET}\n:")
        if len(password) < MIN_LONGITUD:
            print(f"{ROJO}Eroor: el Password debe tener al menos {MIN_LONGITUD} caracteres{RESET}")
        elif not re.search(r"[A-Za-z]", password):
            print(f"{ROJO}Error: el paswoord debe tener al menos una letra{RESET}")
        elif not re.search(r"\d", password):
            print(f"{ROJO}Error: el paswoord debe tener al menos un numero{RESET}")
        else:
            return password


password = create_password()
print(f"{VERDE}Password valido{RESET}")