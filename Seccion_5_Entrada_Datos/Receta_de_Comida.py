# Crear un programa para solicitar algunos valores importantes para una receta de comida
# Los valores que debe introducir el usuario son:
#   * Nombre de la Receta
#   * Ingredientes
#   * Tiempo de preparación (en minutos)
#   * Dificultad (Facil, Media, Alta)
# Mandar a imprimir la receta

# Función para validar si los datos de entradas no son vacios
def pedir_dato(campo: str) -> str:
    while True:
        valor = input(f"{campo}: ").strip()
        if valor:       # Valida si en valor no es vacio
            return valor
        print("⚠️  Este campo no puede estar vacío. Intenta de nuevo.")

# Función para validar la dificultad entre opciones permitidas
def pedir_dificultad() -> str:
    opciones = ["Fácil", "Media", "Alta"]
    while True:
        valor = input("Ingrese la dificultad (Fácil, Media, Alta): ").strip().capitalize()      # Convierte la primera letra de una cadena en mayúscula y el resto en minúsculas.
        if valor in opciones:
            return valor
        print("❌ Dificultad no válida. Elija entre: Fácil, Media, Alta.")

print(" Receta de Cocina ".center(80, '*'))
nombre_receta = pedir_dato("Ingrese el nombre de la receta: ")
ingredientes = pedir_dato("Ingrese los ingredientes: ")
tiempo_preparacion = pedir_dato("Ingrese el tiempo de preparación (min): ")
dificultad = pedir_dificultad()

print("\n" + "-" * 30 + "\n")
print(f"Nombre de la receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparación: {tiempo_preparacion}")
print(f"Dificultad: {dificultad}")