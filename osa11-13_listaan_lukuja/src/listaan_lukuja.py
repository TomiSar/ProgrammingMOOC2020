# TEE RATKAISUSI TÄHÄN:
# Kirjoita rekursiivinen funktio listaan_lukuja(luvut: list), joka lisää listaan lukuja niin kauan, 
# että sen pituus on viidellä jaollinen. Jokainen listaan lisättävä luku on aina yhden suurempi kuin listan viimeinen luku.
def listaan_lukuja(luvut: list):
    if len(luvut) % 5 != 0:
        luvut.append(luvut[-1] + 1)
        listaan_lukuja(luvut)

#main
if __name__ == "__main__":
    luvut = [1,3,4,5,10,11]
    listaan_lukuja(luvut)
    print(luvut)