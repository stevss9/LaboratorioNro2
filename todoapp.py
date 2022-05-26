#Importamos las librerias
from flask import Flask, redirect, render_template

#Objeto para inicilizar la aplicacion
app = Flask(__name__)

#Controlador de la ruta inicial
@app.route('/')
def index():
    return render_template('index.html')

#Main de la app
if __name__ == '__main__':
    app.run(debug=True)