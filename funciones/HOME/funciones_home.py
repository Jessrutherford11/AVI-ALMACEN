from flask import render_template, flash

def home(): 
    titulo = "Inicio"
    flash('')
    
    return render_template('HOME/home.html', titulo = titulo)



