from inventario.usuario import Usuario
from datetime import datetime as dt
from cosntantes import CYAN, VERDE, RESET, FORMATO_FECHA
import random
import string

class Prestamo:
    def __init__(self, usuario: Usuario, libros: list, fecha_prestamo: dt, fecha_devolucion: dt):
        self._usuario = usuario
        self._libros = libros
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
        self._id_prestamo = f"PRE-{id}"
        self._devolucion = False

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

    def __str__(self):
        return f"""{VERDE}{self._id_prestamo}:{RESET}
        {CYAN}Usuario: {RESET}{self._usuario.nombre}
        {CYAN}libros: {RESET}{", ".join(l.titulo for l in self._libros)}
        {CYAN}Fecha Prestamo: {RESET}{self._fecha_prestamo.strftime(FORMATO_FECHA)}
        {CYAN}Fecha_Devolucion: {RESET}{self._fecha_devolucion.strftime(FORMATO_FECHA)}"""