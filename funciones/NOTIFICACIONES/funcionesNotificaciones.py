from flask import Flask, render_template, session, redirect, request, flash
from data_base import baseDatos as ConecBD
import random
from forms.NOTIFICACIONES.notificacionesForm import Notificaciones

#BD
BD = ConecBD.conexion()

#FUNCION *VISTA* CONSULTA DE NOTIFICACIONES
def vistaNoti():
    if 'usuario-administrador' in session:
        titulo = 'Notificaciones'
        notifBD = BD['Notificaciones']
        notificacionesRecibidas = notifBD.find()
        return render_template('NOTIFICACIONES/noti.html', titulo=titulo, notificacionesRecibidas=notificacionesRecibidas)