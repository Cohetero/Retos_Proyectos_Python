from utils.constantes import VERDE, AMARILLO, CYAN, RESET
from .evento import Evento

class Taller(Evento):
    def __init__(self,
                 id_evento = None,
                 nombre = None,
                 fecha = None,
                 ubicacion = None,
                 ponente = None,
                 duracion_horas= None,
                 requisitos= None):
        super().__init__(id_evento, nombre, fecha, ubicacion)
        self._ponente = ponente
        self._duracion_horas = duracion_horas
        self._requisitos = requisitos

    def descripcion_detallada(self):
        return f"{CYAN}[Taller]{RESET}{VERDE} {self.nombre} por {self.ponente},{RESET}{AMARILLO} duración: {self.duracion_horas}h, requisitos: {self.requisitos} - {self.fecha} en {self.ubicacion}{RESET}"

    def to_dict(self):
        return {
            "id_evento": self._id_evento,
            "tipo": "Taller",
            "nombre": self._nombre,
            "fecha": self._fecha,
            "ubicacion": self._ubicacion,
            "extra1": self.ponente,
            "extra2": self.duracion_horas,
            "extra3": self._requisitos
        }

    @property
    def ponente(self) -> str:
        return self._ponente
    
    @ponente.setter
    def ponente(self, ponente: str):
        self._ponente = ponente

    @property
    def duracion_horas(self):
        return self._duracion_horas
    
    @duracion_horas.setter
    def duracion_horas(self, duracion_horas):
        self._duracion_horas = duracion_horas

    @property
    def requisitos(self) -> str:
        return self._requisitos
    
    @requisitos.setter
    def requisitos(self, requisitos: str):
        self._requisitos = requisitos