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

print(' Generador de Email '.center(80, '*'))
nombre = pedir_dato("Nombre completo: ")
empresa = pedir_dato("Nombre de la empresa: ")

email = generar_email(nombre, empresa)
print(f'\nEmail generado: {email}')
