class Pelicula:
    def __init__(self, nombre: str):
        self._nombre = nombre

    def __str__(self):
        return f"Pelicula: {self._nombre}"

    # Convierte el objeto a diccionaro para guardar en JSON
    def to_dict(self):
        return {"nombre": self._nombre}

    # Convierte un diccionario del JSON en un objeto Pelicula
    @classmethod
    def from_dict(cls, data):
        return cls(nombre = data["nombre"])
