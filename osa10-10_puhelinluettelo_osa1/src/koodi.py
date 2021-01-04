# Tee ratkaisusi tähän:
# Sovelluslogiikka: Luokka pitää siis sisällään listan henkilöitä ja tarjoaa metodit tietojen lisäämiseen ja hakemiseen.
# Jokaiseen henkilöön voi liittyä useita numeroita, joten toteutetaan luettelon sisäinen tila sanakirjan avulla, 
# koska sanakirjasta on helppo hakea nimen perusteella. Sanakirjaan on helppo tallettaa suoraan myös nimeen liittyvät numerot, 
# joten ainakaan tässä vaiheessa ei tarvita erillistä luokkaa yksittäisen henkilön tietojen tallettamiseen.
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            # henkilöön niittyy lista puhelinnumeroja
            self.__henkilot[nimi] = []
        self.__henkilot[nimi].append(numero)

    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]

    def hae_numerolla(self, numero: str):
        for nimi, numerot in self.__henkilot.items():
            if numero in numerot:
                return nimi
        return None

    def kaikki_tiedot(self):
        return self.__henkilot

# Tietojen haku tiedostosta Laajennetaan ohjelmaa siten, että se lataa käynnistäessään puhelinluettelon tiedostosta, joka on seuraavaa muotoa:
# Erkki;02-1234567;045-4356713 tai Emilia;040-324344
class Tiedostonkasittelija():
    def __init__(self, tiedosto):
        self.__tiedosto = tiedosto

    def lataa(self):
        nimet = {}
        with open(self.__tiedosto) as f:
            for rivi in f:
                osat = rivi.strip().split(';')
                nimi, *numerot = osat
                nimet[nimi] = numerot

        return nimet

    def talleta(self, luettelo: dict):
        with open(self.__tiedosto, "w") as f:
            for nimi, numerot in luettelo.items():
                rivi = [nimi] + numerot
                f.write(";".join(rivi) + "\n")

# Käytttöliittymä: Kun sovelluslogiikan ydintoiminnallisuus on kunnossa, voidaan edetä sovelluksen tekstikäyttöliittymään.
# Käyttöliittymä on siis vastuussa ainoastaan siitä, että se kommunikoi käyttäjän kanssa. Puhelinnumeron säilöminen nimen 
# yhteyteen on jätetty kokonaisuudessan Puhelinluettelo-olion vastuulle.
class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()
        self.__tiedosto = Tiedostonkasittelija("luettelo.txt")

        # listään tiedostossa olevat nimet luetteloon
        for nimi, numerot in self.__tiedosto.lataa().items():
            for numero in numerot:
                self.__luettelo.lisaa_numero(nimi, numero)

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 lisäys")
        print("2 haku")
        print("3 haku numeron perusteella")

    def lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot == None:
            print("numero ei tiedossa") 
            return 
        for numero in numerot:
            print(numero)
    
    def haku_numerolla(self):
        numero = input("numero: ")
        nimi = self.__luettelo.hae_numerolla(numero)
        if nimi != None:
            print(nimi)
        else:
            print("tuntematon numero")

    def lopetus(self):
        self.__tiedosto.talleta(self.__luettelo.kaikki_tiedot())


    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                self.lopetus()
                break
            elif komento == "1":
                self.lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.haku_numerolla()
            else:
                self.ohje()


# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
