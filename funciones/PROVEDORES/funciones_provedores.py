
from flask import render_template, redirect, session, request
#Generacion numeros aleatorios
import random
#Conexion BD
from data_base import baseDatos as Conecdb
#Clase donde se crea la BD 
from forms.PROVEDORES.provedoresForm import Proveedores

BD = Conecdb.conexion()


#CONSULTA REPORTE PROVEDORES
def reporteProvedor():
    if 'usuario-administrador' in session:
        titulo = 'Reporte Provedores'
        provedoresBD = BD['Provedores']
        provedoresRecibidos = provedoresBD.find()
        return render_template('PROVEDORES/consultaProveedores.html', titulo = titulo, provedoresRecibidos = provedoresRecibidos)




#VISTA PROVEDORES
def vistaProvedores():
    if 'usuario-administrador' in session:
        titulo = 'Provedores'
        provedoresBD = BD['Provedores']
        provedoresRecibidos = provedoresBD.find()
        return render_template('PROVEDORES/provedores.html', titulo = titulo, provedoresRecibidos = provedoresRecibidos)

#FUNCION *VISTA* DE AGREGAR PROVEEDORES
def ingresarProvedores():
    if 'usuario-administrador':
        titulo = 'Agregar Nuevo Proveedor' 
        ProvedoresBD = BD['Provedores']
        provedoresRecibidos = ProvedoresBD.find()
        return render_template ('PROVEDORES/agregarProveedores.html', titulo=titulo, provedoresRecibidos=provedoresRecibidos)


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
        empresa = request.form["empresa"]  

        # ** ID ALEATORIO CON EL APELLIDO **
            #La variable 'codigos' va generar un ID aleatorio con la funcion 'random' y 
            # el metodo 'randint' del 1 al 5000 
        codigos = str(random.randint(1,5000))
        #print("Hola soy codigo" , codigos) 
            #La variable 'Unir' Va juntar lo que trae 'codigos' y 'apellidos'.
            #Es decir va traer el codigo aleatorio que se genero y el apellido que se haya ingresado
        Unir = codigos + apellidos
        #print("hola soy unir" , Unir)
            #La variable 'longitud' se pone el numero de caracteres 
            # que va generar al hacer esta union  
        longitud = 9
            #La variable 'extencion' tiene la funcion random con el metodo 'sample' 
                    # """ .sample
                    # devuelve una lista de longitud particular de elementos 
                    # elegidos de la secuencia, es decir, lista, tupla, cadena o conjunto. """
            #Con este metodo va elegir en secuencia las variables 'unir' y 'longitud' 
        extencion = random.sample(Unir,longitud)
        #print("hola soy extension" , extencion)
            #La variable 'aleatorio' convierte con '.join'. una cadena a --> string 
            # lo que trae la variable 'extencion'. 
        aleatorio = "".join(extencion)
        #print("soy aleatorio", aleatorio)re
        #La variable 'codigo' es igual  a 'aleatorio' es decir aqui se guarda lo que 
        #que hizo la variable 'aleatorio'
        codigo = aleatorio
        #print("Hola soy el codigo final", codigo)
        
        if codigo and nombres and apellidos and edad and correo and telefono and direccion and empresa :
            provedor = Proveedores(codigo, nombres, apellidos, edad, correo, telefono, direccion, empresa)
            #Insercion a la BD
            provedoresBD.insert_one(provedor.datosProveedoresJson())
            return redirect('provedores')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')


#EDITAR INFORMACION PROVEEDORES
def informacionProvedor(key):
    if 'usuario-administrador' in session:
        titulo = 'Informacion Proveedor'
        ProvedoresBD = BD['Provedores']
        ProvedoresRecibidos = ProvedoresBD.find_one({'codigo':key})
        return render_template ('PROVEDORES/actualizarinfo.html', titulo=titulo, ProvedoresRecibidos=ProvedoresRecibidos)
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
    
#ACTUALIZAR PROVEDORES
def actualizarProvedor(key,campo):
    if 'usuario-administrador' in session:
        ProveedoresBD = BD ['Provedores']
        dato = request.form['dato']
        #Comprobacion si dato existe
        if dato: 
            #$-- set.poner lo que se manda a campo que tre dato(nombres)
            #Campo es el que se actualizara 
            ProveedoresBD.update_one({'codigo':key},{'$set':{campo:dato}})
        #Se  retorna la funcion de la vista de arriba
        return informacionProvedor(key)

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