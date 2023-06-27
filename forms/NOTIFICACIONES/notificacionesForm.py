class Notificaciones:
    def __init__(self, ID, nombreProducto, stock, fecha):
        self.ID = ID
        self.nombreProducto = nombreProducto
        self.stock = stock
        self.fecha = fecha

    def datosNotificacionesJson(self):
        return{
            'ID': self.ID,
            'nombreProducto': self.nombreProducto,
            'stock': self.stock,
            'fecha': self.fecha

        }