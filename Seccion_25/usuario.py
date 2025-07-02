from constantes import VERDE, CYAN, RESET

class Usuario:
    def __init__(self, id_usuario: int = None, username: str = None, password: str = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return f"{VERDE}Usuario: {RESET}{CYAN}{self._id_usuario} {self._username} {self._password}{RESET}"
    
    @property
    def id_usuario(self) -> int:
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario: int):
        self._id_usuario = id_usuario

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, password: str):
        self._password = password