
"""
Como parte del proyecto para crear una interfaz scada para la emulacion de la microred electrica,
se requiere el uso de una base de datos. En esta implementacion se escogio mongoDB porque es mas
facil integrar su estructura con el paradigma de programacion de objetos.

Lo anterior hara el desarrollo mucho mas agil.

La apliacion web se implementa en Heroku con su debido repositorio en github.
la base de datos se implemento en mongodb atlas.

todo lo anterior usando las versiones gratis

En este ejemplo se muestra como leer documentos de la base de datos de mongodb
"""

from pymongo import MongoClient as mc

client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
db = client.scada
coleccion = db.measures

cursor = coleccion.find()

for c in cursor:
    print(c)

