# Crear un programa para validar el usuario y password proporcionados por el usuario
# Crea 2 constantes con los valores correctos y posteriormente compara que
# el usuario y password proporcionados por el usario sean validos
# Debe solicitar el usuario y el password al usuario y si son iguales que los
# valores correctos almacenados en las constantes debe imprimir True, de los contrario
# debe imprimir False

from getpass import getpass # Oculta la contraseña al escribir

# Constantes
CORRECT_USER = "Cat_08"
CORRECT_PASSWORD = "1234"
INTENTOS_MAXIMOS = 5

def pedir_dato(campo: str, ocultar: bool = False) -> str:
    while True:
        valor = getpass(f"{campo}: ") if ocultar else input(f"{campo}: ")
        valor = valor.strip()
        if valor:       # Valida si en valor no es vacio
            return valor
        print("⚠️  Este campo no puede estar vacío. Intenta de nuevo.")

# Proceso de validación con intentos
intentos = 0
acceso_concedido = False

while intentos < INTENTOS_MAXIMOS:
    print(f"\n🔒 Intento {intentos + 1} de {INTENTOS_MAXIMOS}")

    # Pedir datos al usuario
    user_input = pedir_dato("Usuario: ")
    password_input = pedir_dato("Contraseña: ", ocultar=True)

    # Validación
    if user_input == CORRECT_USER and password_input == CORRECT_PASSWORD:
        acceso_concedido = True
        break
    else:
        print("❌ El usuario o la contraseña son incorrectos.")

    intentos += 1

# Resultado Final
if acceso_concedido:
    print("\n✅ Usuario confirmado, puede ingresar.")
else:
    print("\n🚫 Has superado el número máximo de intentos. Acceso denegado.")