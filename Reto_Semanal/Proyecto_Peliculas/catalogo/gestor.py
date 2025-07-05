from utilidades.utilidades import RUTA_PELICULAS, VERDE, ROJO, CYAN, MAGENTA, RESET
from .pelicula import Pelicula

import json

class Gestor:
    def __init__(self):
        self._peliculas = self.cargar_datos(RUTA_PELICULAS, Pelicula)

    @property
    def peliculas(self) -> list:
        return self._peliculas
    
    @peliculas.setter
    def peliculas(self, peliculas: list):
        self._peliculas = peliculas

    # Metodos de carga y guardado de archivos
    def cargar_datos(self, archivo: str, clase: any):
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                datos = json.load(file)
            return [clase.from_dict(d) for d in datos]
        except FileNotFoundError:
            return []

    def guardar_datos(self):
        with open(RUTA_PELICULAS, "w", encoding="utf-8") as file:
            json.dump([peli.to_dict() for peli in self.peliculas], file, indent = 4)

    # Metodos del Gestor de Peliculas
    def agregar_peliculas(self):
        print(f"{CYAN}\nAgregar una Nueva Pelicula!!!\n{RESET}")
        titulo = input(f"{MAGENTA}Titulo: {RESET}").strip()
        director = input(f"{MAGENTA}Director: {RESET}").strip()
        genero = input(f"{MAGENTA}Genero: {RESET}").strip()
        anio = input(f"{MAGENTA}Anio: {RESET}").strip()
        duracion = input(f"{MAGENTA}Duracion: {RESET}").strip()
        calificacion = input(f"{MAGENTA}Calificacion: {RESET}").strip()
        pelicula = Pelicula(titulo, director, genero, anio, duracion, calificacion)
        self._peliculas.append(pelicula)
        self.guardar_datos()
        print(f"{VERDE}\nPelicula registrada.{RESET}")

    def mostrar_peliculas(self):
        print(f"{CYAN}\nMostrar Todas las Peliculas Registradas!!!\n{RESET}")
        for pelicula in self._peliculas:
            print(pelicula)

    def busqueda_peliculas(self):
        print(f"{CYAN}\nBusqueda de Peliculas!!\n{RESET}")
        busqueda = input(f"{MAGENTA}Buscar por titulo, director, genero:{RESET} ").lower().strip()

        resultados = [p for p in self._peliculas if busqueda in p.titulo.lower() or busqueda in p.director.lower() or busqueda in p.genero.lower()]

        if resultados:
            print(f"{CYAN}\nResultados encontrados:{RESET}")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"{ROJO}\nNo se encuentro libros con ese termino\n{RESET}")

