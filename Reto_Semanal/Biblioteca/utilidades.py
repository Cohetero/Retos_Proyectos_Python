from constantes import MAGENTA, ROJO, RESET

def validar_opcion(msg: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            opcion = int(input(f"{MAGENTA}{msg}{RESET}").strip())
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"{ROJO}\nOpcion fuera de rango...{RESET}")
        except ValueError:
            print(f"{ROJO}\nIntroduzca un numero valido...{RESET}")