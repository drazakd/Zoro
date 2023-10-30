import pyodbc
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

def connect_db():
    return sqlite3.connect('appbd.py')


app = Flask(__name__)  # montre le nom (app) de notre application a flask


# les routes sont les chemin qui vont nous permettre d afficher notre page elle se font grace a @nomdelapp.route("/")
# / pour la route

@app.route("/")  # page principale pour specifier le chemin
def connexion():  # nom de la fontion
    return render_template("index.html")


@app.route("/connexion")  # deuxieme route pour la deuxieme page
def accueil():
    return render_template("base.html")  # lien de la deuxieme page


@app.route("/magasin")  # troisieme route pour la deuxieme page
def magasin():
    return render_template("magasin.html")  # lien de la deuxieme page


@app.route("/deconnexion")  # quatrieme route pour la deuxieme page
def deconnexion():
    return render_template("index.html")  # lien de la deuxieme page


@app.route("/formulaire")  # cinquieme route pour la deuxieme page
def formulaire():
    return render_template("formulaire.html")  # lien de la deuxieme page


@app.route("/add")  # sixieme route pour la deuxieme page
def addmagasin():
    return render_template("add.html")  # lien de la deuxieme page


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
    #   nom = request.form["nom"]
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
    app.run(debug=True)  # debug=True pour ne pas avoir a relancer a chaque fois l'application
