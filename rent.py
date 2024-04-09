import mysql.connector
from deflist_rent import *
import sys
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

repertoire_script = os.path.dirname(os.path.abspath(__file__))
nom_fichier = "rent.py"
chemin_fichier = os.path.join(repertoire_script, nom_fichier)
dotenv_path = os.path.expanduser("~/Desktop/.env")  # Chemin vers votre fichier .env
load_dotenv(dotenv_path)

# Établir la connexion à la base de données
connexion = mysql.connector.connect(
    host= os.getenv("db_host"),
    user= os.getenv("db_user"),
    password= os.getenv("db_password"),
    database= os.getenv("db_database_name")
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
print("Pour avoir des informations sur un client, entrez 1")
print("Pour avoir des informations sur une voiture, entrez 2")
print("Pour voir les voitures disponibles, entrez 3")
print("Pour louer une voiture, entrez 4")
print("Pour rendre une voiture, entrez 5")
print("Pour quitter, entrez 'Back'")
print()

choice_menu = demander_action_rent2()

if choice_menu == "1":

    print()
    print("Voici les information des clients sous la forme ci-dessous:")
    print("Client ID, Prénom, Nom, Numéro de téléphone, Email, Adresse, Age")
    print()

    cursor.execute(f"SELECT * FROM customer;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


elif choice_menu == "2":

    print("Entrez une marque de voiture pour voir toutes les voitures de celle ci")
    print("Attention au majuscules !")
    print("Voici les marques que nous avons:")
    print()
    cursor.execute("SELECT Brand FROM car")
    resultat = cursor.fetchall()
    for row in resultat:
        print(row[0])
    print()
    
    mark2 = [row[0] for row in resultat]

    while True:
        mark = input("Entrez une marque :")
        print()
        cursor.execute("SELECT Brand FROM car")
        resultat = cursor.fetchall()
        if mark not in mark2:
            print("Cette marque n'existe pas ou nous n'avons pas de voiture de cette marque")
            continue
        else: 
            break

        

    print("Voici les information des voitures sous la forme ci-dessous:")
    print("Car ID, Couleur, Plaque, Marque, Etat, Année")
    print()

    cursor.execute("SELECT * FROM car WHERE Brand = %s", (mark,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

elif choice_menu == "3":

    print()
    print("Entrez la date jusqu'a laquelle vous souhaitez avoir une voiture:")

    now = datetime.now()

    while True:
        date = demander_date_rent()
        # Vérifier si la date de rendu est antérieure à la date actuelle
        if date < now:
            print("La date de rendu ne peut pas être antérieure à la date actuelle. Veuillez saisir une nouvelle date.")
            continue
        
        break

    cursor.execute(f"SELECT * FROM car WHERE state = 'libre' AND car_id NOT IN ( SELECT car_id FROM rent WHERE start_date <= '{date}' AND end_date >= '{date}');")
    result = cursor.fetchall()

    if result:
        print("Voitures disponibles à la réservation à la date", date, ":")
        for row in result:
            print(row)
    else:
        print("Aucune voiture disponible à la réservation à la date", date)


elif choice_menu == "4":

    print("Entrez l'identifiant de la voiture que vous voulez prendre:")
    cursor.execute("SELECT car_id FROM car WHERE state = 'libre';")
    rows = cursor.fetchall()
    
    print(*rows)
    

    while True:
        choice6 = demander_nombre_rent()
    
    # Vérifier si l'identifiant saisi par l'utilisateur est parmi ceux affichés au début
        if choice6 not in [row[0] for row in rows]:
            print("Veuillez entrer un identifiant de voiture valide.")
            continue
    
        cursor.execute(f"SELECT state FROM car WHERE car_id = '{choice6}'")
        rows = cursor.fetchone()

        if rows[0] == "libre":
            break
        
        elif rows[0] == None:
            print("Cette voiture n'existe pas")
            
    cursor.execute(f"UPDATE car SET state = 'Occupée' WHERE car_id = {choice6};")

    print()
    print("Maintenant choisissez votre identifiant client:")
    print("1, 2, 3, 4, 5, 6")
    print()

    while True:
        choice7 = demander_nombre_rent()
        
        # Vérifier si l'identifiant saisi par l'utilisateur est parmi ceux affichés au début
        if choice7 not in [1, 2, 3, 4, 5, 6]:
            print("Veuillez entrer un identifiant de client valide.")
            continue
        
        cursor.execute(f"SELECT last_name FROM customer WHERE customer_id = '{choice7}'")
        rows = cursor.fetchone()

        if not rows:
            print("Cet utilisateur n'existe pas")
        else:
            break

    cursor.execute(f"INSERT INTO rent (car_id, customer_id) VALUES ({choice6}, {choice7});")

    print()
    print("Maintenant entrez la date de rendu souhaité de la voiture:")
    print("Un jour minimum !")
    print()

    now = datetime.now()

    while True:
        choice8 = demander_date_rent()
    
    # Vérifier si la date de rendu est antérieure à la date actuelle
        if choice8 < now:
            print("La date de rendu ne peut pas être antérieure à la date actuelle. Veuillez saisir une nouvelle date.")
            continue
        
        break
    cursor.execute(f"UPDATE rent SET start_date = '{now}' WHERE customer_id = {choice7};")
    cursor.execute(f"UPDATE rent SET end_date = '{choice8}' WHERE customer_id = {choice7};")

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
    time.sleep(1)
    print("Voici les informations de votre réservation:")
    print("Voiture ID, Client ID, Date de debut, Date de fin")
    cursor.execute(f"SELECT * FROM rent WHERE car_id = {choice6}")
    rows = cursor.fetchall()    
    for row in rows:
        print(*row)
    time.sleep(2)

elif choice_menu == "5":

        cursor.execute(f"SELECT car_id FROM car WHERE State = 'Occupée'")
        rows = cursor.fetchall()
        
        if not rows:
            print("Il n'y a aucun voiture a rendre")
        else:
            print()
            print("Choisissez la voiture que vous souhaitez rendre:")
            print(*rows)

            choice10 = demander_nombre_rent()

            cursor.execute(f"UPDATE car SET state = 'libre' WHERE car_id = {choice10};")
            cursor.execute(f"DELETE FROM rent WHERE car_id = {choice10}")

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
            print("La voiture a bien été rendu !")


elif choice_menu == "back":
    print("Nous allons quitter le programme...")
    sys.exit(2)

else: 
    print("Ce n'est pas un nombre valide")
    print("Nous allons relancer le programme...")
    time.sleep(2)
    os.system(f"python \"{chemin_fichier}\"")

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




