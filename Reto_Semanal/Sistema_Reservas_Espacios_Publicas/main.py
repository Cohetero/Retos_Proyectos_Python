from espacios.espacio_dao import EspacioDAO
from espacios.auditorio import Auditorio
from espacios.cancha import Cancha
from espacios.salon import Salon
from utils.constantes import *
from utils.validador import *
from utils.logger import log

def menu_principal():
    limpiar_pantalla()
    print(f"{AMARILLO}{' MENU ':=^80}{RESET}")
    print(f"""{CYAN}
    1. Menu de Espacios.
    2. Menu de Reservas.
    0. Salir{RESET}""")
    return validar_entero("> ", 0, 2, True)

def menu_Espacios():
    print(f"{CYAN}{' Sistema de Gestion de Espacios ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
    {CYAN}1. Crear nuevo Espacio.
    2. Listar Todos los Espacios.
    3. Listar Espacios Disponibles.
    4. Actualizar Espacios.
    5. Eliminar Espacios.
    0. Salir.{RESET}""")
    return validar_entero("> ", 0, 5, True)

def Listar_todos_Espacios():
    print(f"{CYAN}\nListar todos los espacios!!!\n{RESET}")
    espacios = EspacioDAO.seleccionar()
    #log.info(f"Numero de registros obtenidos con el select: {len(espacios)}")
    for espacio in espacios:
        print(espacio.descripcion_detallada())

def menu_Reservas():
    print(f"{CYAN}{' Sistema de Reserva de Espacios ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
    {CYAN}1. Crear nueva Reserva.
    2. Listar Reservas.
    3. Buscar Reservas.
    4. Editar Reservas.
    5. Cancelar Reservas.
    0. Salir.{RESET}""")
    return validar_entero("> ", 0, 5, True)

def main():
    opcion = True
    espacios = []
    reservas = []
    while opcion != 0:
        opcion = menu_principal()
        if opcion == 1:
            while opcion != 0:
                opcion = menu_Espacios()
                match opcion:
                    case 1:
                        pass
                    case 2: Listar_todos_Espacios()
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 0:
                        print(f"{CYAN}\nRegresando al menu principal\n{RESET}")
        elif opcion == 2:
            while opcion != 0:
                opcion = menu_Reservas()
                match opcion:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 0:
                        print(f"{CYAN}\nRegresando al menu principal\n{RESET}")
        else:
            print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")
        pausar()



if __name__ == "__main__":
    main()