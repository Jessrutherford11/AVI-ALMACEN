from flask import Flask, render_template, redirect, session, request
from data_base import baseDatos as Conecdb

from forms.ADMINISTRADOR.adminForm import Administrador

BD = Conecdb.conexion()


#FUNCION VISTA PERFIL 
def vistaPefil():
    if 'usuario-administrador' in session:
        titulo = 'Informacion Perfil'
        PerfilBD = BD['users']
        #Se busca el usuario que esta en correo con el cual inicio sesion
        perfilRecibido = PerfilBD.find_one({'email':session['usuario-administrador']})
        return render_template ('PERFIL/perfil.html', titulo = titulo, perfilRecibido = perfilRecibido)
    elif 'usuario-proveedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR PERFIL 
def actualizarPerfil(key,campo):
        PerfilBD = BD['users']
        dato = request.form['dato']
        if dato:
            PerfilBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            return vistaPefil()