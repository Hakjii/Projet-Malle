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



reponse = input("dans quel magasin voulez vous faire des achats (choix possibles : Fleury et Bott, Madame Guipure, Ollivander)? ")
if reponse in 'Fleury et Bott':
    sommes_a_rendre_FB = (0, 60, 63, 231, 899)
    for i in range(len(sommes_a_rendre_FB)):
        resultat_FB = somme_a_donner_FB(sommes_a_rendre_FB[i])
        print(f"pour une somme a rendre de {sommes_a_rendre_FB[i]}")
        if sommes_a_rendre_FB[i] == 0:
            print("il n'y a rien a rendre")
        for keys, values in resultat_FB.items():
            print(f"il faut donner {values} billet de {keys}")

if reponse in 'Madame Guipure':
    sommes_a_rendre_MG = (0, 17, 68, 231, 497, 842)
    for i in range(len(sommes_a_rendre_MG)):
        resultat_MG, somme_a_rendre_MG = somme_a_donner_MG(sommes_a_rendre_MG[i])
        print(f"pour une somme a rendre de {sommes_a_rendre_MG[i]}")
        if sommes_a_rendre_FB[i] == 0:
            print("il n'y a rien a rendre")
        for keys, values in resultat_MG.items():
            print(f"{values} billets de {keys} €")
        if somme_a_rendre_MG > 0:
            print(f"il n'y a plus assez de billet pour tout rendre, il reste {somme_a_rendre_MG} € a rendre")






