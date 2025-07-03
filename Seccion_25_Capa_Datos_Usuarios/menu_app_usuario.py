from usuario_dao import UsuarioDAO
from logger_base import log
from usuario import Usuario
from constantes import *
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def pausar():
    input("\nEnter para continuar...\n")

def menu():
    print(f"{CYAN}{' Sistema de la Bibiloteca Mau ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
        {CYAN}1. Listar usuarios
        2. Agregar usuarios
        3. Modificar usuarios
        4. Eliminar usuarios
        5. Salir{RESET}""")

def validar_opcion(msg: str) -> int:
    while True:
        try:
            opcion = int(input(f"{MAGENTA}{msg}{RESET}").strip())
            return opcion
        except ValueError:
            print(f"{ROJO}\nIntroduzca un numero valido...{RESET}")

def main():
    opcion = None
    while opcion != 5:
        limpiar_pantalla()
        menu()
        opcion = validar_opcion("> ")

        match opcion:
            case 1:
                usuarios = UsuarioDAO.seleccionar()
                for usuario in usuarios:
                    log.info(usuario)
            case 2:
                username = input(f"{VERDE}Escribe el username: {RESET}")
                password = input(f"{VERDE}Escribe el password: {RESET}")
                usuario = Usuario(username=username, password=password)
                usuarios_insertados = UsuarioDAO.insertar(usuario)
                log.info(f"Usuarios insertados: {usuarios_insertados}")
            case 3:
                id_usuario = validar_opcion("Escribe el id_usuario a modificar: ")
                username = input(f"{VERDE}Escribe el username: {RESET}")
                password = input(f"{VERDE}Escribe el password: {RESET}")
                usuario = Usuario(id_usuario, username, password)
                usuarios_actualizados = UsuarioDAO.actualizar(usuario)
                log.info(f"Usuarios actualizadas: {usuarios_actualizados}")
            case 4:
                id_usuario = validar_opcion("Escribe el id_usuario a eliminar: ")
                usuario = Usuario(id_usuario=id_usuario)
                usuarios_eliminados = UsuarioDAO.eliminar(usuario)
                log.info(f"Usuarios elimiandos: {usuarios_eliminados}")
            case 5:
                print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")
            case _: 
                print(f"{CYAN}\nOpcion invalida...\n{RESET}")

        pausar()
    else:
        pass

if __name__ == "__main__":
    main()