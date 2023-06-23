class Notificaciones:
    def __init__(self, ID, nombreProducto, stock):
        self.ID = ID
        self.nombreProducto = nombreProducto
        self.stock = stock

    def datosNotificacionesJson(self):
        return{
            'ID': self.ID,
            'nombreProducto': self.nombreProducto,
            'stock': self.stock

        }