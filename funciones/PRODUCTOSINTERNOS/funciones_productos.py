from flask import Flask, render_template, redirect, session, request
#Genere numeros aleatorioas
import random
from data_base import baseDatos as Conecbd

from forms.PRODUCTOSINTERNOS.productoForm  import Producto

#BD
BD = Conecbd.conexion()

#FUNCION *VISTA* DE AGREGAR PRODUCTOS
def productosAgregar():
    if 'usuario-administrador':
        titulo = "Agregar nuevos productos internos"
        #Para agregar las categorias en prodcuctos
        categoriasBD = BD['Categoria']
        categoriasRecibidas = categoriasBD.find() #consulta 
        #Para agregar el estante en productos
        EstanteBD = BD['anaquel']
        estanteRecibidos = EstanteBD.find()
        return render_template('PRODUCTOSINTERNOS/productosAgregar.html', titulo = titulo, categoriasRecibidas=categoriasRecibidas, estanteRecibidos=estanteRecibidos)



# FUNCION DE AGREGAR PRODUCTOS. -FORMULARIO. 
def nuevoProducto():
    if 'usuario-administrador' in session:
        productosBD = BD['ProductosInternos']
        #Variable del formulario
        nombreProducto = request.form["nombreProducto"]
        categoria = request.form["categoria"]
        stock = request.form["stock"]
        precio = request.form["precio"]
        estante = request.form["estante"]
        distribuidor = request.form["distribuidor"]
        descripcion = request.form["descripcion"]
        estado = request.form["estado"]
        #id aleatorio
        codigo = str(random.randint(400,9000))

        if codigo and nombreProducto and categoria and stock and precio and estante and distribuidor and  descripcion and estado:
            producto = Producto(codigo, nombreProducto, categoria, stock, precio, estante, distribuidor, descripcion, estado)
            #Insercion de datos 
            productosBD.insert_one(producto.datosProductosJson())
            return redirect('/productos') #Redirecciona a la tabla de prodcuctos
    
    elif 'usuario-provedor' in session:
        return redirect('/')



#FUNCION INFORMACION PRODUCTOS
def informacionProducto(key):
    if 'usuario-administrador' in session:
        titulo = 'Informacion Producto'
        ProductosBD = BD['ProductosInternos']
        #Para agregar las categorias en prodcuctos
        categoriasBD = BD['Categoria']
        categoriasRecibidas = categoriasBD.find() #consulta 
        #Para agregar los anaqueles en productos
        anaquelBD = BD['anaquel']
        estanteRecibidos = anaquelBD.find()
        #
        ProductosRecibidos = ProductosBD.find_one({'codigo':key})
        return render_template('PRODUCTOSINTERNOS/productosInfo.html', titulo = titulo, ProductosRecibidos = ProductosRecibidos, categoriasRecibidas=categoriasRecibidas, estanteRecibidos=estanteRecibidos)
        
    elif 'usuario-provedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR PRODCUTOS
def actualizarProducto(key,campo):
    if 'usuario-administrador' in session:
        ProductosBD = BD['ProductosInternos']
        dato = request.form['dato']
        if dato:
            ProductosBD.update_one({'codigo':key}, {'$set':{campo:dato}})
            return informacionProducto(key)

    elif 'usuario-provedor' in session:
        return redirect('/')    


#FUNCION CONSULTAR PRODUCTOS EN TABLA
def consultaProductos():
    if 'usuario-administrador' in session:
        titulo = 'Productos'
        #Consulta 
        productosBD = BD['ProductosInternos']
        productosRecibidos = productosBD.find()
        return render_template('PRODUCTOSINTERNOS/productosConsulta.html', titulo = titulo, productosRecibidos = productosRecibidos)


#FUNCION CONSULTAR OPERACIONES DE LOS PRODUCTOS EN TABLA
def consultaProductosOperaciones():
    if 'usuario-administrador' in session:
        titulo = 'Operaciones-Productos'
        #Consulta 
        productosBD = BD['ProductosInternos']
        productosOperacionesRecibidos = productosBD.find()
        return render_template('PRODUCTOSINTERNOS/productosOperaciones.html', titulo = titulo, productosOperacionesRecibidos = productosOperacionesRecibidos)


#FUNCION ELIMINAR PRODUCTOS
def eliminarProductos(key):
    if 'usuario-administrador' in session:
        productosBD = BD['ProductosInternos']
        productosBD.delete_one({'codigo':key})
        return redirect ('/productos-operaciones')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')


