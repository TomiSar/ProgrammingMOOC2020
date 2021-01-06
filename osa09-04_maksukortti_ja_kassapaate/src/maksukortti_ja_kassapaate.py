class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    # Toteuta metodi siten, että se ottaa kortilta rahaa vain, jos saldoa riittää
    # Onnistuessaan metodi palauttaa True ja muuten False
    def ota_rahaa(self, maara: float):
        if self.saldo >= maara:
            self.saldo -= maara
            return True
        return False

class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0
    
    # Edullinen lounas maksaa 2.50 euroa
    # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
    # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
    def syo_edullisesti(self, maksu: float):
        if maksu >= 2.5:
            self.rahaa += 2.5
            self.edulliset += 1
            maksu -= 2.5
        return maksu

    # Maukas lounas maksaa 4.30 euroa
    # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
    # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
    def syo_maukkaasti(self, maksu: float):
        if maksu >= 4.3:
            self.rahaa += 4.3
            self.maukkaat += 1
            maksu -= 4.3
        return maksu

    # Edullinen lounas maksaa 2.50 euroa
    # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
    # Muuten palautetaan False
    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        if kortti.saldo >= 2.5:
            kortti.ota_rahaa(2.5)
            self.edulliset += 1
            return True
        else:
            return False

    # Maukas lounas maksaa 4.30 euroa
    # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
    # Muuten palautetaan False
    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        if kortti.saldo >= 4.3:
            kortti.ota_rahaa(4.3)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        kortti.lataa_rahaa(summa)
        self.rahaa += summa

#main
if __name__ == "__main__":
    exactum = Kassapaate()
    antin_kortti = Maksukortti(2)
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")     #Kortilla rahaa 2 euroa
    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("Riittikö raha:", tulos)                          #Riittikö raha: False
    exactum.lataa_rahaa_kortille(antin_kortti, 100)         
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")     #Kortilla rahaa 102 euroa
    tulos = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("Riittikö raha:", tulos)                          #Riittikö raha: True
    print(f"Kortilla rahaa {antin_kortti.saldo} euroa")     #Kortilla rahaa 97.7 euroa
    print("Kassassa rahaa", exactum.rahaa)                  #Kassassa rahaa 1100     
    print("Edullisia lounaita myyty", exactum.edulliset)    #Edullisia lounaita myyty 0
    print("Maukkaita lounaita myyty", exactum.maukkaat)     #Maukkkaita lounaita myyty 1

    # exactum = Kassapaate()
    # vaihtorahaa = exactum.syo_edullisesti(10)
    # print("Vaihtorahaa jäi", vaihtorahaa)
    # kortti = Maksukortti(7)
    # tulos = exactum.syo_maukkaasti_kortilla(kortti)
    # print("Riittikö raha:", tulos)
    # tulos = exactum.syo_maukkaasti_kortilla(kortti)
    # print("Riittikö raha:", tulos)
    # tulos = exactum.syo_edullisesti_kortilla(kortti)
    # print("Riittikö raha:", tulos)
    # print("Kassassa rahaa", exactum.rahaa)
    # print("Edullisia lounaita myyty", exactum.edulliset)
    # print("Maukkaita lounaita myyty", exactum.maukkaat)

    # exactum = Kassapaate()
    # vaihtorahaa = exactum.syo_edullisesti(10)
    # print("Vaihtorahaa jäi", vaihtorahaa)
    # vaihtorahaa = exactum.syo_edullisesti(5)
    # print("Vaihtorahaa jäi", vaihtorahaa)
    # vaihtorahaa = exactum.syo_maukkaasti(4.3)
    # print("Vaihtorahaa jäi", vaihtorahaa)
    # print("Kassassa rahaa", exactum.rahaa)
    # print("Edullisia lounaita myyty", exactum.edulliset)
    # print("Maukkaita lounaita myyty", exactum.maukkaat)

    # maksukortti = Maksukortti(10)
    # print("Rahaa",maksukortti.saldo)
    # tulos = maksukortti.ota_rahaa(8)
    # print("Onnistuiko otto:", tulos)
    # print("Rahaa", maksukortti.saldo)
    # tulos = maksukortti.ota_rahaa(4)
    # print("Onnistuiko otto:", tulos)
    # print("Rahaa", maksukortti.saldo)