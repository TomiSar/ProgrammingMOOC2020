class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
    samat = True
    if kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi:
        vanhempi = kirja1
        samat = False
    if kirja2.kirjoitusvuosi < kirja1.kirjoitusvuosi:
        vanhempi = kirja2
        samat = False

    if not samat:
        print(f"{vanhempi.nimi} on vanhempi, se kirjoitettiin {vanhempi.kirjoitusvuosi} ")
    else:
        print(f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.kirjoitusvuosi}")


# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi


# main
if __name__ == "__main__":
    python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
    everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
    norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

    vanhempi_kirja(python, everest)
    vanhempi_kirja(python, norma)