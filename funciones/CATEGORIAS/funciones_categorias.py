
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
        try:
            #Consulta a la BD 
            categoriasBD = BD['Categoria'] 
            #Variable que viene del form de html-name
            nombreCategoria = request.form["nombreCate"] 
            #el id aleatorio
            codigo = str(random.randint(11,9000))
            if codigo and nombreCategoria:
                categoria = Categoria(codigo, nombreCategoria)
                #Insercion de datos a la BD 
                categoriasBD.insert_one(categoria.datosCategoriasJson())
                return redirect('/categorias')
        except Exception :
            print("error en el servidor")
        else:
            return redirect('/home')    
    elif 'usuario-proveedor' in session:
        return redirect('/')

#INFORMACION CATEGORIAS
def informacionCategorias(key):
    if 'usuario-administrador' in session:
        titulo = 'Informacion Categorias'
        CategoriasBD = BD['Categoria']
        categoriasRecibidas = CategoriasBD.find_one({'codigo':key})
        return render_template ('CATEGORIAS/actualizarInfo.html', titulo=titulo, categoriasRecibidas=categoriasRecibidas)
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
    

#ACTUALIZAR CATEGORIAS
def actualizarCategorias(key,campo):
    if 'usuario-administrador' in session:
        CategoriasBD = BD['Categoria']
        dato = request.form['dato']
        if dato:
            CategoriasBD.update_one({'codigo':key}, {'$set':{campo:dato}})
            return informacionCategorias(key)
        
        elif 'usuario-proveedor' in session:
            return redirect('/')



#ELIMINAR CATEGORIAS
def eliminarCategoria(key):
    if 'usuario-administrador' in session:
        categoriasBD = BD['Categoria']
        categoriasBD.delete_one({'codigo':key})
        return redirect ('/categorias')
    
    elif 'usuario-proveedor' in session:
        return redirect('/')
