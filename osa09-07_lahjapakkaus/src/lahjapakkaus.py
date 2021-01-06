class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"

class Pakkaus:
    def __init__(self):
        self.lahjat = []

    #lisää parametrina annettavan lahjan pakkaukseen. Metodi ei palauta mitään arvoa.
    def lisaa_lahja(self, lahja: Lahja):
        self.lahjat.append(lahja)

    #Palauttaa pakkauksessa olevien lahjojen yhteispainon.
    def yhteispaino(self):
        kokonaispaino = 0
        for lahja in self.lahjat:
            kokonaispaino += lahja.paino
        return kokonaispaino

#main
if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)
    pakkaus = Pakkaus()
    pakkaus.lisaa_lahja(kirja)
    print("Lahja:",kirja.nimi)
    print("Lahjojen yhteispaino:", pakkaus.yhteispaino())
    cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
    pakkaus.lisaa_lahja(cd_levy)
    print("Lahjat:",kirja.nimi,"ja",cd_levy.nimi)
    print("Lahjojen yhteispaino:", pakkaus.yhteispaino())

    # kirja = Lahja("Aapiskukko", 2)
    # print("Lahjan nimi:", kirja.nimi)
    # print("Lahjan paino:", kirja.paino)
    # print("Lahja:", kirja)