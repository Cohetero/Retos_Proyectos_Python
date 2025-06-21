from dominio.pelicula import Pelicula
import json
import os


class CatalogoPeliculas:
    def __init__(self, ruta_archivo: str = "data/peliculas.json"):
        self.ruta_archivo = ruta_archivo
        # Si no hay archivo, crea uno
        if not os.path.exists("data"):
            os.makedirs("data")
        self._cargar_catalogo()

    def _cargar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                self.peliculas = [Pelicula.from_dict(d) for d in datos]
        else:
            self.peliculas = []

    def _guardar_catalogo(self):
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump([p.to_dict() for p in self.peliculas], archivo, indent=4)

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        self._guardar_catalogo()

    def listar_peliculas(self):
        return self.peliculas

    def buscar_pelicula(self, nombre):
        return [p for p in self.peliculas if nombre.lower() in p.nombre.lower()]

    def eliminar_catalogo(self):
        self.peliculas = []
        self._guardar_catalogo()