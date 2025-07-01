from constantes import AMARILLO, VERDE, RESET
from collections import Counter # Para hacer el conteo en las listas
from datetime import datetime
import json
import csv

def libros_mas_prestados(ruta_prestamos: str, ruta_libros: str, top_n: int = 5) -> list:
    with open(ruta_prestamos, "r", encoding="utf-8") as file:
        prestamos = json.load(file)

    # Contar las apariciones por ID de libro
    contador = Counter(prestamos.keys())

    # Cargar nombres de libros
    with open(ruta_libros, "r", encoding="utf-8") as file:
        libros = json.load(file)

    diccionario_nombres = {libro["id_libro"]: libro["titulo"] for libro in libros}

    # Convertir a lista con nombre
    resultados = []
    for libro_id, cantidad in contador.most_common(top_n):
        nombre = diccionario_nombres.get(libro_id, "Desconocido")
        resultados.append({"titulo": nombre, "veces_prestado": cantidad})

    return resultados

def usuarios_mas_activos(ruta_prestamos: str, ruta_usuarios: str, top_n: int = 5) -> list:
    with open(ruta_prestamos, "r", encoding="utf-8") as file:
        prestamos = json.load(file)

    # Contar por ID de usuario
    contador = Counter(datos[0] for datos in prestamos.values())

    # Cargar nombres de usuarios
    with open(ruta_usuarios, "r", encoding="utf-8") as file:
        usuarios = json.load(file)
    
    diccionario_nombres = {usuario["id_user"]: usuario["nombre"] + " " + usuario["apellido"] for usuario in usuarios}

    resultados = []
    for usuario_id, cantidad in contador.most_common(top_n):
        nombre = diccionario_nombres.get(usuario_id, "Desconocido")
        resultados.append({"nombre": nombre, "prestamos_realizados": cantidad})

    return resultados

def exportar_csv(nombre_archivo, datos):
    if not datos:
        print(f"{AMARILLO}No hay datos para exportar.{RESET}")
        return

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)

    print(f"{VERDE}Reporte exportadoa '{nombre_archivo}'{RESET}")
