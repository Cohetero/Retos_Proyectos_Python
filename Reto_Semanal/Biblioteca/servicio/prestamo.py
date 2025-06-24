from inventario.usuario import Usuario
from inventario.libro import Libro
from utilidades import validar_opcion
from datetime import datetime as dt, timedelta
from constantes import *
import random
import string
import json

class Prestamo:
    def __init__(self):
        self._usuarios = self.cargar_datos(RUTA_JSON_USUARIOS, Usuario)
        self._libros = self.cargar_datos(RUTA_JSON_LIBROS, Libro)
        self._historial = self.cargar_historial() # clave: id_libro → (id_usuario, fecha_prestamo)
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
        self._id_prestamo = f"PRE-{id}"

    @property
    def id_prestamo(self) -> int:
        return self._id_prestamo

    @property
    def usuarios(self) -> list:
        return self._usuarios
    
    @usuarios.setter
    def usuarios(self, usuarios: list):
        self._usuarios = usuarios

    @property
    def libros(self) -> list:
        return self._libros
    
    @libros.setter
    def libros(self, libros: list):
        self._libros = libros

    @property
    def historial(self) -> dt:
        return self._historial
    
    @historial.setter
    def historial(self, historial: dict):
        self._historial = historial

    # Funciones de carga y guardado 
    def cargar_datos(self, archivo, clase):
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                datos = json.load(file)
            return [clase.from_dict(d) for d in datos]
        except FileNotFoundError:
            return []

    def guardar_datos(self):
        with open(RUTA_JSON_LIBROS, "w", encoding="utf-8") as file:
            json.dump([libro.to_dict() for libro in self.libros], file, indent=4)
        with open(RUTA_JSON_USUARIOS, "w", encoding="utf-8") as file:
            json.dump([usuario.to_dict() for usuario in self.usuarios], file, indent=4)

    def cargar_historial(self):
        try:
            with open(RUTA_JSON_PRESTAMOS, "r", encoding="utf-8") as file:
                return json.loaf(file)
        except FileNotFoundError:
            return {}

    def guardar_historial(self):
        with open(RUTA_JSON_PRESTAMOS, "w", encoding="utf-8") as file:
            json.dump(self.historial, file, indent=4)

    # Funciones de menu
    def registrar_libro(self):
        print(f"{CYAN}\nRegistrar Libro\n{RESET}")

        nombre = input(f"{MAGENTA}Nombre: {RESET}").strip()
        autor = input(f"{MAGENTA}Autor: {RESET}").strip()
        print()
        anio = validar_opcion("Fecha de Publicacion: ", 1800, 2050)
        n_generos = validar_opcion("Cuantos generos tiene? ", 1, 6)
        generos = []

        print("\n")
        for j in range(n_generos):
            genero = input(f"{j+1}°: ").strip()
            generos.append(genero)

        nuevo = Libro(nombre, autor, anio, generos)
        self.libros.append(nuevo)
        self.guardar_datos()
        print(f"{VERDE}\nLibro registrado con ID {nuevo.id_libro}.{RESET}")

    def registrar_usuario(self):
        print(f"{CYAN}\nRegistrar usuario\n{RESET}")

        nombre = input(f"{MAGENTA}Nombre: {RESET}").strip()
        apellido = input(f"{MAGENTA}Apellido/s: {RESET}").strip()

        nuevo = Usuario(nombre, apellido)
        self.usuarios.append(nuevo)
        self.guardar_datos()
        print(f"{VERDE}\nUsuario registrado con ID {nuevo.id_user}.{RESET}")

    def prestar_libros(self):
        self.mostrar_usuarios()
        id_user = input(f"{MAGENTA}ID del usuario: {RESET}").strip()
        usuario = next((u for u in self.usuarios if u.id_user == id_user), None)
        if not usuario:
            print(f"{ROJO}Usuario no encontrado.{RESET}")
            return

        self.mostrar_libros(disponibles = True)
        id_libro = input(f"{MAGENTA}ID del libro a prestar: {RESET}").strip()
        libro = next((l for l in self.libros if l.id_libro == id_libro and l.disponible), None)

        if not libro:
            print(f"{ROJO}Libro no encontrado o no disponible{RESET}")
            return
        
        libro.disponible = False
        usuario.libros_prestados.append(libro.id_libro)
        self.historial[libro.id_libro] = (usuario.id_user, dt.now().strftime(FORMATO_FECHA))
        self.guardar_datos()
        self.guardar_historial()
        print(f"{VERDE}Libro prestados correctamente.{RESET}")

    def devolver_libros(self):
        print(f"{CYAN}\nDevolver Libros\n{RESET}")
        id_libro = input(f"{MAGENTA}ID del libro a devolver:{RESET}").strip()
        libro = next((l for l in self.libros if l.id_libro == id_libro), None)
        if not libro or libro.disponible:
            print(f"{ROJO}\nLibro no Valido o ya Devuelto...{RESET}")
            return

        libro.disponible = True
        for usuario in self.usuarios:
            if id_libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(id_libro)
                break

        self.historial.pop(id_libro, None)
        self.guardar_datos()
        self.guardar_historial()
        print(f"{VERDE}Libro devuelto correctamente.{RESET}")

    def buscar_libros(self):
        print(f"{CYAN}\nBuscar Libros\n{RESET}")
        busqueda = input(f"{MAGENTA}Buscar por Titulo o Autor: {RESET}").lower().strip()
        resultados = [l for l in self.libros if busqueda in l.titulo.lower() or busqueda in l.autor.lower()]

        if resultados:
            print(f"{CYAN}\nResultados encontrados:\n{RESET}")
            for l in resultados:
                print(l)
        else:
            print(f"{ROJO}\nNo se encontraro libros con ese termino.\n{RESET}")

    def mostrar_libros(self, disponibles: bool = None):
        print(f"{CYAN}\nLista de todos los libros.\n{RESET}")
        for libro in self.libros:
            if disponibles is None or libro.disponible == disponibles:
                print(libro)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def mostrar_prestamos_activos(self):
        print(f"{CYAN}\nMostrar todos los prestamos activos\n{RESET}")
        for id_libro, (id_user, fecha) in self.historial.items():
            print(f"{id_libro} prestado a {id_user} desde {fecha}")

    def mostrar_prestamos_vencidos(self):
        print(f"{CYAN}\nMostrar todos los prestamos vencidos\n{RESET}")
        fecha_actual = dt.now()
        for id_libro, (id_user, fecha_str) in self.historial.items():
            fecha = dt.strptime(fecha_str, FORMATO_FECHA)
            if fecha_actual - fecha > timedelta(days=7):
                print(f"{id_libro} → {id_user} | Prestado el {fecha_str}")

    def mostrar_estadisticas(self):
        total = len(self.libros)
        prestados = sum(not l.disponible for l in self.libros)
        disponibles = total - prestados
        print(f"{CYAN}\nEstadisticas:\n{RESET}")
        print(f"""
        * {VERDE}Total de libros:{RESET} {total}
        * {VERDE}Total de usuarios:{RESET} {len(self.usuarios)}
        * {VERDE}Libros prestados actualmente:{RESET} {prestados}
        * {VERDE}Libros disponibles:{RESET} {disponibles}""")