from utilidades.utilidades import RUTA_PELICULAS, RUTA_PELICULAS_CSV, VERDE, AMARILLO, ROJO, CYAN, MAGENTA, RESET, validar_dato_entrada
from .pelicula import Pelicula

import json
import csv

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
        anio = validar_dato_entrada("Anio: ", "int")
        duracion = validar_dato_entrada("Duracion: ", "int")
        calificacion = validar_dato_entrada("Calificacion: ", "float")
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
        busqueda = input(f"{MAGENTA}Buscar por titulo, director, genero o anio:{RESET} ").lower().strip()

        if busqueda.isdigit():
            busqueda = int(busqueda)
            resultados = [p for p in self._peliculas if busqueda == p.anio]
        else:
            resultados = [p for p in self._peliculas if busqueda in p.titulo.lower() or busqueda in p.director.lower() or busqueda in p.genero.lower()]

        if resultados:
            print(f"{CYAN}\nResultados encontrados:{RESET}")
            for resultado in resultados:
                print(resultado)
        else:
            print(f"{ROJO}\nNo se encuentro libros con ese termino\n{RESET}")

    def ordernar_por_anio_calificacion(self):
        print(f"{CYAN}\nOrdenar Peliculas por año o calificacion!!!\n{RESET}")
        opcion = validar_dato_entrada("Ordenar por anio o por califcacion (a/c)", "char")
        peliculas_ordenadas = []
        if opcion == 'a':
            peliculas_ordenadas = sorted(self._peliculas, key=lambda pelicula: pelicula.anio)
        else:
            peliculas_ordenadas = sorted(self._peliculas, key=lambda pelicula: pelicula.calificacion)

        self._peliculas = peliculas_ordenadas
        self.guardar_datos()
        print(f"{CYAN}\nPeliculas ordenado por {'anio' if opcion == 'a' else 'calificaciones'}\n{RESET}")

    def exportar_csv(self):
        print(f"{CYAN}\nExportar a CSV!!!\n{RESET}")
        if not self._peliculas:
            print(f"{AMARILLO}\nNo hay datos para exportar.\n{RESET}")
            return
        
        with open(RUTA_PELICULAS_CSV, "w", newline="", encoding="utf-8") as csvfile:
            headers = ["titulo", "director", "genero", "anio", "duracion", "calificacion"]
            writer = csv.DictWriter(csvfile, fieldnames = headers)
            writer.writeheader()

            for pelicula in self._peliculas:
                writer.writerow(pelicula.to_dict())

        print(f"{VERDE}Reporte exportado '{RUTA_PELICULAS_CSV}'{RESET}")