#CLASE PARA USUARIO
class Administrador:
    def __init__(self, identificador,name, email, contraseña):
        self.identificador = identificador
        self.name = name
        self.email = email
        self.contraseña = contraseña


    def datosAdministradorJson(self):
        return{
            'identificador': self.identificador,
            'name' : self.name,
            'email' : self.email,
            'contraseña' : self.contraseña
        }