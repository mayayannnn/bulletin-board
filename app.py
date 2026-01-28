from db import Todo
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route("/")
def top():
    todos = Todo.select()
    return render_template("top.html" , todos = todos)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    memo = request.form["memo"]
    Todo.create(memo=memo)
    return redirect("/")
    
@app.route("/update/<id>")
def update(id):
    id = int(id)
    memo = Todo.get(Todo.id == id)
    return render_template("update.html",memo=memo)

@app.route("/edit", methods=["POST"])
def edit():
    memo = request.form["memo"]
    id = request.form["id"]
    db = Todo.get(Todo.id == id)
    db.memo = memo
    db.save()
    return redirect("/")

@app.route("/delete/<id>")
def delete(id):
    id = id
    db = Todo.get(Todo.id == id)
    db.delete_instance()
    return redirect("/")

app.run(debug=True,host="0.0.0.0")