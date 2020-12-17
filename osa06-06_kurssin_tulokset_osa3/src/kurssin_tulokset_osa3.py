# tee ratkaisu tänne
# Opiskelijatiedot: opiskelijat1.csv
# Tehtävätiedot: tehtavat1.csv
# Koepisteet: koepisteet1.csv

# nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koetiedot = input("Koepisteet: ")
 
def arvosana(pisteet):
    a = 0
    rajat = [15, 18, 21, 24, 28]
    while a < 5 and pisteet >= rajat[a]:
        a += 1
 
    return a
 
def pisteiksi(lkm):
    return lkm // 4
 
opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
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
 
print("nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana")
for nro, nimi in opiskelijat.items():
    tehtavia = tehtavat[nro]
    teht_pist = pisteiksi(tehtavia)
    koe_pist = kokeet[nro]
    yht_pist = teht_pist + koe_pist
    print(f"{nimi:30}{tehtavia:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana(yht_pist):<10}")
 
# tee ratkaisu tänne