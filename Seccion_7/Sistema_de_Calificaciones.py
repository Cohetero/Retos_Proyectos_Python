# Crear un programa para convertir una calificacion numerica (entre 0 y 10)
# a una letra (de la F a la A
#       Si es mayor o igual a 9 y menor o igual a 10 es una A
#       Si es mayor o igual a 8 y menor a 9 es una B
#       Si es mayor o igual a 7 y menor a 8 es una C
#       Si es mayor o igual a 6 y menor a 7 es una D
#       Si es mayor o igual a 0 y menor a 6 es una F

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

def calificacion(cal: int) -> str:
    if 9 <= cal <= 10:
        return "A"
    elif 8 <= cal < 9:
        return "B"
    elif 7 <= cal < 8:
        return "C"
    elif 6 <= cal < 7:
        return "D"
    else:
        return "F"

def pedir_dato(campo: str, tipo: str) -> any:
    while True:
        entrada = input(f"{MAGENTA}{campo}: {RESET}")

        if tipo == "decimal":
            try:
                entrada = float(entrada)
                if 0 <= entrada <= 10:
                    return entrada
                print(f"{AMARILLO}⚠️ El numero debe estar entre 0 y 10.{RESET}")
            except ValueError:
                print(f"{ROJO}❌ Ingresa un numero válido.{RESET}")
        elif tipo == "texto":
            if entrada:
                return entrada.title() # Para capitalizar el nombre
            print(f"{AMARILLO}⚠️ No se aceptan campos vacios.{RESET}")
        else:
            print(f"{ROJO}❌ Tipo de dato no soportado: {tipo}.{RESET}")
            return None  # Fallback por si el tipo es invalido

def calificar_materias(materias: list) -> list:
    calificaciones  = []
    print("Ingrese las calificaciones de cada materia")
    for i, materia in enumerate(materias):
        nota = pedir_dato(f"{i+1}.- {materia}", "decimal")
        calificaciones.append(nota)
    return calificaciones 

def mostrar_reporte (alumnos: str, materias: str):
    print(f"\n{CYAN}{' BOLETA FINAL ':*^80}{RESET}")
    for alumno in alumnos:
        print(f"\n{AZUL}Nombre: {alumno['nombre']} | Promedio: {alumno['promedio']:.2f}{RESET}")
        for i, materia in enumerate(materias):
            nota = alumno['calificaciones'][i]
            print(f"{AMARILLO}{i+1}.- {materia}: {nota:.2f} ({calificacion(nota)}){RESET}")


materias = ["Matematicas", "Geografia", "Fisica", "Programacion", "Historia", "Ingles"]
alumnos = []

while True:
    print(f"{CYAN}{' Sistema de Calificaciones ':*^80}{RESET}")
    nombre = pedir_dato("Nombre del Alumno", "texto")
    calificaciones = calificar_materias(materias)
    promedio = round(sum(calificaciones) / len(calificaciones), 2)
    alumnos.append({
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio
    })
    seguir = input(f"{MAGENTA}Deseas ingresar otro alumno? (s/n):{RESET} ").strip().lower()
    if seguir != 's':
        break

alumnos_ordenados = sorted(alumnos, key=lambda x: x["promedio"], reverse=True)
mostrar_reporte(alumnos_ordenados, materias)