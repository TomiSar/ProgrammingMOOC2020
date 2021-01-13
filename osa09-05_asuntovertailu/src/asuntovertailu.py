class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta

    #True, jos asunto-olio itse on pinta-alaltaan suurempi kuin verrattava asunto-olio
    def suurempi(self, verrattava):
        return self.nelioita > verrattava.nelioita

    # Palauttaa asunto-olion ja verrattavan asunto-olion hintaeron. Hintaero on asuntojen 
    # hintojen erotuksen (hinta lasketaan kertomalla neliöhinta neliöillä) itseisarvo.
    def hintaero(self, verrattava):
        hinta_ero = abs((self.nelioita * self.neliohinta) - (verrattava.nelioita * verrattava.neliohinta))
        return hinta_ero

    #Palauttaa True, jos asunto-olio on kalliimpi kuin verrattavana oleva asunto-olio.
    def kalliimpi(self, verrattava):
        hinta_ero = (self.nelioita * self.neliohinta) - (verrattava.nelioita * verrattava.neliohinta)
        return hinta_ero > 0

#main
if __name__ == "__main__":
    eira_yksio = Asunto(1, 16, 5500)
    kallio_kaksio = Asunto(2, 38, 4200)
    jakomaki_kolmio = Asunto(3, 78, 2500)

    print(eira_yksio.kalliimpi(kallio_kaksio))      #False
    print(jakomaki_kolmio.kalliimpi(kallio_kaksio)) #True
    print(eira_yksio.hintaero(kallio_kaksio))       #71600
    print(jakomaki_kolmio.hintaero(kallio_kaksio))  #35400
    print(eira_yksio.suurempi(kallio_kaksio))       #False 
    print(jakomaki_kolmio.suurempi(kallio_kaksio))  #True