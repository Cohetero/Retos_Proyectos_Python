from constantes import VERDE, RESET
from computadora import Computadora

class Orden:
    contador_ordenes = 0

    def __init__(self):
        Orden.contador_ordenes += 1
        self.__id_ordenes = Orden.contador_ordenes
        self.computadoras = []

    def agregar_computadora(self, compu: Computadora):
        self.computadoras.append(compu)

    def __str__(self):
        cadena = ""
        for compu in self.computadoras:
            cadena += compu

        return f"""{VERDE}ID: {self.__id_ordenes}{RESET}\n{cadena}"""
    
    @property
    def id(self) -> str:
        return self.__id_ordenes
