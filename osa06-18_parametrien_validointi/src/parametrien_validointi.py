# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
    nimiosat = nimi.split(" ")
    if nimi == " ":
        raise ValueError("nimi on tyhjä merkkijono:" + str(nimi))
    elif len(nimiosat) < 2:
        raise ValueError("nimi ei koostu vähintään kahdesta sanasta" + str(nimi))
    elif len(nimi) > 40:
        raise ValueError("nimen pituus on yli 40 merkkiä" + str(nimi))
    elif ika < 0:
        raise ValueError("ikä on negatiivinen luku" + str(ika))
    elif ika > 150:
        raise ValueError("ikä on suurempi kuin 150" + str(ika))
    else:
        henkilo = (nimi, ika)
        return henkilo
 
if __name__ == "__main__":
    henkilo = uusi_henkilo("Pekka Pekkanen", 48)
    print("Pekka Pekkanen", henkilo)