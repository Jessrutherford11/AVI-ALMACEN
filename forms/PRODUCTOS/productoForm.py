class Producto:
    def __init__(self, codigo, nombreProducto, existencia, descripcion):
        self.codigo = codigo
        self.nombreProducto = nombreProducto
        self.existencia = existencia
        self.descripcion = descripcion

#Insercion en la BD
    def datosProductosJson(self):
        return {
            "codigo": self.codigo,
            "nombreProducto": self.nombreProducto,
            "existencia": self.existencia,
            "descripcion": self.descripcion
        }
