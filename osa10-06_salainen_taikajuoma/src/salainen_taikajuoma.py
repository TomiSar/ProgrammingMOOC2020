class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._ainekset = []

    def lisaa_aines(self, ainesosa: str, maara: float):
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")


# Kirjoita Taikajuoma-luokan perivä luokka SalainenTaikajuoma, jolla resepti voidaan suojata salasanalla.
# Uusi luokka saa konstruktorissa taikajuoman nimen lisäksi salasanan.
# Lisäksi luokalla on metodit
# lisaa_aines(ainesosa: str, maara: float, salasana: str) ja tulosta_resepti(salasana: str)
# Jos metodeja kutsutaan väärällä salasanalla, ne antavat ValueError-poikkeuksen.
# Uudet metodit kutsuvat perityn luokan metodeja, jos salasana on oikein! Älä siis leikkaa ja liimaa toteutuksia luokasta Taikajuoma.
class SalainenTaikajuoma(Taikajuoma):
    def __init__(self, nimi: str, salasana: str):
        super().__init__(nimi)
        self.__salasana = salasana

    def lisaa_aines(self, ainesosa: str, maara: float, salasana: str):
        if salasana == self.__salasana:
            super().lisaa_aines(ainesosa, maara)
        else:
            raise ValueError("Väärä salasana!")
    
    def tulosta_resepti(self, salasana: str):
        if salasana == self.__salasana:
            super().tulosta_resepti()
        else:
            raise ValueError("Väärä salasana!")

# main
if __name__ == "__main__":
    kutistus = SalainenTaikajuoma("Kutistus maksimus", "hokkuspokkus")
    kutistus.lisaa_aines("Kärpässieni", 1.5, "hokkuspokkus")
    kutistus.lisaa_aines("Taikahiekka", 3.0, "hokkuspokkus")
    kutistus.lisaa_aines("Sammakonkutu", 4.0, "hokkuspokkus")
    kutistus.tulosta_resepti("hokkuspokkus")
    kutistus.tulosta_resepti("pokkushokkus") # Väärä salasana!