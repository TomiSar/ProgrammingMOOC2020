# Tee funktio pituudet(merkkijonot: list), joka saa parametriksi listan merkkijonoja. Funktio palauttaa sanakirjan, 
# jossa avaimina on listan merkkijonot ja arvoina merkkijonojen pituudet.
# Funktio tulee toteuttaa sanakirjakoosteen avulla. Funktion maksimipituus def-määrittelyrivi mukaanlukien on kaksi riviä.
def pituudet(merkkijonot: list):
    return {jono: len(jono) for jono in merkkijonot}

#main
if __name__ == "__main__":
    sanalista = ["suo", "kuokka" , "python", "ja", "koodari"]
    sanojen_pituudet = pituudet(sanalista)
    print(sanojen_pituudet)