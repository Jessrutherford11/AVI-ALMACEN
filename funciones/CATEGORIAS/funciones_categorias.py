
from flask import Flask, render_template, redirect, session, request
#Genere numeros aleatorioas
import random
from data_base import baseDatos as Conecbd

from forms.CATEGORIAS.categoriaForm import Categoria 

BD = Conecbd.conexion()

#VISTA CATEGORIAS
def vistaCategoria():
    #Verificacion
    if 'usuario-administrador' in session:
        titulo = 'Categorias'
        #consulta
        categoriasBD = BD['Categoria']
        #Se van a guardar las categorias que se buscaron 
        categoriasRecibidas = categoriasBD.find()
        return render_template('CATEGORIAS/categorias.html', titulo = titulo, categoriasRecibidas = categoriasRecibidas)



#AGREGAR CATEGORIAS
def nuevaCategoria():
    #Verificacion
    if 'usuario-administrador' in session:
        #Consulta a la BD 
        categoriasBD = BD['Categoria'] 
        #Variable que viene del form de html-name
        nombreCategoria = request.form["nombreCate"] 
        #el id aleatorio
        codigo = str(random.randint(0,5000))

        if codigo and nombreCategoria:
            categoria = Categoria(codigo, nombreCategoria)
            #Insercion de datos a la BD 
            categoriasBD.insert_one(categoria.datosCategoriasJson())
            return redirect('/categorias')
        
    elif 'usuario-proveedor' in session:
        return redirect('/')
