from flask import Flask, render_template,redirect,session
from data_base import baseDatos as ConecBD
import random
from forms.SALIDAS.salidasForm import Salidas

#BD
BD = ConecBD.conexion()

#FUNCION *VISTA* CONSULTA SALIDAS 
def vistasSalidas():
    if 'usuario-administrador' in session:
        titulo = 'Salidas'
        salidasBD = BD['Salidas']
        salidasRecibidas = salidasBD.find()
        return render_template('SALIDAS/salidas.html', titulo=titulo, salidasRecibidas=salidasRecibidas)

