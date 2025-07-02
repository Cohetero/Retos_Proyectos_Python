from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    _SELECT = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario (username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario = %s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug("Seleccionando usuarios")
            cursor.execute(cls._SELECT)
            resultados = cursor.fetchall()
            return [Usuario(*fila) for fila in resultados]
    
    @classmethod
    def insertar(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Usuario Insertado: {usuario}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Usuario Actualizado: {usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Usuario Eliminado: {usuario}")
            return cursor.rowcount