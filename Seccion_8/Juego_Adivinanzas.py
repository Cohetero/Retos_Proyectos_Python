"""
    Crear un juego donde el jugador debe adivinar un numero secreto.
    Puedes usar un ciclo while hasta que el jugador adivine correctamente.
    El numero secreto se puede crear usando la funsion randint para generar un valor
    aleatorio ente 1 y 50
    Por cada intento fallido se debe incrementar una variabke que lleve el conteo de intentos.
    El programa debe orientar al jugador indicandole si el valor que proporciono fue mayor
    o menor que el numero secreto
    Finalmente si adivina el numero secerto debe felicitar al usuario e indicar cuantos
    intentos realizo.
    Opcionalmente, se puede limitar el juego a un numero de intentos maximo de lo contrario
    termina el juego
"""

from random import randint
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
DIFICULTADES = {
    1: ("Facil (sin limite)", None), # Sin limite
    2: ("Media", 10),
    3: ("Dificil", 5),
    4: ("Hardcore", 3),
}
MAX = 50
MIN = 1

def limpiar_pantalla():
    os.system("cls" if os.name == 'nt' else "clear")

def pedir_valor() -> int:
    while True:
        valor = input(f"{MAGENTA}Ingrese un valor: {RESET}")
        if valor.isdigit():
            return int(valor)
        print(f"{ROJO}Ingrese un valor numerico positivo{RESET}")

def elegir_dificultad() -> int:
    while True:
        print(f"{AMARILLO}{" Dificultad ":*^100}{RESET}")

        for clave, (nombre, intentos) in DIFICULTADES.items():
            print(f"{AMARILLO}{clave}. {nombre} ({intentos} intentos){RESET}")

        opcion = pedir_valor()
        if opcion in DIFICULTADES:
            return DIFICULTADES[opcion][1]
        print(f"{ROJO}\nIngrese una opcion valida..{RESET}")

def main():
    limpiar_pantalla()
    print(f"{AZUL}{" Juego de Adivinar el Numero ":=^80}{RESET}\n")

    dificultad = elegir_dificultad()
    numero_secreto = randint(MIN, MAX)
    intentos = 0

    while True:
        limpiar_pantalla()
        if dificultad is not None:
            print(f"{AMARILLO}\nNumeros de intentos restantes: {dificultad - intentos}...\n{RESET}")
            if intentos >= dificultad:
                print(f"{AZUL}\nTe has quedado sin intentos. El numero secreto era: {numero_secreto}{RESET}")
                break
                
        print(f"{MAGENTA}El numero secerto esta entre {MIN} y {MAX}{RESET}")
        numero = pedir_valor()
        intentos += 1

        if numero == numero_secreto:
            print(f"{VERDE}Felicidades!!! adivinaste el numero secreto\ncon {intentos+1} intentos{RESET}")
            break

        menor_mayor = "menor" if numero > numero_secreto else "mayor"
        print(f"{AMARILLO}\nEl numero secreto es {menor_mayor}...{RESET}")
        input("Enter para continuar...")
        

if __name__ == "__main__":
    main()