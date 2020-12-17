# tee ratkaisu tänne
def pisin_naapurijono(lista):
    arvot = []
    temp = 0
    laskuri = 0

    for i in lista:
        edellinen = temp
        temp = i

        if temp - 1 == edellinen or temp + 1 == edellinen:
            laskuri += 1
            arvot.append(laskuri)

        else:
            laskuri = 1

    return max(arvot)

if __name__ == "__main__":
    lista = [1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10]
    #lista =  [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    #lista =  [1, 2, 3, 5, 6, 9, 10]
    print(pisin_naapurijono(lista))
