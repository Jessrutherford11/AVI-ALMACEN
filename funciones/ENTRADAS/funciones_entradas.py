from flask import Flask, render_template, session, redirect, request
from data_base import baseDatos as ConecBD
import random
from forms.ENTRADAS.entradasForm import Entradas

#BD
BD = ConecBD.conexion()

#FUNCION *VISTA*  CONSULTA ENTRADAS
def vistaEntrada():
    if 'usuario-administrador' in session:
        titulo =  'Entradas'
        entradasBD = BD['Entradas']
        entradasRecibidas = entradasBD.find()
        return render_template('ENTRADAS/entradas.html', titulo=titulo, entradasRecibidas=entradasRecibidas)


#FUNCION *VISTA* CONSULTA OPERACIONES ENTRADAS
def operacionesEntradas():
    if 'usuario-administrador' in session:
        titulo = 'Operaciones Entradas'
        entradasBD = BD['Entradas']
        entradasRecibidas = entradasBD.find()
        return render_template('ENTRADAS/operacionesEntradas.html', titulo=titulo, entradasRecibidas=entradasRecibidas)



# FUNCION *VISTA* INSERTAR ENTRADAS
def agregarEntradas():
    if 'usuario-administrador' in session:
        titulo = 'Agregar Entradas'
            #Agreagcion de categorias* dentro de entradas
        CategoriasBD = BD['Categoria']
        CategoriasRecibidas = CategoriasBD.find()
            #Agregacion de anaquel* dentro de entradas
        estanteBD = BD['anaquel']
        estanteRecibidos = estanteBD.find()
            #Agregacion de distribuidor*  dentro de entradas
        distribuidorBD = BD['Distribuidor']
        distribuidorRecibido = distribuidorBD.find()
            #Consulta de entradas
        entradasBD = BD['Entradas']
        entradasRecibidas = entradasBD.find()
        return render_template('ENTRADAS/agregarEntradas.html', titulo=titulo,  entradasRecibidas=entradasRecibidas, CategoriasRecibidas=CategoriasRecibidas, estanteRecibidos=estanteRecibidos, distribuidorRecibido=distribuidorRecibido)

#FUNCION AGREGAR ENTRADAS *FORMULARIO*
def agregarNuevaEntrada():
    if 'usuario-administrador' in session:
        entradasBD = BD['Entradas']
        #
        fecha = request.form["fecha"]
        nombreProducto = request.form["nombreProducto"]
        tipoProducto = request.form["tipoProducto"]
        descripcion = request.form["descripcion"]
        cantidad = request.form["cantidad"]
        categoria = request.form["categoria"]
        anaquel = request.form["anaquel"]
        distribuidor = request.form["distribuidor"]
        validacion = request.form["validacion"]
        observaciones = request.form["observaciones"]
        #ID´s aleatorio identificador
        identificador= str(random.randint(200,9000))
        #ID CodigoProducto 
        codigoProductos = str(random.randint(100,8000))
        Unir = codigoProductos + nombreProducto
        Longitud = 8
        Extencion = random.sample(Unir,Longitud)
        Aleatorio = "".join(Extencion)
        codigoProducto = Aleatorio
        print(codigoProducto)

        if identificador and fecha and codigoProducto and nombreProducto and tipoProducto and descripcion and cantidad and categoria and anaquel and distribuidor and validacion and observaciones:
            entradas = Entradas(identificador,fecha,codigoProducto,nombreProducto,tipoProducto,descripcion,cantidad,categoria,anaquel,distribuidor,validacion,observaciones)
            entradasBD.insert_one(entradas.datosEntradasJson())
            #Si se inserta nos llevara a la tabla para consultar 
            return redirect('/entradas')
        
    elif 'usuario-provedor' in session:
        return redirect('/')
    



#FUNCION *VISTA* EDITAR ENTRADAS
def editarInfoEntrada(key):
    if 'usuario-administrador' in session:
        titulo = 'Editar Informacion Entradas'
        entradasBD = BD['Entradas']
            #Agreagcion de categorias dentro de entradas
        CategoriasBD = BD['Categoria']
        CategoriasRecibidas = CategoriasBD.find()
            #Agregacion de anaquel dentro de prodcutos
        estanteBD = BD['anaquel']
        estanteRecibidos = estanteBD.find()
            #Agregacion de distribuidor*  dentro de entradas
        distribuidorBD = BD['Distribuidor']
        distribuidorRecibido = distribuidorBD.find()

        entradasRecibidas = entradasBD.find_one({'identificador':key})
        return render_template('ENTRADAS/actualizarEntradas.html', titulo=titulo, entradasRecibidas=entradasRecibidas , CategoriasRecibidas=CategoriasRecibidas , estanteRecibidos=estanteRecibidos, distribuidorRecibido=distribuidorRecibido)
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR ENTRADAS
def actualizarEntradas(key,campo):
    if 'usuario-administrador' in session:
        entradasBD = BD['Entradas']
        dato = request.form['dato']
        if dato:
            entradasBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            return editarInfoEntrada(key)
        
    elif 'usuario-proveedor' in session:
        return redirect('/')



#FUNCION ELIMINAR ENTRADAS 
def eliminarEntrada(key):
    if 'usuario-administrador' in session:
        entradasBD = BD['Entradas']
        entradasBD.delete_one({'identificador':key})
        return redirect('/operaciones-entradas')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
