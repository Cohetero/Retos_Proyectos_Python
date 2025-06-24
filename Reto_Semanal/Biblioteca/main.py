from servicio.prestamo import Prestamo
from inventario.usuario import Usuario
from inventario.libro import Libro
from utilidades import validar_opcion
from datetime import datetime, timedelta
from constantes import *

import getpass
import json
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def pausar():
    input("\nEnter para continuar...\n")

def menu():
    print(f"{CYAN}{' Sistema de la Bibiloteca Mau ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
        {CYAN}1. Agregar libros
        2. Registar usuarios
        3. Prestar libros
        4. Devolver libros
        5. Buscar libros
        6. Ver libros
        7. Mostrar prestamos activos
        8. Mostrar prestamos vencidos
        9. Ver usuarios
        10. Estadisticas
        11. Salir{RESET}""")

# Seguridad
def acceso_contrasenia()-> bool:
    print(f"{CYAN}\n=== Login de acceso ===\n{RESET}")
    for intento in range(INTENTOS_MAXIMOS):
        print(f"\n{AMARILLO}Intento {intento + 1} de {INTENTOS_MAXIMOS}{RESET}")
        contra = getpass.getpass("Password: ")
        if contra == CLAVE:
            print(f"{VERDE}Acceso Concedido.{RESET}")
            return True
        else:
            print(f"{ROJO}La contraseña es incorrecto")
    return False

def main():
    if not acceso_contrasenia():
        print(f"{ROJO}Acceso Denegado. Demasiado intentos falliedos...{RESET}")
        return

    prestamos = Prestamo()

    while True:
        limpiar_pantalla()
        menu()
        opcion = validar_opcion("(1-11)> ", 1, 11)

        match opcion:
            case 1: 
                prestamos.registrar_libro()
            case 2: 
                prestamos.registrar_usuario()
            case 3: 
                prestamos.prestar_libros()
            case 4: 
                prestamos.devolver_libros()
            case 5: 
                prestamos.buscar_libros()
            case 6: 
                prestamos.mostrar_libros()
            case 7: 
                prestamos.mostrar_prestamos_activos()
            case 8: 
                prestamos.mostrar_prestamos_vencidos()
            case 9:
                prestamos.mostrar_usuarios()
            case 10:
                prestamos.mostrar_estadisticas()
            case 11:
                print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")
            case _: 
                print(f"{CYAN}\nOpcion invalida...\n{RESET}")

        if opcion == 11: break
        pausar()

if __name__ == "__main__":
    main()