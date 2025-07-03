# Se solicita calcular el area y perimeto de un rectangulo aplicando las siguentes formulas:
#   area = base * altura
#   perimetro = 2 * (base + altura)

import platform
import turtle
import os

CLEAR = "cls" if platform.system() == "Windows" else "clear"

def pedir_dato(campo: str) -> float:
    while True:
        try:
            valor = float(input(f"{campo}: ").strip())
            if valor > 0:
                return valor
            print("❌ El valor debe ser mayor que cero.")
        except ValueError:
            print("❌ Ingresa un numero válido.")

def validar_opcion() -> int:
    while True:
        try:
            valor = int(input(": ").strip())
            if 1 <= valor <= 9:
                return valor
            print("❌ La opcióon debe estar entre 1 y 9.")
        except ValueError:
            print("❌ La opcion debe ser un numero entero.")

# Cálculo de área
def calcular_area(opcion: int):
    if opcion == 1:  # Rectángulo
        altura = pedir_dato("Altura")
        base = pedir_dato("Base")
        area = altura * base
    elif opcion == 3:  # Cuadrado
        lado = pedir_dato("Lado")
        area = lado * lado
    elif opcion == 5:  # Triángulo
        altura = pedir_dato("Altura")
        base = pedir_dato("Base")
        area = (altura * base) / 2
    elif opcion == 7:  # Círculo
        pi = 3.1416
        radio = pedir_dato("Radio")
        area = pi * (radio ** 2)

    return "El area", area

# Cálculo de perímetro
def calcular_perimetro(opcion: int):
    if opcion == 2:  # Rectángulo
        altura = pedir_dato("Altura")
        base = pedir_dato("Base")
        perimetro = 2 * (base + altura)
    elif opcion == 4:  # Cuadrado
        lado = pedir_dato("Lado")
        perimetro = lado * 4
    elif opcion == 6:  # Triángulo
        a = pedir_dato("Lado A")
        b = pedir_dato("Lado B")
        c = pedir_dato("Lado C")
        perimetro = a + b + c
    elif opcion == 8:  # Círculo
        pi = 3.1416
        diametro = pedir_dato("Diámetro")
        perimetro = pi * diametro

    return "El perimetro", perimetro

# Main
opcion = 0
menu = """
🟩 ¿Qué deseas calcular?

    1. Área del Rectángulo        2. Perímetro del Rectángulo
    3. Área del Cuadrado          4. Perímetro del Cuadrado
    5. Área del Triángulo         6. Perímetro del Triángulo
    7. Área del Círculo           8. Perímetro del Círculo
    9. Salir
"""
while True:
    print(menu)
    opcion = validar_opcion()

    if opcion == 9:
        print("👋 Hasta luego.")
        break

    if opcion in [1,3,5,7]:
        operacion, resultado = calcular_area(opcion)
    else:
        operacion, resultado = calcular_perimetro(opcion)

    print(f"{operacion} es de: {resultado:.2f}")
    input("Presiona Enter para continuar...")
    os.system(CLEAR)