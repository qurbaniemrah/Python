from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

#Users registration form

class RegisterForm(Form):
    name = StringField("Ad Soyad",validators = [validators.length(min = 4,max = 25)])
    username = StringField("Username",validators = [validators.length(min = 5,max = 35)])
    email = StringField("Email",validators = [validators.Email(message = "Your email is not true")])
    password = PasswordField("Password:",validators = [
        validators.DataRequired(message = "Please create password"),
        validators.EqualTo(fieldname = "confirm",message = "Please enter correct password")
    ])

app = Flask(__name__)


app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "ybblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
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


"""
[
    {"id":1, "title": "Deneme1", "content": "Deneme 1 Icerik"}
    {"id":2, "title": "Deneme2", "content": "Deneme 2 Icerik"}
    {"id":3, "title": "Deneme3", "content": "Deneme 3 Icerik"}
]"""

