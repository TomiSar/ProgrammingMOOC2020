class Kauppalista:
    def __init__(self):
        self.tuotteet = []
 
    def tuotteita(self):
        return len(self.tuotteet)
 
    def lisaa(self, tuote: str, maara: int):
        self.tuotteet.append((tuote, maara))
 
    def tuote(self, n: int):
        return self.tuotteet[n - 1][0]
 
    def maara(self, n: int):
        return self.tuotteet[n - 1][1]
 
def tuotteita_yhteensa(lista: Kauppalista):
    yhteensa = 0
    for i in range(lista.tuotteita()):
        yhteensa += lista.maara(i + 1)
    return yhteensa

# main
if __name__ == "__main__":
    kauppalista = Kauppalista()
    kauppalista.lisaa("banaanit", 10)
    kauppalista.lisaa("omenat", 5)
    kauppalista.lisaa("ananas", 1)
    print(tuotteita_yhteensa(kauppalista))

    # for i in range(1, kauppalista.tuotteita()+1):
    #     tuote = kauppalista.tuote(i)
    #     maara = kauppalista.maara(i)
    #     print(f"{tuote}: {maara} kpl")

    # print(kauppalista.tuotteita())
    # print(kauppalista.tuote(1))
    # print(kauppalista.maara(1))
    # print(kauppalista.tuote(2))
    # print(kauppalista.maara(2))