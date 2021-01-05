class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"

# Hyväksytyt suoritukset
# Funktio saa parametriksi listan suoritus-oliota. 
# Funktio palauttaa listan, jolta löytyy suorituksista ne, joiden arvosana on vähintään 1.
def hyvaksytyt(suoritukset: list):
    return filter(lambda suoritus: suoritus.arvosana >= 1, suoritukset)

# Arvosanan suoritukset
# Funktio saa parametriksi listan suoritus-oliota sekä kokonaisluvun. Funktio palauttaa listan, jolta 
# löytyy suorituksista ne, joiden arvosana on sama kuin toisen parametrin arvo.
def suoritus_arvosanalla(suoritukset: list, arvosana: int):
    return filter(lambda suoritus: suoritus.arvosana == arvosana, suoritukset)

# Kurssin suorittajat
# Funktio saa parametriksi listan suoritus-oliota sekä kurssin nimen. Funktio palauttaa aakkosjärjestyksessä 
# niiden opiskelijoiden nimet, jotka ovat suorittaneet parametrina olevan kurssin arvosanalla joka on suurempi kuin nolla.
def kurssin_suorittajat(suoritukset: list, kurssi: str):
    kurssin_suoritukset = filter(lambda suoritus: suoritus.kurssi == kurssi and suoritus.arvosana > 0, suoritukset)
    kurssin_opiskelijat = map(lambda suoritus: suoritus.opiskelijan_nimi, kurssin_suoritukset)
    return sorted(kurssin_opiskelijat)

#main
if __name__ == "__main__":
    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Tietoliikenteen perusteet", 5)
    s3 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 0)
    s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
    print("Kurssin suorittajat")
    for suoritus in kurssin_suorittajat([s1, s2, s3, s4], "Tietoliikenteen perusteet"):
        print(suoritus)

    # s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    # s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    # s3 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 3)
    # s4 = Suoritus("Olivia Ohjelmoija", "Johdatus yliopistomatematiikkaan", 3)

    # print("\nSuoritukset arvosanalla:")
    # for suoritus in suoritus_arvosanalla([s1, s2, s3, s4], 3):
    #     print(suoritus)

    # s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    # s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    # s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)

    # print("\nHyväksytyt (arvosana suurempi kuin 0):")
    # for suoritus in hyvaksytyt([s1, s2, s3]):
    #     print(suoritus)