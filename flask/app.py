from flask import Flask, render_template, request, redirect, url_for
# Flask is to create  flask instance which is a centralised object for routes and all the data, render template is used to render
#  html templates

app=Flask(__name__, template_folder="templates")
# creating instance, __name__ gives the name of current module and template folder is defined
todos=[{"task":"sample todo", "done": False}]

@app.route("/")
# @app is used as a decorator which maps fuctions with the url and / is for indicating the homepage

def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo=request.form['todo']
    todos.append({"task":  todo , "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo=todos[index]
    if request.method=="POST":
        todo['task']=request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]["done"]= not todos[index]["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))



if __name__=="__main__":
    app.run(debug=True)

#if name= main is that when the module is run directly when we directly run the module the name gets set to main
# app.run is used to run flask and debug=true means errors are displayed 