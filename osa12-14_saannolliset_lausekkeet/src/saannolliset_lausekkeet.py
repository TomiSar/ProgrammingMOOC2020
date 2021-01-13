import re

# Viikonpäivät
# Säännöllisen lausekkeen funktio palauttaa True, jos sen parametrina saama merkkijono sisältää viikonpäivän lyhenteen (ma, ti, ke, to, pe, la tai su).
def on_viikonpaiva(merkkijono: str):
    return re.search("ma|ti|ke|to|pe|la|su", merkkijono) is not None

# Vokaalitarkistus
# Säännöllisen lausekkeen funktio tarkistaa säännöllisen lausekkeen avulla, ovatko parametrina annetun merkkijonon kaikki merkit vokaaleja.
def kaikki_vokaaleja(merkkijono: str):
    return re.search("^[aeiouyåäö]*$", merkkijono) is not None

# Kellonaika
# Säännöllisen lausekkeen funktio tarkistaa säännöllisen lausekkeen avulla, onko parametrina oleva merkkijono muotoa 
# tt:mm:ss oleva kellonaika (tunnit, minuutit ja sekunnit kaksinumeroisina).
def kellonaika(merkkijono: str):
    return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", merkkijono) is not None

#main
if __name__ == "__main__":
    print("Kellonaika:")
    print(kellonaika("12:43:01"))
    print(kellonaika("AB:01:CD"))
    print(kellonaika("17:59:59"))
    print(kellonaika("33:66:77"))

    # print("\nVokaalitarkistus:")
    # print(kaikki_vokaaleja("eioueioieoieouyyyy"))
    # print(kaikki_vokaaleja("autoooo"))  

    # print("\nViikonpäivät:")
    # print(on_viikonpaiva("ma"))
    # print(on_viikonpaiva("pe"))
    # print(on_viikonpaiva("tu"))