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

            

resultat = somme_a_donner(900)
for keys, values in resultat.items():
    print(f"il faut donner {resultat[values]} billet de {resultat[keys]}")


