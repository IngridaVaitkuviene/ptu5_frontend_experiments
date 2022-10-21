# Flask yra populiariausias python'o microframework'as. 
# Jeigu projektas nėra labai didelis, arba tiesiog norime pasidaryti kažkokį GUI per naršyklę, 
# kažką greitai prototipuoti, Flask yra labai geras pasirinkimas. Su flask yra pakankamai paprasta gaminti API's. 
# Diegiasi pip install flask

# Kaip sukurti minimalią svetainę:
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Veikia!"

@app.route("/sveikas/<name>")
def user(name):
    return f"Sveikas, {name}"

@app.route("/grazi_diena")
def grazi_diena():
    return render_template("grazi_diena.html")

@app.route("/zmones")
def zmones():
    zmones = [
        'Justina', 'Darius', 'Ingrida', 'Linas', 
        'Ana', 'Simas', 'Arnoldas', 'Sergejus',
    ]
    return render_template("zmones.html", zmones=zmones)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/hello")
def hello():
    return render_template("hello.html", **request.args)


if __name__ == "__main__":
    app.run(debug=True)
