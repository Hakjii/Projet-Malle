# Projet-Malle

def somme_a_donner(somme_a_rendre):
    if somme_a_rendre >= 200:
        print(f"Il faut rendre {somme_a_rendre // 200} billets de 200€")
        somme_a_rendre = somme_a_rendre % 200
    if somme_a_rendre >= 100:
        print(f"Il faut rendre {somme_a_rendre // 100} billets de 100€")
        somme_a_rendre = somme_a_rendre % 100
    if somme_a_rendre >= 50:
        print(f"Il faut rendre {somme_a_rendre // 50} billets de 50€")
        somme_a_rendre = somme_a_rendre % 50
    if somme_a_rendre >= 20:
        print(f"Il faut rendre {somme_a_rendre // 20} billets de 20€")
        somme_a_rendre = somme_a_rendre % 20
    if somme_a_rendre >= 10:
        print(f"Il faut rendre {somme_a_rendre // 10} billets de 10€")
        somme_a_rendre = somme_a_rendre % 10
    return somme_a_rendre
somme_a_donner(60)
