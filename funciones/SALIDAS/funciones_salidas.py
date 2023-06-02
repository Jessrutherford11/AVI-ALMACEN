from flask import Flask, render_template,redirect,session
from data_base import baseDatos as ConecBD
import random
from forms.SALIDAS.salidasForm import Salidas

#BD
BD = ConecBD.conexion()