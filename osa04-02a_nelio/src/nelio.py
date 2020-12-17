# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):
    if merkkijono == "":
        print(leveys * "*")
    else:
        print(leveys * merkkijono[0])

def nelio(koko, merkki):
        rivi = 0
        while rivi < koko:
            viiva(koko, merkki)
            rivi += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "*")
    print()
    nelio(3, "o")
