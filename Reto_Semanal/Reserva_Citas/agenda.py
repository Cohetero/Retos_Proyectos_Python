from constantes import AZUL, AMARILLO, RESET
from datetime import datetime

class Agenda:
    def __init__(self, nombre_paciente: str, fecha: datetime, motivo: str):
        self._nombre_paciente = nombre_paciente
        self._fecha = fecha
        self._motivo = motivo

    @property
    def nombre_paciente(self) -> str:
        return self._nombre_paciente
    
    @nombre_paciente.setter
    def nombre_paciente(self, nombre_paciente: str):
        self._nombre_paciente = nombre_paciente

    @property
    def fecha(self) -> datetime:
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha: datetime):
        self._fecha = fecha

    @property
    def motivo(self) -> str:
        return self._motivo
    
    @motivo.setter
    def motivo(self, motivo: str):
        self._motivo = motivo

    def __str__(self):
        return f"""{AZUL}{self._fecha.strftime("%Y-%m-%d %H:%M")}{RESET} - {AMARILLO}{self._nombre_paciente}:{RESET} {self._motivo}"""