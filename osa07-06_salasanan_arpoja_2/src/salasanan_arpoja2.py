from random import choice, randint
from string import ascii_lowercase, digits

def luo_hyva_salasana(pituus: int, numero: bool, erikoismerkki: bool):
    erikoismerkit = "!?=+-()#"
    # alkuun yksi kirjain 
    salasana = choice(ascii_lowercase)
    arvontajoukko = ascii_lowercase

    # Jos halutaan numeroita, lisätään vähintään yksi
    if numero:
        salasana = lisaa_merkki(salasana, digits)
        arvontajoukko += digits

    # sama erikoismerkille
    if erikoismerkki:
        salasana = lisaa_merkki(salasana, erikoismerkit)
        arvontajoukko += erikoismerkit

    # Kasataan loppu salasana koko arvontajoukosta
    while len(salasana) < pituus:
        salasana = lisaa_merkki(salasana, arvontajoukko)
    
    return salasana

# Lisää satunnaisen merkin annetusta joukosta joko merkkijonon alkuun tai loppuun
def lisaa_merkki(salasana: str, merkit):
    merkki = choice(merkit)
    if randint(1, 2) == 1:
        return merkki + salasana
    else:
        return salasana + merkki

#main
if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(8, True, True))