def suodata_laskut():
    with open("oikeat.csv", "w") as korrektit:
        with open("vaarat.csv", "w") as epakorrektit:
            with open("laskut.csv") as tiedosto:
                for rivi in tiedosto:
                    osat=rivi.split(";")
                    lasku=osat[1]
                    tulos=osat[2]
                    if "-" in lasku:
                        alkio=lasku.split("-")
                        eka=int(alkio[0])
                        toka=int(alkio[1])
                    elif "+" in lasku:
                        alkio=lasku.split("+")
                        eka=int(alkio[0])
                        toka=int(alkio[1])
                    if eka-toka == int(tulos) or eka+toka == int(tulos):
                        korrektit.write(rivi)
                    elif lasku != int(tulos):
                        epakorrektit.write(rivi)

# tee ratkaisu tänne 
if __name__ == "__main__":
    suodata_laskut()
 