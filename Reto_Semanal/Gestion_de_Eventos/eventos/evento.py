from utils.constantes import VERDE, CYAN, RESET
from datetime import datetime

class Evento:
    def __init__(
            self,
            id_evento: int = None,
            tipo: str = None,
            nombre: str = None,
            fecha: datetime = None,
            ubicacion: str = None,
            extra1: str = None,
            extra2: str = None,
            extra3: str = None):
        self._id_evento = id_evento
        self._tipo = tipo
        self._nombre = nombre
        self._fecha = fecha
        self._ubicacion = ubicacion
        self._extra1 = extra1
        self._extra2 = extra2
        self._extra3 = extra3

    def __str__(self) -> str:
        return f"""{VERDE}{self._id_evento}:{RESET}
        {CYAN}Tipo :{RESET} {self._tipo}
        {CYAN}Nombre :{RESET} {self._nombre}
        {CYAN}Fecha :{RESET} {self._fecha}
        {CYAN}Ubicacion :{RESET} {self._ubicacion}
        {CYAN}Extra 1 :{RESET} {self._extra1}
        {CYAN}Extra 2 :{RESET} {self._extra2}
        {CYAN}Extra 3 :{RESET} {self._extra3}"""

    @property
    def id_evento(self) -> int:
        return self._id_evento
    
    @id_evento.setter
    def id_evento(self, id_evento: int):
        self._id_evento = id_evento

    @property
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        self._tipo = tipo

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def fecha(self) -> datetime:
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha: datetime):
        self._fecha = fecha

    @property
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion: str):
        self._ubicacion = ubicacion

    @property
    def extra1(self) -> str:
        return self._extra1
    
    @extra1.setter
    def extra1(self, extra1: str):
        self._extra1 = extra1

    @property
    def extra2(self) -> str:
        return self._extra2
    
    @extra2.setter
    def extra2(self, extra2: str):
        self._extra2 = extra2

    @property
    def extra3(self) -> str:
        return self._extra3
    
    @extra1.setter
    def extra3(self, extra3: str):
        self._extra3 = extra3