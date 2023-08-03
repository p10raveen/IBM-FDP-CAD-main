from flask import Flask,url_for,redirect 
from flask import render_template
app = Flask(__name__) 

@app.route('/')
def index():
    return "Index Page"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return "<h1>HOME</h1>"

@app.route('/user/<enter>')
def user(enter):
    if enter=="home":
        return redirect(url_for("home"))   # url_for: user to create a dynamic page, work with function name not route name
    elif enter=="about":
        return redirect(url_for("about"))
    else:
        return redirect(url_for("index"))
    
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug= True)



