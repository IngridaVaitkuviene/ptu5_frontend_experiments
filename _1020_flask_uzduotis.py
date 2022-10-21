# 1.Sukurti programą, kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu (rekomenduojama naudoti šablonus)
# 2.Sukurti programą, kuri įvedus norimą žodį adreso eilutėje (po / simbolio) ir paspaudus ENTER, atspausdintų jį penkis kartus.
# 3.Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų visus keliamuosius metus nuo 1900 iki 2100 metų.
# 4.Sukurti programą, kuri leistų įvesti metus ir paspaudus patvirtinimo mygtuką parodytų, ar jie yra keliamieji.


from flask import Flask, render_template, request

app = Flask(__name__)

# 1.
@app.route("/")
def home():
    return "Sveiki, čia mano pirmasis web puslapis ir, aišku, čia nieko nėra, bet aš dar mokausi :) ♥"

# 2.
# @app.route("/<zodis>")
# def penkis_kartus(zodis):
#     return f"{zodis}, {zodis}, {zodis}, {zodis}, {zodis}"

# 3. pirmas variantas
# @app.route("/keliamieji")
# def keliamieji():
#     keliamieji=[]
#     for metai in range(1900, 2101):
#         if metai % 4 == 0 and (metai % 100 !=0 or metai % 400 == 0):
#             keliamieji.append(metai)
#     return f"Keliamieji metai nuo 1900 iki 2100 metų: {keliamieji}"

# 3. antras variantas
# @app.route("/keliamieji")
# def keliamieji():
#     keliamieji_metai=[]
#     for metai in range(1900, 2101):
#         if metai % 4 == 0 and (metai % 100 !=0 or metai % 400 == 0):
#             keliamieji_metai.append(metai)
#     return render_template("keliamieji.html", keliamieji=keliamieji_metai)


# 4. pirmas variantas
# @app.route("/<metai>")
# def ar_keliamieji(metai):
#     if int(metai) % 4 == 0 and (int(metai) % 100 !=0 or int(metai) % 400 == 0):
#         return f"{metai} keliamieji metai"
#     else:
#         return f"{metai} nėra keliamieji metai"

# 4. antras variantas
@app.route("/login_keliamieji")
def login():
    return render_template("login_keliamieji.html")

@app.route("/ar_keliamieji")
def ar_keliamieji():
    ivesti_metai = int(request.args["metai"])
    if ivesti_metai % 4 == 0 and (ivesti_metai % 100 !=0 or ivesti_metai % 400 == 0):
        atsakymas = "keliamieji"
    else:
        atsakymas = "nekeliamieji"
        return render_template("keliamieji_metai.html", **request.args, atsakymas=atsakymas)

if __name__ == "__main__":
    app.run(debug=True)