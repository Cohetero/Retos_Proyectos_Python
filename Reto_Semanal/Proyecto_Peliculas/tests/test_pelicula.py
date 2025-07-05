
from catalogo.pelicula import Pelicula

def test_pelicula():
    peli = Pelicula("Inception", "Christopher Nolan", "Ciencia Ficción", 2010, 148, 8.8)

    print(f"{peli}\n")

    peli.titulo = "Parasite"
    peli.director = "Bong Joon-ho"
    peli.genero = "Drama"
    peli.anio = 2019
    peli.duracion = 132
    peli.calificacion = 8.6

    print(f"{peli}\n")

if __name__ == "__main__":
    test_pelicula()