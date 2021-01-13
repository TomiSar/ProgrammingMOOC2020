def suodata_laskut():
    #avataan kaikki tiedostot 
    with open("laskut.csv") as lahde, open("oikeat.csv", "w") as oikeat, open("vaarat.csv", "w") as vaarat:
        for rivi in lahde:

            palat = rivi.split(";")
            lasku = palat[1] 
            tulos = palat[2]
            #pluslasku vai miinuslasku oikein(True or False) riippuu tuloksesta
            if "+" in lasku:
                operandit = lasku.split("+")
                oikein = int(operandit[0]) + int(operandit[1]) == int(tulos) 
            else:
                operandit = lasku.split("-")
                oikein = int(operandit[0]) - int(operandit[1]) == int(tulos)

            #kirjoitetaan oikeat ja väärät
            if oikein:
                oikeat.write(rivi)
            else:
                vaarat.write(rivi)

# tee ratkaisu tänne 
if __name__ == "__main__":
    suodata_laskut()
 