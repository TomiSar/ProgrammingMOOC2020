#opiskelijat{}, jossa nimi ja kurssi() 
def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi]=[]
 
def lisaa_suoritus(opiskelijat:dict, nimi:str, kurssi: tuple):
    loytyy = False

    for i in range(0, len(opiskelijat[nimi])):
        if opiskelijat[nimi][i][0] == kurssi[0]:
            loytyy = True
            if opiskelijat[nimi][i][1] < kurssi[1]:
                opiskelijat[nimi][i] = kurssi
                
    if loytyy==False and kurssi[1]!=0:
        opiskelijat[nimi].append(kurssi)
 
def tulosta(opiskelijat:dict, nimi: str):
    if nimi not in opiskelijat:
        print("ei löytynyt ketään nimellä",nimi)
    else:
        print(f"{nimi}:")
        if opiskelijat[nimi]==[]:
            print(" ei suorituksia")
        else:
            summa=0
            kurssit=0
            suoritukset=[]
            for i in range(len(opiskelijat[nimi])):
                if opiskelijat[nimi][i][1] != 0:
                    suoritukset.append(f"  {opiskelijat[nimi][i][0]} {opiskelijat[nimi][i][1]}")
                    summa += opiskelijat[nimi][i][1]
                    kurssit += 1
            print(" suorituksia", kurssit, "kurssilta:")
            for j in suoritukset:
                print(j)
            keskiarvo=summa/kurssit
            opiskelijat[nimi].append(keskiarvo)
            print(" keskiarvo",keskiarvo)
#suorituksia 2 kurssilta:
#  Ohpe 3
#  Tira 2
# keskiarvo 2.5
 
def kooste(opiskelijat: dict):
    print("opiskelijoita",len(opiskelijat))
    maxsuorituksia=0
    maxka=0
    ka=[]
    for nimi in opiskelijat:
        summa=0
        kurssit=0
        for i in range(len(opiskelijat[nimi])):
            summa += opiskelijat[nimi][i][1]
            kurssit += 1
        keskiarvo = summa / kurssit
        ka.append(keskiarvo)
        if keskiarvo > maxka:
            maxka = keskiarvo
            maxkaop=nimi
        if len(opiskelijat[nimi]) > maxsuorituksia:
            maxsuorituksia=kurssit
            maxsuoop=nimi   
    print("eniten suorituksia",maxsuorituksia,maxsuoop)
    print("paras keskiarvo", maxka, maxkaop)
#opiskelijoita 2
#eniten suorituksia 3 Pekka
#paras keskiarvo 4.5 Liisa
 
if __name__ == "__main__" :
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)
