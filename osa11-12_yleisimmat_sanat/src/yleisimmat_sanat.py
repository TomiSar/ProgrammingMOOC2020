# Tee funktio yleisimmat_sanat(tiedoston_nimi: str, raja: int), joka saa parametrikseen tiedoston nimen. 
# Funktio palauttaa sanakirjan, joka sisältää tiedostossa olevien sanojen esiintymislukumäärän niiden sanojen osalta, 
# joilla on vähintään toisen parametrin raja verran esiintymiä.
from string import punctuation

def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    with open(tiedoston_nimi) as tiedosto:
        sisalto = tiedosto.read()
 
        # poistetaan rivinvaihdot ja välimerkit
        sisalto = sisalto.replace("\n", " ")
        for valimerkki in punctuation:
            sisalto = sisalto.replace(valimerkki, "")
 
        sanat = sisalto.split(" ")
        return {sana: sanat.count(sana) for sana in sanat if sanat.count(sana) >= raja}

#main
if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 3))