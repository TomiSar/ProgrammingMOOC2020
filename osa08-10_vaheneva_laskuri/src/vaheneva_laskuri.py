class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa
        self.alkuperainen_arvo = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        if self.arvo > 0:
            self.arvo -= 1

    def nollaa(self):
        self.arvo = 0

    def palauta_alkuperainen_arvo(self):
        self.arvo = self.alkuperainen_arvo

# main
if __name__ == "__main__":

    laskuri = VahenevaLaskuri(55)
    laskuri.tulosta_arvo() #arvo: 55
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.tulosta_arvo() #arvo: 51
    laskuri.palauta_alkuperainen_arvo()
    laskuri.tulosta_arvo() #arvo: 55

    # laskuri = VahenevaLaskuri(100)
    # laskuri.tulosta_arvo() #arvo: 100
    # laskuri.nollaa()
    # laskuri.tulosta_arvo() #arvo: 0

    # laskuri = VahenevaLaskuri(1)
    # laskuri.tulosta_arvo() #arvo: 1
    # laskuri.vahenna()
    # laskuri.vahenna()
    # laskuri.tulosta_arvo() #arvo: 0