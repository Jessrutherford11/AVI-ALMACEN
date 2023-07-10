#INPORTACION DE LIBRERIA NECESARIA PARA LA CONEXION CON MONGO.

#LIBRERIA DE MONFODB PARA PYTHON.s
from pymongo import MongoClient
#LIBRERIA PARA LA VALIDACION DE SEGURIDAD DE LA CONEXION.
import certifi

MONGO_URL = 'mongodb+srv://jessi:NBHD0511@clusteravi-almacen.iyllw6j.mongodb.net/?retryWrites=true&w=majority'
#Para forma local
#MONGO_URL = 'mongodb://localhost:27017'

#Se pone solo al correrlo web 
ca = certifi.where()

#FUNCION CONEXXION BD
def conexion():
    try:
        #Para forma local
        #cliente = MongoClient(MONGO_URL)
        cliente = MongoClient(MONGO_URL, tlsCAfile=ca)
        bd = cliente['Avi-Almacen']#BD
        
    except ConnectionError:
        print('ERROR EN CONECTAR A LA BD')
    return bd

#Para comporbar si corre la conexion
#print (conexion())