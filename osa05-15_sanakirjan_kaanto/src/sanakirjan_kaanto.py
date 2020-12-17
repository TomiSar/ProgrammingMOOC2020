def kaanna(sanakirja: dict):
    avaimet = []
    arvot = []

    for avain in sanakirja:
        avaimet.append(sanakirja[avain]) #avaimet
        arvot.append(avain)              #arvot
    
    sanakirja.clear()

    i = 0
    for avain in avaimet:
        sanakirja[avain] = arvot[i]
        i += 1

if __name__ == "__main__":
    #s = { 1: 10, 2: 20, 3: 30 }
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)