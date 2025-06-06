"""
    Crear un programa para gestionar el inventario de un almacen.
    Para ello se debe utilizar una lista de Python para mantener un
    registro de los productos disponibles en el almacen

    Y para alamacenar el detalle del producto se debe utilizar un diccionario,
    con el id, nombre, precio y cantidad disponible del producto en almacen.
"""

from random import randint
import os

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# Constantes
MIN = 1000
MAX = 9999

def limpiar_pantalla():
    os.system("cls" if os.name == 'int' else "clear")

def menu():
    print(f"{AZUL}{" Sistema de Gestion de Inventario ":=^80}{RESET}\n")
    print(f"""{CYAN} Menu {RESET}{MAGENTA}
    1.- Agregar Producto
    2.- Eliminar Producto
    3.- Buscar Producto
    4.- Modificar Producto
    5.- Mostrar Productos
    6.- Salir{RESET}""")

def validar_Dato(campo: str, tipo: str) -> int:
    while True:
        try:
            valor = input(f"{MAGENTA}{campo}{RESET}").strip()
            if tipo == "int":
                if valor.isdigit():
                    return int(valor)
                print(f"{AMARILLO}Ingrese un numero positivo{RESET}")
            elif tipo == "string":
                return valor
            elif tipo == "float":
                try:
                    return float(valor)
                except ValueError:
                    print(f"{ROJO}Solo se permiten numeros con decimales...{RESET}")
        except Exception as e:
            print(f"{ROJO}ERROR: {e}{RESET}")

def generar_ID(nombre: str, existentes: list) -> str:
    while True:
        nuevo_id = nombre[:3].upper() + str(randint(MIN, MAX))
        if not any(p['ID'] == nuevo_id for p in existentes):
            return nuevo_id

def list_Products(products: list):
    if not products:
        print(f"{AMARILLO}No hay productos en el Inventario{RESET}")
        return

    print(f"{CYAN}\nInventario actual:{RESET}")
    for product in products:
        print(f"""ID: {product['ID']}
            Nombre: {product.get('Nombre')}
            Cantidad: {product.get('Cantidad')}
            Precio: {product.get('Precio'):,.2f}\n{"-"*40}""")

def get_Products(products: list) -> dict:
    no_productos = validar_Dato("\nCuantos productos se agregaran?\n: ", "int")
    nuevos = []

    for _ in range(no_productos):
        nombre = validar_Dato("Nombre del Producto: ","string")
        cantidad = validar_Dato("Cantidad del Producto: ","int")
        precio = validar_Dato("Precio del Producto: ","float")
        ID = generar_ID(nombre, products + nuevos)
        
        nuevos.append({
            "ID": ID,
            "Nombre": nombre,
            "Cantidad": cantidad,
            "Precio": precio
        })
        print(f"{VERDE}Producto '{nombre}' agregado con ID {ID}.{RESET}\n")

    return nuevos

def remove_Product(products: list) -> list:
    if not products:
        print(f"{AMARILLO}No hay productos en el Inventario{RESET}")
        return products

    id = validar_Dato("\nID del Producto a Eliminar\n: ", "string")
    for i, product in enumerate(products):
        if product['ID'] == id:
            print(f"{VERDE}Se elimino {product['ID']}:{product['Nombre']}{RESET}")
            products.pop(i)
            break
    else:
        print(f"{AMARILLO}No se encontro el ID: {id} en la lista de productos...{RESET}")

    return products

def update_Product(products: list) -> list:
    if not products:
        print(f"{AMARILLO}No hay productos en el Inventario{RESET}")
        return products

    id = validar_Dato("\nID del Producto a Modificar\n: ", "string")
    for product in products:
        if product['ID'] == id:
            print(f"{MAGENTA}ENTER para no modificar nada{RESET}")
            valor = validar_Dato("Nombre del Producto: ","string")
            if valor:
                product['Nombre'] = valor
            valor = validar_Dato("Cantidad del Producto: ","int")
            if valor:
                product['Cantidad'] = valor
            valor = validar_Dato("Precio del Producto: ","float")
            if valor:
                product['Precio'] = valor
            print(f"{VERDE}Producto actualizado exitosamente.{RESET}")
            break
    else:
        print(f"{AMARILLO}No se encontro el ID: {id} en la lista de productos...{RESET}")

    return products

def search_Product(products: list):
    if not products:
        print(f"{AMARILLO}No hay productos en el Inventario{RESET}")
        return

    no_productos = validar_Dato("\nCuantos productos va a buscar?\n: ", "int")
    products_res = products.copy()
    search_products = []

    while len(search_products) < no_productos and products_res:
        id = validar_Dato("\nID del Producto a Buscar\n: ", "string")
        for i, product in enumerate(products_res):
            if product['ID'] == id:
                search_products.append(product)
                products_res.pop(i)
                print(f"{VERDE}Producto encontrado: {product['Nombre']}{RESET}")
                break
        else:
            print(f"{AMARILLO}No se encontro el ID: {id} en la lista de productos...{RESET}")

    print(f"{VERDE}Lista de Productos Encontrados{RESET}")
    list_Products(search_products)



def main():
    productos = []
    opcion = 0

    while opcion != 6:
        limpiar_pantalla()
        menu()
        opcion = validar_Dato("-> ", "int")

        if opcion == 1:
            productos.extend(get_Products(productos))
        elif opcion == 2:
            productos = remove_Product(productos)
        elif opcion == 3:
            search_Product(productos)
        elif opcion == 4:
            productos = update_Product(productos)
        elif opcion == 5:
            list_Products(productos)
        elif opcion == 6:
            print(f"{MAGENTA}Cerrando el sistema... ¡Hasta luego!{RESET}")
        else:
            print(f"{ROJO}Opcion invalida. Intente de nuevo.{RESET}")

        input("Enter para continuar...\n")

if __name__ == "__main__":
    main()