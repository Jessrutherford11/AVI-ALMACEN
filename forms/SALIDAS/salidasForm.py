class Salidas ():
    def __init__(self, identificador, fecha, nombreProducto, tipoProducto, categoria, cantidad, distribuidor, unidad, placas, operador ):
        self.identificador = identificador
        self.fecha = fecha
        self.nombreProducto = nombreProducto
        self.tipoProducto = tipoProducto
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
            "nombreProducto" : self.nombreProducto,
            "tipoProducto": self.tipoProducto,
            "categoria" : self.categoria,
            "cantidad": self.cantidad,
            "distribuidor":self.distribuidor,
            "unidad": self.unidad,
            "placas": self.placas,
            "operador": self.operador
        }