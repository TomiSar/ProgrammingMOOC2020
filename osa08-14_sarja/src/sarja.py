# Tee ratkaisusi tähän:
class Sarja:
    def __init__(self, nimi: str, kaudet: int, genret: list):
        self.nimi = nimi
        self.kaudet = kaudet
        self.genret = genret
        self.arvostelut = [0, 0, 0, 0, 0, 0]
        self.arvosteluja = 0

    def arvosana(self):
        if self.arvosteluja == 0:
            return 0
        else:
            summa = 0
            for i in range(0, 6):
                summa += self.arvostelut[i] * i
            return summa / self.arvosteluja

    def __str__(self):
        genret = ", ".join(self.genret)
 
        if self.arvosteluja == 0:
            arvostelut = "ei arvosteluja"
        else:
            summa = 0
            for i in range(0, 6):
                summa += self.arvostelut[i] * i
            keskiarvo = summa / self.arvosteluja
            arvostelut = f"arvosteluja {self.arvosteluja}, keskiarvo {keskiarvo:.1f} pistettä"

        return f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {genret}\n{arvostelut}"

    def arvostele(self, arvosana: int):
        self.arvosteluja += 1
        self.arvostelut[arvosana] += 1

def arvosana_vahintaan(arvosana: float, sarjat: list):
    tulos = []
    for sarja in sarjat:
        if sarja.arvosana() >= arvosana:
            tulos.append(sarja)
    return tulos
 
def sisaltaa_genren(genre: str, sarjat: list):
    tulos = []
    for sarja in sarjat:
        if genre in sarja.genret:
            tulos.append(sarja)
    return tulos

#main
if __name__ == "__main__":
    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)

# dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# dexter.arvostele(4)
# dexter.arvostele(5)
# dexter.arvostele(5)
# dexter.arvostele(3)
# dexter.arvostele(0)
# print(dexter)

# dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# print(dexter)