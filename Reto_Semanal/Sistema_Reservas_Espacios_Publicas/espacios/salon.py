from utils.constantes import VERDE, AMARILLO, CYAN, RESET
from .espacio import Espacio

class Salon(Espacio):
    def __init__(self, id_espacio=None, nombre=None, capacidad=0, ubicacion=None):
        super().__init__(id_espacio, nombre, capacidad, ubicacion)

    def descripcion_detallada(self) -> str:
        return f"{CYAN}[Salon] - {RESET}{VERDE} {self._nombre} con capacidad de {self._capacidad}{RESET}{AMARILLO} ubicado en {self._ubicacion}{RESET}"