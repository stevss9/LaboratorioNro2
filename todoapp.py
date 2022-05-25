from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////listas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class Tarea(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False

db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    content = request.form['content']



if __name__ == '__main__':
    app.run(debug=True)
