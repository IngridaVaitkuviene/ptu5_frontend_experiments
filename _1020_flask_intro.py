from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(debug=True)
