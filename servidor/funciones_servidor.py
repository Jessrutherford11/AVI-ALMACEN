#SI NO HAY UNA PAGINA DE LA ROTA SE MANDE UN ERROR

from flask import render_template

def error_404(error):
    titulo = "404 PAGINA NO ENCONTRADA"
    return render_template("SERVIDOR/servidor.html", titulo=titulo)


