from flask import render_template

def home():
    titulo = "Inicio"
    return render_template('HOME/home.html', titulo = titulo)