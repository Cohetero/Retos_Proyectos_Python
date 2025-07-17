from eventos.evento_dao import EventoDAO
from eventos.evento import Evento
from utils.logger_base import log
from utils.constantes import *
from utils.validador import *

def menu():
    print(f"{CYAN}{' Sistema Gestion Eventos ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
        {CYAN}1. Crear nuevo evento
        2. Listar todos los eventos
        3. Buscar por fecha
        4. Editar evento existente
        5. Eliminar evento
        0. Salir{RESET}""")

def crear_objeto_evento() -> Evento:
    tipo = validar_texto("Tipo del Evento")
    nombre = validar_texto("Nombre del Evento")
    fecha = validar_fecha(FORMATO_FECHA_HORA)
    ubicacion = validar_texto("Ubicacion del Evento")
    extra1 = input(f"{MAGENTA}Extra 1 (ENTER para saltarlo){RESET}: ").strip()
    extra2 = input(f"{MAGENTA}Extra 2 (ENTER para saltarlo){RESET}: ").strip()
    extra3 = input(f"{MAGENTA}Extra 3 (ENTER para saltarlo){RESET}: ").strip()

    evento = Evento(
        tipo = tipo,
        nombre = nombre,
        fecha = fecha,
        ubicacion = ubicacion,
        extra1 = None if not extra1 else extra1,
        extra2 = None if not extra2 else extra2,
        extra3 = None if not extra3 else extra3
    )
    return evento

def buscar_por_id_evento(eventos: list, id_evento: int) -> Evento:
    if eventos:
        for eve in eventos:
            if id_evento == eve.id_evento:
                evento = eve
                break
        else:
            evento = None
    else:
        evento = EventoDAO.seleccionar_buscar_por_id(id_evento)
    
    return evento

def main():
    opcion = None
    eventos = []
    while opcion != 0:
        limpiar_pantalla()
        menu()
        opcion = validar_entero("> ")

        match opcion:
            case 1:
                print(f"{CYAN}\nCrear nuevo evento!!!\n{RESET}")
                evento = crear_objeto_evento()
                eventos_insertados = EventoDAO.insertar(evento)
                print(f"{VERDE}Eventos insertados: {RESET}{eventos_insertados}")
                log.info(f"Eventos insertados: {eventos_insertados}")

            case 2:
                print(f"{CYAN}\nListar todos los eventos!!!\n{RESET}")
                busqueda = validar_si_no("Desea ordernar por fecha? ")
                eventos = EventoDAO.seleccionar_todo(busqueda)
                log.info(f"Numero de registros obtenidos con el select: {len(eventos)}")
                for evento in eventos:
                    evento.descripcion_detallada()

            case 3:
                print(f"{CYAN}\nBuscar por fecha!!!\n{RESET}")
                fecha = validar_fecha(FORMATO_FECHA_DIA)
                eventos = EventoDAO.seleccionar_buscar_por_fecha(fecha)
                log.info(f"Numero de registros obtenidos con el select: {len(eventos)}")
                for evento in eventos:
                    print(evento)
            case 4:
                print(f"{CYAN}\nEditar evento existente!!!\n{RESET}")
                id_evento = validar_entero("ID del evento a actualizar")
                evento = buscar_por_id_evento(eventos, id_evento)

                if evento:
                    evento_actualizado = crear_objeto_evento()
                    evento_actualizado.id_evento = id_evento
                    evento_actualizado = EventoDAO.actualizar(evento_actualizado)
                    log.info(f"Evento actualizado: {evento_actualizado}")
                    log.info(f"Evento actualizado: {evento_actualizado}")
                else:
                    print(f"{AMARILLO}ID Evento ({id_evento} no encontrado...){RESET}")
            case 5:
                print(f"{CYAN}\nEliminar evento!!!\n{RESET}")
                id_evento = validar_entero("ID del evento a eliminar")
                evento = buscar_por_id_evento(eventos, id_evento)

                if evento:
                    print(evento)
                    eliminacion = validar_si_no("Seguro que que quiere eliminar el evento?")
                    if eliminacion:
                        evcento_eliminado = EventoDAO.eliminar(evento)
                        print(f"Evento elimiando: {evcento_eliminado}")
                        log.info(f"Evento elimiando: {evcento_eliminado}")
                else:
                    print(f"{AMARILLO}ID Evento ({id_evento} no encontrado...){RESET}")
            case 0:
                print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")
            case _: 
                print(f"{CYAN}\nOpcion invalida...\n{RESET}")
        pausar()

if __name__ == "__main__":
    main()