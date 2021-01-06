def hae_nimi(reseptiikka, sana):
    reseptit = []
    nimet = []
    finalista = []
    with open(reseptiikka) as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.split("\n\n")
        for alkio in sisalto:
            alkio = alkio.split("\n")
            reseptit.append(alkio)
        for alkio in reseptit:
            nimet.append(alkio[0])
        for i in nimet:
            if sana.lower() in i or sana.capitalize() in i:
                finalista.append(i)
        return finalista 
 
def hae_aika(reseptiikka, aika):
    reseptit = []
    ajat = []
    with open(reseptiikka) as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.split("\n\n")
        for alkio in sisalto:
            alkio = alkio.split("\n")
            reseptit.append(alkio)
        for resepti in reseptit:
            if int(resepti[1]) <= aika:
                ajat.append((f"{resepti[0]}, valmistusaika {resepti[1]} min"))
    return ajat
 
def hae_raakaaine(reseptiikka, aine):
    reseptit = []
    aineet = []
    with open(reseptiikka) as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.split("\n\n")
        for alkio in sisalto:
            alkio = alkio.split("\n")
            reseptit.append(alkio)
        for resepti in reseptit:
            if aine in resepti[2:]:
                aineet.append((f"{resepti[0]}, valmistusaika {resepti[1]} min"))
    return aineet

#main
if __name__ == "__main__":
    loydetyt = hae_raakaaine("reseptit1.txt", "maito")
    for resepti in loydetyt:
        print(resepti)
    # loydetyt = hae_aika("reseptit1.txt", 20)
    # for resepti in loydetyt:
    #     print(resepti)
    # loydetyt = hae_nimi("reseptit1.txt", "pulla")
    # for resepti in loydetyt:
    #     print(resepti)