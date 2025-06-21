from usuario import Usuario
from libro import Libro

from datetime import datetime as dt
from cosntantes import AZUL, RESET


class Prestamo:
    def __init__(self, usuario: Usuario, libro: Libro, fecha_prestamo: dt, fecha_devolucion: dt):
        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    @property
    def usuario(self) -> Usuario:
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario: Usuario):
        self._usuario = usuario

    @property
    def libro(self) -> Libro:
        return self._libro
    
    @libro.setter
    def libro(self, libro: Libro):
        self._libro = libro

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