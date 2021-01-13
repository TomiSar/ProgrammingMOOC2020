def pisimmat(lista):
    nimilista = []

    for nimi in lista:
        if len(nimilista) == 0 or len(nimi) > len(nimilista[0]):
            nimilista = [nimi]
        #Jos pisimpiä merkkijonoja on useampia, funktio palauttaa ne kaikki listassa.
        elif len(nimi) == len(nimilista[0]):
            nimilista.append(nimi)

    return nimilista

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos) # ['emilia', 'juhani']