from flask import Flask, render_template,redirect,session,request 
import random
from data_base import baseDatos as Conecbd
from forms.CLIENTES.clientesForm import Clientes

BD = Conecbd.conexion()

#VISTA CLIENTES
def vistaClientes():
    if 'usuario-administrador' in session:
        titulo = 'Clientes'
        clientesBD = BD['Clientes']
        clientesRecibidos = clientesBD.find()
        return render_template('CLIENTES/clientes.html', titulo = titulo, clientesRecibidos = clientesRecibidos)



#AGREGAR CLIENTES
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
        #id aleatorio
        codigo = str(random.randint(0,4000))

        if codigo and nombres and apellidos and edad and correo and telefono and direccion:
            cliente = Clientes(codigo, nombres, apellidos, edad, correo, telefono, direccion)
            #Insercion a la BD
            ClientesBD.insert_one(cliente.datosClientesJson())
            return redirect('clientes')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')