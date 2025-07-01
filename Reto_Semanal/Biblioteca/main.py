from servicio.historial_prestamos import *
from servicio.prestamo import Prestamo
from utilidades import validar_opcion
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
        11. Menu de Reportes
        12. Salir{RESET}""")

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

def mostrar_menu(prestamos: Prestamo):
    while True:
        limpiar_pantalla()
        print(f"""{AMARILLO}\n\tMENU DE REPORTES{RESET}
            {CYAN}1. Libros mas prestados
            2. Usuarios mas prestados
            3. Exportar libros mas prestados
            4. Exportar usuarios mas activos
            5. Salir {RESET}""")
        
        opcion = validar_opcion("(1-5)> ", 1, 5)

        match opcion:
            case 1:
                libros = libros_mas_prestados(RUTA_JSON_PRESTAMOS, RUTA_JSON_LIBROS)
                for libro in libros:
                    print(f"{libro['titulo']}: {libro['veces_prestado']} veces")
            case 2:
                usuarios = usuarios_mas_activos(RUTA_JSON_PRESTAMOS, RUTA_JSON_USUARIOS)
                for usuario in usuarios:
                    print(f"{usuario['nombre']}: {usuario['prestamos_realizados']} prestamos")
            case 3:
                libros = libros_mas_prestados(RUTA_JSON_PRESTAMOS, RUTA_JSON_LIBROS)
                exportar_csv(RUTA_CSV_LIBROS_PRESTAMOS, libros)
            case 4:
                usuarios = usuarios_mas_activos(RUTA_JSON_PRESTAMOS, RUTA_JSON_USUARIOS)
                exportar_csv(RUTA_CSV_USUARIOS_PRESTAMOS, usuarios)

        if opcion == 5: break
        pausar()

def main():
    if not acceso_contrasenia():
        print(f"{ROJO}Acceso Denegado. Demasiado intentos falliedos...{RESET}")
        return

    prestamos = Prestamo()

    while True:
        limpiar_pantalla()
        menu()
        opcion = validar_opcion("(1-12)> ", 1, 12)

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
                mostrar_menu(prestamos)
            case 12:
                print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")
            case _: 
                print(f"{CYAN}\nOpcion invalida...\n{RESET}")

        if opcion == 12: break
        pausar()

if __name__ == "__main__":
    main()