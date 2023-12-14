#1 gallion = 17 mornilles , 1 mornille = 29 noises
total_G = 0
total_M = 0
total_N = 0
    
while total_N > 29 or total_M > 17:
    if total_N > 29:
        total_N -= 29
        total_M += 1
    if total_M > 17:
        total_M -= 17
        total_G += 1
print(f"Il y a {total_G} Gallion, il y a {total_M} Mornille et il y a {total_N} noise ")

