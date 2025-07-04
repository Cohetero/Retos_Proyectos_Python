from constantes import VERDE, RESET

class Color:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, color: str):
        self._color = color

    def __str__(self):
        return f"{VERDE}Color: {RESET}{self._color}"