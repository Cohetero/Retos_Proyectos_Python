from utilidades.utilidades import VERDE, RESET

class Pelicula:
    def __init__(self, titulo: str, director: str, genero: str, anio: int, duracion: int, calificacion: float):
        self._titulo = titulo
        self._director = director
        self._genero = genero
        self._anio = anio
        self._duracion = duracion
        self._calificacion = calificacion

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def director(self) -> str:
        return self._director
    
    @director.setter
    def director(self, director: str):
        self._director = director

    @property
    def genero(self) -> str:
        return self._genero
    
    @genero.setter
    def genero(self, genero: str):
        self._genero = genero

    @property
    def anio(self) -> int:
        return self._anio
    
    @anio.setter
    def anio(self, anio: int):
        self._anio = anio

    @property
    def duracion(self) -> int:
        return self._duracion
    
    @duracion.setter
    def duracion(self, duracion: int):
        self._duracion = duracion

    @property
    def calificacion(self) -> float:
        return self._calificacion
    
    @calificacion.setter
    def calificacion(self, calificacion: float):
        self._calificacion = calificacion

    def to_dict(self):
        return {
            "titulo": self._titulo,
            "director": self._director,
            "genero": self._genero,
            "anio": self._anio,
            "duracion": self._duracion,
            "calificacion": self._calificacion
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            titulo = data["titulo"],
            director = data["director"],
            genero = data["genero"],
            anio = data["anio"],
            duracion = data["duracion"],
            calificacion = data["calificacion"]
        )

    def __str__(self):
        return f"""{VERDE}Titulo: {RESET} {self._titulo}
        {VERDE}Director: {RESET} {self._director}
        {VERDE}Genero: {RESET} {self._genero}
        {VERDE}Anio: {RESET} {self._anio}
        {VERDE}Duracion: {RESET} {self._duracion}
        {VERDE}Calificacion: {RESET} {self._calificacion}"""
