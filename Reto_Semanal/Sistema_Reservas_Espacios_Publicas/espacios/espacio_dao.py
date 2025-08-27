from db.cursor_del_pool import CursorDelPool
from utils.logger import log
from .auditorio import Auditorio
from .cancha import Cancha
from .salon import Salon

class EspacioDAO:
    _SELECT = "SELECT * FROM espacios ORDER BY id;"
    _SELECT_SEARCH_ID_EVENT = "SELECT * FROM espacios WHERE id = %s"
    _SELECT_ESPACIOS_DISPONIBLES = """
        SELECT e.*
        FROM espacios AS e
        LEFT JOIN Reservas AS r ON e.id = r.espacio_id
        WHERE r.espacio_id is NULL
            OR r.fecha > NOW();
    """
    _INSERTAR = (
        "INSERT INTO espacios (tipo, nombre, capacidad, ubicacion)"
        "VALUES (%s, %s, %s, %s);"
    )
    _ACTUALIZAR = (
        "UPDATE espacios SET tipo=%s, nombre=%s, capacidad=%s, ubicacion=%s "
        "WHERE id = %s;"
    )
    _ELIMINAR = "DELETE FROM espacios WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            resultados = cursor.fetchall()
            log.debug("Seleccionando la tabla de espacios")
            return (cls._distribuir_espacios_por_tipo(fila) for fila in resultados)

    @classmethod
    def seleccionar_buscar_por_id(cls, id_evento: int):
        with CursorDelPool() as cursor:
            valores = (id_evento,)
            cursor.execute(cls._SELECT_SEARCH_ID_EVENT, valores)
            resultado = cursor.fetchone()
            log.debug("Buscando eventos por id_evento")
            return cls._distribuir_espacios_por_tipo(resultado) if resultado else None

    @classmethod
    def seleccionar_espacios_disponibles(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT_ESPACIOS_DISPONIBLES)
            resultados = cursor.fetchall()
            log.debug("Seleccionando la tabla de espacios")
            return (cls._distribuir_espacios_por_tipo(fila) for fila in resultados)

    @classmethod
    def insertar(cls, espacio: dict):
        with CursorDelPool() as cursor:
            valores = (espacio["tipo"], espacio["nombre"], espacio["capacidad"], espacio["ubicacion"])
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Espacio Insertado: {espacio}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, espacio: dict):
        with CursorDelPool() as cursor:
            valores = (espacio["tipo"], espacio["nombre"], espacio["capacidad"], espacio["ubicacion"], espacio["id_espacio"])
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Espacio Actualizado: {espacio}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, espacio):
        with CursorDelPool() as cursor:
            valores = (espacio.id_espacio,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Espacio Eliminado: {espacio}")
            return cursor.rowcount

    def _distribuir_espacios_por_tipo(fila: list):
        tipo = fila[1].lower()
        if tipo == "auditorio":
            return Auditorio(
                id_espacio = fila[0],
                nombre = fila[2],
                capacidad = fila[3],
                ubicacion = fila[4]
            )
        elif tipo == "cancha":
            return Cancha(
                id_espacio = fila[0],
                nombre = fila[2],
                capacidad = fila[3],
                ubicacion = fila[4]
            )
        elif tipo == "salón":
            return Salon(
                id_espacio = fila[0],
                nombre = fila[2],
                capacidad = fila[3],
                ubicacion = fila[4]
            )
        else:
            log.error("Tipo de evento desconocido: " + fila)
            raise ValueError("Tipo de evento desconocido")