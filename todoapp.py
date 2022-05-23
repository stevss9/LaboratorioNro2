from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='DESKTOP-11JM9HJ'
app.config['MYSQL_USER']='sa'
app.config['MYSQL_PASSWORD']='090700'
app.config['MYSQL_DB']='Lab2'
mysql= MySQL(app)

@app.route("/")
def index():
    return 'HOLA MUNDO'

@app.route("/add")
def add():
    return 'Agregar productos a la lista'

@app.route("/edit")
def edit():
    return 'Editar productos a la lista'

@app.route("/delete")
def delete():
    return 'Eliminar productos a la lista'

if __name__=="__main__":
    app.run(port = 3000, debug = True)