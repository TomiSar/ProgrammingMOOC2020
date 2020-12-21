# tee ratkaisu tänne
def henkilon_keskiarvo(henkilo: dict):
    return henkilo["tulos1"] + henkilo["tulos2"] + henkilo["tulos3"] / len(henkilo)

def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    pienin_henkilo = henkilo1
    if henkilon_keskiarvo(henkilo2) < henkilon_keskiarvo(pienin_henkilo):
        pienin_henkilo = henkilo2
    if henkilon_keskiarvo(henkilo3) < henkilon_keskiarvo(pienin_henkilo):
        pienin_henkilo = henkilo3
    return pienin_henkilo

if __name__ == "__main__":
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}
    print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))