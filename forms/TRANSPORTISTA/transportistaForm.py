
class Transportista:
    def __init__(self, identificador, nombre, lineaTransportista,unidad, telefono):
        self.identificador = identificador
        self.nombre =  nombre
        self.lineaTransportista = lineaTransportista
        self.unidad = unidad
        self.telefono = telefono
        
    
    def datosTransportistaJson(self):
        return{
            "identificador": self.identificador,
            "nombre": self.nombre,
            "lineaTransportista": self.lineaTransportista,
            "unidad":self.unidad,
            "telefono": self.telefono
        }
