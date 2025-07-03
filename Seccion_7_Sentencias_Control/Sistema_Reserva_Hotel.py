# Se Solicita crear un sistema de Reservacion de un Hotel.
# Se debe pedir la siguiente informacion al usuario:
#       * Nombre de cliente
#       * Dias de estadia en el Hotel
#       * Cuarto con vista al mar
# El Hotel tiene las siguientes tarifas:
#       * Cuarto sin vista al mar: $ 150.50 x dia
#       * Cuarto con vista al mar: # 190.50 x día
# El sistema debe calcular el costo total de la estadia dependiendo si
# escogio un cuarto con vista al mar o no. Ademas de indicar si escogio
# un cuarto con vista al mar o no.

# Códigos de colores ANSI
RESET = "\033[0m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# Constantes de precios
CUARTO_SIN_VISTA_MAR = 150.50
CUARTO_CON_VISTA_MAR = 190.50

def pedir_dato(
        campo: str,
        tipo: str = "texto",
        minimo: int = None,
        maximo: int = None,
        valor_defecto: any = None
) -> any:
    while True:
        mensaje = f"{MAGENTA}{campo}"
        if valor_defecto is not None:
            mensaje += f" [Por defecto: {valor_defecto}]"
        mensaje += f":{RESET} "

        entrada = input(mensaje).strip()

        # Si el usuario no escribe nada y hay un valor por defecto
        if not entrada and valor_defecto is not None:
            return valor_defecto

        if tipo == "texto":
            if entrada:
                return entrada.title() # Para capitalizar el nombre
            print(f"{AMARILLO}⚠️ No se aceptan campos vacios.{RESET}")
        elif tipo == "entero":
            try:
                valor = int(entrada)
                if minimo is not None and valor < minimo:
                    print(f"{ROJO}❌ El valor debe ser al menos {minimo}.{RESET}")
                    continue
                if maximo is not None and valor > maximo:
                    print(f"{ROJO}❌ El valor no puede ser mayor {maximo}.{RESET}")
                    continue
                return valor
            except ValueError:
                print(f"{ROJO}❌ Tiene que ingresar un número.{RESET}")
        elif tipo == "booleano":
            if entrada.lower() in ("si", "s"):
                return True
            elif entrada.lower() in ("no", "n"):
                return False
            print(f"{AMARILLO}⚠️ Responde con 'Si' o 'No'.{RESET}") 
        else:
            print(f"{ROJO}❌ Tipo de dato no soportado: {tipo}.{RESET}")
            return None  # Fallback por si el tipo es invAlido

def calcular_costo(dias: int, vista_mar: bool) -> float:
    tarifa = CUARTO_CON_VISTA_MAR if vista_mar else CUARTO_SIN_VISTA_MAR
    return dias * tarifa

print(f"{CYAN} Bienvenido al Sistema de Reservacion del Hotel{RESET}")
nombre_cliente = pedir_dato("Introduzca su nombre", tipo="texto")
dias_estancia = pedir_dato("Cuantos dias estara en estadia?", tipo="entero", minimo=1, maximo=15)
cuarto_vista_mar = pedir_dato("Quiere el cuarto con vista al mar? (SI/NO)", tipo="booleano", valor_defecto=False)

costo_total = calcular_costo(dias_estancia, cuarto_vista_mar)

print(f"{AZUL}Hola {nombre_cliente}{RESET}")
print(f"Ha elegido cuarto con vista al mar? {'Si' if cuarto_vista_mar else 'No'}")
print(f"{VERDE}Costo Total de la estadia: ${costo_total:,.2f}{RESET}")