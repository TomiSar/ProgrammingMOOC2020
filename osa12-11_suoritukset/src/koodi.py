class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"

# Suorittajat
# Funktio suorittajien_nimet(suoritukset: list) joka saa parametriksi listan suoritus-oliota. Funktio palauttaa listan, jolta löytyy suorittajien nimet.
def suorittajien_nimet(suoritukset: list):
    return map(lambda suoritus: suoritus.opiskelijan_nimi, suoritukset)
    # suorittajat = map(lambda s: s.opiskelijan_nimi, suoritukset)
    # return suorittajat

# Kurssit
# Funktio joka saa parametriksi listan suoritus-oliota. Funktio palauttaa listan, jolla on suorituksessa olevien kurssien nimet aakkosjärjestyksessä. 
# Kukin kurssi esiintyy listalla vain kerran.
def kurssien_nimet(kurssit: list):
    kurssien_nimet = map(lambda kurssi: kurssi.kurssi, kurssit)
    return sorted(list(set(kurssien_nimet)))

#main
if __name__ == "__main__":
    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)

    print("Kurssit:")
    for nimi in kurssien_nimet([s1, s2, s3]):
        print(nimi)

    print("\nOpiskelijat:")
    for nimi in suorittajien_nimet([s1, s2, s3]):
        print(nimi)

    # suoritus = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 5)
    # print(suoritus.opiskelijan_nimi)
    # print(suoritus.arvosana)
    # print(suoritus.kurssi)
    # print(suoritus)