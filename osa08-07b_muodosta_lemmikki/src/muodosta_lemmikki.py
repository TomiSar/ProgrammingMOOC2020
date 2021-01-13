class Lemmikki:
    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi

# Kirjoita luokan ulkopuolelle funktio uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int), 
# joka luo ja palauttaa uuden Lemmikki-tyyppisen (eli Lemmikki-luokkaa vastaavan) olion.
def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int):
    lemmikki = Lemmikki(nimi, laji, syntymavuosi)
    return lemmikki

# main
if __name__ == "__main__":
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)