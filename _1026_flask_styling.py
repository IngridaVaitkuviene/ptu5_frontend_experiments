from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("styling/home.html")

@app.route("/containers")
def containers():
    return render_template("styling/containers.html")

# gridas kaip tinklelis
@app.route("/grid")
def grid():
    return render_template("styling/grid.html")

@app.route("/page")
def fullpage():
    return render_template("styling/fullpage.html")

# kaip gridas, tik jis turi daugiau nukrypimu, nera tinkleliu, dydis nepriklauso nuo elemento dydziu
@app.route("/flex")
def flex():
    return render_template("styling/flex.html")

@app.route("/flexpage")
def flexpage():
    return render_template("styling/flexpage.html")

if __name__=="__main__":
    app.run(debug=True)