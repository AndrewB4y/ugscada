

from pymongo import MongoClient as mc
import time; #se obtiene un timestamp
ts = time.time()


doc_id = "1"


def InsertarDato(dato):
    client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
    db = client.scada
    coleccion = db.measures
    coleccion.insert(dato)



def ActualizarDato(dato):

    client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
    db = client.scada
    coleccion = db.measures
    coleccion.update_one({'_id':doc_id}, {"$set": dato})


while True:
    entr_usr = input("digite el valor de consumo en la carga")

    medida = { # documento de ejemplo para insertar en mongodb
        "magnitud":entr_usr,
        "time":0,
        "Nodo":"Carga"
        }

    ActualizarDato(medida)

    time.sleep(5)
