# tee ratkaisu tänne
def poista_isot(lista):
    uusilista = []
    for mjono in lista:
        if not mjono.isupper():
            uusilista.append(mjono)

    return uusilista

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)