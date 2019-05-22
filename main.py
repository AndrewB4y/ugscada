from flask import Flask, render_template
from pymongo import MongoClient as mc

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
	client = mc("mongodb+srv://admin:admin@ugridscadamdb-bmod6.mongodb.net/test?retryWrites=true")
	db = client.scada
	coleccion = db.measures

	cursor = coleccion.find()

	cursor[0].get("magnitud")

	return cursor[0].get("magnitud")



@app.route('/bayo', methods=['GET', 'POST'])
def bayo():
	
	return "El string Bayo"


if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
