from db.cursor_del_pool import CursorDelPool
from utils.logger_base import log
from .evento import Evento

class EventoDAO:
    _SELECT = "SELECT * FROM eventos ORDER BY id_evento"
    _INSERTAR = (
        "INSERT INTO eventos (tipo, nombre, fecha, ubicacion, extra1, extra2, extra3) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    _ACTUALIZAR = (
        "UPDATE eventos SET tipo=%s, nombre=%s, fecha=%s, ubicacion=%s, extra1=%s, extra2=%s, extra3=%s "
        "WHERE id_evento = %s"
    )
    _ELIMINAR = "DELETE FROM eventos WHERE id_evento = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug("Seleccionando usuarios")
            cursor.execute(cls._SELECT)
            resultados = cursor.fetchall()
            return [Evento(*fila) for fila in resultados]