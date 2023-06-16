from flask import Flask, render_template,redirect,session,request
from data_base import baseDatos as ConecBD
import random
from forms.SALIDAS.salidasForm import Salidas

#BD
BD = ConecBD.conexion()

#FUNCION *VISTA* CONSULTA SALIDAS 
def vistaSalidas():
    if 'usuario-administrador' in session:
        titulo = 'Salidas'
        salidasBD = BD['Salidas']
        salidasRecibidas = salidasBD.find()
        return render_template('SALIDAS/salidas.html', titulo=titulo, salidasRecibidas=salidasRecibidas)
    


#FUNCIO *VISTA* CONSULTA OPERACIONES SALIDAS
def operacionesSalidas():
    if 'usuario-administrador' in session:
        titulo = 'Operaciones Salidas'
        salidasBD = BD['Salidas']
        salidasRecibidas = salidasBD.find()
        return render_template('SALIDAS/operacionesSalidas.html', titulo=titulo, salidasRecibidas=salidasRecibidas)
    




#FUNCION *VISTA* AGREGAR SALIDAS
def agregarSalidas():
    if 'usuario-administrador' in session:
        titulo = 'Agregar Salidas'
        #Agreagcion de categorias* dentro de Salidas
        CategoriasBD = BD['Categoria']
        CategoriasRecibidas = CategoriasBD.find()
        #Agregacion de distribuidor*  dentro de SalidAa
        distribuidorBD = BD['Seller']
        distribuidorRecibido = distribuidorBD.find()
        #Agregacion de transportista*  dentro de SalidAa
        transportistaBD = BD['Transportista']
        transportistaRecibido = transportistaBD.find()
        #Agregacion de entradas->Productos*  dentro de Salidas
        entradaBD = BD['Entradas']
        entradasRecibidas = entradaBD.find()
    #Consulta de Salidas
        salidasBD = BD['Salidas']
        salidasRecibidas = salidasBD.find()
        return render_template('SALIDAS/agregarSalidas.html', titulo=titulo, salidasRecibidas=salidasRecibidas, CategoriasRecibidas=CategoriasRecibidas, distribuidorRecibido=distribuidorRecibido, entradasRecibidas=entradasRecibidas, transportistaRecibido=transportistaRecibido)
        

#FUNCION AGREGAR SALIDAS *FORMULARIO*
def agregarNuevasSalidas():
    if 'usuario-administrador' in session:
        salidasBD = BD['Salidas']
        #
        fecha = request.form["fecha"]
        tipoProducto = request.form["tipoProducto"]
        nombreProducto = request.form["nombreProducto"]
        categoria = request.form["categoria"]
        cantidad = request.form["cantidad"]
        distribuidor = request.form["distribuidor"]
        transportista = request.form['transportista']
        unidad = request.form["unidad"]
        placas = request.form["placas"]
        operador = request.form["operador"]
        #ID´s aleatorio identificador
        identificadorS= str(random.randrange(400,9000,4))
        salida =str('S')
        Unir = identificadorS + salida
        Longi = 4
        Extencion = random.sample(Unir,Longi)
        Aleatorio = "".join(Extencion)
        identificador = Aleatorio
        print(identificador)

        if identificador and fecha and  tipoProducto and nombreProducto  and categoria and cantidad  and distribuidor and transportista and unidad and placas and operador :
            salidas = Salidas(identificador,fecha, tipoProducto,nombreProducto,categoria,cantidad, distribuidor,transportista,unidad,placas, operador)
            salidasBD.insert_one(salidas.datosSalidasJson())
            #Si se inserta nos llevara a la tabla para consultar 
            return redirect('/salidas')
        
    elif 'usuario-provedor' in session:
        return redirect('/')
    

#FUNCION *VISTA* EDITAR SALIDAS
def editarInfoSalidas(key):
    if 'usuario-administrador' in session:
        titulo = 'Editar Informacion Salidas'
        salidasBD = BD['Salidas']
        #Agregacion de entradas->Productos*  dentro de Salidas
        entradaBD = BD['Entradas']
        entradasRecibidas = entradaBD.find()
        #Agreagcion de categorias* dentro de Salidas
        CategoriasBD = BD['Categoria']
        CategoriasRecibidas = CategoriasBD.find()
        #Agregacion de distribuidor*  dentro de SalidAa
        distribuidorBD = BD['Seller']
        distribuidorRecibido = distribuidorBD.find()
        #Agregacion de transportista*  dentro de SalidAa
        transportistaBD = BD['Transportista']
        transportistaRecibido = transportistaBD.find()

        salidasRecibidas = salidasBD.find_one({'identificador':key})
        return render_template('SALIDAS/actualizarSalidas.html', titulo=titulo, salidasRecibidas=salidasRecibidas, entradasRecibidas=entradasRecibidas, CategoriasRecibidas=CategoriasRecibidas, distribuidorRecibido=distribuidorRecibido, transportistaRecibido=transportistaRecibido)
        
    elif 'usuario-provedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR SALIDAS
def actualizarSalidas(key, campo):
    if 'usuario-administrador' in session:
        salidasBD = BD['Salidas']
        dato = request.form['dato']
        if dato:
            salidasBD.update_one({'identificador': key}, {'$set':{campo:dato}})
            return editarInfoSalidas(key)

    elif 'usuario-provedor' in session:
        return redirect('/')
    
    


#FUNCION ELIMINAR SALIDAS
def eliminarSalidas(key):
    if 'usuario-administrador' in session:
        salidasBD = BD ['Salidas']
        salidasBD.delete_one({'identificador':key})
        return redirect('/operaciones-salidas')
    
    elif 'usuario-provedor' in session:
        return redirect('/')
    