from servicio.prestamo import Prestamo
from inventario.usuario import Usuario
from inventario.libro import Libro
from datetime import datetime, timedelta
from cosntantes import *
import json
import os

def limpiar_pantalla():
    os.system("cls" if os.name == "int" else "clear")

def menu():
    print(f"{CYAN}{" Sistema de la Bibiloteca Mau ":=^80}{RESET}")
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

def validar_dato(msg: str) -> int:
    while True:
        valor = input(f"{MAGENTA}{msg}{RESET}").strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(f"{ROJO}Tiene que ser un valor numerico...{RESET}")

def acceso_contrasenia()-> bool:
    print(f"{CYAN}\nLogin\n{RESET}")
    intentos = 0
    acceso_concedido  = False
    while intentos < INTENTOS_MAXIMOS:
        print(f"\n{AMARILLO}Intento {intentos + 1} de {INTENTOS_MAXIMOS}{RESET}")
        
        try:
            contra = int(input("contraseña: "))
        except ValueError:
            print(f"{ROJO}La contraseña debe ser numerico.{RESET}")
            intentos += 1
            continue

        if contra == CLAVE:
            acceso_concedido  = True
            break
        else:
            print(f"{ROJO}La contraseña es incorrecto")

        intentos += 1

    return acceso_concedido 

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
                if n_libros <= 3:
                    break
                else:
                    print(f"{AMARILLO}\nEl limite de prestamos son de 3 libros: {libros.size()}\n{RESET}")
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
                print(f"{VERDE}Libro Agregado...{RESET}")
            usuario.libros_prestados = usuario_libros_prestados
            break
    else:
        print(f"{AMARILLO}No se encontro el usuario...{RESET}")
        return

def devolver_libros(usuarios:list, libros: list):
    print(f"{CYAN}\nDevolver Libros\n{RESET}")
    id_user = input(f"{MAGENTA}ID del Usuario: {RESET}")
    
    for usuario in usuarios:
        if usuario.id_user == id_user:
            n_libros = validar_dato("Cuantos libros se van a devolver? ")
            cont = 0
            while cont < n_libros:
                id_libro = input(f"{VERDE}\nId del Libro: {RESET}")
                for libro in libros:
                    if libro.id_libro == id_libro:
                        libro.disponible = True
                        for i, user_libro in enumerate(usuario.libros_prestados):
                            if user_libro.id_libro == id_libro:
                                usuario.libros_prestados.pop(i)
                                break
                        break
                else:
                    cont -= 1
                cont += 1

    else:
        print(f"{AMARILLO}\nNo se encontro ningun Usuario con el ID: {id_user}...{RESET}")

def buscar_libros(libros: list):
    print(f"{CYAN}\nBuscar Libros\n{RESET}")
    print(f"""{VERDE}
    1. Por Titulo
    2. Por Autor
    3. Por Genero
    {RESET}""")
    opcion = validar_dato("> ")

    match opcion:
        case 1:
            titulo = input(f"{MAGENTA}\nNombre del Libro:{RESET}").strip().lower()
            for libro in libros:
                if libro.titulo.lower() == titulo:
                    print(libro)
        case 2:
            autor = input(f"{MAGENTA}\nNombre del Autor:{RESET}").strip().lower()
            for libro in libros:
                if libro.autor.lower() == autor:
                    print(libro)
        case 3:
            genero = input(f"{MAGENTA}\nNombre del Genero:{RESET}").strip()
            for libro in libros:
                if genero in libro.generos:
                    print(libro)
        case _:
            print(f"{CYAN}\nOpcion invalida...\n{RESET}")

def mostrar_estadisticas(libros: list, usuarios: list, prestamos: list):
    libros_disponibles = sum(1 for libro in libros if libro.disponible)
    prestamos_actuales = sum(1 for prestamo in prestamos if prestamo.devolucion)
    print(f"{CYAN}\nEstadisticas Sencillas:\n{RESET}")
    print(f"""
    * {VERDE}Total de libros:{RESET} {len(libros)}
    * {VERDE}Total de usuarios:{RESET} {len(usuarios)}
    * {VERDE}Libros prestados actualmente:{RESET} {prestamos_actuales}
    * {VERDE}Libros disponibles:{RESET} {libros_disponibles}
    """)

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

def guardar_archivo(ruta_archivo: str, lista: list):
    with open(ruta_archivo, "w", encoding="utf-8") as file:
        json.dump([obj.to_dict() for obj in lista], file, indent=4)

def cargar_archivo(ruta_archivo: str, tipo_object: str = None) -> list:
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            datos = json.load(file)
            if tipo_object == "Libro":
                new_list = [Libro.from_dict(d) for d in datos]
            elif tipo_object == "Usuario":
                new_list = [Usuario.from_dict(d) for d in datos]
            else:
                new_list = [Prestamo.from_dict(d) for d in datos]
    else:
        new_list = []

    return new_list

def main():
    if acceso_contrasenia():
        libros = cargar_archivo(RUTA_JSON_LIBROS, "Libro")
        usuarios = cargar_archivo(RUTA_JSON_USUARIOS, "Usuario")
        #prestamos = cargar_archivo(RUTA_JSON_PRESTAMOS)
        prestamos = []

        while True:
            limpiar_pantalla()
            menu()
            opcion = validar_dato("> ")

            match opcion:
                case 1: 
                    agregar_libro(libros)
                    guardar_archivo(RUTA_JSON_LIBROS, libros)
                case 2: 
                    registrar_usuarios(usuarios)
                    guardar_archivo(RUTA_JSON_USUARIOS, usuarios)
                case 3: 
                    prestar_libros(prestamos, libros, usuarios)
                    #guardar_archivo(RUTA_JSON_PRESTAMOS, prestamos)
                    guardar_archivo(RUTA_JSON_LIBROS, libros)
                    guardar_archivo(RUTA_JSON_USUARIOS, usuarios)
                case 4: 
                    devolver_libros(usuarios, libros)
                case 5: 
                    buscar_libros(libros)
                case 6: 
                    mostrar_listas(libros, "Lista de todos los libros")
                case 7: 
                    mostrar_prestamos_disponibles(prestamos)
                case 8: 
                    mostrar_prestamos_vencidos(prestamos)
                case 9:
                    mostrar_listas(usuarios, "Lista de todos los libros")
                case 10:
                    mostrar_estadisticas(libros, usuarios, prestamos)
                case 11:
                    print(f"{CYAN}\nHasta Luego!!!\n{RESET}")
                case _: 
                    print(f"{CYAN}\nOpcion invalida...\n{RESET}")

            if opcion == 11: break

            input("\nEnter para continuar...\n")
    else:
        print(f"{ROJO}Acceso Denegado{RESET}")


if __name__ == "__main__":
    main()