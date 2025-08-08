from utils.logger_base import log
from .conexion import Conexion
import time

class CursorDelPool:
    # Resource o Context Manager
    def __enter__(self):
        log.debug("Entrando al bloque with")
        self._pool = Conexion.get_pool()
        self._connection = self._pool.getconn()
        self._cursor = self._connection.cursor()
        self._start_time = time.time()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        tiempo_total = time.time() - self._start_time
        log.debug(f"Tiempo total de transaccion: {tiempo_total:.4f} segundos")

        if valor_excepcion:
            self._connection.rollback()
            log.error(f"Ocurrio una excepcion: {valor_excepcion} {tipo_excepcion} {traceback}")
        else:
            self._connection.commit()
            log.debug("Commit de la transaccion")

        self._cursor.close()
        self._pool.putconn(self._connection)
        log.debug("Conexion devuelta al pool")