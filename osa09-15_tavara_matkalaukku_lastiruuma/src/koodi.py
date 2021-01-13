# Tavara, josta muodostetut oliot vastaavat erilaisia tavaroita. Tallennettavat tiedot ovat tavaran nimi ja paino (kg).
class Tavara:
    def __init__(self, nimi: str, paino: int):
        self.__nimi = nimi
        self.__paino = paino

    #palauttetaan tavaran nimi
    def nimi(self):
        return self.__nimi

    #palauttetaan tavaran paino
    def paino(self):
        return self.__paino

    def __str__(self):
        return f"{self.__nimi} ({self.__paino} kg)"

# Matkalaukku, liittyy tavaroita ja konstruktori maksimipaino, joka määrittelee tavaroiden suurimman mahdollisen yhteispainon.
# Luokan tulee valvoa, että sen sisältämien tavaroiden yhteispaino ei ylitä maksimipainoa. Jos maksimipaino ylittyisi 
# lisättävän tavaran vuoksi, metodi lisaa_tavara ei saa lisätä uutta tavaraa laukkuun.
class Matkalaukku:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__tavarat = []

    # palauttaa matkalaukun yhteispainon, joka on sen sisältävien tavaroiden painojen summa
    def paino(self):
        yhteispaino = 0
        for tavara in self.__tavarat:
            yhteispaino += tavara.paino()
        return yhteispaino

    # Jos maksimipaino ylittyisi lisättävän tavaran vuoksi, metodi ei saa lisätä uutta tavaraa laukkuun.
    def lisaa_tavara(self, tavara):
        if self.__maksimipaino < self.paino() + tavara.paino():
            return
        self.__tavarat.append(tavara)

    # tulostaa kaikki matkalaukussa olevat tavarat
    def tulosta_tavarat(self):
        for tavara in self.__tavarat:
            print(tavara)

    # palauttaa painoltaan suurimman tavaran. Jos yhtä raskaita tavaroita on useita, metodi voi palauttaa 
    # minkä tahansa niistä. Metodin tulee palauttaa olioviite. Jos laukku on tyhjä, palauta arvo None.
    def raskain_tavara(self):
        if self.__tavarat is None:
            return None
        
        raskain = self.__tavarat[0]
        for tavara in self.__tavarat:
            if tavara.paino() > raskain.paino():
                raskain = tavara
        return raskain

    # Käytetään osan 7 lopussa esiteltävää yhden rivin ehtoa
    def __str__(self):
        loppu_a = "a" if len(self.__tavarat) != 1 else ""
        return f"{len(self.__tavarat)} tavara{loppu_a} ({self.paino()} kg)"


# Lastiruuma luokan tulee valvoa, että sen matkalaukkujen yhteispaino ei ylitä maksimipainoa.
class Lastiruuma:
    def __init__(self, maksimipaino: int):
        self.__maksimipaino = maksimipaino
        self.__matkalaukut = []

    # palauttaa lastiruuman yhteispainon, joka on sen sisältävien matkalaukkujen painojen summa
    def paino(self):
        yhteispaino = 0
        for matkalaukku in self.__matkalaukut:
            yhteispaino += matkalaukku.paino()
        return yhteispaino

    # Jos maksimipaino ylittyisi uuden matkalaukun vuoksi, metodi lisaa_matkalaukku ei saa lisätä uutta matkalaukkua.
    def lisaa_matkalaukku(self, matkalaukku):
        if self.__maksimipaino < self.paino() + matkalaukku.paino():
            return
        self.__matkalaukut.append(matkalaukku)

    # tulostaa kaikki lastiruuman matkalaukuissa olevat tavarat
    def tulosta_tavarat(self):
        for matkalaukku in self.__matkalaukut:
            matkalaukku.tulosta_tavarat()

    def __str__(self):
        loppu_a = "a" if len(self.__matkalaukut) != 1 else ""
        return f"{len(self.__matkalaukut)} matkalaukku{loppu_a}, tilaa {self.__maksimipaino-self.paino()} kg"

#main
if __name__ == "__main__":
    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)

    lastiruuma = Lastiruuma(1000)
    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)

    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()

    # lastiruuma = Lastiruuma(1000)
    # print(lastiruuma)

    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)

    # adan_laukku = Matkalaukku(10)
    # adan_laukku.lisaa_tavara(kirja)
    # adan_laukku.lisaa_tavara(puhelin)

    # pekan_laukku = Matkalaukku(10)
    # pekan_laukku.lisaa_tavara(tiiliskivi)
    # lastiruuma.lisaa_matkalaukku(adan_laukku)    
    # print(lastiruuma)
    # lastiruuma.lisaa_matkalaukku(pekan_laukku)
    # print(lastiruuma)

    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)

    # matkalaukku = Matkalaukku(10)
    # matkalaukku.lisaa_tavara(kirja)
    # matkalaukku.lisaa_tavara(puhelin)
    # matkalaukku.lisaa_tavara(tiiliskivi)

    # print("Matkalaukussa on seuraavat tavarat:")
    # matkalaukku.tulosta_tavarat()
    # paino_yht = matkalaukku.paino()
    # print(f"Yhteispaino: {paino_yht} kg")
    # raskain = matkalaukku.raskain_tavara()
    # print(f"Raskain tavara: {raskain}")

    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # tiiliskivi = Tavara("Tiiliskivi", 4)
    # matkalaukku = Matkalaukku(5)
    # print(matkalaukku)
    # matkalaukku.lisaa_tavara(kirja)
    # print(matkalaukku)
    # matkalaukku.lisaa_tavara(puhelin)
    # print(matkalaukku)
    # matkalaukku.lisaa_tavara(tiiliskivi)
    # print(matkalaukku)

    # kirja = Tavara("Aapiskukko", 2)
    # puhelin = Tavara("Nokia 3210", 1)
    # print("Kirjan nimi:", kirja.nimi())
    # print("Kirjan paino:", kirja.paino())
    # print("Kirja:", kirja)
    # print("Puhelin:", puhelin)