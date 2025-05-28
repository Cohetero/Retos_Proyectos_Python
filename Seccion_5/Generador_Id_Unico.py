# El sistema deberá generar un valor aleatorio de 4 digitos, con ayuda de la función randint
# Finalmente, con los datos obtenidos generar un ID único uniendo los valores como sigue:
# Ejemplo:
#       Nombre              -> Juan     -> JU
#       Apellido            -> Perez    -> PE
#       Año de Nacimiento   -> 1995     -> 95
#       Valor Aleatorio     -> randint  -> 7326
# Resultado ID Único: JUPE957326

from random import randint  # importar random

# Función para validar si los datos de entradas no son vacios
def pedir_dato(campo: str) -> str:
    while True:
        valor = input(f"{campo}: ").strip()
        if valor:       # Valida si en valor no es vacio
            return valor
        print("⚠️  Este campo no puede estar vacío. Intenta de nuevo.")

# Función para validar año de nacimiento
def pedir_anio() -> str:
    while True:
        anio = input("¿Cuáñ es tu anño de nacimiento (YYYY)? ").strip()
        if anio.isdigit() and len(anio) == 4:       # verifica que todos los caracteres sean dígitos
            return anio
        print("❌ El año debe tener 4 dígitos. Intenta de nuevo.")

# Función para generar un ID Unico
def generar_ID_Unico(nombre, apellido, anio) -> str:
    nombre_recortado = nombre.strip().upper()[:2]
    apellido_recortado = apellido.strip().upper()[:2]
    anio_recortado = anio[-2:]  # Últimos 2 dígitos del año
    num_aleatorio = randint(1000, 9999)
    return f"{nombre_recortado}{apellido_recortado}{anio_recortado}{num_aleatorio}"

# Solicitar datos
nombre = pedir_dato("¿Cuál es tu nombre? ")
apellido = pedir_dato("¿Cuál es tu apellido? ")
anio_nacimiento = pedir_anio()

# Generar ID
id_unico = generar_ID_Unico(nombre, apellido, anio_nacimiento)

# Mostrar Resultados
print("\n" + "-" * 30 + "\n")
print(f"Hola {nombre}")
print(f"\tTu nuevo número de identificación (ID) generado por el sistema es: \n\t{id_unico}")