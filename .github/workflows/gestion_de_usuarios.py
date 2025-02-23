## gestion_de_usuarios.py
class GestionDeUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, username, password):
        if username in self.usuarios:
            raise ValueError("El usuario ya existe.")
        self.usuarios[username] = password

    def autenticar_usuario(self, username, password):
        return self.usuarios.get(username) == password
