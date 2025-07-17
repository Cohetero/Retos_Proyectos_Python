from db.cursor_del_pool import CursorDelPool
from utils.logger_base import log
from .evento import Evento

class EventoDAO:
    _SELECT = "SELECT * FROM eventos ORDER BY id_evento"
    _SELECT_SEARCH_ID_EVENT = "SELECT * FROM eventos WHERE id_evento = %s"
    _SELECT_SEARCH_DATE = "SELECT * FROM eventos WHERE fecha::date = %s"
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
    def seleccionar_todo(cls, ordernar_fecha: bool):
        with CursorDelPool() as cursor:
            if ordernar_fecha:
                select = cls._SELECT.replace("id_evento", "fecha")
            else:
                select = cls._SELECT
            cursor.execute(select)
            resultados = cursor.fetchall()
            log.debug("Seleccionando eventoss")
            return [Evento(*fila) for fila in resultados]

    @classmethod
    def seleccionar_buscar_por_id(cls, id_evento: int):
        with CursorDelPool() as cursor:
            valores = (id_evento,)
            cursor.execute(cls._SELECT_SEARCH_ID_EVENT, valores)
            resultado = cursor.fetchone()
            log.debug("Buscando eventos por id_evento")
            return Evento(*resultado) if resultado else None

    @classmethod
    def seleccionar_buscar_por_fecha(cls, fecha):
        with CursorDelPool() as cursor:
            valores = (fecha,)
            cursor.execute(cls._SELECT_SEARCH_DATE, valores)
            resultados = cursor.fetchall()
            log.debug("Buscando eventos por fecha")
            return [Evento(*fila) for fila in resultados]

    @classmethod
    def insertar(cls, evento: Evento):
        with CursorDelPool() as cursor:
            valores = (evento.tipo, evento.nombre, evento.fecha, evento.ubicacion, evento.extra1, evento.extra2, evento.extra3)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Evento Insertado: {evento}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, evento: Evento):
        with CursorDelPool() as cursor:
            valores = (evento.tipo, evento.nombre, evento.fecha, evento.ubicacion, evento.extra1, evento.extra2, evento.extra3, evento.id_evento)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Evento Actualizado: {evento}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, evento: Evento):
        with CursorDelPool() as cursor:
            valores = (evento.id_evento,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Evento Eliminado: {evento}")
            return cursor.rowcount