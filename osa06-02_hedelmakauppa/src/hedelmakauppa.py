def lue_hedelmat():
    sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            nimi = osat[0]
            hinta = float(osat[1])
            sanakirja[nimi] = hinta
    
    return sanakirja

#main
if __name__ == "__main__":
    sanakirja = lue_hedelmat()
    print(sanakirja)
