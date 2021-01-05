from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

# Toteuta funktio kaikkien_opintopisteiden_summa, joka saa parametriksi listan suorituksia ja laskee suoritusten yhteenlasketun opintopistemäärän.
# reducen apufunktio joka huolehtii yhden alkion arvon lisäämisestä summaan
def opintopisteiden_summaaja(summa, suoritus):
    return summa + suoritus.opintopisteet

def kaikkien_opintopisteiden_summa(suoritukset: list):
    return reduce(opintopisteiden_summaaja, suoritukset, 0)

# Hyväksyttyjen opintopistemäärä
# Funktio saa parametriksi listan suorituksia ja laskee arvosanan 1 tai parempien omaavien suoritusten yhteenlasketun opintopistemäärän.
def hyvaksyttyjen_opintopisteiden_summa(suoritukset: list):
    hyvaksytyt = filter(lambda suoritus: suoritus.arvosana > 0, suoritukset)
    return reduce(opintopisteiden_summaaja, hyvaksytyt, 0)

# Hyväksyttyjen suoritusten keskiarvo
# Toteuta funktio keskiarvo, joka saa parametriksi listan suorituksia ja laskee arvosanan 1 tai parempien omaavien suoritusten arvosanojen keskiarvon.
def keskiarvo(suoritukset: list):
    def arvosanojen_summaaja(summa, suoritus):
        return summa + suoritus.arvosana 

    hyvaksytyt = list(filter(lambda suoritus: suoritus.arvosana > 0, suoritukset))
    arvosanojen_summa = reduce(arvosanojen_summaaja, hyvaksytyt, 0)
    return arvosanojen_summa / len(hyvaksytyt)

#main
if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print("Hyväksyttyjen suoritusten keskiarvo:")
    print(summa)

    # s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    # s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    # s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    # summa = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
    # print("\nHyväksyttyjen opintopistemäärä:")
    # print(summa)

    # s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    # s2 = Suoritus("Ohjelmoinnin jatkokutssi", 4, 5)
    # s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    # summa = kaikkien_opintopisteiden_summa([s1, s2, s3])
    # print("\nOpintopistemäärä:")
    # print(summa)