import mysql.connector

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

    # Insérer une nouvelle entrée dans la table 'car'
    cursor.execute("INSERT INTO car (Brand) VALUES ('BMW');")
    connexion.commit()  # Commit pour sauvegarder les modifications dans la base de données

    # Exécuter une requête SELECT pour récupérer les données de la table 'car'
    cursor.execute("SELECT Brand FROM car")
    
    # Récupérer les résultats de la requête SELECT
    rows = cursor.fetchall()

    # Afficher les résultats
    print("Liste des marques de voitures :")
    for row in rows:
        print(row[0])

    # Fermer le curseur et la connexion
    cursor.close()
    connexion.close()
else:
    print("La connexion a échoué!")