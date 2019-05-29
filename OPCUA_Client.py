##client.py

from opcua import Client
import time
from random import randint

from pymongo import MongoClient as mc
import time; #se obtiene un timestamp
ts = time.time()

url = "opc.tcp://172.16.49.71:4840"     #Server IP and port
client = Client(url)

client.connect()
print("Client Connected")


def ActualizarDato(id, dato):
    client = mc("mongodb+srv://admin:admin@bayo0-2gtne.gcp.mongodb.net/test?retryWrites=true")
    #client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
    db = client.uGridVars
    coleccion = db.scadaVars
    coleccion.update_one({'_id':id}, {"$set": dato})


try:
    while True:

        Pm = client.get_node("ns=2;i=2")
        PotActiva = Pm.get_value()
        print('Potencia Activa Medida = {0}'.format(PotActiva))
        medida = { # documento de ejemplo para insertar en mongodb
            #"magnitud":("{:.2f}kW".format(PotActiva/1000)),
            "magnitud":PotActiva,
            "time":"0",
            "Nodo":"Carga_Activa"
        }
        ActualizarDato("1",medida)
        #Tempe = randint(10,50)
        #print('C_Temp = {0}'.format(Tempe))
        #Temp.set_value(Tempe)
        #time.sleep(3)

        Qm = client.get_node("ns=2;i=3")
        PotReact = Qm.get_value()
        print('Potencia Reactiva Medida = {0}'.format(PotReact))
        medida = { # documento de ejemplo para insertar en mongodb
            #"magnitud":("{:.2f}kW".format(PotReact/1000)),
            "magnitud": PotReact,
            "time":"0",
            "Nodo":"Carga_Reactiva"
        }
        ActualizarDato("2",medida)
        time.sleep(5)
        #Pressu = randint(200,999)
        #print('C_Temp = {0}'.format(Pressu))
        #Press.set_value(Pressu)

        time.sleep(2)
finally:
    client.disconnect()
