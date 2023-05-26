class Entradas:
    def __init__(self, identificador, fecha, nombreProducto, tipoProducto, descripcion, cantidad, usuario, anaquel):
        self.identificador = identificador
        self.fecha = fecha
        self.nombreProducto = nombreProducto
        self.tipoProducto = tipoProducto
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.usuario = usuario
        self.anaquel = anaquel

#Nombre de la tabla en la insercion de la BD
    def datosEntradasJson(self):
        return{
            "identificador": self.identificador,
            "fecha": self.fecha,
            "nombreProducto" : self.nombreProducto,
            "tipoProducto": self.tipoProducto,
            "descripcion" : self.descripcion,
            "cantidad" : self.cantidad,
            "usuario": self.usuario,
            "anaquel": self.anaquel
        }