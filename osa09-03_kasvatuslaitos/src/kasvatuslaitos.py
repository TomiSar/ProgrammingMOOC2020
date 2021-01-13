# Älä muuta luokkaa Henkilo!
class Henkilo:
    def __init__(self, nimi: str, ika: int, pituus: int, paino: int):
        self.nimi = nimi
        self.ika = ika
        self.pituus = pituus
        self.paino = paino

class Kasvatuslaitos:
    def __init__(self):
        self.punnitusten_lkm = 0

    # Saa parametrina henkilön ja palauttaa parametrina olevan henkilön paino (punnitusten lkm kasvaa, kun punnitaan Henkilo)
    def punnitse(self, henkilo: Henkilo):
        self.punnitusten_lkm += 1
        return henkilo.paino
    
    # Kasvattaa parametrina olevan henkilön painoa yhdellä
    def syota(self, henkilo: Henkilo):
        henkilo.paino += 1

    # Palauttaa kasvatuslaitoksen tekemät punnitukset
    def punnitukset(self):
        return self.punnitusten_lkm

# main
if __name__ == "__main__":    
    haagan_neuvola = Kasvatuslaitos()
    eero = Henkilo("Eero", 1, 110, 7)
    pekka = Henkilo("Pekka", 33, 176, 85)
    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}")  #Punnituksia tehty 0
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}") #Punnituksia tehty 2
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    haagan_neuvola.punnitse(eero)
    print(f"Punnituksia tehty {haagan_neuvola.punnitukset()}") #Punnituksia tehty 6

# eero = Henkilo("Eero", 1, 110, 7)
# pekka = Henkilo("Pekka", 33, 176, 85)
# print(f"{eero.nimi} painaa {haagan_neuvola.punnitse(eero)} kg")
# print(f"{pekka.nimi} painaa {haagan_neuvola.punnitse(pekka)} kg")
# print() 
# haagan_neuvola.syota(eero)
# haagan_neuvola.syota(eero)
# haagan_neuvola.syota(eero)
# print(f"{eero.nimi} painaa {haagan_neuvola.punnitse(eero)} kg")
# print(f"{pekka.nimi} painaa {haagan_neuvola.punnitse(pekka)} kg")

# haagan_neuvola = Kasvatuslaitos()
# eero = Henkilo("Eero", 1, 110, 7)
# pekka = Henkilo("Pekka", 33, 176, 85)
# print(f"{eero.nimi} painaa {haagan_neuvola.punnitse(eero)} kg")
# print(f"{pekka.nimi} painaa {haagan_neuvola.punnitse(pekka)} kg")