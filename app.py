from crypt import methods
from datetime import datetime
from flask_bootstrap import Bootstrap5
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:root@localhost:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)

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

now = datetime.now()
try:
    new_items = todo(title="Go to shop some snacks",description="Move a little bit to kin Marche and buy something",date=now.strftime("%d/%m/%Y %H:%M:%S"))
    db.session.add(new_items)
    db.session.commit()
except:
    #error in sql insert
    pass
finally:
    pass


@app.route("/")
def index():
    return render_template("index.html",
            data=todo.query.all(),
            url_save=url_for("save_to_do"),
            url_get_task=url_for("get_to_do"),
            url_delete_task=url_for("delete_to_do"),
            url_mark_complete=url_for("make_to_do_complete")
    )

@app.route("/get_tasks/", methods=['GET'])
def get_to_do():
    pass

@app.route("/save_to_do/", methods=['POST'])
def save_to_do():
    pass

@app.route("/delete_task/<int: id>",methods=['GET'])
def delete_to_do(id):
    pass

@app.route("/make_complete/<int: id>/",methods=['GET'])
def make_to_do_complete(id):
    pass