# Se les deja crear la aplicacion de cajero automatico,
# Las funciones principales de un cajero automatico con:
#       * Depositar
#       * Retirar
#       * Consultar el saldo
# El saldo puede tener un valor inicial por ejemplo $1000
# Si haces un retiro se resta de tu saldo y si haces un deposito
# se sumna a tu saldo.

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
INTENTOS_MAXIMOS = 3

def limpiar_pantalla():
    os.system("cls" if os.name == 'nt' else "clear")

def acceso_contrasenia(nip_cuenta: int, cliente: str)-> bool:
    limpiar_pantalla()
    print(f"{CYAN}{f" Hola {cliente} ":*^100}{RESET}")
    intentos = 0
    acceso_concedido  = False
    while intentos < INTENTOS_MAXIMOS:
        print(f"\n{AMARILLO}Intento {intentos + 1} de {INTENTOS_MAXIMOS}{RESET}")
        
        try:
            nip = int(input("NIP: "))
        except ValueError:
            print(f"{ROJO}El NIP debe ser numerico.{RESET}")
            intentos += 1
            continue

        if nip == nip_cuenta:
            acceso_concedido  = True
            break
        else:
            print(f"{ROJO}El NIP es incorrecto")

        intentos += 1

    return acceso_concedido 

def mostrar_clientes(cuentas: list) -> int:
    limpiar_pantalla()
    print(f"{CYAN}{" Cuentas Disponibles ":*^100}{RESET}")
    
    for i, cuenta in enumerate(cuentas):
        print(f"{AMARILLO}{i+1}. {cuenta['cliente']}")
    
    while True:
        try:
            id_client = int(input(": ")) - 1
            if 0 <= id_client < len(cuentas):
                break
            print(f"{AMARILLO}La opcion debe ser dentro el rango de opciones...{RESET}")
        except ValueError:
            print(f"{ROJO}Ingrese un numero valido...{RESET}")

    return id_client

def operacion_cuenta(cuenta: dict, opcion: str) -> dict:
    while True:
        try:
            monto = float(input(f"{MAGENTA}Saldo a {opcion} {RESET}$"))

            if monto <= 0:
                print(f"{AMARILLO}La cantidad debe ser positiva.{RESET}")
                continue

            if opcion == "depositar":
                if monto > 10000:
                    print(f"{AMARILLO}No se puede depositar mas de {RESET}{VERDE}$10000{RESET}")
                    continue
                cuenta['saldo'] += monto
                cuenta['historial'].append(f"{MAGENTA}Deposito de {RESET}{VERDE}${monto:,.2f}{RESET}")
                return cuenta
            elif opcion == "retirar" :
                if monto <= cuenta['saldo']:
                    if monto > 5000:
                        print(f"{AMARILLO}No se puede retirar mas de {RESET}{VERDE}$5000{RESET}")
                        continue
                    cuenta['saldo'] -= monto
                    cuenta['historial'].append(f"{MAGENTA}Retiro de {RESET}{VERDE}${monto:,.2f}{RESET}")
                    return cuenta
                else:
                    print(f"{ROJO}Saldo insuficiente para retirar.{RESET}")
            else:
                print(f"{ROJO}Operación desconocida.{RESET}")
                return cuenta
        except ValueError:
            print(f"{ROJO}Ingrese una cantidad valida...{RESET}")

def mostrar_menu():
    print(f"{CYAN}{" Cajero Automatico ":*^100}{RESET}")
    print(f"""{AZUL} Menu de Opciones{RESET}{AMARILLO}
    1.- Depositar
    2.- Retirar
    3.- Consultar Saldo
    4.- Consultar Historial
    5.- Salir{RESET}""")

def main():
    cuentas = [
        {
            "nip": 1234,
            "saldo": 1500.00,
            "cliente": "Mauricio Cohetero Baltazar",
            "historial": []
        },
        {
            "nip": 4321,
            "saldo": 5430.54,
            "cliente": "Emilia Luna Torres",
            "historial": []
        },
        {
            "nip": 3051,
            "saldo": 7450.78,
            "cliente": "Andrea Lopez Garcia",
            "historial": []
        }
    ]

    id_cliente = mostrar_clientes(cuentas)

    if acceso_contrasenia(cuentas[id_cliente]['nip'], cuentas[id_cliente]['cliente']):
        opcion = 0
        while opcion != 5:
            limpiar_pantalla()
            mostrar_menu()

            try:
                opcion = int(input("-> "))
            except ValueError:
                print(f"{ROJO}Ingrese un numero valido...{RESET}")
                input("Enter para continuar...")
                continue

            if opcion == 1:
                print(f"{AZUL}\nDeposito{RESET}\n")
                cuentas[id_cliente] = operacion_cuenta(cuentas[id_cliente], "depositar")
            elif opcion == 2:
                print(f"{AZUL}\Retiro{RESET}\n")
                cuentas[id_cliente] = operacion_cuenta(cuentas[id_cliente], "retirar")
            elif opcion == 3:
                print(f"\n{VERDE}Su saldo es de {RESET}{AMARILLO}${cuentas[id_cliente]['saldo']:,.2f}{RESET}")
            elif opcion == 4:
                print(f"\n{VERDE}Su Historial{RESET}")
                for historial in cuentas[id_cliente]['historial']:
                    print(historial)
            elif opcion == 5:
                print(f"{MAGENTA}Gracias por usar el cajero. ¡Hasta luego!{RESET}")
            else:
                print(f"{ROJO}Opción inválida.{RESET}")

            input("Enter para continuar...")
    else:
        print(f"{ROJO}Acceso denegado...{RESET}")

if __name__ == "__main__":
    main()