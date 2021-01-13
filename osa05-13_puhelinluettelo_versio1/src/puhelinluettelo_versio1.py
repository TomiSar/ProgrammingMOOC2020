def hae_henkilo(henkilot):
    nimi = input("nimi: ")
    if nimi in henkilot:
        print(henkilot[nimi])
    else:
        print("ei numeroa")

def lisaa_henkilo(henkilot):
    nimi = input("nimi: ")
    numero = input("numero: ")
    henkilot[nimi] = numero
    print("ok!")

def main():
    henkilot = {}
    while True:
        komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if komento == "1":
            hae_henkilo(henkilot)
        if komento == "2":
            lisaa_henkilo(henkilot)
        if komento == "3":
            break
    print("lopetetaan...")

main()