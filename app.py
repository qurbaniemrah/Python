from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():

 return "<p>Hello</p>"

@app.route("/about")
def about():
    return "<p>Haqqimda</p>"

if __name__ == "__main__":
    app.run(debug = True)