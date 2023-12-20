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
    return dico_somme, somme_a_rendre


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
    return dico_somme, somme_a_rendre


def somme_a_donner_O(total_G, total_M, total_N):
    dico_monnaie = {'G': total_G, 'M': total_M, 'N': total_N}
    dico_somme = {'G': 0, 'M': 0, 'N': 0}

    # noises
    while dico_monnaie['N'] > 29 or dico_monnaie['M'] > 17:
        # mornille
        if dico_monnaie['N'] > 29:
            dico_monnaie['N'] -= 29
            dico_monnaie['M'] += 1
            dico_somme['M'] += 1
        # galion
        if dico_monnaie['M'] > 17:
            dico_monnaie['M'] -= 17
            dico_monnaie['G'] += 1
            dico_somme['G'] += 1

    
    return dico_somme, somme_a_rendre



def dico_resultat(sommes_a_rendre, magasin):
    for i in range(len(sommes_a_rendre)):
        if magasin == '1':
            resultat, somme_restante  = somme_a_donner_FB(sommes_a_rendre[i])
        elif magasin == '2':
            resultat, somme_restante = somme_a_donner_MG(sommes_a_rendre[i])
        elif magasin == '3':
            resultat, somme_restante = somme_a_donner_O(sommes_a_rendre[i])
    return resultat, somme_restante


def question_utilisateur():
    question = input("Voulez-vous afficher les résultats imposés ou choisir votre propre résultat (choix 1 ou 2) : ")
    if question == "1":
        if reponse == "1":
            somme_a_rendre_FB = (0, 60, 63, 231, 899)
            return somme_a_rendre_FB, question
        elif reponse == "2":
            somme_a_rendre_MG = (0, 17, 68, 231, 497, 842)
            return somme_a_rendre_MG, question
        elif reponse == "3":
            somme_a_rendre_O = ((0, 0, 0), (0, 0, 654), (0, 23, 78), (2, 11, 9), (7, 531, 451))
            return somme_a_rendre_O, question
    elif question == "2":
        if reponse == "1" or reponse == "2":
            choix = tuple([int(input("Choisissez une somme à rendre : "))])
            return choix, question
        # A CONTINUER
        elif reponse == "3":
            total_G = int(input("choisissez le nombre de gallion a rendre : "))
            total_M = int(input("choisissez le nombre de Mornilles a rendre : "))
            total_N = int(input("choisissez le nombre de Noises a rendre : "))
            return total_G, total_M, total_M, question
    else:
        return None, None

# A CONTINUER
def afficher_resultat(dico_resultat, somme_a_rendre):
    resultat, somme_restante = dico_resultat

    for nombre in somme_a_rendre:
        print(f"\nPour une somme à rendre de {nombre}:")
        for billet, quantite in resultat.items():
            print(f"Il faut {quantite} billets de {billet}")

        if somme_restante > 0:
            print(f"Il reste {somme_restante} de monnaie à rendre.")



reponse = input("Vous êtes sur le chemin de traverse\nDans quel magasin voulez vous faire des achats, Fleury et Bott (1), Madame Guipure (2), Ollivander (3) ?\nToute autre réponse vous fera sortir du chemin de traverse.")
while reponse in ("1", "2", "3"):
    if reponse == "1" or reponse == "2" or reponse == "3":
        somme_a_rendre, question = question_utilisateur()
        while question in {"1", "2"}:
            resultat = dico_resultat(somme_a_rendre, reponse)
            afficher_resultat(resultat, somme_a_rendre)
            somme_a_rendre, question = question_utilisateur()
    reponse = input("Vous êtes sur le chemin de traverse\nDans quel magasin voulez vous faire des achats, Fleury et Bott (1), Madame Guipure (2), Ollivander (3) ?\nToute autre réponse vous fera sortir du chemin de traverse.")

       
