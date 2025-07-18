from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, id_evento = None, nombre = None, fecha = None, ubicacion = None):
        self._id_evento = id_evento
        self._nombre = nombre
        self._fecha = fecha
        self._ubicacion = ubicacion

    @abstractmethod
    def descripcion_detallada(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @property
    def id_evento(self) -> int:
        return self._id_evento
    
    @id_evento.setter
    def id_evento(self, id_evento: int):
        self._id_evento = id_evento

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion: str):
        self._ubicacion = ubicacion