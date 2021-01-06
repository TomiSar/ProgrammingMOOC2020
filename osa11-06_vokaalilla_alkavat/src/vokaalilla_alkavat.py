# Kirjoita funktio vokaalilla_alkavat(sanat: list), joka saa parametrikseen listan merkkijonoja.
# Tehtävänäsi on listakoostetta hyödyntäen muodostaa ja palauttaa uusi lista, joka sisältää vain 
# alkuperäisen listan ne sanat, jotka alkavat vokaalilla (a, e, i, o, u, y, ä, ö). Sekä pienien että suurten kirjaimien pitää kelvata.
def vokaalilla_alkavat(sanat: list):
    return [sana for sana in sanat if sana[0].lower() in "aeiouyäö"]

# main
if __name__ == "__main__":
    klista = ["auto","mopo","Etana","kissa","Koira","OMENA","appelsiini"]
    for vok in vokaalilla_alkavat(klista):
        print(vok)