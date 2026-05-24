from flask import *
import sqlite3

# Création d'un objet application web Flask
app = Flask(__name__, static_url_path='/static')

# Fonctions utilisées pour appeler des commandes SQL
def lire_base():
    """ 
        Récupére des questions dans la table
        Renvoie (list of tuples) : liste des questions
    """
    connexion = sqlite3.connect("bdd/Question.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT * 
    FROM Question
    ORDER BY ID"""
    resultat = curseur.execute(requete_sql)
    qcm = resultat.fetchall()
    connexion.close()
    return qcm

def lire_base1():
    """ Récupére des questions dans la table
        Renvoie (list of tuples) : liste des utilisateurs
    """
    connexion = sqlite3.connect("bdd/Question.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT *
    FROM users
    ORDER BY id"""
    resultat1 = curseur.execute(requete_sql)
    qcm1 = resultat1.fetchall()
    connexion.close()
    return qcm1

def ajoute_enregistrement(indice, donnees):
    """ Créé l'enregistrement avec le nouvel id et les données saisies
        Renvoire un booléen : True si l'ajout a bien fonctionné
    """
    # Test si tous les champs sont renseignés
    parametre0 = donnees['nom']
    parametre1 = donnees['prenom']
    if parametre0 == "" or parametre1 == "" :
        return False
    parametres = (indice, parametre0, parametre1)
    connexion = sqlite3.connect("bdd/Question.db")
    curseur = connexion.cursor()
    requete_sql = """
    INSERT INTO users (id, nom, prenom) VALUES (?,?,?);"""
    res = curseur.execute(requete_sql, parametres)
    connexion.commit()
    connexion.close()
    return True

def idmax():
    """ Récupére l'id du prochain enregistrement
        Renvoie un entier
    """
    connexion = sqlite3.connect("bdd/Question.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT MAX(id)
    FROM users;"""
    res = curseur.execute(requete_sql)
    index = res.fetchall()
    connexion.close()
    return int(index[0][0])+1 # Transtype le résultat de la recherche et ajoute 1



# Création d'une fonction accueillir() associee a l'URL "/"
# pour générer une page web dynamique
@app.route("/")
def accueillir():
    """Présentation du site"""
    return render_template("index.html")

# Page utilisant une base de données
@app.route("/questions")
def sondage():
    """Questions du sondage"""
    questions = lire_base()
    return render_template("questionnaire.html", questions=questions)

@app.route("/resultats", methods = ['POST'])
def resultats():
    result = request.form
    chiffre = idmax()
    ajoute_enregistrement(chiffre, result)  # Créé l'enregistrement avec le nouvel id et les données saisies
    nombres = lire_base1()
    return render_template("resultats.html", nombres=nombres)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)