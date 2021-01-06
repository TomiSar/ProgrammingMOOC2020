# Tehtäväpohjassa on määritelty luokat Tietokonepeli ja Pelivarasto. Pelivarastoon voidaan säilöä tietokonepelejä.
class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi

class Pelivarasto:
    def __init__(self):
        self.__pelit = []

    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit

# Pelimuseo, joka perii luokan Pelivarasto. Pelimuseo-luokassa uudelleentoteutetaan
# metodi anna_pelit() niin, että se palauttaa listassa ainoastaan ne pelit, jotka on tehty ennen vuotta 1990.
# Lisäksi luokassa tulee olla konstruktori, josta kutsutaan yliluokan Pelivarasto konstruktoria. Konstruktorilla ei ole parametreja.
class Pelimuseo(Pelivarasto):
    def __init__(self):
        super().__init__()
    
    # palauttaa listassa ainoastaan ne pelit, jotka on tehty ennen vuotta 1990
    def anna_pelit(self):
        pelilista = []
        for peli in super().anna_pelit():
            if peli.vuosi < 1990:
                pelilista.append(peli)
        return pelilista
    
# main
if __name__ == "__main__":
    museo = Pelimuseo()
    museo.lisaa_peli(Tietokonepeli("Pacman", "Namco", 1980))
    museo.lisaa_peli(Tietokonepeli("GTA2", "Rockstar", 1999))
    museo.lisaa_peli(Tietokonepeli("Sims", "EA", 2000))
    museo.lisaa_peli(Tietokonepeli("Bubble Bobble", "Taito", 1986))
    for peli in museo.anna_pelit():
        print(peli.nimi)