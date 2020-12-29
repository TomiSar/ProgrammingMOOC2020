# Tee ratkaisusi luokan Auto perään
# Älä muuta luokkaa!
class Auto:
    def __init__(self, merkki: str, huippunopeus: int):
        self.merkki = merkki
        self.huippunopeus = huippunopeus
    def __str__(self):
        return f"Auto (merkki: {self.merkki}, huippunopeus: {self.huippunopeus})"

# TEE RATKAISUSI TÄHÄN:
# saa parametrikseen listan Auto-luokan olioita. Funktio palauttaa listassa olevista autoista 
# nopeimman auton merkin. Voit olettaa, että nopein auto on yksikäsitteinen.
def nopein_auto(autot: list):
    nopein_merkki = autot[0].merkki
    nopein_nopeus = autot[0].huippunopeus

    for auto in autot:
        if nopein_nopeus < auto.huippunopeus:
            nopein_nopeus = auto.huippunopeus
            nopein_merkki = auto.merkki
    return nopein_merkki

#main
if __name__ == "__main__":
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Ferrari", 280)
    auto3 = Auto("Lada", 110)
    auto4 = Auto("Lamborghini", 350)
    auto5 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    print(nopein_auto(autot))