from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente;"
    INSERTAR = "INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s);"
    ACTUALIZAR = "UPDATE cliente SET nombre = %s, apellido = %s, membresia = %s WHERE id_cliente = %s;"
    ELIMINAR = "DELETE FROM cliente WHERE id_cliente = %s;"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)

            return clientes
        except Exception as e:
            print(f"Ocurrio un errror al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente: Cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrio un errror al insertar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente: Cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrio un errror al eliminar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente: Cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()

            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrio un errror al eliminar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == "__main__":
    # Insertar
    # cliente1 = Cliente(nombre="Nyla", apellido="Scrum", membresia=470)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f"Clientes insertados: {clientes_insertados}")

    # Actualizar
    # cliente1 = Cliente(3, "Eri", "Flores", 480)
    # clientes_actualizados = ClienteDAO.actualizar(cliente1)
    # print(f"Clientes actualizados: {clientes_actualizados}")

    # Eliminar
    cliente1 = Cliente(id = 4)
    clientes_eliminados = ClienteDAO.eliminar(cliente1)
    print(f"Clientes eliminados: {clientes_eliminados}")

    # Seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)