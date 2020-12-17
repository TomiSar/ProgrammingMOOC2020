# tee ratkaisu tänne
while True:
    print("1 - lisää sana, 2 - hae sana, 3 - poistu")
    #1: tallenna tiedostoon muodossa sana1 - sana2 
    #2: hae tiedostosta for rivi, if sana in rivi, print rivi
    valinta = int(input("Valinta: "))
 
    if valinta == 1:
        sanafin = input("Anna sana suomeksi: ")
        sanaeng = input("Anna sana englanniksi: ")
        with open("sanakirja.txt","a") as tiedosto:
            tiedosto.write(f"{sanafin} - {sanaeng}\n")
        print("Sanapari lisätty")
 
    elif valinta == 2:
        sana = input("Anna sana: ")
        with open("sanakirja.txt") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                if sana in rivi:
                    print(rivi)
                    
    elif valinta == 3:
        print("Moi!")
        break