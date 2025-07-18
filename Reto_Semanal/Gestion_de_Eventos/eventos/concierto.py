from utils.constantes import VERDE, AMARILLO, CYAN, RESET
from .evento import Evento

class Concierto(Evento):
    def __init__(self, id_evento = None, nombre = None, fecha = None, ubicacion = None, banda = None, genero = None):
        super().__init__(id_evento, nombre, fecha, ubicacion)
        self._banda = banda
        self._genero = genero

    def descripcion_detallada(self):
        return f"{CYAN}[Concierto]{RESET}{VERDE} {self.nombre} por {self.banda} ({self.genero}){RESET}{AMARILLO} en {self.ubicacion} el {self.fecha}{RESET}"

    def to_dict(self):
        return {
            "id_evento": self._id_evento,
            "tipo": "Concierto",
            "nombre": self._nombre,
            "fecha": self._fecha,
            "ubicacion": self._ubicacion,
            "extra1": self._banda,
            "extra2": self._genero,
            "extra3": None
        }

    @property
    def banda(self) -> str:
        return self._banda
    
    @banda.setter
    def banda(self, banda: str):
        self._banda = banda

    @property
    def genero(self) -> str:
        return self._genero
    
    @genero.setter
    def genero(self, genero: str):
        self._genero = genero