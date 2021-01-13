# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(leveys, merkkijono):
    if merkkijono == "":
        print(leveys * "*")
    else:
        print(leveys * merkkijono[0])

def kuvio(yla_leveys, yla_merkki, ala_leveys, ala_merkki):
    rivi = 1
    while (rivi <= yla_leveys):
        viiva(rivi, yla_merkki)
        rivi += 1
    rivi = 1
    while rivi <= ala_leveys:
        viiva(yla_leveys, ala_merkki)
        rivi += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
