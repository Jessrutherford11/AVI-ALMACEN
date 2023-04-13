class Categoria:
    #Iniciar
    def __init__(self, codigo, nombreCategoria):
        self.codigo = codigo
        self.nombreCategoria = nombreCategoria
#Insercion en la BD
    def datosCategoriasJson(self):
        return {
            "codigo": self.codigo,
            "nombreCategoria": self.nombreCategoria
        } 