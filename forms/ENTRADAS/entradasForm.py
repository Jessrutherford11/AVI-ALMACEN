class Entradas:
    def __init__(self, identificador, fecha, codigoProducto, nombreProducto, tipoProducto, descripcion, stock, categoria, anaquel, distribuidor, validacion,observaciones):
        self.identificador = identificador
        self.fecha = fecha
        self.codigoProducto = codigoProducto
        self.nombreProducto = nombreProducto
        self.tipoProducto = tipoProducto
        self.descripcion = descripcion
        self.stock = stock
        self.cateoria = categoria
        self.anaquel = anaquel
        self.distribuidor = distribuidor
        self.validacion = validacion
        self.observaciones = observaciones
        
#Nombre de la tabla en la insercion de la BD
    def datosEntradasJson(self):
        return{
            "identificador": self.identificador,
            "fecha": self.fecha,
            "codigoProducto":self.codigoProducto,
            "nombreProducto" : self.nombreProducto,
            "tipoProducto": self.tipoProducto,
            "descripcion" : self.descripcion,
            "stock" : self.stock,
            "categoria": self.cateoria,
            "anaquel": self.anaquel,
            "distribuidor":self.distribuidor,
            "validacion": self.validacion,
            "observaciones": self.observaciones
        }