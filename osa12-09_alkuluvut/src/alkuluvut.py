# Alkuluvuksi sanotaan kokonaislukua, joka on vähintään 2 ja jaollinen ainoastaan 1:llä ja itsellään. Ensimmäiset alkuluvut ovat 2, 3, 5, 7, 11 ja 13
# Kirjota generaattorifunktio alkuluvut(), joka luo uuden generaattorin. Generaattori palauttaa yksi kerrallaan 
# alkulukuja järjestyksessä 2:sta alkaen. Huomaa, että generaattori ei pysähdy koskaan, vaan palauttaa lisää lukuja niin kauan kuin niitä pyydetään.
def alkuluvut():
    luku = 1
    while True:
        if onko_alkuluku(luku):
            yield luku
        luku += 1

def onko_alkuluku(luku: int):
    if luku < 2:
        return False
    # Mahdollinen jakaja on vähintään 2 ja enintään luku-1
    for i in range(2, luku):
        if luku % i == 0:
            return False
    return True

#main
if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))