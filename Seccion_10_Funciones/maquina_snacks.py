"""
    Crear un programa donde podras comprar snacks de una lista inicial
    Cada snack tiene su id, nombre y precio
    Para comprar un scnack se debe indicar el id del snack a comprar y se
    agregar a una lista de productos comprados
    Ademas se debe mostrar el ticket de venta final con el total de productos
    y el total de la venta
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
    os.system("cls" if os.name == 'int' else "clear")

def menu():
    print(f"{AZUL}{" Maquina de Snacks ":=^80}{RESET}\n")
    print(f"""{AMARILLO} Menu {RESET}{RESET}
    1.- Mostrar Snacks
    2.- Comprar Snacks
    3.- Mostrar Ticket
    4.- Quitar Snack
    5.- Salir
    """)

def validar_Dato(campo: str, tipo: str | None = None) -> str | int:
    while True:
        valor = input(f"{MAGENTA}{campo}{RESET}").strip()
        if tipo == "int":
            if valor.isdigit():
                return int(valor)
            else:
                print(f"{ROJO}Debes ingresar un numero entero valido.{RESET}")
        elif tipo is None:
                return valor.upper()


def print_Snacks(snacks: list):
    if not snacks:
        print(f"{AMARILLO}No hay snacks en la Maquina..{RESET}")
        return

    print(f"{CYAN}\nSnacks en la Maquina:{RESET}")
    for snack in snacks:
        if snack.get('Cantidad') > 0:
            print(f"""{AMARILLO}ID: {snack.get('ID')} - {RESET}{VERDE}${snack.get('Precio'):,.2f}{RESET} {snack.get('Nombre')} : {snack.get('Cantidad')}""")

def comprar_Snacks(snacks: list, ticket: list):
    while True:
        limpiar_pantalla()
        print_Snacks(snacks)
        id_snack = validar_Dato("\nQue snack quiere comprar? (ID): ")

        snack_encontrado = next((s for s in snacks if s["ID"] == id_snack), None)
        if snack_encontrado:
            if snack_encontrado["Cantidad"] == 0:
                print(f"{AMARILLO}Este snack está agotado.{RESET}")
            else:
                cantidad = validar_Dato("Cuantos? ", "int")
                if snack_encontrado.get("Cantidad") >= cantidad:
                    print(f"{VERDE}Snack Agregado...{RESET}")
                    ticket.append({
                        "ID": snack_encontrado.get("ID"),
                        "Nombre": snack_encontrado.get("Nombre"),
                        "Precio": snack_encontrado.get("Precio"),
                        "Cantidad": cantidad
                    })
                    snack_encontrado["Cantidad"] -= cantidad
                else:
                    print(f"{ROJO}Solo hay {snack_encontrado["Cantidad"]} disponibles.{RESET}")
        else:
            print(f"{ROJO}ID no encontrado. Intenta nuevamente.{RESET}")

        continuar = validar_Dato("Desea comprar algo mas? ", )
        if continuar == "NO":
            break

def mostrar_Ticket(ticket: list):
    if not ticket:
        print(f"{AMARILLO}No se ha realizado ninguna compra...{RESET}")
        return

    precio_total = 0
    print(f"{CYAN}\nTicket:{RESET}")

    for snack in ticket:
        print(f"""\t{snack.get("Nombre")} : {VERDE}${snack.get("Precio"):,.2f} X {snack.get("Cantidad")}{RESET}""")
        precio_total += snack.get("Precio") * snack.get("Cantidad")
    print(f"\tPrecio Total: {VERDE}${precio_total:,.2f}{RESET}")

def eliminar_snack_Ticket(ticket: list):
    if not ticket:
        print(f"{AMARILLO}No se ha realizado ninguna compra...{RESET}")
        return

    while True:
        print(f"{CYAN}\nSnacks en tu ticket:{RESET}")
        for snack in ticket:
            print(f"""{AMARILLO}ID: {snack.get('ID')} - {RESET}{VERDE}${snack.get('Precio'):,.2f}{RESET} {snack.get('Nombre')} : {snack.get('Cantidad')}""")

        id_snack = validar_Dato("ID del snack que quiere quitar: ")
        for i, snack in enumerate(ticket):
            if id_snack == snack.get("ID"):
                confirm = validar_Dato(f"¿Eliminar {snack['Nombre']} del ticket? (Sí/No): ")
                if confirm == "SI":
                    print(f"{VERDE}Snack Eliminado del ticket...{RESET}")
                    ticket.pop(i)
                break
        else:
            print(f"{ROJO}ID no encontrado en el ticket.{RESET}")

        continuar = validar_Dato("Desea eliminar algo mas? ", )
        if continuar == "NO":
            break



def main():
    snacks = [
        {"ID": "A1", "Nombre": "Sabritas", "Cantidad": 4, "Precio": 22.50},
        {"ID": "A2", "Nombre": "Doritos", "Cantidad": 9, "Precio": 20.00},
        {"ID": "B1", "Nombre": "Cheetos", "Cantidad": 8, "Precio": 12.50},
        {"ID": "B2", "Nombre": "Takis Fuego", "Cantidad": 8, "Precio": 16.00},
        {"ID": "C1", "Nombre": "Ruffles", "Cantidad": 2, "Precio": 22.00},
        {"ID": "C2", "Nombre": "Crujitos", "Cantidad": 7, "Precio": 18.00}
    ]
    ticket = []
    opcion = 0

    while opcion != 5:
        limpiar_pantalla()
        menu()
        opcion = validar_Dato("-> ", "int")

        match opcion:
            case 1:
                print_Snacks(snacks)
            case 2:
                comprar_Snacks(snacks, ticket)
            case 3:
                mostrar_Ticket(ticket)
            case 4:
                eliminar_snack_Ticket(ticket)
            case 5:
                print(f"{MAGENTA}¡Hasta Luego!{RESET}")
                mostrar_Ticket(ticket)

        input("\nEnter para continuar...\n")


if __name__ == "__main__":
    main()