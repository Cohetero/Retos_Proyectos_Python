from abc import ABC, abstractclassmethod

class Espacio(ABC):
    def __init__(self, id_espacio = None, nombre = None, capacidad = 0, ubicacion = None):
        self._id_espacio = id_espacio
        self._nombre = nombre
        self._capacidad = capacidad
        self._ubicacion = ubicacion

    @abstractclassmethod
    def descripcion_detallada(self):
        pass

    @property
    def id_espacio(self) -> int:
        return self._id_espacio
    
    @id_espacio.setter
    def id_espacio(self, id_espacio: int):
        self._id_espacio = id_espacio

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def capacidad(self) -> int:
        return self._capacidad
    
    @capacidad.setter
    def capacidad(self, capacidad: int):
        self._capacidad = capacidad

    @property
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion: str):
        self._ubicacion = ubicacion