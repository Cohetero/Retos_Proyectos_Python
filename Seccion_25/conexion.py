from psycopg_pool import ConnectionPool
from logger_base import log
import atexit
import sys
import os

class Conexion:
    _MIN_CON = 1
    _MAX_CON = 5
    _TIMEOUT = 5
    _pool = None

    @ classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                config = (
                    f"host={os.getenv('DB_HOST', '127.0.0.1')} "
                    f"port={os.getenv('DB_PORT', '5432')} "
                    f"dbname={os.getenv('DB_NAME', 'Test_db')} "
                    f"user={os.getenv('DB_USER', 'postgres')} "
                    f"password={os.getenv('DB_PASSWORD', 'a65B3-19e7A4')} "
                )
                cls._pool = ConnectionPool(
                    conninfo = config,
                    min_size = cls._MIN_CON,
                    max_size = cls._MAX_CON,
                    timeout = cls._TIMEOUT
                )
                atexit.register(cls.cerrar_pool) # Esto cierra las conexionas cuando finaliza el programa
                log.debug(f"Pool de conexiones creado exitosamente: {cls._pool}")
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool: {e}")
                sys.exit()
        return cls._pool

    @classmethod
    def cerrar_pool(cls):
        if cls._pool:
            if not cls._pool.closed:
                cls._pool.close()
                log.debug("Pool de conexiones cerrado.")
            else:
                log.warning("Intento de cerrar un pool ya cerrado")
        else:
            log.warning("Intento de cerrar un poo que nunca fue inicializado")
