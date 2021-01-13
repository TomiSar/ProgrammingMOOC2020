def hae(henkilot):
    nimi = input("nimi: ")
    if nimi in henkilot:
        for numero in henkilot[nimi]:
            print(numero)
    else:
        print("ei numeroa")

def lisaa(henkilot):
    nimi = input("nimi: ")
    numero = input("numero: ")

    #henkilöllä voi olla useampia puhelinnumeroita ja ohjelma listaa jokaisen numeron
    #jos nimeä ei ole luettelossa luodaan uusi lista (muuten lisätään olemassaolevan henkilön listaan uusi numero)
    if nimi not in henkilot:
        henkilot[nimi] = []
    henkilot[nimi].append(numero)
    print("ok!")
    

def main():
    henkilot = {}
    while True:
        komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if (komento == "1"):
            hae(henkilot)
        if (komento == "2"):
            lisaa(henkilot)
        if (komento == "3"):
            break

    print("lopetetaan...")

main()

# Another possible solution
# numerot = []
# luettelo = {}
# while True:
#     komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
#     if komento == 1:
#         nimi = input("nimi: ")
#         if nimi in luettelo:
#             for numero in numerot:
#                 print(numero)
#         if nimi not in luettelo:
#             print("ei numeroa")
 
#     if komento == 2:
#         nimi = input("nimi: ")
#         puhelinnumero = input("numero: ")

#         if nimi not in luettelo:
#             luettelo[nimi] = [puhelinnumero]
#             numero = numerot.append(puhelinnumero)
#         else:
#             luettelo[nimi] = [numerot.append(puhelinnumero)]

#         print('ok!')
    
#     if komento == 3:
#         break
 
# print('lopetetaan...')