def lue_matriisi():
    with open("matriisi.txt") as tiedosto:
        m = []
        for rivi in tiedosto:
            mrivi = []
            alkiot = rivi.split(",")
            for alkio in alkiot:
                mrivi.append(int(alkio))
            m.append(mrivi)
 
    return m
 
# Yhdistää matriisin rivit yhdeksi listaksi
def yhdista(matriisi: list):
    lista = []
    for rivi in matriisi:
        lista += rivi
    return lista
 
def summa():
    lista = yhdista(lue_matriisi())
    return sum(lista)
 
def maksimi():
    lista = yhdista(lue_matriisi())
    return max(lista)
 
def rivisummat():
    matriisi = lue_matriisi()
    summat = []
    for rivi in matriisi:
        summat.append(sum(rivi))
    return summat

#main
if __name__ == "__main__":
    lue_matriisi()
    print(summa())
    print(maksimi())
    print(rivisummat())