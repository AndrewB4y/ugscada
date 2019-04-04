
"""
Como parte del proyecto para crear una interfaz scada para la emulacion de la microred electrica,
se requiere el uso de una base de datos. En esta implementacion se escogio mongoDB porque es mas
facil integrar su estructura con el paradigma de programacion de objetos.

Lo anterior hara el desarrollo mucho mas agil.

La apliacion web se implementa en Heroku con su debido repositorio en github.
la base de datos se implemento en mongodb atlas.

todo lo anterior usando las versiones gratis

En este ejemplo se muestra como escribir documentos a la base de datos de mongodb
"""

import time; #se obtiene un timestamp
ts = time.time()

medida_test = { # documento de ejemplo para insertar en mongodb
    "magnitud":[1500, 11200],
    "time":ts,
    "Nodo":"Carga"
}


from pymongo import MongoClient as mc # se hace la conexion y se inserta el documento en mongo

client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
db = client.scada
coleccion = db.measures
coleccion.insert(medida_test)

"""
Al correr el codigo se podra ver que se inserta el doc en mongo db. el id lo genera mongodb automaticamente
y no es necesario especificarlo. recuerdece siempre que en mongo db se insertan y se leen diccionarios
no objetos, pero estos tienen una equivalencia directa al lenguaje de objetos cosa que no ocurre con las bases
de datos relacionales.
"""