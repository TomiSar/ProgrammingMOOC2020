import json

class Tilasto:
    def __init__(self, pelaajat: list):
        self.__pelaajat = pelaajat
    
    def pisteiden_mukaan(self, pelaaja):
        return pelaaja['goals'] + pelaaja['assists']
    
    def maalien_mukaan(self,  pelaaja):
        # jos maaleja yhtä monta, ratkaiseen pelien vähyys
        return (pelaaja['goals'], -pelaaja['games'])
        
    def pelaajan_tiedot(self, nimi: str):
        for pelaaja in self.__pelaajat:
            if pelaaja['name'] == nimi:
                return pelaaja
        return None
    
    def maat(self):
        return sorted(list(set(pelaaja['nationality'] for pelaaja in self.__pelaajat)))

    def joukkueet(self):
        return sorted(list(set(pelaaja['team'] for pelaaja in self.__pelaajat)))

    def joukkueen_pelaajat(self, joukkue: str):
        pelaajat = [pelaaja for pelaaja in self.__pelaajat if pelaaja['team'] == joukkue]
        return sorted(pelaajat, key=self.pisteiden_mukaan, reverse=True)
    
    def maan_pelaajat(self, maa: str):
        pelaajat = [pelaaja for pelaaja in self.__pelaajat if pelaaja['nationality'] == maa]
        return sorted(pelaajat, key=self.pisteiden_mukaan, reverse=True)

    def eniten_pisteita(self, maara):
        pelaajat = sorted(self.__pelaajat, key=self.pisteiden_mukaan, reverse=True)
        return pelaajat[0: maara]

    def eniten_maaleja(self, maara):
        pelaajat = sorted(self.__pelaajat, key=self.maalien_mukaan, reverse=True)
        return pelaajat[0: maara]

class Sovellus:
    def __init__(self):
        self.__tilasto = None
    
    def ohje(self):
        ohje = """
komennot:
0 lopeta
1 hae pelaaja
2 joukkueet
3 maat
4 joukkueen pelaajat
5 maan pelaajat
6 eniten pisteitä
7 eniten maaleja"""
        print(ohje)
    
    def format(self, pelaaja: dict):
        """apumetodi, joka muotoilee pelaajasta tulostukseen sopivan merkkijonon"""
        pisteet = pelaaja['goals'] + pelaaja['assists']
        return f"{pelaaja['name']:20} {pelaaja['team']}  {pelaaja['goals']:2} + {pelaaja['assists']:2} = {pisteet:3}"

    def lue_tiedosto(self):        
        tiedoston_nimi = input("tiedosto: ")
        with open(tiedoston_nimi) as tiedosto:
            data = tiedosto.read()
        
        pelaajat = json.loads(data)
        print(f"luettiin {len(pelaajat)} pelaajan tiedot")
        self.__tilasto = Tilasto(pelaajat)

    def hae_pelaaja(self):
        nimi = input("nimi: ")
        pelaaja = self.__tilasto.pelaajan_tiedot(nimi)
        if pelaaja:
            print(self.format(pelaaja))

    def hae_joukkueet(self):
        for joukkue in self.__tilasto.joukkueet():
            print(joukkue)

    def hae_maat(self):
        for maa in self.__tilasto.maat():
            print(maa)

    def joukkueen_pelaajat(self):
        joukkue = input("joukkue: ")
        for pelaaja in self.__tilasto.joukkueen_pelaajat(joukkue):
            print(self.format(pelaaja))

    def maan_pelaajat(self):
        maa = input("maa: ")
        for pelaaja in self.__tilasto.maan_pelaajat(maa):
            print(self.format(pelaaja))
    
    def eniten_pisteita(self):
        pisteet = int(input("kuinka monta: "))
        for pelaaja in self.__tilasto.eniten_pisteita(pisteet):
            print(self.format(pelaaja))
    
    def eniten_maaleja(self):
        maalit = int(input("kuinka monta: "))
        for pelaaja in self.__tilasto.eniten_maaleja(maalit):
            print(self.format(pelaaja))
    
    def suorita(self):
        self.lue_tiedosto()
        self.ohje()

        while True:
            komento = input("\nkomento: ")
            if komento == "0":
                return
            elif komento == "1":
                self.hae_pelaaja()
            elif komento == "2":
                self.hae_joukkueet()
            elif komento == "3":
                self.hae_maat()
            elif komento == "4":
                self.joukkueen_pelaajat()
            elif komento == "5":
                self.maan_pelaajat()
            elif komento == "6":
                self.eniten_pisteita()
            elif komento == "7":
                self.eniten_maaleja()

#main
Sovellus().suorita()