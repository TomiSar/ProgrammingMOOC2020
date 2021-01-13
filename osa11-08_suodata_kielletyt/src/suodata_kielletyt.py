# Tee funktio suodata_kielletyt(merkkijono: str, kielletyt: str) joka palauttaa sen parametrina olevasta merkkijonosta version, 
# joka ei sisällä yhtään merkkiä sen toisena parametrina olevasta "kiellettyjen merkkien" merkkijonosta.
def suodata_kielletyt(merkkijono: str, kielletyt: str):
    return "".join([merkki for merkki in merkkijono if merkki not in kielletyt])

# main
if __name__ == "__main__":
    lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
    suodatettu = suodata_kielletyt(lause, "!?:,.")
    print(suodatettu)