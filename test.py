from flask import Flask

app = Flask(__name__) #__name__ je funkcija koja veli flasku gdje su mi svi files(u ovom slucaju - u ovom folderu)


#refrence na app varijablu koju smo gore kreirali:
@app.route("/") #python decorator
#route znaci da nas nekamo usmjerava, u ovom slucaju "/" je root lokacije


#ovdje stvaramo novu funckiju koja ce se pokrenuti kada dodjemo u root na webu
def index():
    return "Drink more energy drinks RIGHT NOW!"


#govorimo programu nek pokrene tu aplikaciju na webu, na host-u i port-u kojega smo mi sami odredili(ako jedan port ne radi probamo drugi)
app.run(host="0.0.0.0", port=80)
#0.0.0.0 znaci da bude pokrenul rutu na sve moguce adrese koje PC upravlja