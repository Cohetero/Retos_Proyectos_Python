class Calculadora:
    """Clase para realizar operaciones básicas entre dos números."""
    # self._nombre Atributo protegido
    # self.__nombre Atributo privado
    def __init__(self, op1: float, op2: float):
        self._operador1 = op1
        self._operador2 = op2

    @property
    def operador1(self) -> float:
        return self._operador1

    @operador1.setter
    def operador1(self, valor: float):
        self._operador1 = valor

    @property
    def operador2(self) -> float:
        return self._operador2

    @operador2.setter
    def operador2(self, valor: float):
        self._operador2 = valor

    def sumar(self) -> float:
        return self._operador1 + self._operador2

    def restar(self) -> float:
        return self._operador1 - self._operador2

    def multiplicar(self) -> float:
        return self._operador1 * self._operador2

    def dividir(self) -> float:
        if self._operador2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return self._operador1 / self._operador2

    def modulo(self) -> float:
        if self._operador2 == 0:
            raise ZeroDivisionError("No se puede hacer modulo entre cero.")
        return self._operador1 % self._operador2
