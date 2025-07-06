from utilidades.utilidades import *
from catalogo.pelicula import Pelicula
from catalogo.gestor import Gestor

def menu():
    print(f"{CYAN}{' MENU ':=^80}{RESET}")
    print(f"""{AMARILLO}
    1. Agregar nueva Pelicula
    2. Mostrar todas las Peliculas
    3. Busqueda de Peliculas
    4. Ordenar Peliculas por año o calificacion
    5. Exportar a CSV
    6. Salir{RESET}""")

def main():
    opcion = None
    gestor_peliculas = Gestor()
    while opcion != 6:
        limpiar_pantalla()
        menu()
        opcion = validar_dato_entrada("> ", "int")

        match opcion:
            case 1: gestor_peliculas.agregar_peliculas()
            case 2: gestor_peliculas.mostrar_peliculas()
            case 3: gestor_peliculas.busqueda_peliculas()
            case 4: gestor_peliculas.ordernar_por_anio_calificacion()
            case 5: gestor_peliculas.exportar_csv()
            case 6: print(f"{CYAN}\nHasta Luego!!!\n{RESET}")
            case _: print(f"{CYAN}\nOpcion invalida...\n{RESET}")

        pausar()

if __name__ == "__main__":
    main()