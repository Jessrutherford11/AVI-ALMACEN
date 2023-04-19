#LOGICA DE LOGIN 
#inicio sesion, cerrar sesion, autentificaciones, etc.

from flask import render_template, request,flash, session, redirect
#Para contraseñas hash
from werkzeug.security import check_password_hash

from data_base import baseDatos as Conecbd

#Conexion a la BD
BD = Conecbd.conexion()


#Funcion vista de login
def vistalogin():
    titulo = "Iniciar Sesion"
    return render_template('LOGIN/index.html', titulo=titulo)

#Funcion login para administrador
def inicioSesionAdminis():
    correo = request.form['email']
    password = request.form['contraseña']
    usuario = False
    if correo and password:
        user = BD['users']#tabla de la BD
        userRecibido = user.find_one({'email':correo})
        if userRecibido:
            if(check_password_hash(userRecibido['contraseña'], password)==True):
                session['usuario-administrador'] = userRecibido['email']
                usuario = True
                session.pop('usuario-proveedor',None)
                return redirect('/home')    
            elif(check_password_hash(userRecibido['contraseña'],password)==False):
                flash('Error: Contraseña incorrecta')
        elif usuario == False:
            flash('Error: El usuario no existe')   
        return vistalogin()
    flash('Por favor llene todos los campos')      
    return vistalogin()