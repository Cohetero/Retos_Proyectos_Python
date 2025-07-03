from dispositivo_entrada import Teclado, Raton
from computadora import Computadora
from monitor import Monitor
from orden import Orden
from constantes import *
import os

def limpiar_pantalla():
    os.system("cls" if os.name == 'int' else "clear")

def menu():
    print(f"{CYAN}{" Bienvenido a la Aplicacion Mundo PC ":=^80}{RESET}")
    print(f"""{AMARILLO}Menu{RESET}
        1. Agregar Raton
        2. Mostrar Ratones
        3. Agregar Teclado
        4. Mostrar Teclados
        5. Agregar Monitor
        6. Mostrar Monitores
        7. Agregar Computadora
        8. Mostrar Computadoras
        9. Agregar Orden
        10. Mostar Ordenes
        11. Salir""")

def mostrar_lista(lista: list):
    for obj in lista:
        print(obj)

def validar_dato(msg: str) -> int:
    while True:
        valor = input(f"{MAGENTA}{msg}{RESET}").strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(f"{ROJO}Tiene que ser un valor numerico...{RESET}")

def agregar_disposito(valor: int, str1: str, str2: str) -> list:
    num_disp = validar_dato("Numero de dispositicos a agregar: ")
    dispositivos = []

    for i in range(num_disp):
        print("\n")
        valor_1 = input(f"{MAGENTA}{str1}: {RESET}").strip()
        valor_2 = input(f"{MAGENTA}{str2}: {RESET}").strip()
        if valor == 1: # Raton
            dispositivos.append(Raton(valor_1, valor_2))
        elif valor == 2: # Teclado
            dispositivos.append(Teclado(valor_1, valor_2))
        else:
            dispositivos.append(Monitor(valor_1, valor_2))

    return dispositivos

def buscar_objeto(id: int, objs: list) -> any:
    for obj in objs:
        if obj.id == id:
            return obj
    else:
        return None
    
def seleccionar_objeto(objs: list, msg: str) -> any:
    while True:
        limpiar_pantalla()
        mostrar_lista(objs)
        id = validar_dato(msg)

        obj = buscar_objeto(id, objs)

        if obj is not None:
            return obj
        else:
            print(f"{ROJO}El ID no se encontro\nIntente de nuevo...{RESET}")
            input("\nEnter para continuar...\n")

def agregar_computadora(ratones: Raton, teclados: Teclado, monitores: Monitor) -> list:
    num_disp = validar_dato("Numero de dispositicos a agregar: ")
    computadoras = []

    for i in range(num_disp):
        print("\n")
        nombre = input(f"{MAGENTA}Nombre para la Computadora: {RESET}").strip()

        raton = seleccionar_objeto(ratones, "ID del Raton: ")
        teclado = seleccionar_objeto(teclados, "ID del Teclado: ")
        monitor = seleccionar_objeto(monitores, "ID del Monitor: ")

        computadoras.append(Computadora(nombre, monitor, teclado, raton))

    return computadoras

def agregar_orden(computadoras: Computadora) -> list:
    num_orden = validar_dato("Numero de ordenes a agregar: ")
    ordenes = []

    for i in range(num_orden):
        ordn = Orden()
        while True:
            print("\n")
            compu = seleccionar_objeto(computadoras, "Id de la Computadora: ")
            ordn.agregar_computadora(compu)

            opcion = input("Desea introduccir otra computadora? (Si/ No) > ").strip()
            if opcion.lower() == "no":
                break
        ordenes.append(ordn)


    return ordenes

if __name__ == "__main__":
    ratones = []
    teclados = []
    monitores = []
    computadoras = []
    ordenes = []

    while True:
        limpiar_pantalla()
        menu()
        opcion = validar_dato("> ")

        match opcion:
            case 1:
                print(f"{CYAN}\nAgregar Raton\n{RESET}")
                ratones.extend(agregar_disposito(1, "Marca", "Tipo de Entrada"))

            case 2:
                print(f"{CYAN}\nMostrar Ratones\n{RESET}")
                mostrar_lista(ratones)

            case 3:
                print(f"{CYAN}\nAgregar Teclado\n{RESET}")
                teclados.extend(agregar_disposito(2, "Marca", "Tipo de Entrada"))

            case 4:
                print(f"{CYAN}\nMostrar Teclados\n{RESET}")
                mostrar_lista(teclados)

            case 5:
                print(f"{CYAN}\nAgregar Monitor\n{RESET}")
                monitores.extend(agregar_disposito(3, "Marca", "Tamaño"))

            case 6:
                print(f"{CYAN}\nMostrar Monitores\n{RESET}")
                mostrar_lista(monitores)

            case 7:
                print(f"{CYAN}\nAgregar Computadora\n{RESET}")
                computadoras.extend(agregar_computadora(ratones, teclados, monitores))

            case 8:
                print(f"{CYAN}\nMostrar Computadoras\n{RESET}")
                mostrar_lista(computadoras)

            case 9:
                print(f"{CYAN}\nAgregar Orden\n{RESET}")

            case 10:
                print(f"{CYAN}\nMostar Ordenes\n{RESET}")

            case 11:
                print(f"{CYAN}\nHasta Luego!!!\n{RESET}")

            case _:
                print(f"{AMARILLO}\nOpcion invalida...\n{RESET}")

        if opcion == 11:
            break
        input("\nEnter para continuar...\n")