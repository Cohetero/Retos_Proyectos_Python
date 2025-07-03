from constantes import AZUL, RESET

from figura_geometrica import Figura_Geometrica
from color import Color

class Rectangulo(Figura_Geometrica, Color):
    def __init__(self, ancho: float, alto: float, color: str):
        Figura_Geometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def area(self):
        a = self.alto * self.ancho
        print(f"{AZUL}\nArea del Rectangulo: {RESET}{a}")

    def __str__(self):
        return super().__str__()