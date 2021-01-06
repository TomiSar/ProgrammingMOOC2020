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

    def __iter__(self):
        self.n = 0
        return self

    # Iteraattorin metodin __next__ tulee palauttaa tupleja, joiden ensimmäinen alkio on 
    # tuotteen nimi ja toisen listalla olevan tuotteen lukumäärä.
    def __next__(self):
        if self.n < len(self.tuotteet):
            tuote = self.tuotteet[self.n]
            self.n += 1
            return tuote
        else:
            raise StopIteration

# main
if __name__ == "__main__":
    lista = Kauppalista()
    lista.lisaa("banaanit", 10)
    lista.lisaa("omenat", 5)
    lista.lisaa("ananas", 1)

    for tuote in lista:
        print(f"{tuote[0]}: {tuote[1]} kpl")