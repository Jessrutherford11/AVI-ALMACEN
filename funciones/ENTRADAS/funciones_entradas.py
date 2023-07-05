from flask import Flask, render_template, session, redirect, request, flash
from data_base import baseDatos as ConecBD
import random
from forms.ENTRADAS.entradasForm import Entradas

#
import locale
from time import gmtime, strftime

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
        distribuidorBD = BD['Seller']
        distribuidorRecibido = distribuidorBD.find()
            #Consulta de entradas
        entradasBD = BD['Entradas']
        entradasRecibidas = entradasBD.find()
        return render_template('ENTRADAS/agregarEntradas.html', titulo=titulo,  entradasRecibidas=entradasRecibidas, CategoriasRecibidas=CategoriasRecibidas, estanteRecibidos=estanteRecibidos, distribuidorRecibido=distribuidorRecibido)


#FUNCION AGREGAR ENTRADAS *FORMULARIO*
def agregarNuevaEntrada():
    if 'usuario-administrador' in session:
        entradasBD = BD['Entradas']
        salidasCantidad = BD['Salidas']
        #
        nombreProducto = request.form["nombreProducto"]
        tipoProducto = request.form["tipoProducto"]
        descripcion = request.form["descripcion"]
        stock = request.form["stock"] 
        categoria = request.form["categoria"]
        anaquel = request.form["anaquel"]
        distribuidor = request.form["distribuidor"]
        validacion = request.form["validacion"]
        observaciones = request.form["observaciones"]
    

        #ID´s aleatorio identificador
        identificadorE= str(random.randrange(200,8000,4))
        entrada =str('E')
        Unir = identificadorE + entrada
        Longi = 4
        Extencion = random.sample(Unir,Longi)
        Aleatorio = "".join(Extencion)
        identificador = Aleatorio
        #print(identificador)

        #ID CodigoProducto 
        codigoProductos = str(random.randint(100,8000))
        Unir = codigoProductos + nombreProducto
        Longitud = 8
        Extencion = random.sample(Unir,Longitud)
        Aleatorio = "".join(Extencion)
        codigoProducto = Aleatorio
        #print(codigoProducto)

        #FECHA Actual
        locale.setlocale(locale.LC_ALL, "es")
        """A-> Dia de la semana
        d ->dia del mes
        b ->Abrebacion de mes
        Y -> Año
        H : M -> Hora y minuto
        """ 
        fecha = strftime("%A  %d de %b de %Y a las %H:%M")
        #print(fecha)

        #DIA SE LA SEMANA
        dia = strftime("%A")
        print ("DIA DE LA SEMANA DE ENTRADAS:" , dia)

        if identificador and fecha and codigoProducto and nombreProducto and tipoProducto and descripcion and stock and categoria and anaquel and distribuidor and validacion and observaciones and dia:
            entradas = Entradas(identificador,fecha,codigoProducto,nombreProducto,tipoProducto,descripcion,stock,categoria,anaquel,distribuidor,validacion,observaciones,dia)
            entradasBD.insert_one(entradas.datosEntradasJson())
            flash("Entrada Registrada Correcatente: " + nombreProducto)
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
        distribuidorBD = BD['Seller']
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
            flash("Entrada Actualizada : " +key)
            return editarInfoEntrada(key)
        
    elif 'usuario-proveedor' in session:
        return redirect('/')



#FUNCION ELIMINAR ENTRADAS 
def eliminarEntrada(key):
    if 'usuario-administrador' in session:
        entradasBD = BD['Entradas']
        entradasBD.delete_one({'identificador':key})
        flash("Entrada Eliminada: " + key)
        return redirect('/operaciones-entradas')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')



# *REPORTE* ENTRADAS
def reporteEntrada():
    if 'usuario-administrador' in session:
        titulo = 'Reporte Entradas'
        entradasBD = BD['Entradas']
        entradasRecibidas = entradasBD.find()
        return render_template('ENTRADAS/reporteEntradas.html', titulo = titulo, entradasRecibidas=entradasRecibidas)

