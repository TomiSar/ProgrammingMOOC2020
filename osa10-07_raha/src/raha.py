class Raha:
    def __init__(self, eurot: int, sentit: int):
        self.__eurot = eurot
        self.__sentit = sentit

    # f-stringillä on näppärä ominaisuus alkunollien
    # lisäämiseksi:02d esim. tarkoittaa, että tulostuksessa 
    # on vähintään kaksi numeroa. Saman voisi toki tehdä myös
    def __str__(self):
        return f"{self.__eurot}.{self.__sentit:02d} eur"

    # Apumetodi arvon laskemiseksi sentteinä helpottaa vertailuja
    def __arvo(self):
        return self.__eurot * 100 + self.__sentit

    # Toinen apumetodi, jolla muunnetaan annetut sentit arvoksi
    def __aseta_arvo(self, sentteja: int):
        self.__eurot = sentteja // 100
        self.__sentit = sentteja - self.__eurot * 100

    # Yhtäsuuruus
    def __eq__(self, toinen: "Raha"):
        return self.__arvo() == toinen.__arvo()

    # Pienempi kuin
    def __lt__(self, toinen: "Raha"):
        return self.__arvo() < toinen.__arvo()

    # # Suurempi kuin
    def __gt__(self, toinen: "Raha"):
        return self.__arvo() > toinen.__arvo()

    # # Erisuuruus
    def __ne__(self, toinen: "Raha"):
        return self.__arvo() != toinen.__arvo()


    # Plus
    def __add__(self, toinen: "Raha"):
        summa = Raha(0, 0)
        summa.__aseta_arvo(self.__arvo() + toinen.__arvo())
        return summa

    # Miinus
    def __sub__(self, toinen: "Raha"):
        erotus = self.__arvo() - toinen.__arvo()
        if erotus < 0:
            raise ValueError("Erotuksen tulos on negatiivinen!")
        erotusraha = Raha(0, 0)
        erotusraha.__aseta_arvo(self.__arvo() - toinen.__arvo())
        return erotusraha 

# main
if __name__ == "__main__":
    # print(e1)
    # e1.eurot = 1000
    # print(e1)

    e1 = Raha(4, 5)
    e2 = Raha(2, 95)
    e3 = e1 + e2
    e4 = e1 - e2
    print(e3)
    print(e4)
    e5 = e2 - e1

    # e1 = Raha(4, 10)
    # e2 = Raha(2, 5)

    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)

    # e1 = Raha(4, 10)
    # e2 = Raha(2, 5)
    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)

    # e1 = Raha(4, 10)
    # e2 = Raha(2, 5)
    # e3 = Raha(4, 10)
    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)

    # e1 = Raha(4, 10)
    # e2 = Raha(2, 5)  # kaksi euroa ja viisi senttiä
    # print(e1)
    # print(e2)