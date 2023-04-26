
from flask import Flask, render_template, redirect, session, request
#Generacion numeros aleatorios
import random
#Conexion BD
from data_base import baseDatos as Conecdb
#Clase donde se crea la BD 
from forms.PROVEDORES.provedoresForm import Proveedores

BD = Conecdb.conexion()

#VISTA PROVEDORES
def vistaProvedores():
    if 'usuario-administrador' in session:
        titulo = 'Provedores'
        provedoresBD = BD['Provedores']
        provedoresRecibidos = provedoresBD.find()
        return render_template('PROVEDORES/provedores.html', titulo = titulo, provedoresRecibidos = provedoresRecibidos)
    

#AGREGAR PROVEDORES
def nuevoProveedor():
    if 'usuario-administrador' in session:
        #Consulta a la BD
        provedoresBD = BD['Provedores']
        #Variable del html del formulario
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"] 
        edad = request.form["edad"] 
        correo = request.form["correo"] 
        telefono = request.form["telefono"] 
        direccion = request.form["direccion"]  
        #id aleatorio con el nombre
        codigo = str(random.randint(0,4000)) + nombres

        if codigo and nombres and apellidos and edad and correo and telefono and direccion:
            provedor = Proveedores(codigo, nombres, apellidos, edad, correo, telefono, direccion)
            #Insercion a la BD
            provedoresBD.insert_one(provedor.datosProveedoresJson())
            return redirect('provedores')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')










#ELIMINAR PROVEEDORES
def eliminarProvedor(key):
    if 'usuario-administrador' in session:
        #Tabla donde eliminara y conexion 
        ProvedoresBD = BD ['Provedores']
        #Se pasa la key y el nombre de la variable
        ProvedoresBD.delete_one({'codigo':key})
        return redirect ('/provedores')
    
    elif 'usuario-provedor' in session:
        return redirect ('/')