# Kirjoita generaattorifunktio parilliset(alku: int, maksimi: int), joka saa parametrikseen alkuarvon ja maksimin. 
# Funktio tuottaa alkuarvosta lähtien parillisia lukuja. Kun saavutetaan maksimi, generaattori pysähtyy.
def parilliset(alku: int, maksimi: int):
    if alku % 2 != 0:
        alku += 1
    while alku <= maksimi:
        yield alku
        alku += 2

#main
if __name__ == "__main__":
    luvut = parilliset(11, 21)
    #luvut = parilliset(2, 10)
    for luku in luvut:
        print(luku)