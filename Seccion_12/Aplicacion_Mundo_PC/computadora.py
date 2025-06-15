from dispositivo_entrada import Teclado, Raton
from constantes import AMARILLO, RESET
from monitor import Monitor

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre: str, monitor: Monitor, teclado: Teclado, raton: Raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""{AMARILLO}ID: {self.__id_computadora} - {self._nombre}{RESET}
        Monitor: {self._monitor}\nTeclado: {self._teclado}\nRaton: {self._raton}"""
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def id(self) -> str:
        return self.__id_computadora