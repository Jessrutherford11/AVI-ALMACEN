#ANAQUELES O ESTANTES DONDE SE ENCONTRARAN DICHOS PRODUCTOS.

class Anaquel:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre      

    
    def datosAnaquelJson(self):
        return {
            "identificador": self.identificador,
            "nombreAnaquel": self.nombre

        }