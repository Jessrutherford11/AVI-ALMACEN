from flask import Flask, render_template, redirect, session, request, flash
from data_base import baseDatos as Conecdb
from forms.ADMINISTRADOR.adminForm import Administrador
import random

from werkzeug.security import generate_password_hash


BD = Conecdb.conexion()


#FUNCION VISTA PERFIL 
def vistaUsuarios():
    if 'usuario-administrador' in session:
        titulo = 'Informacion Usuarios'
        usuarioBD = BD['users']
        usuarioRecibido = usuarioBD.find()
        return render_template ('USUARIOS/usuario.html', titulo = titulo, usuarioRecibido=usuarioRecibido)
    elif 'usuario-proveedor' in session:
        return redirect('/')


#FUNCION *VISTA* AGREGAR USUARIOS *FORMULARIO
def agregarUsuario():
    if 'usuario-administrador' in session:
        titulo = 'Agregar Usuarios'
        usuarioBD = BD['users']
        usuarioRecibido = usuarioBD.find()
        return render_template ('USUARIOS/agregarUsuario.html', titulo = titulo, usuarioRecibido=usuarioRecibido)
    

#AGREGAR CLIENTES. *FORMULARIO*
def nuevoUsuario():
    if 'usuario-administrador' in session:
        #Consulta a la BD
        usuarioBD = BD['users']
        #Variable del html del formulario
        name = request.form["name"]
        email = request.form["email"] 
        contraseña = request.form["contraseña"] 
        #ID ALEATORIO CON NOMBRE
        codigos = str(random.randint(2,5000))
        Unir = codigos + name
        Longitud = 8
        Extencion = random.sample(Unir,Longitud)
        Aleatorio = "".join(Extencion)
        identificador = Aleatorio
        print(identificador)


        if name and email and contraseña:
            key = generate_password_hash(contraseña, method = 'sha256')
            usuario = Administrador(identificador, name, email, key)
            #Insercion a la BD
            usuarioBD.insert_one(usuario.datosAdministradorJson())
            flash("Usuario Agregado Correctamente: " + name)
            return redirect('/usuarios')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')


def eliminarUsuario(key):
    if 'usuario-administrador' in session:
        usuarioBD = BD['users']
        usuarioBD.delete_one({'identificador':key})
        flash("Usuario Eliminado: " + key)
        return redirect('/usuarios')

    elif 'usuario-proveedor' in session:
        return redirect('/')