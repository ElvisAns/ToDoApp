from crypt import methods
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