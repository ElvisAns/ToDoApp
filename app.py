from flask import Flask
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
    title = db.Column(db.String(),nullable=False,unique=True)
    description = db.Column(db.String(50),nullable=False)
    completed = db.Column(db.Boolean,default=0)
    def __repr__(self): #will handle printing more especially in debugging
        return f'<Person : {self.title} , {self.description}> is it completed yet? {self.completed}'
