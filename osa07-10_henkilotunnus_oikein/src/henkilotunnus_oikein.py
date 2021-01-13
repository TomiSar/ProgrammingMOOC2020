from datetime import datetime
def onko_validi(hetu: str):
    if len(hetu) != 11:
        return False
    numerot = hetu[:6]+hetu[7:10]
    for n in numerot:
        if n not in numerot:
            return False
    valimerkki=hetu[6]
    if valimerkki not in "+-A":
        return False
    paiva = int(hetu[0:2])
    kuukausi = int(hetu[2:4])
    vuosi = int(hetu[4:6])
    if valimerkki == "+":
        vuosi += 1800
    if valimerkki == "-":
        vuosi += 1900
    if valimerkki == "A":
        vuosi += 2000
    try:
        paivays=datetime(vuosi, kuukausi, paiva)
    except:
        return False
    merkit = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    kohta = int(numerot) % 31
    return merkit[kohta] == hetu[-1]

#main
if __name__ == "__main__":
    print(onko_validi("120501A644E")) # True 100400A644E (true)
    print(onko_validi("180880-0455")) # True