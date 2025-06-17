"""
🐍 Reto Semanal #2 - Sistema de Reservas de Citas
🎯 Objetivo:
Crear un programa que permita a los usuarios agendar, cancelar y consultar citas, simulando el sistema de una clínica o consultorio.

✅ Requisitos mínimos:
1. Usa mínimo 2 módulos:
    - main.py (interfaz de usuario)
    - agenda.py (donde estará la lógica con clases)

2. Usa al menos una clase (Cita o Agenda).
3. Guarda las citas en un archivo .txt o .json para persistencia de datos.
4. Cada cita debe tener:
    - Nombre del paciente
    - Fecha y hora
    - Motivo de la cita

💡 Opciones del programa:
    - 📅 Agendar una nueva cita
    - ❌ Cancelar una cita por nombre y fecha
    - 📖 Ver todas las citas agendadas
    - 💾 Las citas deben guardarse automáticamente

✍️ Ejemplo de uso:

Bienvenido al sistema de citas

1. Agendar cita
2. Cancelar cita
3. Ver citas
4. Salir

> 1
Nombre: Mauricio
Fecha (YYYY-MM-DD HH:MM): 2025-06-14 10:30
Motivo: Revisión general
✅ ¡Cita agendada!

> 3
📅 2025-06-14 10:30 - Mauricio: Revisión general
------------------------
⭐ Nivel extra (si te animas):
Verifica que no haya dos citas a la misma hora.

Ordena las citas por fecha.

Usa json en lugar de .txt
"""

from agenda import Agenda
from constantes import *
from datetime import datetime
import json
import os

def limpiar_pantalla():
    os.system("cls" if os.name == 'int' else "clear")

def menu():
    print(f"{CYAN}{" Bienvenido al Consultorio de la Clinica ":=^80}{RESET}")
    print(f"""{AMARILLO}MENU{RESET}
        {CYAN}1. Agendar Cita{RESET}
        {CYAN}2. Cancelar Cita{RESET}
        {CYAN}3. Ver Citas{RESET}
        {CYAN}4. Salir{RESET}""")

def validar_dato(msg: str) -> int:
    while True:
        valor = input(f"{MAGENTA}{msg}{RESET}").strip()
        if valor.isdigit():
            return int(valor)
        else:
            print(f"{ROJO}Tiene que ser un valor numerico...{RESET}")

def validar_fecha_existente(citas: list, fecha: datetime) -> bool:
    for i, cita in enumerate(citas):
        if cita.fecha == fecha:
            return True
    else:
        return False

def formatear_fecha(citas: list, fecha_existe: bool = False) -> datetime:
    formato = FORMATO_FECHA
    while True:
        try:
            fecha = input(f"{MAGENTA}\tFecha{RESET}{AMARILLO}(YYYY-MM-DD HH:MM): {RESET}").strip()
            fecha_conversion = datetime.strptime(fecha, formato)
            if fecha_existe:
                if not validar_fecha_existente(citas, fecha_conversion):
                    return fecha_conversion
                else:
                    print(f"{AMARILLO}\n\tLa fecha: {fecha_conversion}, ya esta agendada...\n{RESET}")
            else:
                return fecha_conversion
        except ValueError:
            print(f"{ROJO}\n\tERROR: Formato de cadena invalido{RESET}\n")

def guardar_archivo_json(citas: list):
    datos = []
    for cita in citas:
            dato = {
                "nombre": cita.nombre_paciente,
                "fecha": cita.fecha.strftime(FORMATO_FECHA),
                "motivo": cita.motivo
            }
            datos.append(dato)
    with open("agenda.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)

def leer_archivo_json() -> list:
    citas = []

    if not os.path.exists("agenda.json"):
        return citas  # El archivo no existe, retornamos lista vacía

    with open("agenda.json", "r", encoding="utf-8") as file:
        contenido = file.read()
        if not contenido.strip():  # El archivo está vacío o lleno de espacios
            return citas

        try:
            datos = json.loads(contenido)  # Convertimos a lista de dicts
            for item in datos:
                cita = Agenda(
                    nombre_paciente = item["nombre"],
                    fecha = datetime.strptime(item["fecha"], FORMATO_FECHA),
                    motivo = item["motivo"]
                )
                citas.append(cita)
        except json.JSONDecodeError:
            print("Archivo JSON con formato invalido.")

    return citas

def ordenar_lista_por_fecha(citas: list):
    citas.sort(key = lambda c: c.fecha)

def agendar_cita(citas: list):
    num_citas = validar_dato("Numero de citas para agendar: ")

    for i in range(num_citas):
        nombre = input(f"{MAGENTA}\n\tNombre del Paciente: {RESET}").strip()
        fecha = formatear_fecha(citas, True)
        motivo = input(f"{MAGENTA}\tMotivo: {RESET}").strip()
        citas.append(Agenda(nombre, fecha, motivo))
        print(f"{VERDE}\t¡Cita agendada!{RESET}")

def cancelar_cita(citas: list):
    print(f"\n{MAGENTA}Introduzca una fecha para cancelar la cita{RESET}")
    fecha = formatear_fecha(citas)

    for i, cita in enumerate(citas):
        if cita.fecha == fecha:
            print(f"\n\t{cita}\n")
            respuesta = input(f"{AMARILLO}\tSeguro que quiere cancelar esta cita? (Si/No){RESET}").strip().lower()

            if respuesta == "si":
                citas.pop(i)
                print(f"\n\t{VERDE}Cita cancelada{RESET}")
            break
    else:
        print(f"{AMARILLO}No se encontro una cita agendanda con la hora dada{RESET}")

def ver_citas(citas: list):
    if len(citas) == 0:
        print(f"{AMARILLO}No hay citas agendadas...{RESET}")
    for cita in citas:
        print(cita)
    print("\n")

if __name__ == "__main__":
    citas = leer_archivo_json()

    while True:
        ordenar_lista_por_fecha(citas)
        limpiar_pantalla()
        menu()
        opcion = validar_dato("> ")

        match opcion:
            case 1:
                print(f"{CYAN}\nAgendar Citas\n{RESET}")
                agendar_cita(citas)
                guardar_archivo_json(citas)
            case 2:
                print(f"{CYAN}\nCancelar Citas\n{RESET}")
                cancelar_cita(citas)
                guardar_archivo_json(citas)
            case 3:
                print(f"{CYAN}\nVer Citas\n{RESET}")
                ver_citas(citas)
            case 4:
                print(f"{CYAN}\nHasta Luego!!!\n{RESET}")
            case _:
                print(f"{CYAN}\nOpcion invalida...\n{RESET}")
    
        if opcion == 4: break

        input("\nEnter para continuar...\n")