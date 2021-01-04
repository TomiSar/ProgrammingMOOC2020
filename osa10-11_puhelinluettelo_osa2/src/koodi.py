# Luokka henkilön tietojen esittämiseen. Siirretään henkilön tietojen (eli puhelinnumerojen sekä osoitteen) 
# esittäminen oman luokkansa Henkilo vastuulle
class Henkilo:
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = None
 
    def nimi(self):
        return self.__nimi
 
    def numerot(self):
        return self.__numerot
 
    def lisaa_numero(self, numero: str):
        self.__numerot.append(numero)
 
    def osoite(self):
        return self.__osoite
 
    def lisaa_osoite(self, osoite: str):
        self.__osoite = osoite
 
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}
 
    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_numero(numero)
 
    def lisaa_osoite(self, nimi: str, osoite: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
        self.__henkilot[nimi].lisaa_osoite(osoite)
 
    def hae_tiedot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]
 
    def kaikki_tiedot(self):
        return self.__henkilot
 
# Tee ratkaisusi tähän:
class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()
 
    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")
 
 
    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)
 
    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)
 
    def haku(self):
        nimi = input("nimi: ")
        tiedot = self.__luettelo.hae_tiedot(nimi)
        if tiedot==None:
            print("numero ei tiedossa")
            print("osoite ei tiedossa")
            return
 
        numerot = tiedot.numerot()
        if len(numerot)==0:
            print("numero ei tiedossa") 
        else: 
            for numero in numerot:
                print(numero)
 
        osoite = tiedot.osoite()
        if osoite!=None:
            print(osoite)
        else:
            print("osoite ei tiedossa")
 
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()

#main
#if __name__ == "__main__":
    # henkilo = Henkilo("Erkki")
    # print(henkilo.nimi())
    # print(henkilo.numerot())
    # print(henkilo.osoite())
    # henkilo.lisaa_numero("040-123456")
    # henkilo.lisaa_osoite("Mannerheimintie 10 Helsinki")
    # print(henkilo.numerot())
    # print(henkilo.osoite())