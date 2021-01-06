# Kirjoita luokka Pankkitili, joka mallintaa pankkitiliä. Luokalla tulee olla
# konstruktori, joka saa parametrikseen tilinomistajan (str), tilinumeron (str) ja saldon (float)
class Pankkitili:
    def __init__(self, tilinomistaja: str, tilinumero: str, saldo: float):
        self.__tilinomistaja = tilinomistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo

    # yksityinen metodi, joka vähentää tililtä yhden prosentin rahaa. Luokassa kutsutaan tätä 
    # metodia aina, kun asiakas kutsuu jompaa kumpaa metodeista talleta tai nosta. Prosentti 
    # vähennetään aina varsinaisen operaation jälkeen (eli. esimerkiksi vasta sitten, kun rahat on talletettu). 
    def __palvelumaksu(self):
        self.__saldo *= 0.99

    # metodi, jolla tilille voidaan tallettaa rahaa
    def talleta(self, summa: float):
        self.__saldo += summa
        self.__palvelumaksu()

    # metodi, joka nostaa tililtä rahasumman
    def nosta(self, summa: float):
        self.__saldo -= summa
        self.__palvelumaksu()

    # havainnointimetodi, joka palauttaa tilin saldon
    @property
    def saldo(self):
        return self.__saldo

# main
if __name__ == "__main__":
    tili = Pankkitili("Raimo Rahakas", "123456-789", 1000)
    print("Alussa tilillä rahaa:",tili.saldo)               #Alussa tilillä rahaa: 1000
    tili.nosta(100)
    print("Noston jälkeen tilillä rahaa:",tili.saldo)       #Noston jälkeen tilillä rahaa: 891.0
    tili.talleta(100)
    print("Talletuksen jälkeen tilillä rahaa:",tili.saldo)  #Talletuksen jälkeen tilillä rahaa: 981.09