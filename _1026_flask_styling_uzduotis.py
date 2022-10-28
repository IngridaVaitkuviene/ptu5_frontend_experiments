from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/zalia_balta")
def home():
    return render_template("styling/zalia_balta.html")

@app.route("/vikipedija")
def vikipedija():
    return render_template("styling/vikipedija.html")

if __name__=="__main__":
    app.run(debug=True)