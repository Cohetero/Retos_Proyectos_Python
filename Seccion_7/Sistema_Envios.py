# Crea un programa pra determinar el cosot de envio de un paquete segun el destino
# (nacional o internacional) y el peso del paquete.
#                      |--> Nacional = 10 x kilo
#       Costo Tarifas---
#                      |--> Internacional = 20 x kilo
# El programa debe solicitar 2 valores:
#       1. Destino (nacional o internacional)
#       2. Peso (kilogramos) del paquete
# Al final debe imprimir el costo de envio del paquete

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

TARIFAS_ENVIO = {
    "nacional": {
        "tarifa_por_kg": 10,
        "descripcion": "Envio dentro del pais"
    },
    "internacional": {
        "tarifa_por_kg": 20,
        "descripcion": "Envio fuera del pais"
    }
}

def pedir_opcion_destino() -> str:
    print(f"{MAGENTA}Tipos de destino disponibles:{RESET}")
    for clave, datos in TARIFAS_ENVIO.items():
        print(f"  → {clave.title():<15} - {datos['descripcion']} ({VERDE}${datos['tarifa_por_kg']}/kg{RESET})")
    while True:
        opcion = input(f"{MAGENTA}Seleccione el tipo de destino:{RESET} ").strip().lower()
        if opcion in TARIFAS_ENVIO:
            return opcion
        print(f"{ROJO}❌ Opción invalida. Escribe 'nacional' o 'internacional'.{RESET}")

def pedir_peso() -> float:
    while True:
        entrada = input(f"{MAGENTA}Ingrese el peso del paquete en kilogramos:{RESET} ").strip()
        try:
            peso = float(entrada)
            if peso > 0:
                return peso
            print(f"{AMARILLO}⚠️ El peso debe ser mayor a cero.{RESET}")
        except ValueError:
            print(f"{ROJO}❌ Ingrese un numero válido para el peso.{RESET}")

def calcular_total(destino: str, peso: float) -> float:
    tarifa = TARIFAS_ENVIO[destino]["tarifa_por_kg"]
    return peso * tarifa

print(f"{CYAN}{' Sistema de Envios ':*^80}{RESET}")
destino = pedir_opcion_destino()
peso = pedir_peso()
costo = calcular_total(destino, peso)

print()
print(f"{VERDE}✅ Detalle del Envio:{RESET}")
print(f"  • Tipo de envio: {destino.title()} - {TARIFAS_ENVIO[destino]['descripcion']}")
print(f"  • Peso del paquete: {peso:.2f} kg")
print(f"  • Costo total: {VERDE}${costo:,.2f}{RESET}")