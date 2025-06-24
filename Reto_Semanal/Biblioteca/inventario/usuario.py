from cosntantes import AZUL, AMARILLO, RESET
import random
import string

class Usuario:
    def __init__(self, nombre: str, apellido: str, libros_prestados: list = [], id_user: str = None):
        self._nombre = nombre
        self._apellido = apellido
        self._libros_prestados = libros_prestados
        if id_user:
            self._id_user = id_user
        else:
            id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
            self._id_user = f"USER-{id}"

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self) -> str:
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido: str):
        self._apellido = apellido

    @property
    def id_user(self) -> int:
        return self._id_user

    @property
    def libros_prestados(self) -> list:
        return self._libros_prestados
    
    @libros_prestados.setter
    def libros_prestados(self, libros_prestados: list):
        self._libros_prestados = libros_prestados

    def to_dict(self):
        return {
            "id_user": self._id_user,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "libros_prestados": self._libros_prestados
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre = data["nombre"],
            apellido = data["apellido"],
            libros_prestados = data["libros_prestados"],
            id_user = data["id_user"]
        )

    def __str__(self):
        return f"""{AMARILLO}{self._id_user}{RESET}
        {AZUL}Nombre: {RESET}{self._nombre}
        {AZUL}Apellid: {RESET}{self._apellido}
        {AZUL}Libros Prestados: {RESET}{', '.join(l.titulo for l in self._libros_prestados)}"""