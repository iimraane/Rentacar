import mysql.connector
from deflist_rent import *
import sys
import os

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

print("En continuant vous accepter nos CGU: https://octagonal-outrigger-c6f.notion.site/Les-CGU-094464a0eda142a9ad849f7e729965bf?pvs=4")
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
    print("Entrez l'identifiant du client que vous souhaitez examiner:")
    print("1, 2, 3, 4, 5, 6")
    print()

    choice2 = demander_nombre_rent()

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
    print()

    choice4 = demander_nombre_rent()

    cursor.execute(f"SELECT * FROM car WHERE car_id = {choice4};")

    # Récupérer les résultats de la requête SELECT
    rows = cursor.fetchall()

    print("Car ID, Couleur, Plaque, Marque, Etat")
    for row in rows:
        print(*rows)

else:
    pass

print()
print("Ensuite, voulez vous prendre une voiture ? (Oui/Non)")
print()

choice5 = demander_action_rent()

if choice5 == "oui":

    print("Entrez l'identifiant de la voiture que vous voulez prendre:")
    print("19, 20, 21, 22, 23, 24")
    print()

    while True:
        choice6 = demander_nombre_rent()

        cursor.execute(f"SELECT state FROM car WHERE car_id = {choice6}")
        row = cursor.fetchone()

        if row is None:
            print("Cet identifiant de voiture n'existe pas. Veuillez réessayer.")
            continue

        if row[0] != "Libre":
            print("Cette voiture est déjà prise. Veuillez choisir une autre.")
        else:
            break  # Sortir de la boucle si la voiture est libre

    
    cursor.execute(f"UPDATE car SET state = 'Occupée' WHERE car_id = {choice6};")

    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print("Maintenant choisissez votre identifiant client:")
    print("1, 2, 3, 4, 5, 6")
    print()

    choice7 = demander_nombre_rent()

    cursor.execute(f"UPDATE rent SET car_id = {choice6}, customer_id = {choice7};")

    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print("Maintenant entrez la date de rendu souhaité de la voiture:")
    print()

    choice8 = obtenir_date_rent()

    cursor.execute(f"UPDATE rent SET start_date = CURDATE() WHERE id = {choice7};")
    cursor.execute(f"UPDATE rent SET end_date = '{choice8}' WHERE customer_id = {choice7};")

    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

else: 
    pass

print()
print("Voulez vous rendre une voiture ? (Oui/Non)")
print()

choice9 = demander_action_rent()

if choice9 == "oui":

    print()
    print("Choisissez la voiture que vous souhaitez rendre:")
    cursor.execute(f"SELECT car_id FROM car WHERE State = 'Occupée'")
    
    rows = cursor.fetchall()
    
    print(*rows)

    choice10 = demander_nombre_rent()

    cursor.execute(f"UPDATE car SET state = 'Libre' WHERE car_id = {choice10};")

    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    print()
    print("La voiture a bien été rendu !")


else: 
    print()
    print("Voulez vous recommencez ? (Oui/Non)")
    print()

    choice11 = demander_action_rent()

    if choice11 == "non":
        sys.exit()
    
    else: 
        os.system(f"python \"{chemin_fichier}\"")





