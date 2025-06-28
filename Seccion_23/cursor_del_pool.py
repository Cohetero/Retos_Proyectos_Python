from conexion import Conexion
from logger_base import log
import time

class CursorDelPool:
    # Resource o Context Manager
    def __enter__(self):
        log.debug("Entrando al bloque with.")
        self._pool = Conexion.obtener_pool()
        self._conexion = self._pool.getconn()
        self._cursor = self._conexion.cursor()
        self._start_time = time.time()  # Guardamos el tiempo de inicio
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        tiempo_total = time.time() - self._start_time
        log.debug(f"Tiempo total de transacción: {tiempo_total:.4f} segundos")

        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio una excepcion: {valor_excepcion} {tipo_excepcion} {traceback}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transaccion")

        self._cursor.close()
        self._pool.putconn(self._conexion)
        log.debug("Conexion devuelta al pool")

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())