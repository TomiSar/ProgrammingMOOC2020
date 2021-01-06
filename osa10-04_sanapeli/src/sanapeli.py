import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")


# PisinSana eli pelin versio, missä kunkin kierroksen voittaja on sen kierroksen aikana pidemmän sanan syöttänyt käyttäjä.
# Uusi versio toteuteaan perimällä luokka Sanapeli ja ylikirjoittamalla sen metodi kierroksen_voittaja sopivalla tavalla.
# Tasapelin kohdalla voidaan määrittelyjen mukaan palauttaa mikä tahansa muu luku.
class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        else:        
            return 0

# EnitenVokaaleja eli pelin versio, missä kunkin kierroksen voittaja on se pelaaja, jonka sanassa oli enemmän vokaaleja.
class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    
    # Apumetodi jolla lasketaan sanassa olevat vokaalit
    def laske_vokaalit(self, sana: str):
        vokaalit = "aeiouyåöäö"
        vokaalit_lkm = 0
        for merkki in sana:
            if merkki in vokaalit:
                vokaalit_lkm += 1
        return vokaalit_lkm

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if self.laske_vokaalit(pelaaja1_sana) > self.laske_vokaalit(pelaaja2_sana):
            return 1
        elif self.laske_vokaalit(pelaaja2_sana) > self.laske_vokaalit(pelaaja1_sana):
            return 2
        else:        
            return 0


# KiviPaperiSakset joka mallintaa nimensä mukaisesti kivi, paperi ja sakset -peliä.
# Pelin säännöt ovat seuraavat:
# kivi voittaa sakset (kivellä voi rikkoa sakset eikä saksilla voi leikata kiveä)
# paperi voittaa kiven (kiven voi peittää paperilla)
# sakset voittaa paperin (saksilla voi leikata paperia)
# Jos pelaajan syöte on epäkelpo, eli se ei ole mikään sanoista kivi, paperi, sakset pelaaja häviää kierroksen, ellei molempien syöte ole epäkelpo.
class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        valinnat = { "kivi" : 0, "paperi" : 1, "sakset" : 2 }
        # Syöte on epäkelpo
        if pelaaja1_sana not in valinnat.keys() and pelaaja2_sana not in valinnat.keys():
            return 0
        if pelaaja1_sana not in valinnat.keys():
            return 1
        if pelaaja2_sana not in valinnat.keys():
            return 2
        
        # Lasketaan sanakirjan avulla arvojen erotus
        # Esimerkiksi: pelaaja1 valitsee paperin, arvoksi 1
        # pelaaja 2 valitsee kiven, arvoksi 0
        # pelaaja 1 voittaa kun suhde on 1 tai -2
        # ...ja pelaaja 2 kun suhde on -1 tai 2
        # jos suhde on 0, molemmilla on sama valinta
        suhde = valinnat[pelaaja1_sana] - valinnat[pelaaja2_sana]
        if suhde == 0:
            return 0
        if suhde == 1 or suhde == -2:
            return 1
        return 2

# main
if __name__ == "__main__":
    p = KiviPaperiSakset(3)
    p.pelaa()
    # p = EnitenVokaaleja(3)
    # p.pelaa()
    # p = PisinSana(3)
    # p.pelaa()
    # p = Sanapeli(3)
    # p.pelaa()