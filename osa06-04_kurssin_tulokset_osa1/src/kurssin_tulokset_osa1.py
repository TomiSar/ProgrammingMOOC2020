# tee ratkaisu tänne
# Opiskelijatiedot: opiskelijat1.csv
# Tehtävätiedot: tehtavat1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")

nimet = {}
with open (opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        nimet[osat[0]] = osat[1] + " " + osat[2]

pisteet = {}
with open (tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        opnro = osat[0]
        pisteet[opnro] = []
        for piste in osat[1:]:
            pisteet[opnro].append(int(piste))

for opnro, nimi in nimet.items():
    if opnro in pisteet:
        pisteetyht = sum(pisteet[opnro])
        print(f"{nimi} {pisteetyht}")