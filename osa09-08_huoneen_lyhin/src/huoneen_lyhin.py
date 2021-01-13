class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:
    def __init__(self):
        self.henkilot = []
 
    # lisää huoneeseen parametrina annetun henkilön
    def lisaa(self, henkilo: Henkilo):
        self.henkilot.append(henkilo)
    
    # palauttaa arvon True tai False, joka kertoo, onko huone tyhjä
    def on_tyhja(self):
        return len(self.henkilot) == 0
    
    # tulostaa huoneessa olevat henkilöt
    def tulosta_tiedot(self):
        yhteispituus = 0
        for henkilo in self.henkilot:
            yhteispituus += henkilo.pituus
        print(f"Huoneessa {len(self.henkilot)} henkilöä, yhteispituus {yhteispituus} cm")
        for henkilo in self.henkilot:
            print(f'{henkilo.nimi} ({henkilo.pituus} cm)')

    # palauttaa huoneeseen lisätyistä henkilöistä lyhimmän. Mikäli huone on tyhjä, metodi palauttaa None-viitteen. Metodin ei tule poistaa henkilöä huoneesta.
    def lyhin(self):
        lyhin_henkilo = None
        lyhin_pituus = 0
        for henkilo in self.henkilot:
            if lyhin_henkilo is None or lyhin_pituus > henkilo.pituus:
                lyhin_henkilo = henkilo
                lyhin_pituus = henkilo.pituus
        return lyhin_henkilo

    # poistaa ja palauttaa huoneesta lyhimmän henkilön. Mikäli huone on tyhjä, metodi palauttaa None-viitteen.
    def poista_lyhin(self):
        lyhin_henkilo = self.lyhin()    # Hyödynnetään aikaisempaa metodia
        if lyhin_henkilo:               # Vastaa ehtoa is Not None
            self.henkilot.remove(lyhin_henkilo)
        return lyhin_henkilo     

#main
if __name__ == "__main__":
    huone = Huone()
    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()
    print()
    poistettu = huone.poista_lyhin()
    print(f"Poistetaan huoneesta lyhin henkilö: {poistettu.nimi}")
    print()

    huone.tulosta_tiedot()

    # huone = Huone()
    # print("Huone tyhjä?", huone.on_tyhja())
    # print("Lyhin:", huone.lyhin())
    # huone.lisaa(Henkilo("Lea", 183))
    # huone.lisaa(Henkilo("Kenya", 182))
    # huone.lisaa(Henkilo("Nina", 172))
    # huone.lisaa(Henkilo("Auli", 186))
    # print("Huone tyhjä?", huone.on_tyhja())
    # print("Lyhin:", huone.lyhin())
    # print()
    # huone.tulosta_tiedot()

    # huone = Huone()
    # print("Huone tyhjä?", huone.on_tyhja())
    # huone.lisaa(Henkilo("Lea", 183))
    # huone.lisaa(Henkilo("Kenya", 182))
    # huone.lisaa(Henkilo("Auli", 186))
    # huone.lisaa(Henkilo("Nina", 172))
    # huone.lisaa(Henkilo("Terhi", 185))
    # print("Huone tyhjä?", huone.on_tyhja())
    # huone.tulosta_tiedot()