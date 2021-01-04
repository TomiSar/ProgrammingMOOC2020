# TEE RATKAISUSI TÄHÄN:
# Tee funktio tahtirivit(luvut: list), joka saa parametriksi listan kokonaislukuja. 
# Funktio palauttaa listan, joka koostuu tähtiriveistä, joiden pituus vastaa parametrina olevan listan lukuja.
from math import sqrt
def neliojuuret(luvut: list):
    return [sqrt(luku) for luku in luvut]

#main
if __name__ == "__main__":
    rivit = neliojuuret([1,2,3,4])
    for rivi in rivit:
        print(rivi)