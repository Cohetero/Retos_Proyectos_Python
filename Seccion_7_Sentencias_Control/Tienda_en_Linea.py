# Crear un sistema que ofrezca descuentos dependiendo el monto de la compra,
# o si es miembro de la tienda.
# Se deben revisar las siguientes condiciones:
#       1. Si ha comprado mas de  $1000 y es miembro -> Descuento de 10%
#       2. Si solo es miembro de la tienda -> Descuento del 5%
#       3. Si no es miembro ni compro mas de  $1000 -> Decuento del 0%

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

def pedir_cifra(campo: str) -> float:
    while True:
        try:
            valor = float(input(f"{AZUL}{campo}:{RESET} ").strip())
            if valor > 0:
                return valor
            print(f"{ROJO}❌ El valor debe ser mayor que cero.{RESET}")
        except ValueError:
            print(f"{ROJO}❌ Ingresa un numero válido.{RESET}")

def pedir_dato(campo: str) -> bool:
    while True:
        valor = input(f"{AZUL}{campo} (Si/No):{RESET} ").strip().lower()
        if valor in ("si", "s"):
            return True
        elif valor in ("no", "n"):
            return False
        print(f"{AMARILLO}⚠️ Responde con 'Si' o 'No'.{RESET}")

def calcular_descuento(compra: float, es_miembro: bool) -> float:
    if compra > 1000 and es_miembro:
        return 10
    elif es_miembro:
        return 5
    return 0


compra = pedir_cifra("Cuanto fue de total su compra? ")
es_miembro = pedir_dato("Es miembro? ")

porcentaje = calcular_descuento(compra, es_miembro)
descuento = compra * porcentaje /100
precio_final = compra - descuento

print(f"\n{CYAN}Decuento aplicado: {porcentaje}%{RESET}")
print(f"{VERDE}Total a pagar: ${precio_final:,.2f}{RESET}")



