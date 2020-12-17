# tee ratkaisu tänne
import math
 
def hae_asematiedot(asema_tiedosto:str):
    asemat = {}
    with open(asema_tiedosto) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if osat[0] == "Longitude":
                continue
            asemat[osat[3]] = (float(osat[0]), float(osat[1]))
 
    return asemat
 
def etaisyys(asemat: dict, asema1: str, asema2: str):
    longitude1, latitude1 = asemat[asema1]
    longitude2, latitude2 = asemat[asema2]
    # huomaa että edellinen on sama kun tekisimme
    # kordinaatit = asemat[asema2]
    # longitude2 = kordinaatit[0]
    # latitude2 = kordinaatit[0]
 
    x_kilometreina = (longitude1-longitude2) * 55.26
    y_kilometreina = (latitude1-latitude2) * 111.2
    return math.sqrt(x_kilometreina**2 + y_kilometreina**2)
 
def suurin_etaisyys(asemat: dict):
    pisin = 0
    for mista in asemat:
        for mihin in asemat:
            e = etaisyys(asemat, mista, mihin)
            if e > pisin:
                asema1 = mista
                asema2 = mihin
                pisin = e
 
    return asema1, asema2, pisin


if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')
    e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    print(e)
    e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
    print(e)