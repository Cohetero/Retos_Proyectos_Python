from constantes import MAGENTA, AZUL, RESET

class Dispositivo_Entrada:
    def __init__(self, marca: str, tipo_entrada: str):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return f"""{AZUL}Marca:{RESET} {self._marca}
        {AZUL}Tipo de entrada:{RESET} {self._tipo_entrada}\n"""
    
    @property
    def marca(self) -> str:
        return self._marca
    
    @marca.setter
    def marca(self, marca: str):
        self._marca = marca

    @property
    def tipo_entrada(self) -> str:
        return self._tipo_entrada
    
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada: str):
        self._tipo_entrada = tipo_entrada

class Raton(Dispositivo_Entrada):
    contador_ratones = 0

    def __init__(self, marca: str, tipo_entrada: str):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones

    def __str__(self) -> str:
        return f"""{AZUL}ID: {self.__id_raton}{RESET}
        """ + super().__str__()
    
    @property
    def id(self) -> str:
        return self.__id_raton

class Teclado(Dispositivo_Entrada):
    contador_teclados = 0

    def __init__(self, marca: str, tipo_entrada: str):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados

    def __str__(self) -> str:
        return f"""{AZUL}ID: {self.__id_teclado}{RESET}
        """ + super().__str__()
    
    @property
    def id(self) -> str:
        return self.__id_teclado