def suurin():
    with open("luvut.txt") as tiedosto:
        alku = True
        for luku in tiedosto:
            if alku or int(luku) > suurin:
                suurin = int(luku)
                alku = False
        return suurin

#main
if __name__ == "__main__":
    luku = suurin()
    print(f"{suurin()}")