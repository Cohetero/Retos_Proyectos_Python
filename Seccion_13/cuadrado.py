from constantes import AZUL, RESET

from figura_geometrica import Figura_Geometrica
from color import Color

class Cuadrado(Figura_Geometrica, Color):
    def __init__(self, lado: float, color: str):
        Figura_Geometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        a = self.alto * self.ancho
        print(f"{AZUL}\nArea del Cuadrado: {RESET}{a}")

    def __str__(self):
        return super().__str__()