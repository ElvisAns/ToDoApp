from flask import Flask, render_template, request, redirect, url_for,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://udacitystudios@localhost:5432/todoapp'
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)
  completed = db.Column(db.Boolean, nullable=False, default=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

@app.route('/todos/create', method=['POST'])
def create_todo():
  error = False
  body = {}
  try:
    description = request.form.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if error:
    abort (400)
  else:
    return jsonify(body)

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())