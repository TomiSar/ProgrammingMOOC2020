class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus

    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"

    def pinta_ala(self):
        return self.leveys * self.korkeus

# Nelio joka perii luokan Suorakulmio. Suorakulmiosta poiketen neliön kaikki sivut ovat 
# saman pituisia, eli neliö on eräänlainen yksinkertaisempi erikoistapaus suorakulmiosta. Luokka ei saa määritellä uusia attribuutteja!
class Nelio(Suorakulmio):
    # Annetaan sivun pituus sekä leveydeksi että korkeudeksi yliluokan konstruktorille
    def __init__(self, sivunpituus: int):
        super().__init__(sivunpituus, sivunpituus)

    def __str__(self):
        return f"neliö {self.leveys}x{self.leveys}"

# SuorakulmainenKolmio joka perii luokanSuorakulmio. Luokka ei saa määritelä uusia attribuutteja! 
# Suorakulmaisen kolmion pinta-ala on sen korkeys*leveys jaettuna kahdella.
class SuorakulmainenKolmio(Suorakulmio):
    def __str__(self):
        return f"suorakulmainen kolmio {self.leveys}x{self.korkeus}"

    # perii metodin luokalta Suorakulmio 
    def pinta_ala(self):
        return super().pinta_ala() / 2

# main
if __name__ == "__main__":
    kolmio = SuorakulmainenKolmio(3, 4)
    print(kolmio)
    print("kolmion pinta-ala:",kolmio.pinta_ala())

    nelio = Nelio(4)
    print(nelio)
    print("neliön pinta-ala:", nelio.pinta_ala())