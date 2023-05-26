from flask import Flask, render_template, request, session, redirect
from data_base import baseDatos as ConectBD
import random

from forms.ANAQUEL.anaquelForm import Anaquel

BD = ConectBD.conexion()

#VISTA DE ANAQUEL. 
def vistaAnaquel():
    if 'usuario-administrador' in session:
        titulo = 'Consulta Anaqueles'
        AnaquelBD = BD['anaquel']
        anaquelRecibido = AnaquelBD.find()
        return render_template('ANAQUEL/anaquel.html', titulo=titulo, anaquelRecibido=anaquelRecibido)
    

#VISTA INGRESAR ANAQUEL.
def ingresarAnaquel():
    if 'usuario-administrador' in session:
        titulo = "Agregar Anaquel-Estante"
        Anaquel = BD['anaquel']
        anaquelRecibido = Anaquel.find()
        return render_template('ANAQUEL/agregarAnaquel.html', titulo=titulo, anaquelRecibido=anaquelRecibido)
    
#FUNCION AGREGAR ANAQUEL*FORMULARIO*
def nuevoAnaquel():
    if 'usuario-administrador' in session:
        anaquelBD = BD['anaquel']
        nombreAnaquel = request.form["nombreAnaquel"]
        #id random
        identificador = str(random.randrange(1,1000,4))

        if identificador and nombreAnaquel:
            anaquel = Anaquel(identificador,nombreAnaquel)
            anaquelBD.insert_one(anaquel.datosAnaquelJson())
            return redirect('anaqueles')
        
    elif 'usuario-proveedor' in session:
        return redirect('/')
        

#FUNCION ELIMINAR ANAQUEL
def eliminarAnaquel(key):
    if 'usuario-administrador' in session:
        anaquelBD = BD['anaquel']
        anaquelBD.delete_one({'identificador':key})
        return redirect('/anaqueles')

    elif 'usuario-proveedor' in session:
        return redirect('/')


#FUNCION EDITAR INFORMACION ANAQUELES *VISTA*
def informacionAnaquel(key):
    if 'usuario-administrador' in session:
        titulo = 'Editar Informacion Anaquel'
        anaquelBD = BD['anaquel']
        anaquelRecibido = anaquelBD.find_one({'identificador':key})
        return render_template('ANAQUEL/actualizarAnaquel.html', titulo=titulo, anaquelRecibido=anaquelRecibido)
    
    elif 'usuario-proveedor' in session:
        return redirect('/')

#FUNCION ACTUALIZAR ANAQUEL 
def actualizarAnaquel(key,campo):
    if 'usuario-administrador' in session:
        anaquelBD = BD['anaquel']
        dato = request.form['dato']
        if dato:
            anaquelBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            return informacionAnaquel(key)
        
        elif 'usuario-proveedor' in session:
            return redirect('/')






