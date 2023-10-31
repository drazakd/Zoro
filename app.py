import pyodbc
from flask import Flask, render_template, request, url_for, flash, redirect

DSN = "Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;"
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from Magasin")

app = Flask(__name__)  # montre le nom (app) de notre application a flask
app.config['SECRET_KEY'] = 'clés_flash'


# les routes sont les chemins qui vont nous permettre d'afficher notre page, elles se font grâce à @nomdelapp.route("/")
# / pour la route

@app.route("/")  # page principale pour specifier le chemin
def connexion():  # nom de la fonction
    return render_template("index.html")


@app.route("/connexion")  # deuxième route pour la deuxième page
def accueil():
    return render_template("base.html")  # lien de la deuxième page


@app.route("/magasin")  # troisième route pour la deuxième page
def magasin():
    return render_template("magasin.html")  # lien de la deuxième page


@app.route("/deconnexion")  # quatrième route pour la deuxième page
def deconnexion():
    return render_template("index.html")  # lien de la deuxième page


@app.route("/formulaire")  # cinquième route pour la deuxième page
def formulaire():
    return render_template("formulaire.html")  # lien de la deuxième page


@app.route("/add")  # sixième route pour la deuxième page
def addmagasin():
    return render_template("add.html")  # lien de la deuxième page


@app.route("/modifier")
def modifier():
    return render_template("modifiermagasin.html")


@app.route("/magasinmodif")
def magasinmodif():
    return render_template("magasinmodifie.html")


@app.route("/supprimer")
def supprimer():
    return render_template("supprimera.html")


@app.route("/magsup")
def magsup():
    return render_template("magasinsupprime.html")


@app.route("/formulaireproduit")
def formulaireproduit():
    return render_template("formulaireproduit.html", methods=['GET', 'POST'])


# @app.route("/produit")
# def produit():
#     return render_template("produit.html")

@app.route("/produit", methods=["GET", "POST"])
def produit():
    """
  Traite les données du formulaire de produit.
  """
    # Récupère les données du formulaire.
    #   Nom = request.form["nom"]
    #   description = request.form["description"]
    #   stockactuel = request.form["stockactuel"]
    #   prixunitaire = request.form["prixunitaire"]

    # Insère les données dans un tableau.
    #   produit = {
    #     "nom": nom,
    #     "description": description,
    #     "stockactuel": stockactuel,
    #     "prixunitaire": prixunitaire,
    #   }

    # Crée la sortie HTML de la page produit.
    return render_template("produit.html", produit=produit)


if __name__ == '__main__':  # si notre nom = a main executer app
    app.run(debug=True)  # debug=True pour ne pas avoir à relancer à chaque fois l'application
