from constantes import CYAN, RESET

class Monitor:
    contador_monitores = 0

    def __init__(self, marca: str, tamanio: str):
        self._marca = marca
        self._tamanio = tamanio
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores

    def __str__(self) -> str:
        return f"""{CYAN}ID: {self.__id_monitor}{RESET}
        {CYAN}Marca:{RESET} {self._marca}
        {CYAN}Tamaño:{RESET} {self._tamanio}"""
    
    @property
    def marca(self) -> str:
        return self._marca
    
    @marca.setter
    def marca(self, marca: str):
        self._marca = marca

    @property
    def tamanio(self) -> str:
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: str):
        self._tamanio = tamanio

    @property
    def id(self) -> str:
        return self.__id_monitor