#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
app = Flask(__name__, template_folder='templates')

#Clave  de la app
app.secret_key = '090700'

#Array donde almacenaremos los datos
task_list = []

#Controlador de la ruta inicial
@app.route('/')
def index():
    return render_template('index.html', task_list=task_list)

#Controlador de la ruta de envio de datos
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        task_description = request.form['task_description']
        task_email = request.form['task_email']
        task_priority = request.form['task_priority']

        if task_description == '' or task_email == '':            
            return redirect(url_for('index'))
        else:
            task_list.append({'task_description': task_description, 'task_email': task_email, 'task_priority': task_priority })
            return redirect(url_for('index'))

#Controlador de la ruta para delete los datos de la tabla
@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':        
        if task_list == []:
            return redirect(url_for('index'))
        else:
            task_list.clear()
            return redirect(url_for('index'))

#Main de la app
if __name__ == '__main__':
    app.run(debug=True)