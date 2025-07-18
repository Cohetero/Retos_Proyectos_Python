from eventos.evento_dao import EventoDAO
from eventos.exposicion import Exposicion
from eventos.concierto import Concierto
from eventos.taller import Taller
from utils.logger_base import log
from utils.constantes import *
from utils.validador import *

import json
import csv

def menu():
    print(f"{CYAN}{' Sistema Gestion Eventos ':=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
        {CYAN}1. Crear nuevo evento
        2. Listar todos los eventos
        3. Buscar por fecha
        4. Editar evento existente
        5. Eliminar evento
        6. Exportar a CSV
        0. Salir{RESET}""")

def crear_diccionario_evento():
    tipo = validar_entero("Tipo del Evento:\n\t1. Exposición\n\t2. Concierto\n\t3. Taller\n", 1, 3, True)
    if tipo == 1:
        tipo = "Exposición"
    elif tipo == 2:
        tipo = "Concierto"
    elif tipo == 3:
        tipo = "Taller"

    nombre = validar_texto("Nombre del Evento")
    fecha = validar_fecha(FORMATO_FECHA_HORA)
    ubicacion = validar_texto("Ubicacion del Evento")
    extra1 = input(f"{MAGENTA}Extra 1 (ENTER para saltarlo){RESET}: ").strip()
    extra2 = input(f"{MAGENTA}Extra 2 (ENTER para saltarlo){RESET}: ").strip()
    extra3 = input(f"{MAGENTA}Extra 3 (ENTER para saltarlo){RESET}: ").strip()

    evento = {
        "tipo": tipo,
        "nombre": nombre,
        "fecha": fecha,
        "ubicacion": ubicacion,
        "extra1": None if not extra1 else extra1,
        "extra2": None if not extra2 else extra2,
        "extra3": None if not extra3 else extra3
    }
    return evento

def buscar_por_id_evento(eventos: list, id_evento: int):
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

def exportar_csv(eventos: list):
    print(f"{CYAN}\nExportar a CSV!!!\n{RESET}")

    if not eventos:
        eventos = EventoDAO.seleccionar_todo()

    with open(RUTA_EVENTOS_CSV, "w", newline="", encoding="utf-8") as csvfile:
        headers = ["id_evento", "tipo", "nombre", "fecha", "ubicacion", "extra1", "extra2", "extra3"]
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()

        for evento in eventos:
            writer.writerow(evento.to_dict())

    print(f"{VERDE}Reporte exportado '{RUTA_EVENTOS_CSV}'{RESET}")

def main():
    opcion = None
    eventos = []
    while opcion != 0:
        limpiar_pantalla()
        menu()
        opcion = validar_entero("> ", 0, 6, True)

        match opcion:
            case 1:
                print(f"{CYAN}\nCrear nuevo evento!!!\n{RESET}")
                evento = crear_diccionario_evento()
                eventos_insertados = EventoDAO.insertar(evento)
                print(f"{VERDE}Eventos insertados: {RESET}{eventos_insertados}")
                log.info(f"Eventos insertados: {eventos_insertados}")

            case 2:
                print(f"{CYAN}\nListar todos los eventos!!!\n{RESET}")
                busqueda = validar_si_no("Desea ordernar por fecha? ")
                eventos = EventoDAO.seleccionar_todo(busqueda)
                log.info(f"Numero de registros obtenidos con el select: {len(eventos)}")
                for evento in eventos:
                    print(evento.descripcion_detallada())

            case 3:
                print(f"{CYAN}\nBuscar por fecha!!!\n{RESET}")
                fecha = validar_fecha(FORMATO_FECHA_DIA)
                eventos = EventoDAO.seleccionar_buscar_por_fecha(fecha)
                log.info(f"Numero de registros obtenidos con el select: {len(eventos)}")
                for evento in eventos:
                    print(evento.descripcion_detallada())
            case 4:
                print(f"{CYAN}\nEditar evento existente!!!\n{RESET}")
                id_evento = validar_entero("ID del evento a actualizar", 0, 0, False)
                evento = buscar_por_id_evento(eventos, id_evento)

                if evento:
                    evento_actualizado = crear_diccionario_evento()
                    evento_actualizado["id_evento"] = id_evento
                    evento_actualizado = EventoDAO.actualizar(evento_actualizado)
                    log.info(f"Evento actualizado: {evento_actualizado}")
                    log.info(f"Evento actualizado: {evento_actualizado}")
                else:
                    print(f"{AMARILLO}ID Evento ({id_evento} no encontrado...){RESET}")
            case 5:
                print(f"{CYAN}\nEliminar evento!!!\n{RESET}")
                id_evento = validar_entero("ID del evento a eliminar", 0, 0, False)
                evento = buscar_por_id_evento(eventos, id_evento)

                if evento:
                    print(evento.descripcion_detallada())
                    eliminacion = validar_si_no("Seguro que que quiere eliminar el evento?")
                    if eliminacion:
                        evento_eliminado = EventoDAO.eliminar(evento)
                        print(f"Evento elimiando: {evento_eliminado}")
                        log.info(f"Evento elimiando: {evento_eliminado}")
                else:
                    print(f"{AMARILLO}ID Evento ({id_evento} no encontrado...){RESET}")
            case 6:
                exportar_csv(eventos)
            case 0:
                print(f"{CYAN}\nGracias por usar el sistema. Hasta Luego!!!\n{RESET}")
        pausar()

if __name__ == "__main__":
    main()