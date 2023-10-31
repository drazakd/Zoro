from flask import Flask, render_template, request, url_for, flash, redirect
import pyodbc
# from flask_sqlalchemy import SQLAlchemy

# Connexion à la base de données SQL Server

DSN = 'Driver={SQL Server};Server=DESKTOP-6RB7ER5\\SQLEXPRESS;Database=product;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from Produit")





app=Flask(__name__)#montre le nom (app) de notre application a flask
app.config['SECRET_KEY']='clés_flash'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://Server=DESKTOP-6RB7ER5\\SQLEXPRESS;Database=product'
# db = SQLAlchemy(app)

#les routes sont les chemin qui vont nous permettre d afficher notre page elle se font grace a @nomdelapp.route("/") / pour la route

@app.route("/") #page principale pour specifier le chemin
def connexion(): #nom de la fontion
    return render_template("index.html")

@app.route("/connexion") #deuxieme route pour la deuxieme page
def accueil():
    return render_template("base.html") #lien de la deuxieme page

@app.route("/magasin") #troisieme route pour la deuxieme page
def magasin():
    return render_template("magasin.html") #lien de la deuxieme page

@app.route("/deconnexion") #quatrieme route pour la deuxieme page
def deconnexion():
    return render_template("index.html") #lien de la deuxieme page


@app.route("/formulaire") #cinquieme route pour la deuxieme page
def formulaire():
    return render_template("formulaire.html") #lien de la deuxieme page



@app.route("/add") #sixieme route pour la deuxieme page
def addmagasin():
    return render_template("add.html") #lien de la deuxieme page



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

@app.route("/produit", methods=['GET','POST'])
def produit():
    DSN = 'Driver={SQL Server};Server=DESKTOP-6RB7ER5\\SQLEXPRESS;Database=product;'
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("select * from Produit")
    data = cursor.fetchall()
    conn.close()
    return render_template("produit.html", data=data)

# @app.route("/produit")
# def produit():
#     return render_template("produit.html")
# class Product(db.Model):
#     __tablename__ = 'Produit'
#     CodeProduit = db.Column(db.Integer, primary_key=True, autoincrement=True)

@app.route("/formulaireproduit", methods=["GET","POST"])
def formulaireproduit():
    if request.method == 'POST':

        nom = request.form["nom"]
        description = request.form["description"]
        stockactuel = request.form["stockactuel"]
        prixunitaire = request.form["prixunitaire"]
        DSN = 'Driver={SQL Server};Server=DESKTOP-6RB7ER5\\SQLEXPRESS;Database=product;'
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Produit (Nom, Descriptions, StockActuel, PrixUnitaire)
            VALUES ( ?, ?, ?, ?)
         ''', (nom, description, stockactuel, prixunitaire))
        conn.commit()
        conn.close()
        flash("Votre produit a été enregistré avec succès !", 'info')
        return redirect(url_for('produit'))
    data=''
    return render_template("formulaireproduit.html",data=data)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item_id = int(item_id)

    # Connexion à la base de données
    conn = pyodbc.connect(DSN)

    # Création d'un objet curseur
    cursor = conn.cursor()

    # Récupération des données du produit depuis la base de données
    cursor.execute('SELECT * FROM produit WHERE CodeProduit = ?', (item_id,))
    data = cursor.fetchone()

    # Si la méthode de la requête est POST, mise à jour des données du produit dans la base de données
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.form['nom']
        description = request.form['description']
        stockactuel = request.form['stockactuel']
        prixunitaire = request.form['prixunitaire']

        # Mise à jour des données du produit dans la base de données
        cursor.execute('''
            UPDATE produit
            SET Nom = ?, Descriptions = ?, StockActuel = ?, PrixUnitaire = ?
            WHERE CodeProduit = ?
        ''', (nom, description, stockactuel, prixunitaire, item_id))

        # Validation des modifications dans la base de données
        conn.commit()

        # Fermeture de la connexion à la base de données
        conn.close()

        # Affichage d'un message de succès à l'utilisateur
        flash(f'Le produit numéro {item_id} a été modifié avec succès !', 'info')

        # Redirection de l'utilisateur vers la page du produit
        return redirect(url_for('produit'))

    # Retour du modèle de formulaire du produit
    return render_template('formulaireproduit.html', data=data)

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    item_id = int(item_id)

    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM produit WHERE CodeProduit = ?', (item_id,))

    conn.commit()
    conn.close()

    flash(f'Le produit numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('produit'))

if __name__== '__main__': # si notre nom = a main executer app
    app.run(debug=True) #debug=True pour ne pas avoir a relancer a chaque fois l'application