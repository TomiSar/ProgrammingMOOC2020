# tee ratkaisu tänne
def suodata_virheelliset():
    with open("lottonumerot.csv") as syote, open("korjatut_numerot.csv", "w") as tulos:
        for rivi in syote:
            osat = rivi.strip().split(";")
            if len(osat) != 2:
                continue
            viikko = osat[0].split(" ")
            virhe = False
            if len(viikko) != 2 or viikko[0] != "viikko":
                virhe = True
            try:
                mika = int(viikko[1])
            except:
                virhe = True
            lista = osat[1].split(",")
            if len(lista) != 7:
                virhe = True
            mukana = []
            for alkio in lista:
                try:
                    numero = int(alkio)
                    if numero < 1 or numero > 39 or numero in mukana:
                        virhe = True
                    mukana.append(numero)
                except:
                    virhe = True
            if not virhe:
                tulos.write(rivi)
            
#ohjelman kutsuminen
if __name__ == "__main__":
    suodata_virheelliset()

