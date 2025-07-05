from utilidades.utilidades import *
from catalogo.pelicula import Pelicula
from catalogo.gestor import Gestor

def menu():
    print(f"{CYAN}{' MENU ':=^80}{RESET}")
    print(f"""{AMARILLO}
    1. Agregar nueva Pelicula
    2. Mostrar todas las Peliculas
    3. Busqueda de Peliculas
    4. Exportar a CSV
    5. Salir{RESET}""")

def main():
    opcion = None
    gestor_peliculas = Gestor()
    while opcion != 5:
        menu()
        opcion = int(input("> "))

        match opcion:
            case 1: gestor_peliculas.agregar_peliculas()
            case 2: gestor_peliculas.mostrar_peliculas()
            case 3: gestor_peliculas.busqueda_peliculas()
            case 4: print(f"{CYAN}\nExportar a CSV!!!\n{RESET}")
            case 5: print(f"{CYAN}\nHasta Luego!!!\n{RESET}")
            case _: print(f"{CYAN}\nOpcion invalida...\n{RESET}")

if __name__ == "__main__":
    main()