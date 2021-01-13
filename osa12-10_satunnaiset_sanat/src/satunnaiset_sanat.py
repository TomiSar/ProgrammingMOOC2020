from random import choice

# Tee funktio sanageneraattori(kirjaimet: str, pituus: int, maara: int), joka muodostaa 
# ja palauttaa annettujen parametrien avulla satunnaisia sanoja tuottavan generaattorin.
# Satunnainen sana muodostetaan valitsemalla pituus kappaletta kirjaimia valikoimasta kirjaimet. 
# Sama kirjain saa esiintyä sanassa monta kertaa.Generaattori palauttaa maara kappaletta sanoja ennen kuin se pysähtyy.
def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    return ("".join([choice(kirjaimet) for i in range(pituus)]) for j in range(maara))

#main
if __name__ == "__main__":
    sanagen = sanageneraattori("abcdefg", 3, 5)
    for sana in sanagen:
        print(sana)