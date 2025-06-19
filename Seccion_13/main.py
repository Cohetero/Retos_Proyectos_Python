from rectangulo import Rectangulo
from cuadrado import Cuadrado
from constantes import *

import os

def limpiar_pantalla():
    os.system("cls" if os.name == 'int' else "clear")

def menu():
    print(f"{CYAN}{" Testeo de Figuras ":=^80}{RESET}")
    print(f"""{AMARILLO}Menu{RESET}
        1. Area de Cuadrado
        2. Area de Rectangulo
        3. Nuevos valores para el Cuadrado
        4. Nuevos valores para el Rectangulado
        5. Salir""")

def validar_dato(msg: str) -> int:
    while True:
        valor = input(f"{MAGENTA}{msg}{RESET}").strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(f"{ROJO}Tiene que ser un valor numerico...{RESET}")


if __name__ == "__main__":
    print("Cuadrado")
    lado = validar_dato("Introduzca un valor numerico: ")
    color = input("Color: ").strip()
    c1 = Cuadrado(lado, color)

    print("Rectangulo")
    base = validar_dato("Introduzca un valor numerico: ")
    altura = validar_dato("Introduzca un valor numerico: ")
    color = input("Color: ").strip()
    r1 = Rectangulo(base, altura, color)

    while True:
        limpiar_pantalla()
        menu()
        opcion = validar_dato("> ")

        match opcion:
            case 1:
                print(f"{CYAN}\nArea de Cuadrado\n{RESET}")
                print(c1)
                c1.area()

            case 2:
                print(f"{CYAN}\nArea de Rectangulo\n{RESET}")
                print(r1)
                r1.area()

            case 3:
                print(f"{CYAN}\nNuevos valores para el Cuadrado\n{RESET}")
                lado = validar_dato("Introduzca un valor numerico: ")
                c1.ancho = c1.alto = lado

            case 4:
                print(f"{CYAN}\nNuevos valores para el Rectangulado\n{RESET}")
                base = validar_dato("Introduzca un valor numerico: ")
                altura = validar_dato("Introduzca un valor numerico: ")
                r1.ancho = base
                r1.alto = altura

            case 5:
                print(f"{CYAN}\nHasta Luego!!!\n{RESET}")

            case _:
                print(f"{AMARILLO}\nOpcion invalida...\n{RESET}")

        if opcion == 5:
            break
        input("\nEnter para continuar...\n")