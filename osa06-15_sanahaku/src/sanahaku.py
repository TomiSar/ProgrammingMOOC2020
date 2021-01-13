def hae_sanat(hakusana: str):
    tulokset = []

    with open("sanat.txt") as tiedosto:
        # Tätä tarvitaan myöhemmin
        hakusana_ilman_tahtea = hakusana.replace("*","")
        
        for sana in tiedosto:
            sana = sana.replace("\n","")
            # Onko asteriskia
            if "*" in hakusana:
                # Alussa vai lopussa?
                if hakusana[0] == "*":
                    if sana.endswith(hakusana_ilman_tahtea):
                        tulokset.append(sana)
                else:
                    if sana.startswith(hakusana_ilman_tahtea):
                        tulokset.append(sana)
            # Onko pisteitä
            elif "." in hakusana:
                # onko yhtä pitkä
                if len(hakusana) == len(sana):
                    osuma = True
                    for i in range(len(hakusana)):
                        if hakusana[i] != "." and hakusana[i] != sana[i]:
                            osuma = False
                            break
                    if osuma:
                        tulokset.append(sana)
            # Ei ollut kumpaakaan, vain kokonainen sana täsmää
            else:
                if sana == hakusana:
                    tulokset.append(sana)
    return tulokset

#main
if __name__ == "__main__" :
    print(hae_sanat("*vokes"))
