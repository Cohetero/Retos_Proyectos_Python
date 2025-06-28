from psycopg_pool import ConnectionPool
from logger_base import log
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
                    f"dbname={os.getenv('DB_NAME', 'test_db')} "
                    f"user={os.getenv('DB_USER', 'postgres')} "
                    f"password={os.getenv('DB_PASSWORD', '1234')} "
                )
                cls._pool = ConnectionPool(
                    conninfo = config,
                    min_size = cls._MIN_CON,
                    max_size = cls._MAX_CON,
                    timeout = cls._TIMEOUT
                )
                log.debug(f"Pool de conexiones creado exitosamente: {cls._pool}")
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool: {e}")
                sys.exit()
        return cls._pool

    #@classmethod
    #def obtenerConexion(cls):
    #    # getconn Se encarga de regresar un objeto de conexion hacia la base de datos
    #    conexion = cls.obtenerPool().getconn()
    #    log.debug(f"Conexion obtenida del pool: {conexion}")
    #    return conexion

    #@classmethod
    #def liberarConexion(cls, conexion):
    #    # Coloca el objeto de conexion de nueva cuenta en el pull de conexiones
    #    cls.obtenerPool().putconn(conexion)
    #    log.debug(f"Rregresamos la conexión al pool: {conexion}")

    @classmethod
    def cerrar_pool(cls):
        if cls._pool and not cls._pool.closed:
            cls._pool.close()
            log.debug("Pool de conexiones cerrado.")
        # Se cierran todos los objetos de conexion
        #cls.obtenerPool().close()

if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()