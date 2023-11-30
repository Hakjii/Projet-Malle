# Projet-Malle


def somme_a_donner(somme_a_rendre):
    tuple_somme = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    dico_somme = {}
    for nombre in tuple_somme:
        if somme_a_rendre >= nombre:
            compteur = somme_a_rendre // nombre
            dico_somme[nombre] = compteur
            somme_a_rendre = somme_a_rendre % nombre
    return dico_somme

            
reponse = input("dans quel magasin voulez vous faire des achats ? ")
if reponse in 'Fleury et Bott':
    sommes_a_rendre = (0, 60, 63, 231, 899)
    for i in range(len(sommes_a_rendre)):
        resultat = somme_a_donner(sommes_a_rendre[i])
        for keys, values in resultat.items():
            print(f"il faut donner {values} billet de {keys} pour une somme a rendre de {sommes_a_rendre[i]}")





