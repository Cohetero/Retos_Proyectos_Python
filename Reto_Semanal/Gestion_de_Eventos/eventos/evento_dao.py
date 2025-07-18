from db.cursor_del_pool import CursorDelPool
from utils.logger_base import log
from .exposicion import Exposicion
from .concierto import Concierto
from .taller import Taller

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
    def seleccionar_todo(cls, ordernar_fecha: bool = False):
        with CursorDelPool() as cursor:
            if ordernar_fecha:
                select = cls._SELECT.replace("id_evento", "fecha")
            else:
                select = cls._SELECT
            cursor.execute(select)
            resultados = cursor.fetchall()
            log.debug("Seleccionando eventoss")
            return [cls._construir_evento_desde_fila(fila) for fila in resultados]

    @classmethod
    def seleccionar_buscar_por_id(cls, id_evento: int):
        with CursorDelPool() as cursor:
            valores = (id_evento,)
            cursor.execute(cls._SELECT_SEARCH_ID_EVENT, valores)
            resultado = cursor.fetchone()
            log.debug("Buscando eventos por id_evento")
            return cls._construir_evento_desde_fila(resultado) if resultado else None

    @classmethod
    def seleccionar_buscar_por_fecha(cls, fecha):
        with CursorDelPool() as cursor:
            valores = (fecha,)
            cursor.execute(cls._SELECT_SEARCH_DATE, valores)
            resultados = cursor.fetchall()
            log.debug("Buscando eventos por fecha")
            return [cls._construir_evento_desde_fila(fila) for fila in resultados]

    @classmethod
    def insertar(cls, evento: dict):
        with CursorDelPool() as cursor:
            valores = (evento["tipo"], evento["nombre"], evento["fecha"], evento["ubicacion"], evento["extra1"], evento["extra2"], evento["extra3"])
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Evento Insertado: {evento}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, evento):
        with CursorDelPool() as cursor:
            valores = (evento["tipo"], evento["nombre"], evento["fecha"], evento["ubicacion"], evento["extra1"], evento["extra2"], evento["extra3"], evento["id_evento"])
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Evento Actualizado: {evento}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, evento):
        with CursorDelPool() as cursor:
            valores = (evento.id_evento,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Evento Eliminado: {evento}")
            return cursor.rowcount

    def _construir_evento_desde_fila(fila: list):
        tipo = fila[1]
        if tipo.lower() == "concierto":
            return Concierto(
                id_evento = fila[0],
                nombre = fila[2],
                fecha = fila[3],
                ubicacion = fila[4],
                banda = fila[5],
                genero = fila[6]
            )
        elif tipo.lower() == "exposición":
            return Exposicion(
                id_evento = fila[0],
                nombre = fila[2],
                fecha = fila[3],
                ubicacion = fila[4],
                artista = fila[5],
                tipo_arte = fila[6]
            )
        elif tipo.lower() == "taller":
            return Taller(
                id_evento = fila[0],
                nombre = fila[2],
                fecha = fila[3],
                ubicacion = fila[4],
                ponente = fila[5],
                duracion_horas = fila[5],
                requisitos = fila[7]
            )
        else:
            raise ValueError("Tipo de evento desconocido")