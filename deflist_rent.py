# Exécuter une requête SELECT pour récupérer les données de la table 'car'
#cursor.execute("SELECT Brand FROM car")

# Récupérer les résultats de la requête SELECT
# rows = cursor.fetchall()

# for row in rows:
#     print(row[0])

# cursor.close()
# connexion.close()

def demander_nombre_rent2():
    #Demander à l'utilisateur s'il veut rejouer ou revenir au menu.
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["1", "2", "3", "4", "5", "6", "back"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur

def demander_nombre_rent3():
    #Demander à l'utilisateur s'il veut rejouer ou revenir au menu.
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["1", "2", "3", "4", "5", "6", "back"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur

def demander_action_rent():
    #Demander à l'utilisateur s'il veut rejouer ou revenir au menu.
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["oui", "non"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur

def demander_nombre_rent(max_val=4, min_val=1):
    try:
        # Tentez de convertir l'entrée en un nombre entier
        entree_utilisateur = int(input("Votre choix :"))
        return entree_utilisateur
        # Si la conversion est réussie, la boucle se termine
    
    except ValueError:
        # Si une exception ValueError est levée, cela signifie que l'entrée n'est pas un nombre
            print("Ce n'est pas un nombre valide. Veuillez réessayer.")
            return demander_nombre_rent()
    

from datetime import datetime

def demander_date_rent():
    while True:
        try:
            # Demander à l'utilisateur de saisir une date au format 'YYYY-MM-DD'
            date_str = input("Veuillez entrer une date au format YYYY-MM-DD : ")
            
            # Convertir la chaîne en objet datetime
            date = datetime.strptime(date_str, "%Y-%m-%d")
            
            # Si la conversion réussit, retourner la date
            return date
        except ValueError:
            # Si la conversion échoue, afficher un message d'erreur
            print("Format de date invalide. Veuillez entrer une date au format YYYY-MM-DD.")
            print()

def demander_action_rent2():
    #Demander à l'utilisateur s'il veut rejouer ou revenir au menu.
    while True:
        # Demander à l'utilisateur son choix et le mettre en minuscules
        entree_utilisateur = input("Votre choix : ").lower()
        # Vérifier si le choix de l'utilisateur est valide
        if entree_utilisateur in ["1", "2", "3", "4", "5", "back"]:
            return entree_utilisateur  # Retourner le choix de l'utilisateur
        else:
            print("Ce n'est pas une entrée valide. Veuillez réessayer.")  # Message d'erreur