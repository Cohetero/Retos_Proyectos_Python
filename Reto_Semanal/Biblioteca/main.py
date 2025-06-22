from servicio.prestamo import Prestamo
from inventario.usuario import Usuario
from inventario.libro import Libro
from datetime import datetime, timedelta
from cosntantes import *
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def menu():
    print(f"{CYAN}{" Sistema de la Bibiloteca Mau ":=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
        {CYAN}1. Agregar libros
        2. Registar usuarios
        3. Prestar libros
        4. Ver libros
        5. Mostrar prestamos activos
        6. Ver usuarios
        7. Salir{RESET}""")

def validar_dato(msg: str) -> int:
    while True:
        valor = input(f"{MAGENTA}{msg}{RESET}").strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(f"{ROJO}Tiene que ser un valor numerico...{RESET}")

def agregar_libro(libros: list):
    print(f"{CYAN}\nAgregar Libros\n{RESET}")
    n_libros = validar_dato("Cuantos libros desea agregar? ")

    for i in range(n_libros):
        nombre = input(f"{MAGENTA}Nombre: {RESET}").strip()
        autor = input(f"{MAGENTA}Autor: {RESET}").strip()
        anio = validar_dato("Fecha de Publicacion: ")
        n_generos = validar_dato("Cuantos Generos tiene el libro: ")
        generos = []

        print("\n")
        for j in range(n_generos):
            genero = input(f"{j+1}°: ").strip()
            generos.append(genero)

        libro = Libro(nombre, autor, anio, generos)
        libros.append(libro)
        print("\n")

def registrar_usuarios(usuarios: list):
    print(f"{CYAN}\nRegistrar usuarios\n{RESET}")
    n_usuarios = validar_dato("Cuantos usuarios desde agregar? ")

    for i in range(n_usuarios):
        nombre = input(f"{MAGENTA}Nombre: {RESET}").strip()
        apellido = input(f"{MAGENTA}Apellido/s: {RESET}").strip()

        usuario = Usuario(nombre, apellido)
        usuarios.append(usuario)
        print("\n")

def prestar_libros(prestamos: list, libros: list, usuarios: list):
    print(f"{CYAN}\nPrestar Libros\n{RESET}")
    id_usuario = input(f"{MAGENTA}ID del Usuario: {RESET}").strip()

    for usuario in usuarios:
        if usuario.id_user == id_usuario:
            print(usuario)
            while True:
                n_libros = validar_dato("Cuantos libros se van a prestar? ")
                if n_libros < libros.size():
                    break
                else:
                    print(f"{AMARILLO}\nEl limite de los libros para pedir prestado son: {libros.size()}\n{RESET}")
            busqueda_libros = libros.copy()
            usuario_libros_prestados = []
            n = 0
            for i in range(n_libros):
                book = None
                while True:
                    id_libro = input(f"{MAGENTA}ID del Libro: {RESET}").strip()
                    for j, libro in enumerate(busqueda_libros):
                        if libro.id_libro == id_libro:
                            if libro.disponible:
                                print(libro)
                                book = libro
                                busqueda_libros.pop(j)
                                libros[j+n].disponible = False
                                n += 1
                            else:
                                print(f"{AMARILLO}\nEl ibro con id {id_libro} ya esta disponible...\n{RESET}")
                            break
                    if book is not None:
                        break
                    else:
                        print(f"{AMARILLO}\nNo se encontro el libro con id {id_libro}\n{RESET}")
                usuario_libros_prestados.append(book)


                fecha_prestamo = datetime.now()
                fecha_devolucion = fecha_prestamo + timedelta(days=7)
                prestamo = Prestamo(usuario, usuario_libros_prestados, fecha_prestamo, fecha_devolucion)
                prestamos.append(prestamo)
            usuario.libros_prestados = usuario_libros_prestados
            break
    else:
        print(f"{AMARILLO}No se encontro el usuario...{RESET}")
        return

def mostrar_listas(lista: list, msg: str):
    print(f"{CYAN}\n{msg}\n{RESET}")
    for item in lista:
        print(item)

def mostrar_prestamos_disponibles(prestamos: list):
    print(f"{CYAN}\nMostrar todos los prestamos activos\n{RESET}")
    for prestamo in prestamos:
        if not prestamo.devolucion:
            print(prestamo)

def mostrar_prestamos_vencidos(prestamos: list):
    fecha_actual = datetime.now()
    for prestamo in prestamos:
        if not prestamo.devolucion and prestamo.fecha_devolucion.date() <= fecha_actual.date():
            print(prestamo)

def mostrar_libros_disponibles(libros: list):
    print(f"{CYAN}\nLibros Disponibles\n{RESET}")
    for libro in libros:
        if libro.disponible:
            print(libro)

def main():
    # USER-S1WWCZ
    # LIB-WI3AST

    prestamos = []
    usuarios = []
    libros = []

    while True:
        limpiar_pantalla()
        menu()
        opcion = validar_dato("> ")

        match opcion:
            case 1: agregar_libro(libros)
            case 2: registrar_usuarios(usuarios)
            case 3: prestar_libros(prestamos, libros, usuarios)
            case 4: mostrar_listas(libros, "Lista de todos los libros")
            case 5: mostrar_prestamos_disponibles(prestamos)
            case 6: mostrar_listas(usuarios, "Lista de todos los libros")
            case 7: print(f"{CYAN}\nHasta Luego!!!\n{RESET}")
            case _: print(f"{CYAN}\nOpcion invalida...\n{RESET}")

        if opcion == 7: break

        input("\nEnter para continuar...\n")


if __name__ == "__main__":
    main()