# Tee ratkaisusi tähän:
class Maksukortti:
    def __init__(self, alkusaldo):
        self.saldo = alkusaldo
 
    def __str__(self):
        return f"Kortilla on rahaa {self.saldo:.1f} euroa"

    #vähentää kortin saldoa 2.60 eurolla --> saldo ei voi mennä negatiiviseksi
    def syo_edullisesti(self):
        if self.saldo >= 2.6:
            self.saldo -= 2.6

    #vähentää kortin saldoa 4.60 eurolla --> saldo ei voi mennä negatiiviseksi
    def syo_maukkaasti(self):
        if self.saldo >= 4.6:
            self.saldo -= 4.6
 
    def lataa_rahaa(self, summa: float):
        if summa < 0:
            raise ValueError("ladattava määrä ei saa olla negatiivinen")
        self.saldo += summa


pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)
pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()
print(f"Pekka: {pekan_kortti}")
print(f"Matti: {matin_kortti}")
pekan_kortti.lataa_rahaa(20)
matin_kortti.syo_maukkaasti()
print(f"Pekka: {pekan_kortti}")
print(f"Matti: {matin_kortti}")
pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()
matin_kortti.lataa_rahaa(50)
print(f"Pekka: {pekan_kortti}")
print(f"Matti: {matin_kortti}")

# kortti = Maksukortti(10)
# print(kortti)
# kortti.lataa_rahaa(15)
# print(kortti)
# kortti.lataa_rahaa(10)
# print(kortti)
# kortti.lataa_rahaa(200)
# print(kortti)

# kortti.lataa_rahaa(-10)
# kortti = Maksukortti(10)

# kortti = Maksukortti(4)
# print(kortti)
# kortti.syo_edullisesti()
# print(kortti)
# kortti.syo_edullisesti()
# print(kortti)

# kortti = Maksukortti(50)
# print(kortti)