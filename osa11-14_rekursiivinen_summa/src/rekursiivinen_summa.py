# Tee rekursiivinen funktio summa(luku: int) summan 1 + 2 + ... + luku laskemiseen.
def summa(luku: int):
    # kun luku on 1, ei ole muita summattavia...
    if luku <= 1:
        return luku
    return luku + summa(luku - 1)

# main
if __name__ == "__main__":
    tulos = summa(3)
    print(tulos)
    print(summa(5))
    print(summa(10))