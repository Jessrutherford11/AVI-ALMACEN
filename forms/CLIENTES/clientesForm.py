class Clientes:
    def __init__(self, codigo, nombres,apellidos, edad, correo, telefono, direccion, empresa):
        self.codigo = codigo
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.correo = correo 
        self.telefono = telefono
        self.direccion = direccion
        self.empresa = empresa
    
    def datosClientesJson(self):
        return {
            "codigo": self.codigo,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "edad": self.edad,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "empresa": self.empresa
        }