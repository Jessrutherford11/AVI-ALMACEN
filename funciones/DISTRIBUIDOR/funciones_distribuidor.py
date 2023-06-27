from flask import Flask, render_template, redirect,session, request, flash
import random
from data_base import baseDatos as ConectBD
from forms.DISTRIBUIDOR.distribuidorForm import Distribuidor


#BD

BD = ConectBD.conexion()

#FUNCION CONSULTA SELLER / DISTRIBUIDOR *VISTA* 
def vistaDistribuidor():
    if 'usuario-administrador' in session:
        titulo = 'Seller'
        distribuidorBD = BD['Seller']
        distribuidorRecibido = distribuidorBD.find()
        return render_template('DISTRIBUIDOR/consulta_distribuidor.html', titulo=titulo, distribuidorRecibido=distribuidorRecibido)

#FUNCION INGRESAR SELLER / DISTRIBUIDOR *VISTA*
def ingresarDistribuidor():
    if 'usuario-administrador' in session:
        titulo = 'Agregar Seller'
        distribuidorBD = BD['Seller']
        distribuidorRecibido = distribuidorBD.find()
        return render_template('DISTRIBUIDOR/agregarDistribuidor.html', titulo=titulo, distribuidorRecibido=distribuidorRecibido)


#FUNCION DE AGREGAR NUEVO SELLER / DISTRIBUIDOR*FORMULARIO*
def agregarNuevoDistribuidor():
    if 'usuario-administrador' in session:
        distribuidorBD = BD['Seller']
        nombre = request.form['nombre']
        direccion = request.form['direccion'] 
        telefono = request.form['telefono']
        #ID ALEATORIO CON NOMBRE 
        IdentificadorD = str(random.randrange(1,4000,4))
        Unir = IdentificadorD + nombre 
        Longitud = 7
        Extencion = random.sample(Unir,Longitud)
        Aleatorio = "".join(Extencion)
        identificador = Aleatorio
        #print(identificador)

        if identificador and nombre and direccion and telefono:
            distribuidor = Distribuidor(identificador, nombre, direccion,telefono)
            #INSERCION BD
            distribuidorBD.insert_one(distribuidor.datosDistribuidorJson())
            flash(nombre  +  "  Agregado correctamnete ")
            return redirect('/distribuidor')
        
    elif 'usuario-proveedor' in session:
        return redirect('/')    


#FUNCION *VISTA¨EDITAR INFO SELLER / DISTRIBUIDOR
def informacionDistribuidor(key):
    if 'usuario-administrador' in session:
        titulo = 'Editar Infomacion Distribuidor'
        distribuidorBD = BD['Seller']
        distribuidorRecibido = distribuidorBD.find_one({'identificador':key})
        return render_template('DISTRIBUIDOR/actualizarDistribuidor.html', titulo=titulo, distribuidorRecibido=distribuidorRecibido)
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
    
#FUNCION ACTUALIZAR INFO SELLER / DISTRIBUIDOR
def actualizarDistribuidor(key,campo):
    if 'usuario-administrador' in session:
        distribuidorBD = BD['Seller']
        dato = request.form['dato']
        if dato:
            distribuidorBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            flash("Se agrego correctamente: " + key)
            return informacionDistribuidor(key)
        
        elif 'usuario-proveedor' in session:
            return redirect('/')





#FUNCION ELIMINAR SELLER / DISTRIBUIDOR 
def eliminarDistribuidor(key):
    if 'usuario-administrador' in session:
        distribuidorBD = BD['Seller']
        distribuidorBD.delete_one({'identificador':key})
        flash("Se elimino correctamente: " + key)
        return redirect('/distribuidor')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')