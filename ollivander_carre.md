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

    
    return dico_somme


RENDUS_OBLIGATOIRES = ((0, 0, 0), (0, 0, 654), (0, 23, 78), (2, 11, 9), (7, 531, 451))
resultat = somme_a_donner_O(*RENDUS_OBLIGATOIRES[4])
print(resultat)
