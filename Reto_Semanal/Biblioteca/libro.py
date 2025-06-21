from cosntantes import VERDE, RESET
from datetime import datetime as dt

class Libro:
    def __init__(self, titulo: str, autor: str, anio: dt, generos: list):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._generos = generos

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, autor: str):
        self._autor = autor

    @property
    def anio(self) -> dt:
        return self._anio
    
    @anio.setter
    def anio(self, anio: dt):
        self._anio = anio

    @property
    def generos(self) -> list:
        return self._generos
    
    @generos.setter
    def generos(self, generos: list, flag: bool):
        if flag:
            self._generos = generos
        else:
            self._generos.extend(generos)