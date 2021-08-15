from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt






app = Flask(__name__)
@app.route("/")
def index():
    numbers = [1, 2, 3, 4, 5]
    return render_template("index.html",answer = "evet",)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/article/<string:id>")
def detail(id):
    return "Article Id:" +id     
if __name__ == "__main__":
    app.run(debug=True)

