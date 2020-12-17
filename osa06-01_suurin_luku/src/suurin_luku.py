# tee ratkaisu tänne
def suurin():
    luvut = []

    with open("luvut.txt") as tiedosto:
        for rivi in tiedosto:
            luvut.append(rivi)

    luvut.sort(reverse=True)
    return  int(luvut[0])

if __name__ == "__main__":
    luku = suurin()
    print(f"{suurin()}")