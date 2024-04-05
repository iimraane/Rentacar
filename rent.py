import mysql.connector
from deflist_rent import *
import sys
import os
from datetime import datetime, timedelta
import time

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier = "rent.py"
chemin_fichier = os.path.join(repertoire_script, nom_fichier)

# Établir la connexion à la base de données
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="imrane789",
    database="VOITURE_TUTO"
)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor = connexion.cursor()

# Vérifier si la connexion est établie avec succès
if connexion.is_connected():
    print("Connexion réussie!")

else:
    print()
    print("Erreur de connection a la base de donnée")
    sys.exit(2)

print("En continuant vous accepter nos CGU: https://tinyurl.com/CGU-Rentacar")
print()
print()
print("Bienvenue dans le logiciel 'Rentacar'")
print()
print("Je vais proceder par étape:")
print("Voulez vous afficher les informations d'un client ? (Oui/Non)")
print()


choice = demander_action_rent()

if choice == "oui":

    print()
    print("Entrez l'identifiant du client que vous souhaitez examiner :")
    print("1, 2, 3, 4, 5, 6")
    print("Entrez 'Back' pour continuer")
    print()

    while True:
        choice2 = demander_nombre_rent2()

        if choice2 == "back":
            break

        cursor.execute(f"SELECT * FROM customer WHERE customer_id = {choice2};")
        rows = cursor.fetchall()
        print()
        for row in rows:
            print(*row)

else:
    pass


print()
print("Ensuite, voulez vous afficher les informations sur une voiture ? (Oui/Non)")
print()

choice3 = demander_action_rent()

if choice3 == "oui":
    print()
    print("Entrez l'identifiant de la voiture que vous souhaitez examiner:")
    print("19, 20, 21, 22, 23, 24")
    print("Entrez 'back' pour continuer")
    print()

    while True:
        choice4 = demander_nombre_rent3()

        cursor.execute(f"SELECT * FROM car WHERE car_id = {choice4};")

        # Récupérer les résultats de la requête SELECT
        rows = cursor.fetchall()

        if choice4 == "back":
            break

        print()
        print("Car ID, Couleur, Plaque, Marque, Etat")
        print()
        for row in rows:
            print(row)  # Affichez chaque ligne, pas l'ensemble des résultats

else:
    pass

print()
print("Ensuite, voulez vous prendre une voiture ? (Oui/Non)")
print()

choice5 = demander_action_rent()

if choice5 == "oui":
    print("Entrez l'identifiant de la voiture que vous voulez prendre:")
    cursor.execute("SELECT car_id FROM car WHERE state = 'libre'")
    rows = cursor.fetchall()
    
    print(*rows)
    

    while True:
        choice6 = demander_nombre_rent()

        cursor.execute(f"SELECT state FROM car WHERE car_id = '{choice6}'")
        rows = cursor.fetchone()

        if rows == "libre":
            break
        
        elif rows != "libre":
            print("La voiture est deja prise, veuillez en choisir une autre")
        
        elif rows == None:
            print("Cette voiture n'existe pas")
        
    cursor.execute(f"UPDATE car SET state = 'Occupée' WHERE car_id = {choice6};")
    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print("Maintenant choisissez votre identifiant client:")
    print("1, 2, 3, 4, 5, 6")
    print()

    while True:
        choice7 = demander_nombre_rent()

        cursor.execute(f"SELECT last_name FROM customer WHERE customer_id = '{choice7}'")
        rows = cursor.fetchone()

        if not rows:
            print("Cette utilisateur n'existe pas")
        
        else:
            break

    cursor.execute(f"INSERT INTO rent (car_id, customer_id) VALUES ({choice6}, {choice7});")
    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print("Maintenant entrez la date de rendu souhaité de la voiture:")
    print()

    while True:
        choice8 = obtenir_date_rent()
        difference_dates = choice8 - datetime.now().date()
        if difference_dates.days > 30:
            print("La date de location est trop éloignée dans le futur. Veuillez choisir une date dans les 30 prochains jours.")
        else:
            break

    cursor.execute(f"UPDATE rent SET start_date = '{datetime.now().date()}' WHERE id = {choice7};")
    cursor.execute(f"UPDATE rent SET end_date = '{choice8}' WHERE id = {choice7};")

    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)   
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print("Location enregistrée !")
    print()
    

print()
print("Voulez vous rendre une voiture ? (Oui/Non)")
print()

choice9 = demander_action_rent()

if choice9 == "oui":

    print()
    print("Choisissez la voiture que vous souhaitez rendre:")
    cursor.execute(f"SELECT car_id FROM car WHERE State = 'Occupée'")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(*rows)

    choice10 = demander_nombre_rent()

    cursor.execute(f"UPDATE car SET state = 'Libre' WHERE car_id = {choice10};")

    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print("La voiture a bien été rendu !")

print()
print("Voulez vous recommencez ? (Oui/Non)")
print()

choice11 = demander_action_rent()

if choice11 == "non":
    print("Vous allez quitter le programme")
    sys.exit(2)
        
else: 
    os.system(f"python \"{chemin_fichier}\"")
    
cursor.close()
connexion.close()




