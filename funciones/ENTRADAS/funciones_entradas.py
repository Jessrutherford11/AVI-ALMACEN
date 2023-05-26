from flask import Flask, render_template, session, redirect, request
from data_base import baseDatos as ConecBD
import random
from forms.ENTRADAS.entradasForm import Entradas

#BD
BD = ConecBD.conexion()

def consultaEntradas():
    if 'usuario-administardor' in session:
        titulo = 'Consulta Entradas'
        entradasBD = BD['Entradas']
        entradasRecibidas = entradasBD.find()
        return render_template('ENTRADAS/consultaEntradas.html', titulo=titulo, entradasRecibidas=entradasRecibidas)

