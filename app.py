from flask import Flask, render_template, request, url_for, flash, redirect
import pyodbc

# Connexion à la base de données SQL Server

DSN = 'Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from Produit")

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


@app.route("/magasin", methods=['GET', 'POST'])
def magasin():
    DSN = "Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;"
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("select * from Magasin")
    data = cursor.fetchall()
    conn.close()
    return render_template("magasin.html", data=data)


"""@app.route("/magasin")  # troisième route pour la deuxième page
def magasin():
    return render_template("magasin.html")  # lien de la deuxième page"""


@app.route("/deconnexion")  # quatrième route pour la deuxième page
def deconnexion():
    return render_template("index.html")  # lien de la deuxième page


@app.route("/formulaire", methods=["GET", "POST"])
def formulaire():
    if request.method == 'POST':
        nom = request.form["nom"]
        adresse = request.form["adresse"]
        telephone = request.form["telephone"]
        email = request.form["email"]
        DSN = "Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;"
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Magasin (Nom, Adresse, Telephone, Email)
            VALUES ( ?, ?, ?, ?)
         ''', (nom, adresse, telephone, email))
        conn.commit()
        conn.close()
        flash("Votre magasin a été enregistré avec succès !", 'info')
        return redirect(url_for('magasin'))
    data = ''
    return render_template("formulaire.html", data=data)


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


@app.route("/produit", methods=['GET', 'POST'])
def produit():
    # -------------------------------------------------------------
    # 1. Déclaration des variables et des objets
    # -------------------------------------------------------------
    # Variables
    DSN = 'Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;'

    # Objets
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    # -------------------------------------------------------------
    # 2. Exécution des requêtes SQL et récupération des données
    # -------------------------------------------------------------
    cursor.execute("select * from Produit")
    data = cursor.fetchall()

    # -------------------------------------------------------------
    # 3. Fermeture de la connexion et affichage des données
    # -------------------------------------------------------------
    conn.close()

    # Affichage des données dans le template HTML
    return render_template("produit.html", data=data)


@app.route("/formulaireproduit", methods=["GET", "POST"])
def formulaireproduit():
    if request.method == 'POST':
        nom = request.form["nom"]
        description = request.form["description"]
        stockactuel = request.form["stockactuel"]
        prixunitaire = request.form["prixunitaire"]
        DSN = 'Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;'
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
    data = ''
    return render_template("formulaireproduit.html", data=data)


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


@app.route('/MagEdit/<int:item_id>', methods=['GET', 'POST'])
def MagEdit(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Magasin WHERE IdMagasin = ?', (item_id,))
    data = cursor.fetchone()
    if request.method == 'POST':
        nom = request.form["nom"]
        adresse = request.form["adresse"]
        telephone = request.form["telephone"]
        email = request.form["email"]
        cursor.execute('''
            UPDATE Magasin
            SET Nom = ?, Adresse = ?, Telephone = ?, Email = ?
            WHERE IdMagasin = ?
        ''', (nom, adresse, telephone, email, item_id))
        conn.commit()
        conn.close()
        flash(f'Le magasin numéro {item_id} a été modifié avec succès !', 'info')
        return redirect(url_for('magasin'))
    return render_template('formulaire.html', data=data)


@app.route('/MagDelete/<int:item_id>', methods=['GET', 'POST'])
def MagDelete(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Magasin WHERE IdMagasin = ?', item_id)
    conn.commit()
    conn.close()
    flash(f'Le magasin numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('magasin'))


@app.route("/vente")
def vente():
    DSN = "Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;"
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT Vente.IdVente, Produit.Nom, Magasin.Nom, Vente.Quantite, Vente.PrixTotal 
    FROM Magasin, Produit, Vente
    WHERE Magasin.IdMagasin=Vente.IdMagasin AND Produit.CodeProduit=Vente.CodeProduit
    """)
    data = cursor.fetchall()
    conn.close()
    return render_template("vente.html", data=data)


@app.route("/formulairevente", methods=["GET", "POST"])
def formulairevente():
    DSN = "Driver={SQL Server};Server=y_muhamad\\SQLEXPRESS;Database=ZORO;"
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit")
    prods = cursor.fetchall()
    cursor.execute('SELECT * FROM Magasin')
    mags = cursor.fetchall()

    if request.method == 'POST':
        nomproduit = request.form["nomproduit"]
        nommagasin = request.form["nommagasin"]
        quantite = request.form["quantite"]
        cursor.execute('''
        SELECT Produit.PrixUnitaire FROM Produit WHERE Produit.CodeProduit = ?
        ''', nomproduit)
        prixunitaire = cursor.fetchone()
        prixtotal = int(quantite) * int(prixunitaire[0])
        cursor.execute('''
            INSERT INTO Vente (Quantite, PrixTotal, CodeProduit, IdMagasin)
            VALUES ( ?, ?, ?, ?)
         ''', (quantite, prixtotal, nomproduit, nommagasin))
        conn.commit()
        conn.close()
        flash("Votre magasin a été enregistré avec succès !", 'info')
        return redirect(url_for('vente'))
    data = ''
    return render_template("formulairevente.html", data=data, mags=mags, prods=prods)


@app.route('/VentEdit/<int:item_id>', methods=['GET', 'POST'])
def ventedit(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produit")
    prods = cursor.fetchall()
    cursor.execute('SELECT * FROM Magasin')
    mags = cursor.fetchall()
    cursor.execute("""
        SELECT Magasin.Nom, Produit.Nom
        FROM Vente
        INNER JOIN Magasin ON Vente.IdMagasin = Magasin.IdMagasin
        INNER JOIN Produit ON Vente.CodeProduit = Produit.CodeProduit
        WHERE IdVente = ?
    """, item_id)
    magsel, prodsel = cursor.fetchone()
    cursor.execute('''
    SELECT Vente.Quantite
    FROM Vente
    WHERE IdVente = ?
    ''', item_id)
    data = cursor.fetchone()
    if request.method == 'POST':
        nomproduit = request.form["nomproduit"]
        nommagasin = request.form["nommagasin"]
        quantite = request.form["quantite"]
        cursor.execute('''
            SELECT Produit.PrixUnitaire FROM Produit WHERE Produit.CodeProduit = ?
        ''', nomproduit)
        prixunitaire = cursor.fetchone()
        prixtotal = int(quantite) * int(prixunitaire[0])
        cursor.execute('''
            UPDATE Vente
            SET Quantite = ?, PrixTotal = ?, CodeProduit = ?, IdMagasin = ?
            WHERE IdVente = ?
         ''', (quantite, prixtotal, nomproduit, nommagasin, item_id))
        conn.commit()
        conn.close()
        flash(f'Le magasin numéro {item_id} a été modifié avec succès !', 'info')
        return redirect(url_for('vente'))
    return render_template('formulaireventedit.html', magsel=magsel, prodsel=prodsel, data=data, prods=prods, mags=mags)


@app.route('/VenteDelete/<int:item_id>', methods=['GET', 'POST'])
def VenteDelete(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Vente WHERE IdVente = ?', item_id)
    conn.commit()
    conn.close()
    flash(f'La vente numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('vente'))


if __name__ == '__main__':  # si notre nom = a main executer app
    app.run(debug=True)  # debug=True pour ne pas avoir à relancer à chaque fois l'application
