from inventario.usuario import Usuario
from datetime import datetime as dt
from cosntantes import CYAN, VERDE, RESET, FORMATO_FECHA
import random
import string

class Prestamo:
    def __init__(self, usuario: Usuario, libros: list, fecha_prestamo: dt, fecha_devolucion: dt, devolucion: bool = False, id_prestamo: str = None):
        self._usuario = usuario
        self._libros = libros
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._devolucion = devolucion
        if id_prestamo:
            self._id_prestamo = id_prestamo
        else:
            id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
            self._id_prestamo = f"PRE-{id}"
        

    @property
    def id_prestamo(self) -> int:
        return self._id_prestamo

    @property
    def usuario(self) -> Usuario:
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario: Usuario):
        self._usuario = usuario

    @property
    def libros(self) -> list:
        return self._libros
    
    @libros.setter
    def libros(self, libros: list):
        self._libros = libros

    @property
    def fecha_prestamo(self) -> dt:
        return self._fecha_prestamo
    
    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo: dt):
        self._fecha_prestamo = fecha_prestamo

    @property
    def fecha_devolucion(self) -> dt:
        return self._fecha_devolucion
    
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion: dt):
        self._fecha_devolucion = fecha_devolucion

    @property
    def devolucion(self) -> bool:
        return self._devolucion
    
    @devolucion.setter
    def devolucion(self, devolucion: bool):
        self._devolucion = devolucion

    def to_dict(self):
        return {
            "id_prestamo": self._id_prestamo,
            "usuario": self._usuario.to_dict(),
            "libros": [l.to_dict() for l in self._libros],
            "fecha_prestamo": self._fecha_prestamo.strftime(FORMATO_FECHA),
            "fecha_devolucion": self._fecha_devolucion.strftime(FORMATO_FECHA),
            "devolucion": self._devolucion
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            usuario = data["usuario"],
            libros = data["libros"],
            fecha_prestamo = dt.strptime(data["fecha_prestamo"], FORMATO_FECHA),
            fecha_devolucion = dt.strptime(data["fecha_devolucion"], FORMATO_FECHA),
            id_prestamo = data["id_prestamo"],
            devolucion = data["devolucion"]
        )

    def __str__(self):
        return f"""{VERDE}{self._id_prestamo}:{RESET}
        {CYAN}Usuario: {RESET}{self._usuario.nombre}
        {CYAN}libros: {RESET}{", ".join(l.titulo for l in self._libros)}
        {CYAN}Fecha Prestamo: {RESET}{self._fecha_prestamo.strftime(FORMATO_FECHA)}
        {CYAN}Fecha_Devolucion: {RESET}{self._fecha_devolucion.strftime(FORMATO_FECHA)}"""