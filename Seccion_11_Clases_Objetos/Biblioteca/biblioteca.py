from constantes import VERDE, AMARILLO, ROJO, RESET
from libro import Libro
from random import choice


class Biblioteca:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._libros = []

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    def agregar_libros(self, titulo: str, autor: str, generos: list):
        libro = Libro(titulo, autor, generos)
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor: str):
        cont = 0
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                libro.imprimir()
                cont += 1

        if cont > 0:
            print(f"{VERDE}Libros encontrados: {cont}{RESET}")
        else:
            print(f"{AMARILLO}No se encontro ningun libro{RESET}")

    def buscar_libros_por_genero(self, genero: str) -> Libro:
        cont = 0
        for libro in self._libros:
            if any(genero.lower() in g for g in libro.generos):
                libro.imprimir()
                cont += 1

        if cont > 0:
            print(f"{VERDE}Libros encontrados: {cont}{RESET}")
        else:
            print(f"{AMARILLO}No se encontro ningun libro{RESET}")

    def mostrar_todos_libros(self):
        print(f"{AMARILLO}Total de libros {Libro.contador_libros}{RESET}")
        for libro in self._libros:
            libro.imprimir()

    def mostrar_libro(self):
        if self._libros:
            libro = choice(self._libros)
            libro.imprimir()
        else:
            print(f"{AMARILLO}No hay libros para recomendar{RESET}")