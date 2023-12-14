#1 gallion = 17 mornilles , 1 mornille = 29 noises
def somme_a_donner_O():
    total_G = int(input('combien de gallion a rendre:'))
    total_M = int(input('combien de mornille a rendre:'))
    total_N = int(input('combien de noises a rendre:'))
        
    while total_N > 29 or total_M > 17:
        if total_N > 29:
            total_N -= 29
            total_M += 1
        if total_M > 17:
            total_M -= 17
            total_G += 1
    print(f"Il y a {total_G} Gallion, il y a {total_M} Mornille et il y a {total_N} noise ")

somme_a_donner_O()

