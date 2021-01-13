#pohjana malliratkaisu kurssi_tulokset_osa3
#Laajennetaan vielä hieman aiemmin kurssien tulokset generoivaa sovellusta. Tällä hetkellä tiedostosta luetaan opiskelijoiden nimet, tehtäväpisteet sekä koepisteet. Laajennetaan ohjelmaa siten, että myös kurssin nimi ja laajuus luetaan tiedostosta
#Ohjelma luo kaksi tiedostoa tulos.txt (samanlainen kuin tehtävän edellisen osan tulostus) ja tulos.csv
#Esimerkkitulostus
#opiskelijatiedot: opiskelijat1.csv
#tehtävätiedot: tehtavat1.csv
#koepisteet: koepisteet1.csv
#kurssin tiedot: kurssi1.txt
#Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv
 
#opiskelijatiedot='opiskelijat1.csv'
#tehtavatiedot='tehtavat1.csv'
#koetiedot='koepisteet1.csv'
#kurssitiedot='kurssi1.txt'
opiskelijatiedot = input("opiskelijatiedot: ")
tehtavatiedot = input("tehtävätiedot: ")
koetiedot = input("koepisteet: ")
kurssitiedot = input("kurssin tiedot: ") 
print("Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv")
 
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
 
kurssitieto={}
with open(kurssitiedot) as tiedosto:
    for rivi in tiedosto:
        rivi=rivi.replace("\n","")
        osat=rivi.split(":")
        kurssitieto[osat[0]]=osat[1].strip()
 
with open('tulos.txt','w') as tulos: 
    #tulos.write(f"{kurssitieto['nimi']}, {kurssitieto['laajuus opintopisteina']} opintopistettä \n")
    rivi=f"{kurssitieto['nimi']}, {kurssitieto['laajuus opintopisteina']} opintopistettä\n"
    tulos.write(rivi)  
    tulos.write(f"{'='*(len(rivi)-1)} \n")
    tulos.write("nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana\n")
    for nro, nimi in opiskelijat.items():
        tehtavia = tehtavat[nro]
        teht_pist = pisteiksi(tehtavia)
        koe_pist = kokeet[nro]
        yht_pist = teht_pist + koe_pist
        tulos.write(f"{nimi:30}{tehtavia:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana(yht_pist):<10}\n")
 
with open('tulos.csv','w') as tulos:
    for nro, nimi in opiskelijat.items():
        tehtavia = tehtavat[nro]
        teht_pist = pisteiksi(tehtavia)
        koe_pist = kokeet[nro]
        yht_pist = teht_pist + koe_pist
        tulos.write(f"{nro};{nimi};{arvosana(yht_pist)}\n")