from flask import Flask, redirect, render_template, session,request, flash
import random
from data_base import baseDatos as ConectBD
from forms.TRANSPORTISTA.transportistaForm import Transportista

#BD
BD = ConectBD.conexion()

#FUNCION VISTA* CONSULTA TRANSPORTISTA
def vistaTransportista():
    if 'usuario-administrador' in session:
        titulo = 'Transportistas'
        transportistaBD = BD['Transportista']
        transportistaRecibido = transportistaBD.find()
        return render_template('TRANSPORTISTA/consultarTransportista.html', titulo=titulo, transportistaRecibido=transportistaRecibido)
    

#FUNCION VISTA* INGRESAR TRANSPORTISTA
def ingresarTransportista():
    if 'usuario-administrador' in session:
        titulo = 'Agregar Transportistas'
        transportistaBD = BD['Transportista']
        transportistaRecibido = transportistaBD.find()
        return render_template('TRANSPORTISTA/agregarTransportista.html', titulo=titulo, transportistaRecibido=transportistaRecibido)
    

#FUNCION DE AGREGAR NUEVO TRANSPORTISTA *FORMULARIO*
def agregarNuevoTransportista():
    if 'usuario-administrador' in session:
        transportistaBD = BD['Transportista']
        nombre = request.form['nombre']
        lineaTransportista = request.form['linea'] 
        unidad = request.form['unidad'] 
        telefono = request.form['telefono']
        #ID ALEATORIO CON NOMBRE 
        IdentificadorT = str(random.randrange(1,4000,2))
        Unir = IdentificadorT + nombre 
        Longitud = 7
        Extencion = random.sample(Unir,Longitud)
        Aleatorio = "".join(Extencion)
        identificador = Aleatorio
        #print(identificador)

        if identificador and nombre and lineaTransportista and unidad and telefono:
            transportista = Transportista (identificador, nombre, lineaTransportista, unidad, telefono)
            #INSERCION BD
            transportistaBD.insert_one(transportista.datosTransportistaJson())
            flash("Transportista : "  +  nombre  +  " se agrego correctamente")
            return redirect('/transportista')
        
    elif 'usuario-proveedor' in session:
        return redirect('/')  
    


#FUNCION VISTA* EDITAR TRANSPORTISTA
def editarInfoTransportista(key):
    if 'usuario-administrador' in session:
        titulo = 'Editar Informacion Transportistas'
        transportistaBD = BD['Transportista']
        transportistaRecibido = transportistaBD.find_one({'identificador':key})
        return render_template('TRANSPORTISTA/actualizarTransportista.html', titulo=titulo, transportistaRecibido=transportistaRecibido)
    
    elif 'usuario-proveedor' in session:
        return redirect('/') 
    

#FUNCION ACTUAKIZAR TRANSPORTISTA
def actualizarTransportista(key,campo):
    if 'usuario-administrador' in session:
        transportistaBD = BD['Transportista']
        dato = request.form['dato']
        if dato:
            transportistaBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            flash("Se actualizado correctamente : "  +key)
        return editarInfoTransportista(key)
    
    elif 'usuario-proveedor' in session:
        return redirect('/') 
    

#FUNCION ELIMINAR TRANSPORTISTA
def eliminarTransportista(key):
    if 'usuario-administrador' in session:
        transportistaBD = BD['Transportista']
        transportistaBD.delete_one({'identificador': key})
        flash("Se elimino correctamente: " + key)
        return redirect('/transportista')
    
    elif 'usuario-proveedor' in session:
        return redirect('/') 