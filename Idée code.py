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
    dico_billets = {200 : 1, 100 : 3, 50 : 1, 20 : 1, 10 : 1, 2 : 5}
    dico_somme = {}
    for nombre, quantite_disponible in dico_billets.items():
        if somme_a_rendre >= nombre and quantite_disponible > 0:
            compteur = somme_a_rendre // nombre
            if compteur > quantite_disponible:
                compteur = quantite_disponible
            dico_somme[nombre] = compteur
            somme_a_rendre -= compteur * nombre
            dico_billets[nombre] -= compteur   # a completer parce que c'est pas ouf


        if compteur > 0:
            print("il n'y a plus de billets disponibles") # a faire pour quand il reste plus de billets
    return dico_somme

res = somme_a_donner_MG(231)
for keys, values in res.items():
    print(f"{values} billets de {keys} €")



reponse = input("dans quel magasin voulez vous faire des achats (choix possibles : Fleury et Bott, Madame Guipure, Ollivander)? ")
if reponse in 'Fleury et Bott':
    sommes_a_rendre = (0, 60, 63, 231, 899)
    for i in range(len(sommes_a_rendre)):
        resultat = somme_a_donner_FB(sommes_a_rendre[i])
        for keys, values in resultat.items():
            print(f"il faut donner {values} billet de {keys} pour une somme a rendre de {sommes_a_rendre[i]}")





