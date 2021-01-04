# TEE RATKAISUSI TÄHÄN:
# Kirjoita luokka Lottorivi, joka saa konstruktorissaan parametrikseen kierroksen numeron (kokonaisluku) 
# sekä seitsemänalkioisen kokonaislukulistan. Lista kuvaa kierroksen oikeita numeroita (eli oikeaa riviä). Kirjoita lisäksi luokalle metodi
class Lottorivi:
    def __init__ (self, kierros: int, oikeat: int):
        self.kierros = kierros
        self.__oikeat = oikeat

    # palauttaa kokonaislukuna tiedon siitä, kuinka monta osumaa rivissä oli
    def osumien_maara(self, pelattu_rivi: list):
        return len([numero for numero in pelattu_rivi if numero in self.__oikeat])

    # palauttaa uuden listan. Uudessa listassa on vanhoilla paikoillaan oikeat numerot (eli ne, jotka löytyvät myös oikeasta rivistä), muiden paikalla on -1.
    def osumat_paikoillaan(self, pelattu_rivi: list):
        return [numero if numero in self.__oikeat else -1 for numero in pelattu_rivi]

#main
if __name__ == "__main__":
    oikea = Lottorivi(8, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]
    print(oikea.osumat_paikoillaan(oma_rivi)) # [1, -1, -1, 10, -1, 20, 30]

    # oikea = Lottorivi(5, [1,2,3,4,5,6,7])
    # oma_rivi = [1,4,7,11,13,19,24]
    # print(oikea.osumien_maara(oma_rivi)) # 3