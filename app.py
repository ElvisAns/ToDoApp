from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:root@localhost:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class todo(db.Model):
    __tablename__ = 'todo' #dont use uppercase letter and space
    id =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False,unique=True)
    description = db.Column(db.String(),nullable=False)
    completed = db.Column(db.Boolean,default=False)
    date = db.Column(db.DateTime,nullable=False)
    def __repr__(self): #will handle printing more especially in debugging
        return f'<Person : {self.title} , {self.description}> is it completed yet? {self.completed}'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_tasks/")
def get_to_do():
    pass

@app.route("/save_to_do/")
def save_to_do():
    pass

@app.route("/delete_task/")
def delete_to_do():
    pass

@app.route("/make_complete/")
def make_to_do_complete():
    pass