from flask import Flask, render_template, redirect, session, request, flash, g
from data_base import baseDatos as Conecdb

from werkzeug.security import generate_password_hash

BD = Conecdb.conexion()


#FUNCION VISTA PERFIL 
def vistaPefil():
    if 'usuario-administrador' in session:
        titulo = 'Informacion Perfil'
        PerfilBD = BD['users']
        #Se busca el usuario que esta en correo con el cual inicio sesion
        perfilRecibido = PerfilBD.find_one({'email': session['usuario-administrador']})
        return render_template ('PERFIL/perfil.html', titulo = titulo, perfilRecibido = perfilRecibido)
    elif 'usuario-proveedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR PERFIL <NAME>
def actualizarPerfil(key, campo):
        PerfilBD = BD['users']
        dato = request.form['dato']
        if dato:
            PerfilBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            return vistaPefil()
        

#FUNCION ACTUALIZAR PERFIL <CORREO>
def actualizarCorreo(key, campo):
        PerfilBD = BD['users']
        dato = request.form['dato']
        if dato:
            PerfilBD.update_one({'identificador':key}, {'$set':{campo:dato}})
            return redirect('/')


#FUNCION ACTUALIZAR CONTRASEÑA 
def actualizarContraseña(key, campo):
    if 'usuario-administrador' in session:
        try:
            PerfilBD = BD['users']
            dato = request.form['dato']
            if dato:
                #Si dato existe. Se genera una contraseña hasheada.
                dato = generate_password_hash(dato, method='sha256')
                PerfilBD.update_one({'identificador':key}, {'$set': {campo: dato}})
                flash("CONTRASEÑA ACTUALIZADA CORRECTAMENTE") 
                return vistaPefil()
            else:
                flash("ERROR AL ACTUALIZAR CONTRASEÑA")
        except Exception as e:
            flash("ERROR EN EL SERVIDOR: "+str(e))
            return vistaPefil()
    elif 'usuario-provedor' in session:
        return redirect('/')
