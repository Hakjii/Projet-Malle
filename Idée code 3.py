# Projet-Malle


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
    return dico_somme, somme_a_rendre

def somme_a_donner_O(somme_a_rendre): # 1 gallion = 17 mornilles , 1 mornille = 29 noises
    dico_somme = {}

def afficher_resultat(sommes_a_rendre):
    for i in range(len(sommes_a_rendre)):
        if reponse == 'Fleury et Bott':
            resultat = somme_a_donner_FB(sommes_a_rendre[i])
        elif reponse in 'Madame Guipure':
            resultat = somme_a_donner_MG(sommes_a_rendre[i])
        elif reponse in "Ollivander":
            resultat = somme_a_donner_O(sommes_a_rendre[i])
        print(f"pour une somme a rendre de {sommes_a_rendre[i]}")
        if sommes_a_rendre[i] == 0:
            print("il n'y a rien a rendre")
        for keys, values in resultat.items():
            print(f"il faut donner {values} billet de {keys}")

def question_achat_FB():
    question = input("voulez vous faire d'autres achats")
    if question in ("Oui", "oui", "OUI"):
        question_somme = int(input("indiquez une somme a rendre"))
        somme = sommes_a_rendre_FB(question_somme)
        return somme
reponse_CT = input("Vous êtes sur le chemin de traverse voulez vous faire des achats ? ")
while reponse_CT in ("Oui", "oui", "OUI"):
    reponse = input("Dans quel magasin voulez vous faire des achats, Madame Guipure, Fleury et Bott, Ollivander ?")
    if reponse in "Fleury et Bott":
        sommes_a_rendre_FB = (0, 60, 63, 231, 899)
        afficher_resultat(sommes_a_rendre_FB)
        question_achat_FB()
    elif reponse in "Madame Guipure":
        sommes_a_rendre_MG = (0, 17, 68, 231, 497, 842)
        afficher_resultat(sommes_a_rendre_MG)
    elif reponse in "Ollivander":
        sommes_a_rendre_O = ()
        





