#LOGICA DE LOGIN 
#inicio sesion, cerrar sesion, autentificaciones, etc.

from flask import render_template, request,flash, session, redirect
#Para contraseñas hash
from werkzeug.security import check_password_hash, generate_password_hash

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
                #En sesion se guarda una variable que sera nomnbre. 
                session['nombre'] = userRecibido['name']
                print(session)
                usuario = True
                flash('Bienvendio:'+session['nombre'] )
                session.pop('usuario-proveedor',None)
                return redirect('/home')    
            elif(check_password_hash(userRecibido['contraseña'],password)==False):
                flash('Error: Contraseña incorrecta')
                return redirect('/') 
        elif usuario == False:
            flash('Error: El usuario no existe')   
            return redirect('/') 
    flash('Error: Por favor llene todos los campos')      
    return redirect('/') 


#FUNCION DE PROTECCION DE RUTAS
def proteccionRutas():
    #respuesta de ruta
    ruta = request.path
    if 'usuario-administrador' in session:
        pass
    #Si empieza con 'static' no entra. 
    elif not 'usuario-proveedor' in session and ruta!="/" and ruta!="/login" and ruta!= "/iniciarsesion" and not ruta.startswith("/static"):
        flash('Inicia sesion para continuar')
        return redirect('/login')
    if 'usuario-administrador' in session:
        pass
    #Si empieza con 'static' no entra. 
    elif not 'usuario-proveedor' in session and ruta!="/" and ruta!="/login" and ruta!= "/iniciarsesion" and not ruta.startswith("/static"):
        flash('Inicia sesion para continuar')


#FFUNCION CERRAR SESION
def cerrarSesion():
    #se destruye la sesion con pop.
    #Destruye lo que trae session que es el correo de administrador. 
    session.pop('usuario-administrador', None)
    return redirect('/')
