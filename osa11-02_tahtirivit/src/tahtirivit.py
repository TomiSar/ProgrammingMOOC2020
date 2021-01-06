# Tee funktio tahtirivit(luvut: list), joka saa parametriksi listan kokonaislukuja. Funktio palauttaa listan, 
# joka koostuu tähtiriveistä, joiden pituus vastaa parametrina olevan listan lukuja.
def tahtirivit(luvut: list):
    return [luku * "*" for luku in luvut]

#main
if __name__ == "__main__":
    rivit = tahtirivit([1,2,3,4])
    for rivi in rivit:
        print(rivi)

    print()

    rivit = tahtirivit([4, 3, 2, 1, 10])
    for rivi in rivit:
        print(rivi)