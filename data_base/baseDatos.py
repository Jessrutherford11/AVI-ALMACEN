from pymongo import MongoClient
import certifi

MONGO_URL = 'mongodb+srv://jessi:NBHD0511@clusteravi-almacen.iyllw6j.mongodb.net/?retryWrites=true&w=majority'
#MONGO_URL = 'mongodb://localhost:27017'
ca = certifi.where()

#FUNCION CONEXXION BD
def conexion():
    try:
        #cliente = MongoClient(MONGO_URL)
        cliente = MongoClient(MONGO_URL, tlsCAfile=ca)
        bd = cliente['Avi-Almacen']#BD
        
    except ConnectionError:
        print('ERROR EN CONECTAR A LA BD')
    return bd

#Para comporbar si corre la conexion
#print (conexion())