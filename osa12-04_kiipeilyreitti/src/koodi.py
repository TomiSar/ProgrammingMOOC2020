class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

# Tee funktio pituuden_mukaan(reitit: list) joka palauttaa kiipeilyreitit pituuden mukaan käänteisessä järjestyksessä.
def pituuden_mukaan(reitit: list):
    def pituusjarjestys(reitti):
        return reitti.pituus
    return sorted(reitit, key=pituusjarjestys, reverse=True)

# Tee funktio vaikeuden_mukaan(reitit: list) joka palauttaa kiipeilyreitit vaikeuden (eli graden) mukaan laskevassa järjestyksessä. 
# Jos reittien vaikeus on sama, ratkaisee pituus vaikeuden. Pidempi on vaikeampi. Kiipeilyreittien vaikeusasteikko on 4, 4+, 5, 5+, 6A, 6A+, 
# ... eli käytännössä se seuraa aakkosjärjestystä.
def vaikeuden_mukaan(reitit: list):
    def vaikeusjarjestys(reitti):
        return (reitti.grade, reitti.pituus)
    return sorted(reitit, key=vaikeusjarjestys, reverse=True)

#main
if __name__ == "__main__":
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 11, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Pieniä askelia", 12, "6A+")
    reitit = [r1, r2, r3, r4]

    print("Vaikeuden mukaan:")
    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)

    print("\nPituuden mukaan:")
    for reitti in pituuden_mukaan(reitit):
        print(reitti)