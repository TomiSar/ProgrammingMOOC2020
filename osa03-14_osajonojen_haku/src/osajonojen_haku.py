sana = input("Sana: ")
merkki = input("Merkki: ")
indeksi = 0

while indeksi + 3 <= len(sana):
    #jos merkki löytyy kohdasta tulostetaan kohdasta alkaen + 3 merkkiä     
    if sana[indeksi] == merkki:
        print(sana[indeksi:indeksi+3])
    indeksi += 1