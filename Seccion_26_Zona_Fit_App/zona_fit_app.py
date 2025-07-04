from cliente_dao import ClienteDAO
from cliente import Cliente

print("Clientes de Zona Fit (Gym)".center(100, '*'))
opcion = None

while opcion != 5:
    print("""Menu:
    1. Listas Clientes
    2. Agregar Clientes
    3. Modificar Cliente
    4. Eliminar Cliente
    5. Salir""")
    opcion = int(input("Escribe tu opcion (1-5): "))

    match opcion:
        case 1: # Listar clientes
            clientes = ClienteDAO.seleccionar()
            print("\n*** Listado de Clientes ***")
            for cliente in clientes:
                print(cliente)
            print("\n")
        case 2: # Agregar clientes
            nombre_var = input("Escribe el nombre: ")
            apellido_var = input("Escribe el apellido: ")
            membresia_var = input("Escribe la membresia: ")
            cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
            clientes_insertados = ClienteDAO.insertar(cliente)
            print(f"Clientes Insertados: {clientes_insertados}\n")
        case 3: # Actualizar cliente
            id_cliente_var = input("Escribe la id del cliente a modificar: ")
            nombre_var = input("Escribe el nombre: ")
            apellido_var = input("Escribe el apellido: ")
            membresia_var = input("Escribe la membresia: ")
            cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
            clientes_actualizados = ClienteDAO.actualizar(cliente)
            print(f"Clientes Actualizads: {clientes_actualizados}\n")
        case 4: # Eliminar Cliente
            id_cliente_var = input("Escribe la id del cliente a eliminar: ")
            cliente = Cliente(id=id_cliente_var)
            clientes_eliminados = ClienteDAO.eliminar(cliente)
            print(f"Clientes eliminados: {clientes_eliminados}\n")
        case 5:
            print("Hasta Luego\n")
        case _:
            print("Opcion invalida\n")