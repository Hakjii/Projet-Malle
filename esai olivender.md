'''
def somme_a_donner_O(somme_a_rendre):
    somme_table = {
        "galion": {"mornille": 17, "noise": 493},
        "mornille": {"galion": 0, "noise": 29},
        "noise": {"galion": 0, "mornille": 0}
    }
    return somme_table
 
somme_a_donner_O

def somme_a_donner_O(somme_a_rendre):
    somme_table = {
        "galion": {"mornille": 17, "noise": 493},
        "mornille": {"galion": 0, "noise": 29},
        "noise": {"galion": 0, "mornille": 0}
    }

    resultat = ""
    for devise_source, taux_de_change in somme_table.items():
        resultat += f"1 {devise_source} équivaut à :\n"
        for devise_destination, taux in taux_de_change.items():
            resultat += f"  {taux} {devise_destination}\n"
        resultat += "\n"
    
    return resultat

# Exemple d'utilisation pour récupérer la chaîne de caractères
table_string = somme_a_donner_O({})
print(table_string)
'''
def somme_a_donner_O2(somme_a_rendre):
    somme_table = {
        "galion": {"mornille": 17, "noise": 493},
        "mornille": {"galion": 0, "noise": 29},
        "noise": {"galion": 0, "mornille": 0}
    }

    montant_initial = {"galion": 1, "noise": 2}  # Montant initial à convertir

    resultat = {}
    for devise_destination, taux in somme_table["galion"].items():
        montant_converti = montant_initial["galion"] * taux
        resultat[devise_destination] = montant_converti

    for devise_destination, taux in somme_table["noise"].items():
        montant_converti = montant_initial["noise"] * taux
        resultat[devise_destination] += montant_converti

    return resultat

# Exemple d'utilisation pour obtenir le résultat de l'addition
resultat_addition = somme_a_donner_O({})
print(resultat_addition)
