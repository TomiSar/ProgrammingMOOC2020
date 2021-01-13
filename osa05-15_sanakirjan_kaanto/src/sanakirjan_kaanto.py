def kaanna(sanakirja: dict):
    kopio = {}
    for avain in sanakirja:         
        kopio[avain] = sanakirja[avain] #kopio alkuperäisestä sanakirjasta
    for avain in kopio:
        del sanakirja[avain]            #tyhjennetään alkuperäinen
    for avain in kopio:
        sanakirja[kopio[avain]] = avain #kopioidaan avain:arvo alkupeäisen kopioon

#main
if __name__ == "__main__":
    sanakirja = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas", 5: "viides"}
    kaanna(sanakirja)
    print(sanakirja)