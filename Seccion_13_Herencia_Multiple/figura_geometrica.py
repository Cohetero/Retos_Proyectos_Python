from constantes import VERDE, RESET

class Figura_Geometrica:
    def __init__(self, alto: float, ancho: float):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self) -> float:
        return self._alto
    
    @alto.setter
    def alto(self, alto: float):
        self._alto = alto

    @property
    def ancho(self) -> float:
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho: float):
        self._ancho = ancho

    def __str__(self):
        return f"{VERDE}\nAncho:{RESET} {self._ancho}{VERDE}\nAlto:{RESET} {self._alto}"