"""
Crear una aplicacion de calculadora con las opcines de:
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
El programa debe mostrar un menu con cada opcion y debe solicitar los valores
de operando 1 y operando 2 para realizar la operacion seleccionada
"""

import os

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

def limpiar_pantalla():
    os.system("cls" if os.name == 'nt' else "clear")

def pedir_dato() -> float:
    while True:
        try:
            valor = float(input(f":"))
            break
        except ValueError:
            print(f"{ROJO}Debe ser un numero{RESET}")
    return valor

def realizar_operacion(operacion: str):
    operaciones = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else f"{ROJO}ERROR: division entre cero{RESET}",
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y,
    }

    print(f"{MAGENTA}Operador 1{RESET}")
    operador_1 = pedir_dato()
    print(f"{MAGENTA}Operador 2{RESET}")
    operador_2 = pedir_dato()

    if operacion in operaciones:
        resultado = operaciones[operacion](operador_1, operador_2)
        print(f"{VERDE}{operador_1:,.2f} {operacion} {operador_2:,.2f} = {resultado:,.2f}{RESET}")
    else:
        print(f"{AMARILLO}Operacion no valida{RESET}")


def mostrar_menu():
    print(f"{CYAN}{" Calculadora ":*^100}{RESET}")
    print(f"""{AZUL} Menu de Opciones{RESET}{AMARILLO}
    1.- Suma
    2.- Resta
    3.- Multiplicacion
    4.- Division
    5.- Potencia
    6.- Modulo
    7.- Salir{RESET}""")

def main():
    opcion = 0
    opciones = {
        1: ('Suma', '+'),
        2: ('Resta', '-'),
        3: ('Multiplicacion', '*'),
        4: ('Division', '/'),
        5: ('Potencia', '**'),
        6: ('Modulo', '%'),
    }

    while opcion != 7:
        mostrar_menu()

        try:
            opcion = int(input("-> "))
        except ValueError:
            print(f"{ROJO}Ingrese un numero valido...{RESET}")
            input("Enter para continuar...")
            continue

        if opcion in opciones:
            nombre, simbolo = opciones[opcion]
            print(f"{AZUL}\n{nombre}{RESET}\n")
            realizar_operacion(simbolo)

        input("Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()