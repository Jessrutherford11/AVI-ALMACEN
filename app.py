#PRINCIPAL. 
#Importaciones de librerias que se van ocupando. 

from flask import Flask 
import os
import servidor.funciones_servidor as fun_serv
import funciones.LOGIN.funciones_login as fun_login
import funciones.HOME.funciones_home  as fun_home
import funciones.CATEGORIAS.funciones_categorias as fun_cate
import funciones.PRODUCTOS.funciones_productos as fun_prod
import funciones.PROVEDORES.funciones_provedores as fun_prove

app = Flask(__name__)

#Para que se pueda entrar desde cualquier IP y no marque error al entrar sin una llave secreta. 
app.host = "0.0.0.0"
app.port = os.getenv("PORT")
app.secret_key = b'E\x7f\xa9\xa8tg\xd5l@\xaa\x89\x91\xf9\x96\xf4 \x8c\x05\xf2\xe7\xb1L\xcb?'




#********************FUNCION LOGIN -ADMINISTRADORES***************  *****
@app.route('/')
@app.route('/login')   
def loginvista():
    return fun_login.vistalogin()

#FUNCION INICIAR SESION-ADMINISTRADORES
@app.route('/iniciarsesion', methods = ['POST'])
def iniciarSesion():
    return fun_login.inicioSesionAdminis()

#FUNCION DE HOME
@app.route('/home')
def homePage():
    return fun_home.home()

#********************FUNCIONES CATEGORIAS***********************

#FUNCION DE VISTA CATEGORIA. 
@app.route('/categorias')
def categoria():
    return fun_cate.vistaCategoria()

#FUNCION DE AGREGAR CATEGORIA.
@app.route('/agregar-categorias', methods = ['POST'])
def agregarCategoria():
    return fun_cate.nuevaCategoria()


#********************FUNCIONES PRODUCTOS***********************

#FUNCION DE VISTA PRODUCTO. 
@app.route('/productos')
def productos():
    return fun_prod.consultaProductos()

#FUNCION DE VISTA OPERACIONES PRODUCTO. 
@app.route('/productos-operaciones')
def productosOperaciones():
    return fun_prod.consultaProductosOperaciones()


#FUNCION PARA *VISTA* DE AGREGAR PRODUCTOS
@app.route('/ingresar-productos')
def ingresarProductos():
    return fun_prod.productosAgregar()


#FUNCION DE AGREGAR PRODUCTO. INSERT.
@app.route('/agregar-productos', methods = ['POST'])
def agregarProducto():
    return fun_prod.nuevoProducto()




#********************FUNCIONES PROVEDORES***********************

#FUNCION DE VISTA PROVEDOR. 
@app.route('/provedores')
def provedores():
    return fun_prove.vistaProvedores()

#FUNCION DE AGREGAR CATEGORIA.

@app.route('/agregar-proveedores', methods = ['POST'])
def agregarProveedores():
    return fun_prove.nuevoProveedor()








#********************FUNCION DE PAGINA NO ENCONTRADA********************
def paginaNoEncontrada(error):
    return fun_serv.error_404(error)

#Comprobador. Por si falta un elemento y si no lo tiene no correra dicha pagina. 
if __name__ == '__main__':
    app.run(host=app.host, port=app.port, debug=True)
