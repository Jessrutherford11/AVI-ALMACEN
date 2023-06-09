from flask import Flask, render_template,redirect,session,request,flash
import random
from data_base import baseDatos as Conecbd
from forms.CLIENTES.clientesForm import Clientes

BD = Conecbd.conexion()


#CONSULTA CLIENTES*REPORTE*
def reporteCliente():
    if 'usuario-administrador' in session:
        titulo = 'Reporte Clientes'
        clientesBD = BD['Clientes']
        clientesRecibidos = clientesBD.find()
        return render_template('CLIENTES/consultaClientes.html', titulo = titulo, clientesRecibidos = clientesRecibidos)



#VISTA CLIENTES
def vistaClientes():
    if 'usuario-administrador' in session:
        titulo = 'Clientes'
        clientesBD = BD['Clientes']
        clientesRecibidos = clientesBD.find()
        return render_template('CLIENTES/clientes.html', titulo = titulo, clientesRecibidos = clientesRecibidos)


#INGRESAR CLIENTES *VISTA*
def ingresarCliente():
    if 'usuario-administrador':
        titulo = 'Ingresar Nuevo Cliente'
        ClientesBD = BD['Clientes']
        ClientesRecibidos = ClientesBD.find()
        return render_template('CLIENTES/agregarClientes.html', titulo=titulo, ClientesRecibidos=ClientesRecibidos)


#AGREGAR CLIENTES. *FORMULARIO*
def nuevoCliente():
    if 'usuario-administrador' in session:
        #Consulta a la BD
        ClientesBD = BD['Clientes']
        #Variable del html del formulario
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"] 
        edad = request.form["edad"] 
        correo = request.form["correo"] 
        telefono = request.form["telefono"] 
        direccion = request.form["direccion"]  
        empresa = request.form["empresa"] 
        #ID ALEATORIO CON APELLIDOS
        codigos = str(random.randint(2,5000))
        Unir = codigos + apellidos
        Longitud = 9
        Extencion = random.sample(Unir,Longitud)
        Aleatorio = "".join(Extencion)
        codigo = Aleatorio
        #print(codigo)


        if codigo and nombres and apellidos and edad and correo and telefono and direccion and empresa:
            cliente = Clientes(codigo, nombres, apellidos, edad, correo, telefono, direccion, empresa)
            #Insercion a la BD
            ClientesBD.insert_one(cliente.datosClientesJson())
            flash(nombres  +  apellidos  +  "  agregado correctamente ")
            return redirect('clientes')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
    

#INFORMACION CLIENTES. EDITAR.
def informacionCliente(key):
    if 'usuario-administrador' in session:
        titulo = 'Editar Informacion Cliente'
        ClientesBD = BD['Clientes']
        clientesRecibidos = ClientesBD.find_one({'codigo':key})
        return render_template('CLIENTES/actualizarInfo.html', titulo=titulo, clientesRecibidos=clientesRecibidos)

    elif 'usuario-proveedor' in session:
        return redirect('/')
    

#FUNCION ACTUALIZAR CLIENTES.
def actualizarCliente(key,campo):
    if 'usuario-administrador' in session:
        ClientesBD = BD['Clientes']
        dato = request.form['dato']
        if dato:
            ClientesBD.update_one({'codigo':key}, {'$set':{campo:dato}})  
        flash("Se actualizo correctamente: " + key)
        return informacionCliente(key)

    elif 'usuario-proveedor' in session:
        return redirect('/')
        

#ELIMINAR CLIENTES
def eliminarCliente(key):
    if 'usuario-administrador' in session:
        clientesBD = BD['Clientes']
        clientesBD.delete_one({'codigo':key})
        flash("Se elimino correctamente: " + key)
        return redirect('/clientes')

    elif 'usuario-proveedor' in session:
        return redirect('/')
    