class Cliente:
    def __init__(self, id: int = None, nombre: str = None, apellido: str = None, membresia: int = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, "
                f"Apellido: {self.apellido}, Membresia: {self.membresia}")
