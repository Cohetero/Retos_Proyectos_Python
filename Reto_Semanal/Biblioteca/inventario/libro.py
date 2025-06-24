from cosntantes import VERDE, AMARILLO,RESET
import random
import string

class Libro:
    def __init__(self, titulo: str, autor: str, anio: int, generos: list, disponible: bool = True, id_libro: str = None):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._generos = generos
        self._disponible = disponible
        if id_libro:
            self._id_libro = id_libro
        else:
            id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
            self._id_libro = f"LIB-{id}"

    @property
    def id_libro(self) -> int:
        return self._id_libro

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, autor: str):
        self._autor = autor

    @property
    def anio(self) -> int:
        return self._anio
    
    @anio.setter
    def anio(self, anio: int):
        self._anio = anio

    @property
    def disponible(self) -> bool:
        return self._disponible
    
    @disponible.setter
    def disponible(self, disponible: bool):
        self._disponible = disponible

    @property
    def generos(self) -> list:
        return self._generos
    
    @generos.setter
    def generos(self, generos: list):
        self._generos = generos

    def to_dict(self):
        return {
            "id_libro": self._id_libro,
            "titulo": self._titulo,
            "autor": self._autor,
            "anio": self._anio,
            "generos": self._generos,
            "disponible": self._disponible
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            titulo = data["titulo"],
            autor = data["autor"],
            anio = data["anio"],
            generos = data["generos"],
            disponible = data["disponible"],
            id_libro = data["id_libro"]
        )

    def __str__(self):
        return f"""{AMARILLO}{self._id_libro} : {self._titulo}{RESET}
        {VERDE}Autor:{RESET} {self._autor}
        {VERDE}Año:{RESET} {self._anio}
        {VERDE}Generos:{RESET} {', '.join(self._generos)}
        {VERDE}Disponible: {RESET}{'SI' if self._disponible else 'No'}"""