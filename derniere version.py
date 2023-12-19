# coding : utf-8
"""
Auteurs : Thibault, Pierre, Justin
lien github : https://github.com/Hakjii/Projet-Malle
"""

def somme_a_donner_FB(somme_a_rendre):
    tuple_somme = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    dico_somme = {}
    for nombre in tuple_somme:
        if somme_a_rendre >= nombre:
            compteur = somme_a_rendre // nombre
            dico_somme[nombre] = compteur
            somme_a_rendre = somme_a_rendre % nombre
    return dico_somme


def somme_a_donner_MG(somme_a_rendre) :
    dico_billets = {200 : 1, 100 : 3, 50 : 1, 20 : 1, 10 : 1, 5 : 1, 2 : 5}
    dico_somme = {}
    for billet, quantite_disponible in dico_billets.items():
        if somme_a_rendre >= billet and quantite_disponible > 0:
            compteur = somme_a_rendre // billet
            if compteur > quantite_disponible:
                compteur = quantite_disponible
            dico_somme[billet] = compteur
            somme_a_rendre -= compteur * billet
            dico_billets[billet] -= compteur  
    return dico_somme, dico_billets
"""
def somme_a_donner_O(somme_a_rendre): # 1 gallion = 17 mornilles , 1 mornille = 29 noises
    dico_somme = {}

"""
def afficher_resultat(sommes_a_rendre, magasin):
    for i in range(len(sommes_a_rendre)):
        if magasin == 'Fleury et Bott':
            resultat = somme_a_donner_FB(sommes_a_rendre[i])
        elif magasin == 'Madame Guipure':
            resultat = somme_a_donner_MG(sommes_a_rendre[i])
        elif magasin == "Ollivander":
            resultat = somme_a_donner_O(sommes_a_rendre[i])
    return resultat


def question_utilisateur():
    question = input("Voulez vous afficher les résultats imposés ou choisir votre propre résultat (choix 1 ou 2)")
    if question == "1":
        if reponse in "Fleury et Bott":
            somme_a_rendre_FB = (0, 60, 63, 231, 899)
            return somme_a_rendre_FB, question
        elif reponse in "Madame Guipure":
            somme_a_rendre_MG = (0, 17, 68, 231, 497, 842)
            return somme_a_rendre_MG, question
    elif question == "2":
        choix = tuple([int(input("Choisissez une somme à rendre: "))])
        return choix, question

 
def utiliser_resultat(dico_resultat, somme_a_rendre):
    for nombre in somme_a_rendre:
        print(f"pour une somme a rendre de {nombre}")
        for keys, values in dico_resultat.items():
            print(f"il faut {values} billets de {keys}")



reponse = input("Vous êtes sur le chemin de traverse\nDans quel magasin voulez vous faire des achats, Fleury et Bott, Madame Guipure, Ollivander ?\nToute autre réponse vous fera sortir du chemin de traverse.")
while reponse in ("Fleury et Bott", "Madame Guipure", "Ollivander"):
    if reponse == "Fleury et Bott" or reponse == "Madame Guipure" or reponse == "Ollivander":
        somme_a_rendre, question = question_utilisateur()
        while question in {"1", "2"}:
            resultat = afficher_resultat(somme_a_rendre, reponse)
            utiliser_resultat(resultat, somme_a_rendre)
            somme_a_rendre, question = question_utilisateur()
    reponse = input("Vous êtes sur le chemin de traverse\nDans quel magasin voulez vous faire des achats, Fleury et Bott, Madame Guipure, Ollivander ?\nToute autre réponse vous fera sortir du chemin de traverse.")
       
