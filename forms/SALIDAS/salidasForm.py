class Salidas():
    def __init__(self, identificador, fecha, tipoProducto, nombreProducto, categoria, cantidad, distribuidor, unidad, placas, operador ):
        self.identificador = identificador
        self.fecha = fecha
        self.tipoProducto = tipoProducto
        self.nombreProducto = nombreProducto
        self.categoria = categoria
        self.cantidad = cantidad
        self.distribuidor = distribuidor
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
            "distribuidor":self.distribuidor,
            "unidad": self.unidad,
            "placas": self.placas,
            "operador": self.operador
        }