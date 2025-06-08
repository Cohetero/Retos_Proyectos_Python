"""
🌟 Reto semanal #1 - Múltiples cuentas con transferencia
Objetivo:
Agrega a tu cajero automático la función de transferir dinero entre cuentas registradas.
Debes permitir al usuario seleccionar otra cuenta y transferir un monto válido, actualizando los saldos 
y agregando la transferencia al historial de ambas cuentas.

✅ Requisitos mínimos:
Menú con la opción: 5.- Transferir dinero

Mostrar lista de cuentas destino (sin incluir la propia)

Validar que el monto sea positivo y no mayor al saldo

Restar al emisor y sumar al receptor

Registrar en ambos historiales (emisor y receptor)

🧠 Extra opcional (si quieres ir más allá):
Mostrar resumen de la transferencia al final (tipo recibo)

Permitir notas personalizadas (“Pago de renta”, “Regalo”, etc.)

Ordenar historial por fecha con datetime
"""

from datetime import datetime
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
            now = datetime.now()

            if opcion == "depositar":
                if monto > 10000:
                    print(f"{AMARILLO}No se puede depositar mas de {RESET}{VERDE}$10000{RESET}")
                    continue
                cuenta['saldo'] += monto
                cuenta['historial'].append(f"{now} {MAGENTA}Deposito de {RESET}{VERDE}${monto:,.2f}{RESET}")
                return cuenta
            elif opcion == "retirar" :
                if monto <= cuenta['saldo']:
                    if monto > 5000:
                        print(f"{AMARILLO}No se puede retirar mas de {RESET}{VERDE}$5000{RESET}")
                        continue
                    cuenta['saldo'] -= monto
                    cuenta['historial'].append(f"{now} {MAGENTA}Retiro de {RESET}{VERDE}${monto:,.2f}{RESET}")
                    return cuenta
                else:
                    print(f"{ROJO}Saldo insuficiente para retirar.{RESET}")
            else:
                print(f"{ROJO}Operación desconocida.{RESET}")
                return cuenta
        except ValueError:
            print(f"{ROJO}Ingrese una cantidad valida...{RESET}")

def transferir_dinero(cuenta: dict, cuentas: list) -> dict:
    while True:
        while True:
            try:
                print(f"{CYAN}Saldo: {cuenta["saldo"]}{RESET}")
                monto = float(input(f"$"))
                break
            except ValueError:
                print(f"{ROJO}Ingrese una cantidad valida...{RESET}")

        if monto <= 0:
            print(f"{AMARILLO}La cantidad debe ser positiva.{RESET}")
            continue
        elif monto > cuenta["saldo"]:
            print(f"{AMARILLO}La cantidad a transferir es mayor a su saldo actual.{RESET}")
            continue

        print(f"{MAGENTA}Cuentas Disponibles a Transferir{RESET}")
        for i, usuario in enumerate(cuenta["cuentas"]):
            print(f"{i}. {usuario}")
        while True:
            try:
                id_usuario = int(input("ID de la cuenta a transferir: "))
                break
            except ValueError:
                print(f"{ROJO}Ingrese un numero Entero...{RESET}")

        for i in cuentas:
            if i["cliente"] == cuenta["cuentas"][id_usuario]:
                now = datetime.now()
                nota = input(f"{MAGENTA}Nota de la Transferencia (opcional): {RESET}")
                i["saldo"] += monto
                cuenta["saldo"] -= monto
                i['historial'].append(f"{now} {MAGENTA}Recivo de Transferencia de {RESET}{VERDE}${monto:,.2f}{RESET}\nNota:{nota}")
                cuenta['historial'].append(f"{now} {MAGENTA}Decuento de Transferencia {RESET}{VERDE}${monto:,.2f}{RESET}\nNota:{nota}")

                print(f"""{AZUL}=== Recibo de la Transferencia ==={RESET}
        {now.hour}:{now.minute}:{now.second} {now.day}-{now.month}-{now.year}
        Monto de la transferncia {VERDE}${monto}{RESET}""")
                return cuenta



def mostrar_menu():
    print(f"{CYAN}{" Cajero Automatico ":*^100}{RESET}")
    print(f"""{AZUL} Menu de Opciones{RESET}{AMARILLO}
    1.- Depositar
    2.- Retirar
    3.- Consultar Saldo
    4.- Consultar Historial
    5.- Transferir Dinero
    6.- Salir{RESET}""")

def main():
    cuentas = [
        {
            "nip": 1234,
            "saldo": 155275.00,
            "cliente": "Mauricio Cohetero Baltazar",
            "cuentas": ["Emilia Luna Torres", "Andrea Lopez Garcia"],
            "historial": []
        },
        {
            "nip": 4321,
            "saldo": 5430.54,
            "cliente": "Emilia Luna Torres",
            "cuentas": ["Mauricio Cohetero Baltazar"],
            "historial": []
        },
        {
            "nip": 3051,
            "saldo": 7450.78,
            "cliente": "Andrea Lopez Garcia",
            "cuentas": ["Mauricio Cohetero Baltazar"],
            "historial": []
        }
    ]

    while True:
        id_cliente = mostrar_clientes(cuentas)

        if acceso_contrasenia(cuentas[id_cliente]['nip'], cuentas[id_cliente]['cliente']):
            opcion = 0
            while opcion != 6:
                limpiar_pantalla()
                mostrar_menu()

                try:
                    opcion = int(input("-> "))
                except ValueError:
                    print(f"{ROJO}Ingrese un numero valido...{RESET}")
                    input("Enter para continuar...")
                    continue

                match opcion:
                    case 1:
                        print(f"{AZUL}\nDeposito{RESET}\n")
                        cuentas[id_cliente] = operacion_cuenta(cuentas[id_cliente], "depositar")
                    case 2:
                        print(f"{AZUL}\nRetiro{RESET}\n")
                        cuentas[id_cliente] = operacion_cuenta(cuentas[id_cliente], "retirar")
                    case 3:
                        print(f"\n{VERDE}Su saldo es de {RESET}{AMARILLO}${cuentas[id_cliente]['saldo']:,.2f}{RESET}")
                    case 4:
                        print(f"\n{VERDE}Su Historial{RESET}")
                        for historial in cuentas[id_cliente]['historial']:
                            print(historial)
                    case 5:
                        print(f"{AZUL}\nTransferir dinero{RESET}\n")
                        cuentas[id_cliente] = transferir_dinero(cuentas[id_cliente], cuentas)
                    case 6:
                        print(f"{MAGENTA}Gracias por usar el cajero. ¡Hasta luego!{RESET}")
                    case _:
                        print(f"{ROJO}Opción inválida.{RESET}")

                input("Enter para continuar...")
        else:
            print(f"{ROJO}Acceso denegado...{RESET}")

        continuar = input(f"{MAGENTA}Desea ingresar otra cuenta (S/N)? {RESET}").strip().lower()
        if continuar == "n":
            break

if __name__ == "__main__":
    main()