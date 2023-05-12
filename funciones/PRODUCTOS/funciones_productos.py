from flask import Flask, render_template, redirect, session, request
#Genere numeros aleatorioas
import random
from data_base import baseDatos as Conecbd

from forms.PRODUCTOS.productoForm import Producto

#BD
BD = Conecbd.conexion()

#FUNCION *VISTA* DE AGREGAR PRODUCTOS
def productosAgregar():
    if 'usuario-administrador':
        titulo = "Agregar nuevos productos"
        #Para agregar las categorias en prodcuctos
        categoriasBD = BD['Categoria']
        categoriasRecibidas = categoriasBD.find() #consulta 
        return render_template('PRODUCTOS/productosAgregar.html', titulo = titulo, categoriasRecibidas=categoriasRecibidas)



# FUNCION DE AGREGAR PRODUCTOS. -FORMULARIO. 
def nuevoProducto():
    if 'usuario-administrador' in session:
        productosBD = BD['Productos']
        #Variable del formulario
        nombreProducto = request.form["nombreProducto"]
        categoria = request.form["categoria"]
        stock = request.form["stock"]
        precio = request.form["precio"]
        unidad = request.form["unidad"]
        distribuidor = request.form["distribuidor"]
        descripcion = request.form["descripcion"]
        estado = request.form["estado"]
        #id aleatorio
        codigo = str(random.randint(66,9000))

        if codigo and nombreProducto and categoria and stock and precio and unidad and distribuidor and  descripcion and estado:
            producto = Producto(codigo, nombreProducto, categoria, stock, precio, unidad, distribuidor, descripcion, estado)
            #Insercion de datos 
            productosBD.insert_one(producto.datosProductosJson())
            return redirect('/productos') #Redirecciona a la tabla de prodcuctos
    
    elif 'usuario-provedor' in session:
        return redirect('/')



#FUNCION CONSULTAR PRODUCTOS EN TABLA
def consultaProductos():
    if 'usuario-administrador' in session:
        titulo = 'Productos'
        #Consulta 
        productosBD = BD['Productos']
        productosRecibidos = productosBD.find()
        return render_template('PRODUCTOS/productosConsulta.html', titulo = titulo, productosRecibidos = productosRecibidos)



#FUNCION CONSULTAR OPERACIONES DE LOS PRODUCTOS EN TABLA
def consultaProductosOperaciones():
    if 'usuario-administrador' in session:
        titulo = 'Operaciones-Productos'
        #Consulta 
        productosBD = BD['Productos']
        productosOperacionesRecibidos = productosBD.find()
        return render_template('PRODUCTOS/productosOperaciones.html', titulo = titulo, productosOperacionesRecibidos = productosOperacionesRecibidos)




#FUNCION ELIMINAR PRODUCTOS
def eliminarProductos(key):
    if 'usuario-administrador' in session:
        productosBD = BD['Productos']
        productosBD.delete_one({'codigo':key})
        return redirect ('/productos-operaciones')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')


