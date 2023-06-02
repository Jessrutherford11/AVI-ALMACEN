from flask import Flask, render_template, redirect, session, request
import random
from data_base import baseDatos as ConecBD
from forms.PRODUCTOSEXTERNOS.productoForm import ProductoE
#BD
BD = ConecBD.conexion()


#FUNCION *VISTA* CONSULTA DE PRODUCTOS .
def consultaProductos():
    if 'usuario-administrador'in session:
        titulo = 'Consulta Productos Externos'
        ProductosBD = BD['ProductosExternos']
        ProductosRecibidos = ProductosBD.find()
        return render_template('PRODUCTOSEXTERNOS/productosConsulta.html', titulo=titulo, ProductosRecibidos=ProductosRecibidos)


#FUNCION *VISTA* CONSULTA PRODUCTOS OPERACIONES
def consultaProductosOperaciones():
    if 'usuario-administrador' in session:
        titulo = 'Operaciones Productos Externos'
        ProductosBD= BD['ProductosExternos']
        OperacionesProductosRecibidos = ProductosBD.find()
        return render_template('PRODUCTOSEXTERNOS/productosOperaciones.html', titulo=titulo, OperacionesProductosRecibidos=OperacionesProductosRecibidos)



#FUNCION *VISTA* DE AGREGAR PRODUUCTOS
def ingresarProductos():
    if 'usuario-administrador':
        titulo = 'Agregar nuevos productos externos' 
        #Agreagcion de categorias dentro de productos
        CategoriasBD = BD['Categoria']
        CategoriasRecibidas = CategoriasBD.find()
        #agregacion de anaquel dentro de prodcutos
        estanteBD = BD['anaquel']
        estanteRecibidos = estanteBD.find()
        return render_template ('PRODUCTOSEXTERNOS/productosAgregar.html', titulo=titulo, CategoriasRecibidas=CategoriasRecibidas , estanteRecibidos=estanteRecibidos)


#FUNCION AGREGAR PRODUTCOS *FORMULARIO*
def AgregarNuevoProducto():
    if 'usuario-administrador' in session:
        productosBD = BD['ProductosExternos']
        #Variables del formulario
        nombreProducto = request.form["nombreProducto"]
        categoria = request.form["categoria"]
        stock = request.form["stock"]
        precio = request.form["precio"]
        unidad = request.form["unidad"]
        estante = request.form["estante"]
        distribuidor = request.form["distribuidor"]
        descripcion = request.form["descripcion"]
        estado = request.form["estado"]
        #id aleatorio
        codigo = str(random.randint(200,9000))
        if codigo and nombreProducto and categoria and stock and precio and unidad and estante and distribuidor and descripcion and estado:
            producto = ProductoE(codigo, nombreProducto, categoria, stock, precio, unidad, estante, distribuidor, descripcion, estado)
            #Se inserta 
            productosBD.insert_one(producto.datosProductosJson())
            #Si inserta nos mandara a la vista de la tabla de producto extrnos
            return redirect('/productos-externos')
    elif 'usuario-provedor' in session:
        return redirect('/')


#FUNCION EDITAR *VISTA* PRODUCTOS
def editarInformacionProducto(key):
    if 'usuario-administrador' in session:
        titulo = 'Informacion Producto Externo'
        ProductosBD = BD['ProductosExternos']
        #Para agregar las categorias en prodcuctos
        categoriasBD = BD['Categoria']
        categoriasRecibidas = categoriasBD.find() #consulta 
        #Agregacion de anaqueles 
        estanteBD = BD['anaquel']
        estanteRecibidos = estanteBD.find()

        ProductosRecibidos = ProductosBD.find_one({'codigo':key})
        return render_template('PRODUCTOSEXTERNOS/productosInfo.html', titulo = titulo, ProductosRecibidos = ProductosRecibidos, categoriasRecibidas=categoriasRecibidas, estanteRecibidos=estanteRecibidos)
        
    elif 'usuario-provedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR PRODCUTOS
def ActualizarProductos(key,campo):
    if 'usuario-administrador' in session:
        ProductosBD = BD['ProductosExternos']
        dato = request.form['dato']
        if dato:
            ProductosBD.update_one({'codigo':key}, {'$set':{campo:dato}})
            return editarInformacionProducto(key)

    elif 'usuario-provedor' in session:
        return redirect('/')    


#FUNCION ELIMINAR PRODUCTOS
def eliminarProductos(key):
    if 'usuario-administrador' in session:
        ProductosBD = BD['ProductosExternos']
        ProductosBD.delete_one({'codigo':key})
        return redirect('/productos-externos-operaciones')
    
    elif 'usuario-provedor' in session:
        return redirect('/')