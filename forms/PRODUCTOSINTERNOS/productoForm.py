#Tabla en la BD. << PRODUCTOS INTERNOS >>

class Producto:
    def __init__(self, codigo, nombreProducto, categoria, stock, precio, estante, distribuidor, descripcion, estado):
        self.codigo = codigo
        self.nombreProducto = nombreProducto
        self.categoria = categoria
        self.stock = stock
        self.precio = precio
        self.estante = estante
        self.distribuidor = distribuidor
        self.descripcion = descripcion
        self.estado = estado
#Insercion en la BD
    def datosProductosJson(self):
        return {
            "codigo": self.codigo,
            "nombreProducto": self.nombreProducto,
            "categoria": self.categoria,
            "stock": self.stock,
            "precio": self.precio,
            "estante": self.estante,
            "distribuidor": self.distribuidor,
            "descripcion": self.descripcion,
            "estado": self.estado
        }
