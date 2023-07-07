from flask import render_template, session,redirect, flash
from data_base import baseDatos as ConecBD 

BD = ConecBD.conexion()

#FUNCION HOME
def home(): 
    if 'usuario-administrador' in session:    
        titulo = "Inicio"
        entradas = BD['Entradas']
        salidas = BD['Salidas']
        transportista = BD['Transportista']
        seller = BD['Seller']
        entradasTotales = entradas.count_documents({})
        salidasTotales = salidas.count_documents({})
        entradasSalidasTotales = entradasTotales + salidasTotales
        transportistaTotales = transportista.count_documents({})
        sellerTotales = seller.count_documents({})
        entradasRecibidas = entradas.find()
        salidasRecibidas = salidas.find()
        return render_template('HOME/home.html', titulo = titulo, entradasTotales=entradasTotales, salidasTotales=salidasTotales, entradasRecibidas=entradasRecibidas, 
        salidasRecibidas=salidasRecibidas, transportistaTotales=transportistaTotales, sellerTotales=sellerTotales, entradasSalidasTotales=entradasSalidasTotales)
    elif 'usuario-empleado' in session:
        return redirect('/')


#FUNCION HOME-NAV-BAR
def HomeNavBar(): 
    if 'usuario-administrador' in session:    
        titulo = "Inicio"
        entradas = BD['Entradas']
        salidas = BD['Salidas']
        transportista = BD['Transportista']
        seller = BD['Seller']
        entradasTotales = entradas.count_documents({})
        salidasTotales = salidas.count_documents({})
        entradasSalidasTotales = entradasTotales + salidasTotales
        transportistaTotales = transportista.count_documents({})
        sellerTotales = seller.count_documents({})
        entradasRecibidas = entradas.find()
        salidasRecibidas = salidas.find()
        return render_template('HOME/MODULOS/nav-bar.html', titulo = titulo, entradasTotales=entradasTotales, salidasTotales=salidasTotales, entradasRecibidas=entradasRecibidas, 
        salidasRecibidas=salidasRecibidas, transportistaTotales=transportistaTotales, sellerTotales=sellerTotales, entradasSalidasTotales=entradasSalidasTotales)
    elif 'usuario-empleado' in session:
        return redirect('/')






def Grafica():
    entradasBD = BD['Entradas']
    salidasBD = BD['Salidas']
    entradasTotales = entradasBD.count_documents({})
    salidasTotales = salidasBD.count_documents({})

    entradasSalidasTotales = entradasTotales + salidasTotales

    todo={
        'entradas': [entradasTotales],
        'salidas':[salidasTotales]
    }
    return todo