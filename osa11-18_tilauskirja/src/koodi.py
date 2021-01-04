# Tee ratkaisusi tähän:
# Toteuta luokka Tehtava, joka mallintaa ohjelmistoyritykselle annettavia työtehtäviä. Tehtävillä on
# kuvaus, arvio sen viemästä työmäärästä, tieto koodarista, joka toteuttaa tehtävän, tieto siitä, onko tehtävä valmis vai ei, yksikäsitteinen tunniste eli id
class Tehtava:
    id = 0
    @classmethod
    # tehtävien id on juokseva numero, joka alkaa arvosta 1
    def uusi_id(cls):
        Tehtava.id += 1
        return Tehtava.id

    def __init__(self, kuvaus, koodari, tyomaara):
        self.koodari = koodari
        self.kuvaus = kuvaus
        self.tyomaara = tyomaara
        self.id = Tehtava.uusi_id()
        self.valmis = False

    # tehtävän tilan (valmis vai ei vielä valmis) voi tarkistaa funktiolla on_valmis(self) joka palauttaa totuusarvon
    # tehtävä ei ole siinä vaiheessa valmis kun se luodaan
    def on_valmis(self):
        return self.valmis
    
    # tehtävä merkataan valmiiksi kutsumalla metodia merkkaa_valmiiksi(self)
    def merkkaa_valmiiksi(self):
        self.valmis = True

    def __str__(self):
        status = "EI VALMIS" if not self.valmis else "VALMIS"
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {status}"

# Tehdään nyt luokka Tilauskirja, joka kokoaa kaikki ohjelmistoyritykseltä tilatut työtehtävät, joita siis mallinnetaan luokan Tehtava olioilla.
class Tilauskirja:
    def __init__(self):
        self.__tehtavat = []

    # lisää uuden tilauksen tilauskirjaan. Tilauskirja tallettaa tilaukset sisäisesti Tehtava-olioina. Huomaa, että metodilla täytyy olla 
    # juuri nämä parametrit, muuten testit eivät hyväksy metodia!
    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        self.__tehtavat.append(Tehtava(kuvaus, koodari, tyomaara))

    # palauttaa listana kaikki tilauskirjalla olevat tehtävät
    def kaikki_tilaukset(self):
        return self.__tehtavat

    # palauttaa listana kaikki koodarit, joille on tehtävä tilauskirjassa, metodin palauttama lista ei saa sisältää yhtä koodia useampaan kertaan
    def koodarit(self):
        return list(set([t.koodari for t in self.__tehtavat]))

    # Metodi saa parametriksi tehtävän id:n ja merkkaa kyseisen tehtävän valmiiksi:
    def merkkaa_valmiiksi(self, id: int):
        for tehtava in self.__tehtavat:
            if tehtava.id == id:
                tehtava.merkkaa_valmiiksi()
                return
        
        # ei virheellinen
        raise ValueError("väärä id")

    # Metodit toimivat kuten olettaa saattaa, ne palauttavat nimensä mukaisen osajoukon tilauskirjan tehtävistä listana.
    def valmiit_tilaukset(self):
        return [teht for teht in self.__tehtavat if teht.on_valmis()]

    def ei_valmiit_tilaukset(self):
        return [teht for teht in self.__tehtavat if not teht.on_valmis()]

    # Metodi, joka palauttaa tuplen, joka kertoo koodarin valmistuneiden ja vielä valmistumattomien töiden määrän sekä näihin kuluneiden työtuntien summan.
    # Tuplen ensimmäinen alkio siis kertoo valmiiden töiden määrän ja toinen valmistumattomien töiden määrän. 
    # Kolmas alkio on valmiiden töiden työaika-arvioiden summa ja neljäs alkio vielä valmistumattomien töiden työmääräarvioiden summan.
    def koodarin_status(self, koodari: str):
        if koodari not in self.koodarit():
            raise ValueError("olematon koodari")
        
        valmiit_tehtavat = [t for t in self.__tehtavat if t.koodari == koodari and t.on_valmis()]
        ei_valmiit_tehtavat = [t for t in self.__tehtavat if t.koodari == koodari and not t.on_valmis()]
        valmiit_tunnit = sum(t.tyomaara for t in valmiit_tehtavat)
        ei_valmiit_tunnit = sum(t.tyomaara for t in ei_valmiit_tehtavat)
 
        return (len(valmiit_tehtavat), len(ei_valmiit_tehtavat), valmiit_tunnit, ei_valmiit_tunnit)

#main
if __name__ == "__main__":
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)
    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)
    status = tilaukset.koodarin_status("Antti")
    print(status)

    # tilaukset = Tilauskirja()
    # tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    # tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    # tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    # tilaukset.merkkaa_valmiiksi(1)
    # tilaukset.merkkaa_valmiiksi(2)

    # for tilaus in tilaukset.kaikki_tilaukset():
    #     print(tilaus)

    # tilaukset = Tilauskirja()
    # tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    # tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    # tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)

    # for tilaus in tilaukset.kaikki_tilaukset():
    #     print(tilaus)
    # print()
    # for koodari in tilaukset.koodarit():
    #     print(koodari)

    # t1 = Tehtava("koodaa hello world", "Erkki", 3)
    # print(t1.id, t1.kuvaus, t1.koodari, t1.tyomaara)
    # print(t1)
    # print(t1.on_valmis())
    # t1.merkkaa_valmiiksi()
    # print(t1)
    # print(t1.on_valmis())
    # t2 = Tehtava("koodaa webbikauppa", "Antti", 10)
    # t3 = Tehtava("tee mobiilisovellus työaikakirjanpitoon", "Erkki", 25)
    # print(t2)
    # print(t3)