from constantes import VERDE, RESET

class Libro:
    contador_libros = 0

    def __init__(self, titulo: str, autor: str, generos: list):
        self._titulo = titulo
        self._autor = autor
        self._generos = generos
        Libro.contador_libros += 1
        self._id = Libro.contador_libros

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, autor: str):
        self._autor = autor
    
    @property
    def generos(self) -> list:
        return self._generos
    
    @generos.setter
    def generos(self, generos: list):
        self._generos = generos

    @property
    def id(self) -> int:
        return self._id

    @classmethod
    def get_contador_libros(cls) -> int:
        return cls.contador_libros
    
    def imprimir(self):
        generos_str = ", ".join(self._generos)
        print(f"""{VERDE}{self._id} - {self._titulo}{RESET}:
        Autor: {VERDE}{self._autor}{RESET}
        generos: {VERDE}{generos_str}{RESET}\n""")