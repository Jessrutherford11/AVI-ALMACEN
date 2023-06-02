class Distribuidor:
    def __init__(self, identificador, nombre, direccion, telefono):
        self.identificador = identificador
        self.nombre =  nombre
        self.direccion = direccion
        self.telefono = telefono
        
    
    def datosDistribuidorJson(self):
        return{
            "identificador": self.identificador,
            "nombre": self.nombre,
            "direccion":self.direccion,
            "telefono": self.telefono
        }