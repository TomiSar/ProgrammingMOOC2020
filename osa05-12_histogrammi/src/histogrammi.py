# tee ratkaisu tänne
def histogrammi(merkkijono):
    lista = []
    for merkki in merkkijono:
        lisays = merkki + " " + (merkkijono.count(merkki) * "*")
        if lisays not in lista:
            lista.append(lisays)
    
    for rivi in lista:
        print(rivi)
    

if __name__ == "__main__":
    histogrammi("saippuakauppias")