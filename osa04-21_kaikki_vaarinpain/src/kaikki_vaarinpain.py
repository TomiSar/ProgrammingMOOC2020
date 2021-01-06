def kaikki_vaarinpain(lista):
    kaannettylista = []
    for merkkijono in lista:
        #Käännetään listan merkkijonot väärinpäin
        kaannettylista.append(merkkijono[::-1])
    
    #Käännetään käännettylista sanat väärinpäin
    return kaannettylista[::-1]

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)