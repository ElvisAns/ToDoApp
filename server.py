from crypt import methods
from glob import escape
from flask import Flask,url_for
from requests import request

app = Flask(__name__)

@app.route("/user/<string:name>")
def hello_world(name):
    return f'<p>Hello, {name} World!</p>'

names=["Bonjour","Echo"]

@app.route("/user/getbyId/<int:id>/")
def view_per_id(id):
    try:
        res = f'<p>Hello, {names[id]} World!</p>'
    except:
        res = "Error reading your data"
    finally:
        return res

@app.route("/list_routes")
def view_all_routes():
    return f'<a href="{url_for("view_per_id",id=1)}">Go to this ID</a>' #generate url for function name and pass parameters

@app.route("/routesWithMethods",methods=["GET","POST"]) #this route accepts GET and POST
def submitSomething():
    if(request.method=="POST"):
        return "You have sent some post request"
    if(request.method=="GET"):
        return "You have sent some GET request"

#Same as the preceding example we are going to handle request with magic trigers

@app.get("/routesWithShortcutDeco")
def submittedGetReq():
    return "You have sent some GET request"

@app.post("/routesWithShortcutDeco")
def submittedPostReq():
    return "You have sent some post request"

@app.route("/hello/<path:name>/") #here path is the type converter and there is string,int,path,float and uuid
def helloBwan(name):
    return f'<h2>Hello Dear {escape(name)}</h2>' #f help us print template litteral and escape prevent injection but remember in all template, JINJA,the template engine already do it for us