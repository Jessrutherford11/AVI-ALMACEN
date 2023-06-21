class Salidas():
    def __init__(self, identificador, fecha, tipoProducto, nombreProducto, categoria, cantidad, motivo, distribuidor, transportista, unidad, placas, operador ):
        self.identificador = identificador
        self.fecha = fecha
        self.tipoProducto = tipoProducto
        self.nombreProducto = nombreProducto
        self.categoria = categoria
        self.cantidad = cantidad
        self.motivo = motivo
        self.distribuidor = distribuidor
        self.transportista = transportista
        self.unidad = unidad
        self.placas = placas
        self.operador = operador

    #Nombre de la tabla en la insercion de la BD
    def datosSalidasJson(self):
        return{
            "identificador": self.identificador,
            "fecha": self.fecha,
            "tipoProducto": self.tipoProducto,
            "nombreProducto" : self.nombreProducto,         
            "categoria" : self.categoria,
            "cantidad": self.cantidad,
            "motivo": self.motivo,
            "distribuidor":self.distribuidor,
            "transportista":self.transportista,
            "unidad": self.unidad,
            "placas": self.placas,
            "operador": self.operador
        }