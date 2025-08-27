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
    pausar()
    limpiar_pantalla()
    print(f"{CYAN}{' Sistema de Gestion de Espacios ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
    {CYAN}1. Crear nuevo Espacio.
    2. Listar Todos los Espacios.
    3. Listar Espacios Disponibles.
    4. Actualizar Espacios.
    5. Eliminar Espacios.
    6. Salir.{RESET}""")
    return validar_entero("> ", 1, 6, True)

def crear_diccionario_espacio():
    tipo = validar_entero("Tipo del Espacio:\n\t1. Auditorio\n\t2. Cancha\n\t3. Salon\n", 1, 3, True)
    if tipo == 1:
        tipo = "auditorio"
    elif tipo == 2:
        tipo = "cancha"
    elif tipo == 3:
        tipo = "salón"

    nombre = validar_texto("Nombre del Espacio")
    fecha = validar_texto("Capacidad del Espacio")
    ubicacion = validar_texto("Ubicacion del Espacio")

    espacio = {
        "tipo": tipo,
        "nombre": nombre,
        "capacidad": fecha,
        "ubicacion": ubicacion
    }
    return espacio

def crear_Espacios():
    print(f"{CYAN}\nCrear nuevo espacio!!!\n{RESET}")
    espacio = crear_diccionario_espacio()
    espacios_insertados = EspacioDAO.insertar(espacio)
    print(f"{VERDE}espacios insertados: {RESET}{espacios_insertados}")
    log.info(f"espacios insertados: {espacios_insertados}")

def Listar_todos_Espacios(espacios: list):
    print(f"{CYAN}\nListar todos los espacios!!!\n{RESET}")
    espacios = EspacioDAO.seleccionar()
    #log.info(f"Numero de registros obtenidos con el select: {len(espacios)}")
    for espacio in espacios:
        print(espacio.descripcion_detallada())

def listar_espacios_disponibles():
    print(f"{CYAN}\nListar todos los espacios Disponibles!!!\n{RESET}")
    resultados = EspacioDAO.seleccionar_espacios_disponibles()
    for espacio in resultados:
        print(espacio.descripcion_detallada())

def actualizar_Espacios(espacios: list):
    print(f"{CYAN}\nEditar espacio existente!!!\n{RESET}")
    id_espacio = validar_entero("ID del espacio a actualizar", 0, 0, False)
    espacio = buscar_por_id_espacio(espacios, id_espacio)

    if espacio:
        print(espacio.descripcion_detallada())
        espacio_actualizado = crear_diccionario_espacio()
        espacio_actualizado["id_espacio"] = id_espacio
        espacio_actualizado = EspacioDAO.actualizar(espacio_actualizado)
        print(f"Evento actualizado: {espacio_actualizado}")
        log.info(f"espacio actualizado: {espacio_actualizado}")
    else:
        print(f"{AMARILLO}ID espacio ({id_espacio} no encontrado...){RESET}")

def eliminar_Espacios(espacios: list):
    print(f"{CYAN}\nEliminar espacio!!!\n{RESET}")
    id_espacio = validar_entero("ID del espacio a eliminar", 0, 0, False)
    espacio = buscar_por_id_espacio(espacios, id_espacio)

    if espacio:
        print(espacio.descripcion_detallada())
        eliminacion = validar_si_no("Seguro que que quiere eliminar el espacio?")
        if eliminacion:
            espacio_eliminado = EspacioDAO.eliminar(espacio)
            print(f"espacio elimiando: {espacio_eliminado}")
            log.info(f"espacio elimiando: {espacio_eliminado}")
    else:
        print(f"{AMARILLO}ID espacio ({id_espacio} no encontrado...){RESET}")

def buscar_por_id_espacio(espacios: list, id_espacio: int):
    if espacios:
        for eve in espacios:
            if id_espacio == eve.id_espacio:
                espacio = eve
                break
        else:
            espacio = None
    else:
        espacio = EspacioDAO.seleccionar_buscar_por_id(id_espacio)
    
    return espacio

def menu_Reservas():
    pausar()
    limpiar_pantalla()
    print(f"{CYAN}{' Sistema de Reserva de Espacios ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
    {CYAN}1. Crear nueva Reserva.
    2. Listar Reservas.
    3. Buscar Reservas.
    4. Editar Reservas.
    5. Cancelar Reservas.
    6. Salir.{RESET}""")
    return validar_entero("> ", 1, 6, True)

def main():
    opcion = True
    espacios = []
    reservas = []
    while opcion != 0:
        opcion = menu_principal()
        if opcion == 1:
            while opcion != 6:
                opcion = menu_Espacios()
                match opcion:
                    case 1: crear_Espacios()
                    case 2: Listar_todos_Espacios(espacios)
                    case 3: listar_espacios_disponibles()
                    case 4: actualizar_Espacios(espacios)
                    case 5: eliminar_Espacios(espacios)
                    case 6: print(f"{CYAN}\nRegresando al menu principal\n{RESET}")
        elif opcion == 2:
            while opcion != 6:
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
                    case 6:
                        print(f"{CYAN}\nRegresando al menu principal\n{RESET}")
        else:
            print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")



if __name__ == "__main__":
    main()