from flask import Flask, render_template, redirect,session, request
import random
from data_base import baseDatos as ConectBD
from forms.DISTRIBUIDOR.distribuidorForm import Distribuidor


#BD
BD = ConectBD.conexion()

#FUNCION CONSULTA DISTRIBUIDOR *VISTA* 
def vistaDistribuidor():
    if 'usuario-administrador' in session:
        titulo = 'Distribuidor'
        distribuidorBD = BD['Distribuidor']
        distribuidorRecibido = distribuidorBD.find()
        return render_template('DISTRIBUIDOR/consulta_distribuidor.html', titulo=titulo, distribuidorRecibido=distribuidorRecibido)

#FUNCION INGRESAR DISTRIBUIDOR *VISTA*
def ingresarDistribuidor():
    if 'usuario-administrador' in session:
        titulo = 'Agregar Distribuidor'
        distribuidorBD = BD['Distribuidor']
        distribuidorRecibido = distribuidorBD.find()
        return render_template('DISTRIBUIDOR/agregarDistribuidor.html', titulo=titulo, distribuidorRecibido=distribuidorRecibido)

