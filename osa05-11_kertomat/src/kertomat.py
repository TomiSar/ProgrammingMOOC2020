def kertomat(luku):
    sanakirja = {}
    alku = 1
    kertoma = 1
    while alku <= luku:
        kertoma *= alku
        sanakirja[alku] = kertoma
        alku += 1
        
    return sanakirja


if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])