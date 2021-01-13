lista = [1, 2, 3, 4, 5]
while True:
    indeksi = int(input("Anna indeksi: "))
    if indeksi == -1:
        break
    arvo = int(input("Anna arvo: "))
    lista[indeksi] = arvo
    print(lista)