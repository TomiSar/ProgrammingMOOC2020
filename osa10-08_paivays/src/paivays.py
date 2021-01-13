# Tässä tehtävässä toteutetaan luokka Paivays, jonka avulla on mahdollista käsitellä päivämääriä. 
# Oletetaan tässä tehtävässä yksinkertaisuuden vuoksi, että jokaisessa kuussa on 30 päivää.
# Edellisestä johtuen tehtävässä ei poikkeuksellisesti kannata käyttää Pythonin datetime-moduulia.
# Toteutetaan luokka itse. Toteuta luokan runko ja sille vertailuoperaattorit <, >, == ja !=.

class Paivays:
    def __init__(self, paiva: int, kuukausi: int, vuosi: int):
        self.__paiva = paiva
        self.__kuukausi = kuukausi
        self.__vuosi = vuosi

    # Vertailut on helppo tehdä, kun muutetaan päiväys päiviksi
    def __arvo(self):
        return self.__vuosi * 360 + self.__kuukausi * 30 + self.__paiva

    # Muutetaan päivien määrä takaisin päivämääräksi
    def __pvm(self, paivat: int):
        kuukaudet = paivat // 30
        vuodet = kuukaudet // 12
        paivat -= kuukaudet * 30
        kuukaudet -= vuodet * 12
        return Paivays(paivat, kuukaudet, vuodet)

    # < Pienempi kuin
    def __lt__(self, toinen: "Paivays"):
        return self.__arvo() < toinen.__arvo()

    # > Suurempi kuin
    def __gt__(self, toinen: "Paivays"):
        return self.__arvo() > toinen.__arvo()

    # == Yhtä suuri kuin 
    def __eq__(self, toinen: "Paivays"):
        return self.__arvo() == toinen.__arvo()

    # != Eri suuri kuin
    def __ne__(self, toinen: "Paivays"):
        return self.__arvo() != toinen.__arvo()

    # Kasvatus
    # Toteuta päiväykselle operaattori +. Operaattori luo uuden päivämäärän joka on lisättävän 
    # lukeman päiviä verran suurempi kuin alkuperäinen päivämäärä. Alkuperäinen päivä ei saa muuttua.
    def __add__(self, lisatyt_paivat: int):
        return self.__pvm(self.__arvo() + lisatyt_paivat)

    # Erotus
    # Toteuta päiväykselle operaattori -, joka palauttaa päivämäärien eron päivissä laskettuna. Huomaa, että koska
    # oletamme jokaisessa kuukaudessa olevan 30 päivää, tässä tehtävässä vuosien päivien lukumäärä on 12*30 eli 360.
    def __sub__(self, toinen: "Paivays"):
        # abs(x) antaa x:n itseisarvon
        return abs(self.__arvo() - toinen.__arvo())

    def __str__(self):
        return f'{self.__paiva}.{self.__kuukausi}.{self.__vuosi}'
    
# main
if __name__ == "__main__":
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)
    print(p2-p1)
    print(p1-p2)
    print(p1-p3)

    # p1 = Paivays(4, 10, 2020)
    # p2 = Paivays(28, 12, 1985)
    # p3 = p1 + 3
    # p4 = p2 + 400
    # print(p1)
    # print(p2)
    # print(p3)
    # print(p4)

    # p1 = Paivays(4, 10, 2020)
    # p2 = Paivays(28, 12, 1985)
    # p3 = Paivays(28, 12, 1985)
    # print(p1)
    # print(p2)
    # print(p1 == p2)
    # print(p1 != p2)
    # print(p2 == p3)
    # print(p1 < p2)
    # print(p1 > p2)