from constantes import *
from biblioteca import Biblioteca
from libro import Libro
import os

def limpiar_pantalla():
    os.system("cls" if os.name == 'int' else "clear")

def menu(biblio: Biblioteca):
    msg = f" Bienvenido a la Biblioteca {biblio.nombre} "
    print(f"{CYAN}{msg:=^80}{RESET}")
    print(f"""{AMARILLO}Menu:{RESET}
    1. Agregar libros
    2. Buscar libros por autor
    3. Buscar libros por genero
    4. Mostrar todos los libros
    5. Recomendar un libro
    6. Salir""")

def validar_dato(msg: str) -> int:
    while True:
        valor = input(f"{MAGENTA}{msg}{RESET}").strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(f"{ROJO}Tiene que ser un valor numerico...{RESET}")

if __name__ == "__main__":
    nombre = input("Nombre de la biblioteca: ").strip()
    biblio = Biblioteca(nombre)

    while True:
        limpiar_pantalla()
        menu(biblio)
        opcion = validar_dato("Introduzca un valor: ")

        match opcion:
            case 1:
                print(f"{CYAN}\nAgregar libros\n{RESET}")
                cont = validar_dato("Cuantos libros desea agregar: ")

                for i in range(cont):
                    nombre = input(f"{MAGENTA}Nombre del libro: {RESET}").strip()
                    autor = input(f"{MAGENTA}Autor del libro: {RESET}").strip()
                    n_generos = validar_dato("Cuantos Generos tiene el libro: ")
                    generos = []
                    for i in range(n_generos):
                        genero = input(f"{MAGENTA}Genero del libro: {RESET}\n").strip()
                        generos.append(genero.lower())
                    biblio.agregar_libros(nombre, autor, generos)

            case 2:
                print(f"{CYAN}\nBuscar libros por autor\n{RESET}")
                autor = input(f"{MAGENTA}Autor para la busqueda: {RESET}").strip()
                biblio.buscar_libros_por_autor(autor)

            case 3:
                print(f"{CYAN}\nBuscar libros por genero\n{RESET}")
                genero = input(f"{MAGENTA}Genero para la busqueda: {RESET}").strip()
                biblio.buscar_libros_por_genero(genero)

            case 4:
                print(f"{CYAN}\nMostrar todos los libros\n{RESET}")
                biblio.mostrar_todos_libros()

            case 5:
                print(f"{CYAN}\nLibro Recomendado\n{RESET}")
                biblio.mostrar_libro()
            case 6:
                print(f"{CYAN}\nHasta Luego!!!\n{RESET}")
            case _:
                print(f"{AMARILLO}\nOpcion invalida...\n{RESET}")

        if opcion == 6:
            break
        input("\nEnter para continuar...\n")