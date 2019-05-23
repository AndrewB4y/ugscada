from flask import Flask, render_template, request
from pymongo import MongoClient as mc
import json

#app = Flask(__name__)

app = Flask(__name__, template_folder='templates')

PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
	return "Not Found."


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/control', methods=['GET', 'POST'])
def control():
	return render_template('control.html')




@app.route('/leerP', methods=['GET', 'POST'])
def leerP():
	#window.alert("cliente mongo en conexión")
	client = mc("mongodb+srv://admin:admin@bayo0-2gtne.gcp.mongodb.net/test?retryWrites=true")
	#client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
	#client = mc("mongodb+srv://admin:admin@bayo0-2gtne.gcp.mongodb.net/test?retryWrites=true")
	db = client.uGridVars
	coleccion = db.scadaVars
	cursor = coleccion.find()
	cursor[0].get("magnitud")
	return cursor[0].get("magnitud")



@app.route('/write', methods=['GET', 'POST'])
def write():
	di = json.loads(request.args.get('sch'))
	#x = request.args.get('sch')
	ActualizarDato(di, "3")
	return json.dumps(di) # se imprime el diccinario solo con proposito de prueba
	#return x






# este metodo actualiza un record de la coleccion measures
def ActualizarDato(dato, id):
    client = mc("mongodb+srv://admin:admin@bayo0-2gtne.gcp.mongodb.net/test?retryWrites=true")
	#client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
	#client = mc("mongodb+srv://admin:admin@ugridscada-2gtne.mongodb.net/test?retryWrites=true")
    db = client.uGridVars
    coleccion = db.scadaVars
    coleccion.update_one({'_id':id}, {"$set": dato})






if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
