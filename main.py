from flask import Flask, render_template, request
from pymongo import MongoClient as mc
import json
import math

#app = Flask(__name__)

app = Flask(__name__, template_folder='templates')

PORT = 5000
DEBUG = False
Pm = 0
Qm = 0
pf = 1

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
	Pm = cursor[0].get("magnitud")
	pf = Pm / (math.sqrt(Pm^2+Qm^2))
	return ("{:.2f}kVAR".format(Pm/1000))

@app.route('/leerQ', methods=['GET', 'POST'])
def leerQ():
	#window.alert("cliente mongo en conexión")
	client = mc("mongodb+srv://admin:admin@bayo0-2gtne.gcp.mongodb.net/test?retryWrites=true")
	#client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
	#client = mc("mongodb+srv://admin:admin@bayo0-2gtne.gcp.mongodb.net/test?retryWrites=true")
	db = client.uGridVars
	coleccion = db.scadaVars
	cursor = coleccion.find()
	Qm = cursor[1].get("magnitud")
	pf = Pm / (math.sqrt(math.pow(Pm,2)+math.pow(Qm,2)))
	return ("{:.2f}kVAR".format(Qm/1000))

@app.route('/calcPF', methods=['GET', 'POST'])
def calcPF():
	return ("{:.2f}".format(pf))



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
