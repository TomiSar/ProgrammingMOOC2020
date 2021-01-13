class SuperSankari:
    def __init__(self, nimi: str, supervoimat: str):
        self.nimi = nimi
        self.supervoimat = supervoimat

    def __str__(self):
        return f'{self.nimi}, superkyvyt: {self.supervoimat}'


# Kirjoita luokka SuperRyhma, joka mallintaa supersankareista koostuvaa ryhmää.
# Suojatut attribuutit nimi (merkkijono), kotipaikka (merkkijono) ja jasenet (lista)
# Konstruktori, joka saa parametrikseen tässä järjestyksessä nimen ja kotipaikan
# Havainnointimetodit nimelle ja kotipaikalle
# Metodi lisaa_jasen(sankari: SuperSankari), joka lisää uuden jäsenen ryhmään
# Metodi tulosta_ryhma, joka tulostaa ryhmän ja sen jäsenten tiedot
class SuperRyhma(SuperSankari):
    def __init__(self, nimi: str, kotipaikka: str):
        self._nimi = nimi
        self._kotipaikka = kotipaikka
        self._jasenet = []

    @property
    def nimi(self):
        return self._nimi

    @property
    def kotipaikka(self):
        return self._kotipaikka

    def lisaa_jasen(self, sankari: SuperSankari):
        self._jasenet.append(sankari)

    def tulosta_ryhma(self):
        print(f"{self.nimi}, {self.kotipaikka}")
        print("Jäsenet:")
        for jasen in self._jasenet:
            print(jasen)

# main
if __name__ == "__main__":
    supermiekkonen = SuperSankari("Supermiekkonen", "Supernopeus, supervoimakkuus")
    nakymaton = SuperSankari("Näkymätön Makkonen", "Näkymättömyys")
    ryhma_z = SuperRyhma("Ryhmä Z", "Kälviä")

    ryhma_z.lisaa_jasen(supermiekkonen)
    ryhma_z.lisaa_jasen(nakymaton)
    ryhma_z.tulosta_ryhma()