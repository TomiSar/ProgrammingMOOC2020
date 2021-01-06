# Opiskelijatiedot: opiskelijat1.csv
# Tehtävätiedot: tehtavat1.csv
# Koepisteet: koepisteet1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koetiedot = input("Koepisteet: ")
 
def arvosana(pisteet):
    arvosana = 0
    rajat = [15, 18, 21, 24, 28]
    while arvosana < 5 and pisteet >= rajat[arvosana]:
        arvosana += 1
    return arvosana
 
def pisteiksi(lkm):
    return lkm // 4
 
opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue            # otsikkoriviä, ei huomioida!
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2].strip()}"
 
tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        summa = 0
        for i in range(1, 8):
            summa += int(osat[i])
        tehtavat[osat[0]] = summa
 
kokeet = {}
with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue 
        summa = 0
        for i in range(1, 4):
            summa += int(osat[i])
        kokeet[osat[0]] = summa
 
for nro, nimi in opiskelijat.items():
    yht = kokeet[nro] + pisteiksi(tehtavat[nro])
    print(f"{nimi} {arvosana(yht)}")