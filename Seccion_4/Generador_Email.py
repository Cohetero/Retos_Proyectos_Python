# Crear un programa para generar un email a partir de los siguientes datos:
#   Nombre: Mauricio Cohetero Baltazar
#   Empresa: Empresa Patito
#   Dominio: com.mx
# Resultado Final
#   email: mauricio.cohetero.baltazar@empresapatito.como.mx

# Función para generarl email
def generar_email(nombre: str, empresa: str, dominio: str = ".com.mx") -> str:
    nombre_normalizado = nombre.strip().replace(' ', '.').lower()           # Elimina los espacios en blanco al principio y final, remplaza los espacios por '.'
    empresa_normalizado = empresa.strip().replace(' ', '').lower()          #  y se convierte en minusculas
    return f"{nombre_normalizado}@{empresa_normalizado}{dominio}"

# Función para validar si los datos de entradas no son vacios
def pedir_dato(campo: str) -> str:
    while True:
        valor = input(f"{campo}: ").strip()
        if valor:       # Valida si en valor no es vacio
            return valor
        print("⚠️  Este campo no puede estar vacío. Intenta de nuevo.")

# Función para elegir el dominio
def elegir_dominio() -> str:
    dominios = [".com.mx", ".com", ".org", ".net"]      # Lista para elegir los dominios
    print("\nSelecciona un dominio:")
    for i, d in enumerate(dominios, 1):     # For para iterar y mostrar la lista de los dominios
        print(f"{i}. {d}")
    while True:
        opcion = input("Número de dominio (por defecto 1): ").strip()
        if not opcion:          # Si no se pone nada por default envia el primer valor de la lista
            return dominios[0]
        if opcion.isdigit() and 1 <= int(opcion) <= len(dominios):      # Valida que todos los caracteres sean dígitos y si la opcion esta entre el rango 1 al tamaño de la lista
            return dominios[int(opcion) - 1]
        print("❌ Opción no válida. Elige un número de la lista.")

print(' Generador de Email '.center(80, '*'))
nombre = pedir_dato("Nombre completo: ")
empresa = pedir_dato("Nombre de la empresa: ")
dominio = elegir_dominio()

email = generar_email(nombre, empresa, dominio)
print(f'\nEmail generado: {email}')
