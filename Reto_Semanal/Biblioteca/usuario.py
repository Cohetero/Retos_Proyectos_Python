from cosntantes import AZUL, RESET

class Usuario:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._id_user = 1
        self._libros_prestados = []

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def id_user(self) -> int:
        return self._id_user

    @property
    def libros_prestados(self) -> list:
        return self._libros_prestados
    
    @libros_prestados.setter
    def libros_prestados(self, libros_prestados: list, flag: bool):
        if flag:
            self._libros_prestados = libros_prestados
        else:
            self._libros_prestados.extend(libros_prestados)