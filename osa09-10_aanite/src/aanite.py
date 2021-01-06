# Huomaa, että havainnointimetodi eli @property-dekoraattori pitää esitellä luokassa ennen asetusmetodia, 
# muuten seuraa virhe. Tämä johtuu siitä, että @property-dekoraattori määrittelee käytettävän 
# "asetusattribuutin" nimen (edellisessä esimerkiksi rahaa), ja asetusmetodi .setter liittää siihen uuden toiminnallisuuden.
class Aanite:
    def __init__(self, pituus: int):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("Pituus ei voi olla negatiivinen")
    

    # Havainnointimetodi pituus, joka palauttaa pituuden
    @property
    def pituus(self):
        return self.__pituus

    # Asetusmetodi pituus, joka asettaa pituuden arvon
    @pituus.setter
    def pituus(self, pituus):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("Pituus ei voi olla negatiivinen")

#main
if __name__ == "__main__":
    the_wall = Aanite(43)
    print(the_wall.pituus)
    the_wall.pituus = 44
    print(the_wall.pituus)