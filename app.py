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
import funciones.CLIENTES.funciones_clientes as fun_cli
import funciones.PERFIL.funciones_perfil as fun_perfil

app = Flask(__name__)

#Para que se pueda entrar desde cualquier IP y no marque error al entrar sin una llave secreta. 
app.host = "0.0.0.0"
app.port = os.getenv("PORT")
app.secret_key = b'E\x7f\xa9\xa8tg\xd5l@\xaa\x89\x91\xf9\x96\xf4 \x8c\x05\xf2\xe7\xb1L\xcb?'



#********************FUNCION LOGIN -ADMINISTRADORES********************

#FUNCION LOGIN RAIZ
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

#FUNCION PROTECCION RUTAS
@app.before_request
def verificacionRutas():
    return fun_login.proteccionRutas()
    
#********************FUNCIONES PERFIL ********************

#FUNCION DE INFORMACION PERFIL
@app.route('/vista-perfil')
def VistaPerfil():
    return fun_perfil.vistaPefil()


#FUNCION ACTUALIZAR PERFIL 
@app.route('/actualizar-perfil/<key>,<campo>', methods = ['POST'])
def ActualizarPerfil(key,campo):
    return fun_perfil.actualizarPerfil(key,campo)


#********************FUNCION CERRAR SESION***********************

@app.route('/cerrar-sesion')
def cerrarsesion():
    return fun_login.cerrarSesion()



#********************FUNCIONES CATEGORIAS***********************

#FUNCION DE VISTA CATEGORIA. 
@app.route('/categorias')
def categoria():
    return fun_cate.vistaCategoria()

#FUNCION DE AGREGAR CATEGORIA.
@app.route('/agregar-categorias', methods = ['POST'])
def agregarCategoria():
    return fun_cate.nuevaCategoria()
    
#FUNCION DE INFORMACION CATEGORIA
@app.route('/informacion-categorias <key>')
def informacionCategoria(key):
    return fun_cate.informacionCategorias(key)

#FUNCION ACTUALIZAR CATEGORIA
@app.route('/actualizar-categorias <key>, <campo>', methods = ['POST'])
def actualizarCategoria(key,campo):
    return fun_cate.actualizarCategorias(key,campo)

#FUNCION DE ELIMINAR CATEGORIA.
@app.route('/eliminar-categorias <key>')
def eliminarCategorias(key):
    return fun_cate.eliminarCategoria(key)


#********************FUNCIONES PRODUCTOS***********************

#FUNCION DE VISTA PRODUCTO. 
@app.route('/productos')
def productos():
    return fun_prod.consultaProductos()

#FUNCION DE VISTA OPERACIONES PRODUCTO. 
@app.route('/productos-operaciones')
def productosOperaciones():
    return fun_prod.consultaProductosOperaciones()


#FUNCION *VISTA* DE AGREGAR PRODUCTOS
@app.route('/ingresar-productos')
def ingresarProductos():
    return fun_prod.productosAgregar()


#FUNCION DE AGREGAR PRODUCTO. INSERT.
@app.route('/agregar-productos', methods = ['POST'])
def agregarProducto():
    return fun_prod.nuevoProducto()

#FUNCION DE ELIMINAR PRODUCTO
@app.route('/eliminar-producto <key>')
#funcion que se ponen dentro del btn del form
def eliminarProducto(key):
    return fun_prod.eliminarProductos(key)



#********************FUNCIONES PROVEDORES***********************

#FUNCION DE VISTA PROVEDOR. 
@app.route('/provedores')
def provedores():
    return fun_prove.vistaProvedores()

#FUNCION DE AGREGAR PROVEDOR.

@app.route('/agregar-proveedores', methods = ['POST'])
def agregarProveedores():
    return fun_prove.nuevoProveedor()

#FUNCION DE INFORMACION PROVEDOR
@app.route('/informacion-proveedores <key>')
def informacionProveedor(key):
    return fun_prove.informacionProvedor(key)


#FUNCION ACTUALIZAR PROVEDOR
@app.route('/actualizar-proveedores <key>, <campo>', methods = ['POST'])
def actualizarProveedores(key,campo):
    return fun_prove.actualizarProvedor(key, campo)



#FUNCION DE ELIMINAR PROVEEDOR
@app.route('/eliminar-proveedor <key>')
#funcion que se ponen dentro del btn del form
def eliminarProveedores(key):
    return fun_prove.eliminarProvedor(key)


#********************FUNCIONES CLIENTES***********************

#FUNCION DE VISTA CLIENTE. 
@app.route('/clientes')
def clientes():
    return fun_cli.vistaClientes()

#FUNCION DE AGREGAR CLIENTES.

@app.route('/agregar-clientes', methods = ['POST'])
def agregarClientees():
    return fun_cli.nuevoCliente()

















#********************FUNCION DE PAGINA NO ENCONTRADA********************
def paginaNoEncontrada(error):
    return fun_serv.error_404(error)

#***COMPROBADOR***. Por si falta un elemento y si no lo tiene no correra dicha pagina. 
if __name__ == '__main__':
    app.run(host=app.host, port=app.port, debug=True)
