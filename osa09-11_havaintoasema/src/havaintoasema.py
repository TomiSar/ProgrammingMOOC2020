# Luokan kaikkien attribuuttien pitää olla asiakkaalta piilossa. Saat itse päättää luokan sisäisen toteutuksen.
# Havaintoasema, johon voidaan tallentaa säähavaintoja nimi (str), havainnot (int) ja viimeisin havainto (str)
class Havaintoasema:
    def __init__(self, nimi: str):
        self.__nimi = nimi
        self.__havainnot_lkm = 0
        self.__viimeisin_havainto = ""

    # metodi, joka lisää havainnon listan peräään
    def lisaa_havainto(self, havainto: str):
        self.__viimeisin_havainto = havainto
        self.__havainnot_lkm += 1

    # metodi, joka palauttaa viimeksi lisätyn havainnon. Jos havaintoja ei ole tehty, metodi palauttaa tyhjän merkkijonon.
    def viimeisin_havainto(self):
        return self.__viimeisin_havainto

    # metodi, joka palauttaa havaintojen yhteismäärän
    def havaintojen_maara(self):
        return self.__havainnot_lkm

    # metodi, joka palauttaa aseman nimen ja havaintojen yhteismäärän alla olevan esimerkin mukaisessa muodossa.
    def __str__(self):
        return f"{self.__nimi}, {self.__havainnot_lkm} havaintoa"


#main
if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())
    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())
    print(asema.havaintojen_maara())
    print(asema)