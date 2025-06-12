from Calculadora import Calculadora
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
    os.system("cls" if os.name == 'int' else "clear")

def menu():
    print(f"{AZUL}{" Calculadora ":=^80}{RESET}\n")
    print(f"""{AMARILLO} Menu de Operaciones {RESET}{RESET}
    1.- Sumar
    2.- Resta
    3.- Multiplicar
    4.- Dividir
    5.- Modulo
    6.- Nuevos Valores
    7.- Ver Historial
    8.- Borrar historial
    9.- Salir""")

def validarOpcionMenu() -> int:
    while True:
        opcion = input(f"{MAGENTA}Elige una opcion del menu: {RESET}").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= 8:
            return int(opcion)
        else:
            print(f"{ROJO}Opcion no valida, intenta de nuevo{RESET}")

def validarDato() -> float:
    while True:
        valor = input(f"{MAGENTA}Introduzca un numero: {RESET}").strip()
        try:
            return float(valor)
        except ValueError:
            print(f"{AMARILLO}Tiene que ser un numero{RESET}")

def main():
    historial = []
    operador1 = validarDato()
    operador2 = validarDato()
    cal = Calculadora(operador1, operador2)
    while True:
        limpiar_pantalla()
        menu()
        print(f"\nValores actuales: {VERDE}{cal.operador1}{RESET} y {VERDE}{cal.operador2}{RESET}")
        opcion = validarOpcionMenu()

        match opcion:
            case 1:
                print(f"\n{CYAN}SUMA{RESET}\n")
                resultado = f"{AMARILLO}{cal.operador1:,.2f} + {cal.operador2:,.2f}{RESET} = {VERDE}{cal.sumar():,.2f}{RESET}"
                historial.append(resultado)
                print(resultado)
            case 2:
                print(f"\n{CYAN}RESTA{RESET}\n")
                resultado = f"{AMARILLO}{cal.operador1:,.2f} - {cal.operador2:,.2f}{RESET} = {VERDE}{cal.restar():,.2f}{RESET}"
                historial.append(resultado)
                print(resultado)
            case 3:
                print(f"\n{CYAN}MULTIPLICAR{RESET}\n")
                resultado = f"{AMARILLO}{cal.operador1:,.2f} * {cal.operador2:,.2f}{RESET} = {VERDE}{cal.multiplicar():,.2f}{RESET}"
                historial.append(resultado)
                print(resultado)
            case 4:
                print(f"\n{CYAN}DIVIDIR{RESET}\n")
                try:
                    resultado = f"{AMARILLO}{cal.operador1:,.2f} / {cal.operador2:,.2f}{RESET} = {VERDE}{cal.dividir():,.2f}{RESET}"
                    historial.append(resultado)
                    print(resultado)
                except ZeroDivisionError as e:
                    print(f"{ROJO}{e}{RESET}")
            case 5:
                print(f"\n{CYAN}MODULO{RESET}\n")
                try:
                    resultado = f"{AMARILLO}{cal.operador1:,.2f} % {cal.operador2:,.2f}{RESET} = {VERDE}{cal.modulo():,.2f}{RESET}"
                    historial.append(resultado)
                    print(resultado)
                except ZeroDivisionError as e:
                    print(f"{ROJO}{e}{RESET}")
            case 6:
                operador1 = validarDato()
                operador2 = validarDato()
                cal.operador1 = operador1
                cal.operador2 = operador2
            case 7:
                if historial:
                    for i in historial:
                        print(i)
                else:
                    print(f"{AMARILLO}Aun no hay operaciones realizadas.{RESET}")
            case 8:
                historial.clear()
                print(f"{VERDE}Historial Borrado{RESET}")
            case 9:
                print(f"{VERDE}Hasta Luego!!!{RESET}")
                break
            case _:
                print(f"{VERDE}NO es una opcion valida{RESET}")

        input("\nEnter para continuar...\n")



if __name__ == "__main__":
    main()