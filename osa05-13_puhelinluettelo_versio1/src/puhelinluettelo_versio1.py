luettelo = {}
while True:

    komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))

    if komento == 1:
        nimi = input("nimi: ")
        if nimi in luettelo.keys():
             print(luettelo[nimi])
        else:
            print("ei numeroa")

    if komento == 2:
        nimi = input("nimi: ")
        puhelinnumero = input("numero: ")
        luettelo[nimi] = puhelinnumero
        print('ok!')
    
    if komento == 3:
        break

print('lopetetaan...')