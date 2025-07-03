from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas
def mostrar_menu():
    print("\n--- MENÚ CATÁLOGO DE PELÍCULAS ---")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Buscar película")
    print("4. Eliminar catálogo")
    print("5. Salir")

def main():
    catalogo = CatalogoPeliculas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre de la película: ")
            catalogo.agregar_pelicula(Pelicula(nombre))
            print("Película agregada.")
        elif opcion == "2":
            peliculas = catalogo.listar_peliculas()
            if peliculas:
                print("\nLista de películas:")
                for p in peliculas:
                    print(f" - {p}")
            else:
                print("No hay películas registradas.")
        elif opcion == "3":
            nombre = input("Buscar película: ")
            resultados = catalogo.buscar_pelicula(nombre)
            if resultados:
                print("Resultados encontrados:")
                for p in resultados:
                    print(f" - {p}")
            else:
                print("No se encontraron coincidencias.")
        elif opcion == "4":
            confirmacion = input("¿Estás seguro? Esto eliminará todo el catálogo (s/n): ")
            if confirmacion.lower() == "s":
                catalogo.eliminar_catalogo()
                print("Catálogo eliminado.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
