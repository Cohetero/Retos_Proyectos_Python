from utils.constantes import VERDE, AMARILLO, CYAN, RESET
from .evento import Evento

class Exposicion(Evento):
    def __init__(self, id_evento=None, nombre=None, fecha=None, ubicacion=None, artista = None, tipo_arte = None):
        super().__init__(id_evento, nombre, fecha, ubicacion)
        self._artista = artista
        self._tipo_arte = tipo_arte

    def descripcion_detallada(self):
        return f"{CYAN}[Exposición]{RESET}{VERDE} {self.nombre} de {self.artista} ({self.tipo_arte}){RESET}{AMARILLO} en {self.ubicacion} el {self.fecha}{RESET}"

    def to_dict(self):
        return {
            "id_evento": self._id_evento,
            "tipo": "Exposición",
            "nombre": self._nombre,
            "fecha": self._fecha,
            "ubicacion": self._ubicacion,
            "extra1": self._artista,
            "extra2": self._tipo_arte,
            "extra3": None
        }
    
    @property
    def artista(self) -> str:
        return self._artista
    
    @artista.setter
    def artista(self, artista: str):
        self._artista = artista

    @property
    def tipo_arte(self) -> str:
        return self._tipo_arte
    
    @tipo_arte.setter
    def tipo_arte(self, tipo_arte: str):
        self._tipo_arte = tipo_arte