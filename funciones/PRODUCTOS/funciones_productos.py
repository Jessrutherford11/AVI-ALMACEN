from flask import Flask, render_template, redirect, session, request
#Genere numeros aleatorioas
import random
from data_base import baseDatos as Conecbd

from forms.PRODUCTOS.productoForm import Producto

#BD
BD = Conecbd.conexion()


def consultaProductos():
    if 'usuario-administrador' in session:
        titulo = 'Productos'
        #Consulta 
        productosBD = BD['Productos']
        productosRecibidos = productosBD.find()
        return render_template('PRODUCTOS/productosConsulta.html', titulo = titulo, productosRecibidos = productosRecibidos)
    
def productosAgregar():
    if 'usuario-administrador':
        titulo = "Agregar nuevos productos"
        return render_template('PRODUCTOS/productosAgregar.html', titulo = titulo)



#AGREGAR PRODUCTOS
def nuevoProducto():
    if 'usuario-administrador' in session:
        productosBD = BD['Productos']
        #Variable del formulario
        nombreProducto = request.form["nombreProducto"]
        existencia = request.form["existencia"]
        descripcion = request.form["descripcion"]
        #id aleatorio
        codigo = str(random.randint(0,7000))

        if codigo and nombreProducto and existencia and descripcion:
            producto = Producto(codigo, nombreProducto, existencia, descripcion)
            #Insercion de datos 
            productosBD.insert_one(producto.datosProductosJson())
            return redirect('/productos')
    
    elif 'usuario-provedor' in session:
        return redirect('/')


