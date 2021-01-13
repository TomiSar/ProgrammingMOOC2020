# Tee interaktiivinen ohjelma, jonka avulla voit pitää kirjaa opintomenestyksestäsi. Sovelluksen rakenteen saat 
# päättää itse, mutta nyt on hyvä tilaisuus harjoitella Puhelinluettelo-esimerkin kaltaisen oliorakenteen muodostamista.
class Kurssi:
    def __init__(self, nimi: str, arvosana: int, opintopisteet: int):
        self.__nimi = nimi 
        self.__arvosana = arvosana
        self.__opintopisteet = opintopisteet
 
    def arvosana(self):
        return self.__arvosana
 
    def opintopisteet(self):
        return self.__opintopisteet
 
    def __str__(self):
        return f"{self.__nimi} ({self.__opintopisteet} op) arvosana {self.__arvosana}"
 
class Opintorekisteri:
    def __init__(self):
       self.kurssit = {}    
 
    def lisaa_uusi_suoritus(self, kurssin_nimi, arvosana, op):
        if kurssin_nimi in self.kurssit and self.kurssit[kurssin_nimi].arvosana() > arvosana:
            return
 
        self.kurssit[kurssin_nimi] = Kurssi(kurssin_nimi, arvosana, op)
 
    def hae_suoritus(self, kurssin_nimi):
        if not kurssin_nimi in self.kurssit:
            return None
 
        return self.kurssit[kurssin_nimi]        
 
    def hae_tilastot(self):
        kursseja = len(self.kurssit)
        opintopisteet = 0
        arvosanojen_summa = 0
        arvosanat = [0, 0, 0, 0, 0, 0, 0]
 
        for kurssi in self.kurssit.values():
            opintopisteet += kurssi.opintopisteet()
            arvosanojen_summa += kurssi.arvosana()
            arvosanat[kurssi.arvosana()] += 1
        
        return {
            "kursseja": kursseja,
            "opintopisteet": opintopisteet,
            "keskiarvo": arvosanojen_summa / kursseja,
            "arvosanat": arvosanat
        }
 
class Sovellus:
    def __init__(self):
        self.rekisteri = Opintorekisteri()     
 
    def ohje(self):
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
 
    def uusi_suoritus(self):
        kurssin_nimi = input("kurssi: ")
        arvosana = int(input("arvosana: "))
        op = int(input("opintopisteet: "))
        self.rekisteri.lisaa_uusi_suoritus(kurssin_nimi, arvosana, op)
 
    def hae_suoritus(self):
        kurssin_nimi = input("kurssi: ")
        kurssi = self.rekisteri.hae_suoritus(kurssin_nimi)
        if kurssi is None:
            print("ei suoritusta")
        else:
            print(kurssi)        
 
    def tilasto(self):
        t = self.rekisteri.hae_tilastot() 
 
        print(f"suorituksia {t['kursseja']} kurssilta, yhteensä {t['opintopisteet']} opintopistettä")
        print(f"keskiarvo {t['keskiarvo']:.1f}")
        print("arvosanajakauma")
        for i in range(5, 0, -1):
            arvosanan_esiintymat = t['arvosanat'][i]
            rivi = "x"*arvosanan_esiintymat
            print(f"{i}: {rivi}")        
 
    def suorita(self):
        self.ohje()
 
        while True:
            print()
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento=="1":
                self.uusi_suoritus()
            elif komento=="2":
                self.hae_suoritus()
            elif komento=="3":
                self.tilasto()

# Ohjelma
Sovellus().suorita()