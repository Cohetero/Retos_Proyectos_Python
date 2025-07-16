class CampoVacioError(Exception):
    """Se lanza cuando el usuario no escribe nada."""
    pass

class FechaInvalidaError(Exception):
    """Se lanza cuando el usuario escribe una fecha pasada"""
    def __init__(self, fecha):
        self.fecha = fecha
        super().__init__(f"La fecha {fecha} no es valida. Tiene que ser una mas actual.")