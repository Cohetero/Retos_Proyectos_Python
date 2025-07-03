from cursor_del_pool import CursorDelPool
from persona import Persona
from logger_base import log

class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    """
    _SELECCIONAR = "SELECT * FROM personas ORDER BY id_persona"
    _INSERTAR = "INSERT INTO personas(nombre, apellido, correo) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE personas SET nombre = %s, apellido = %s, correo = %s WHERE id_persona = %s"
    _ELIMINAR = "DELETE FROM personas WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            resultados = cursor.fetchall()
            return [Persona(*fila) for fila in resultados]
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona Insertada: {persona}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Objeto Eliminado: {persona}")
            return cursor.rowcount

if __name__ == "__main__":
    # Insertar un registro
    persona1 = Persona(nombre="Erika", apellido="Villa", email="erika@email.com")
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")

    # Actualizar un registro
    persona1 = Persona(1, "Mauricio", "Cohetero Baltazar", "cba@email.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")

    # Eliminar un registro
    persona1 = Persona(id_persona = 20)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas: {personas_eliminadas}")

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)